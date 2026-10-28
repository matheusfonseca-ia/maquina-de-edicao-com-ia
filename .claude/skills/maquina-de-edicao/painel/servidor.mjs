#!/usr/bin/env node
// Painel de escolhas da Máquina de Edição.
//
// Sobe uma página local (só neste computador), abre o navegador e espera a
// pessoa escolher tudo. Quando ela clica em "Começar a edição", grava as
// escolhas em JSON e encerra.
//
// Uso:
//   node servidor.mjs --contexto edit/painel-contexto.json --saida edit/escolhas.json
//
// Opções:
//   --sem-navegador   não abre o navegador (só imprime o endereço)
//   --porta N         porta fixa (padrão: uma livre)
//   --minutos N       desiste depois de N minutos sem resposta (padrão: 60)
//
// Saída no terminal (uma linha cada, pra quem chamou ler):
//   PAINEL_ABERTO <url>
//   ESCOLHAS_SALVAS <caminho>        (código 0)
//   PREFERE_CHAT                     (código 3: a pessoa pediu pra responder no chat)
//   TEMPO_ESGOTADO                   (código 2)

import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { spawn } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const AQUI = path.dirname(fileURLToPath(import.meta.url));

function argumento(nome, padrao = null) {
  const i = process.argv.indexOf(`--${nome}`);
  if (i === -1) return padrao;
  const v = process.argv[i + 1];
  return v && !v.startsWith('--') ? v : true;
}

const arqContexto = argumento('contexto');
const arqSaida = argumento('saida', 'escolhas.json');
const semNavegador = argumento('sem-navegador', false);
const portaFixa = Number(argumento('porta', 0)) || 0;
const minutos = Number(argumento('minutos', 60)) || 60;

let contexto = {};
if (arqContexto) {
  try {
    contexto = JSON.parse(fs.readFileSync(arqContexto, 'utf8').replace(/^﻿/, ''));
  } catch (e) {
    console.error(`Não consegui ler o contexto (${arqContexto}): ${e.message}`);
    process.exit(1);
  }
}

// Arquivos que a página pode pedir: só os listados no contexto.
const pastaVideo = contexto.pasta || (arqContexto ? path.dirname(path.resolve(arqContexto)) : process.cwd());
const permitidos = new Map();
function liberar(chave, caminho) {
  if (!caminho) return null;
  const abs = path.isAbsolute(caminho) ? caminho : path.join(pastaVideo, caminho);
  if (!fs.existsSync(abs)) return null;
  permitidos.set(chave, abs);
  return `/arquivo/${encodeURIComponent(chave)}`;
}

(contexto.audios || []).forEach((a, i) => { a.url = liberar(`audio-${i}`, a.caminho || a.arquivo); });

const TIPOS = {
  '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.css': 'text/css; charset=utf-8',
  '.json': 'application/json', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp',
  '.woff2': 'font/woff2', '.mp3': 'audio/mpeg', '.wav': 'audio/wav', '.m4a': 'audio/mp4',
  '.aac': 'audio/aac', '.flac': 'audio/flac', '.txt': 'text/plain; charset=utf-8', '.svg': 'image/svg+xml',
};

function enviarArquivo(req, res, abs) {
  let st;
  try { st = fs.statSync(abs); } catch { res.writeHead(404); return res.end(); }
  const tipo = TIPOS[path.extname(abs).toLowerCase()] || 'application/octet-stream';
  const range = req.headers.range;
  if (range) {
    const [a, b] = range.replace('bytes=', '').split('-');
    const ini = Number(a) || 0;
    const fim = b ? Math.min(Number(b), st.size - 1) : st.size - 1;
    res.writeHead(206, { 'Content-Type': tipo, 'Content-Range': `bytes ${ini}-${fim}/${st.size}`, 'Accept-Ranges': 'bytes', 'Content-Length': fim - ini + 1 });
    return fs.createReadStream(abs, { start: ini, end: fim }).pipe(res);
  }
  res.writeHead(200, { 'Content-Type': tipo, 'Content-Length': st.size, 'Accept-Ranges': 'bytes', 'Cache-Control': 'no-store' });
  fs.createReadStream(abs).pipe(res);
}

function json(res, codigo, obj) {
  res.writeHead(codigo, { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store' });
  res.end(JSON.stringify(obj));
}

function lerCorpo(req) {
  return new Promise((ok, erro) => {
    let d = '';
    req.on('data', c => { d += c; if (d.length > 2e6) erro(new Error('grande demais')); });
    req.on('end', () => ok(d));
  });
}

function encerrar(codigo, linha) {
  console.log(linha);
  setTimeout(() => process.exit(codigo), 400);
}

const servidor = http.createServer(async (req, res) => {
  const url = new URL(req.url, 'http://127.0.0.1');
  // Só aceita quem está no próprio computador.
  const host = (req.headers.host || '').split(':')[0];
  if (!['127.0.0.1', 'localhost'].includes(host)) { res.writeHead(403); return res.end(); }

  if (url.pathname === '/api/contexto') return json(res, 200, contexto);

  if (url.pathname === '/api/escolhas' && req.method === 'POST') {
    try {
      const corpo = JSON.parse(await lerCorpo(req));
      const destino = path.resolve(arqSaida);
      fs.mkdirSync(path.dirname(destino), { recursive: true });
      fs.writeFileSync(destino, JSON.stringify({ ...corpo, salvoEm: new Date().toISOString() }, null, 2), 'utf8');
      json(res, 200, { ok: true });
      encerrar(0, `ESCOLHAS_SALVAS ${destino}`);
    } catch (e) {
      json(res, 400, { ok: false, erro: e.message });
    }
    return;
  }

  if (url.pathname === '/api/prefiro-chat' && req.method === 'POST') {
    json(res, 200, { ok: true });
    return encerrar(3, 'PREFERE_CHAT');
  }

  if (url.pathname.startsWith('/arquivo/')) {
    const abs = permitidos.get(decodeURIComponent(url.pathname.slice(9)));
    if (!abs) { res.writeHead(404); return res.end(); }
    return enviarArquivo(req, res, abs);
  }

  // Arquivos da própria página.
  const rel = url.pathname === '/' ? 'index.html' : decodeURIComponent(url.pathname.slice(1));
  const abs = path.resolve(AQUI, rel);
  if (!abs.startsWith(AQUI + path.sep) || rel.includes('servidor')) { res.writeHead(404); return res.end(); }
  return enviarArquivo(req, res, abs);
});

function abrirNavegador(url) {
  const [cmd, args] = process.platform === 'win32' ? ['cmd', ['/c', 'start', '""', url]]
    : process.platform === 'darwin' ? ['open', [url]] : ['xdg-open', [url]];
  try { spawn(cmd, args, { stdio: 'ignore', detached: true, windowsHide: true }).unref(); } catch {}
}

servidor.listen(portaFixa, '127.0.0.1', () => {
  const url = `http://127.0.0.1:${servidor.address().port}/`;
  console.log(`PAINEL_ABERTO ${url}`);
  if (!semNavegador) abrirNavegador(url);
});

setTimeout(() => encerrar(2, 'TEMPO_ESGOTADO'), minutos * 60 * 1000).unref?.();
process.on('SIGINT', () => encerrar(130, 'CANCELADO'));
