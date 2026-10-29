"""Valida ZIPs, instalacao isolada e catalogo do painel sem alterar o perfil real."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import socket
import subprocess
import tempfile
import time
import urllib.error
import urllib.request
import zipfile

REPO = Path(__file__).resolve().parents[1]
POWERSHELL = shutil.which('powershell') or shutil.which('pwsh')
GIT_BASH = Path(os.environ.get('ProgramFiles', 'C:/Program Files')) / 'Git/bin/bash.exe'
BASH = str(GIT_BASH) if GIT_BASH.is_file() else shutil.which('bash')


def rodar(args, env=None, sucesso=True):
    r = subprocess.run(args, env=env, capture_output=True, text=True, encoding='utf-8', errors='replace')
    assert (r.returncode == 0) == sucesso, (args, r.returncode, r.stdout, r.stderr)
    return r


def instaladas(perfil):
    return {p.parent.name for p in (perfil / '.claude/skills').glob('*/SKILL.md')}


def hash_pasta(pasta):
    return {str(p.relative_to(pasta)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in pasta.rglob('*') if p.is_file()}


def testar_painel(perfil, contexto, esperado, rejeitar=None):
    pasta = perfil / 'video teste'
    pasta.mkdir(exist_ok=True)
    arq = pasta / 'contexto.json'
    arq.write_text(json.dumps(contexto), encoding='utf-8')
    saida = pasta / 'escolhas.json'
    with socket.socket() as s:
        s.bind(('127.0.0.1', 0))
        porta = s.getsockname()[1]
    servidor = perfil / '.claude/skills/maquina-de-edicao/painel/servidor.mjs'
    proc = subprocess.Popen(['node', str(servidor), '--contexto', str(arq), '--saida', str(saida),
                             '--sem-navegador', '--porta', str(porta)],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)
    base = f'http://127.0.0.1:{porta}'
    try:
        for _ in range(100):
            if proc.poll() is not None:
                raise AssertionError(proc.communicate())
            try:
                with urllib.request.urlopen(base + '/api/contexto', timeout=0.2) as r:
                    recebido = json.load(r)
                break
            except (OSError, urllib.error.URLError):
                time.sleep(0.05)
        else:
            raise AssertionError('Painel nao iniciou')
        assert set(recebido['formatos']) == esperado, recebido
        if rejeitar:
            for escolha in [
                {'caminho': 'formato-pronto', 'formato': {'id': rejeitar}},
                {'caminho': 'repetir-ultimo'},
            ]:
                req = urllib.request.Request(base + '/api/escolhas', data=json.dumps(escolha).encode(),
                                             headers={'Content-Type': 'application/json'})
                try:
                    urllib.request.urlopen(req)
                    raise AssertionError('Aceitou formato nao instalado')
                except urllib.error.HTTPError as e:
                    assert e.code == 400
            assert not saida.exists()
        escolha = {'caminho': 'do-zero'} if not esperado else {
            'caminho': 'formato-pronto', 'formato': {'id': sorted(esperado)[0]}}
        req = urllib.request.Request(base + '/api/escolhas', data=json.dumps(escolha).encode(),
                                     headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req) as r:
            assert r.status == 200
        assert proc.wait(timeout=5) == 0
        assert json.loads(saida.read_text(encoding='utf-8'))['caminho'] == escolha['caminho']
        saida.unlink()
    finally:
        if proc.poll() is None:
            proc.terminate()
        proc.communicate(timeout=5)


def main():
    assert POWERSHELL, 'Execute em um ambiente com PowerShell para gerar os ZIPs.'
    principal = json.loads((REPO / 'pacote.json').read_text(encoding='utf-8-sig'))
    extra = json.loads((REPO / 'order-bump/pacote.json').read_text(encoding='utf-8-sig'))
    p, e = set(principal['skills']), set(extra['skills'])
    assert len(p) == 7 and len(e) == 6 and p.isdisjoint(e)
    assert 'maquina-de-edicao' in p
    with tempfile.TemporaryDirectory(prefix='maquina-entregas-') as t:
        temp = Path(t)
        dist = temp / 'zips'
        rodar([POWERSHELL, '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File',
               str(REPO / 'preparar-pacotes.ps1'), '-Saida', str(dist)])
        pacotes = {}
        for id_, nomes in [('principal', p), ('order-bump', e)]:
            pasta = temp / ('Entrega ' + id_)
            with zipfile.ZipFile(dist / f'maquina-de-edicao-{id_}.zip') as z:
                entradas = [n.replace('\\', '/') for n in z.namelist()]
                skills_zip = {n.split('/')[2] for n in entradas
                              if n.startswith('.claude/skills/') and n.endswith('/SKILL.md')}
                assert skills_zip == nomes, skills_zip
                assert not any(n.startswith(('.git/', 'order-bump/')) for n in entradas)
                assert {'README.md', 'pacote.json', 'instalar.ps1', 'instalar.sh'}.issubset(entradas)
                z.extractall(pasta)
            pacotes[id_] = pasta
        print('OK: ZIP principal com motor + 6; ZIP extra com somente 6, sem sobreposicao.')

        for tipo in ['powershell', 'bash']:
            if tipo == 'bash' and not BASH:
                print('SKIP: Bash indisponivel; teste nativo Mac/Linux continua pendente.')
                continue
            perfil = temp / ('Perfil isolado ' + tipo)
            perfil.mkdir()
            ambiente = dict(os.environ, USERPROFILE=str(perfil), HOME=perfil.as_posix())

            def instalar(id_, sucesso=True):
                arquivo = pacotes[id_] / ('instalar.ps1' if tipo == 'powershell' else 'instalar.sh')
                comando = ([POWERSHELL, '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', str(arquivo)]
                           if tipo == 'powershell' else [BASH, arquivo.as_posix()])
                return rodar(comando, env=ambiente, sucesso=sucesso)

            instalar('order-bump', sucesso=False)
            assert not instaladas(perfil)
            instalar('principal')
            assert instaladas(perfil) == p
            motor = perfil / '.claude/skills/maquina-de-edicao'
            hash_motor = hash_pasta(motor)
            pessoal = perfil / '.maquina-de-edicao/estilos-visuais/meu-estilo.md'
            pessoal.parent.mkdir(parents=True)
            pessoal.write_text('Estilo pessoal preservado', encoding='utf-8')
            preferencias = pessoal.parents[1] / 'preferencias.md'
            preferencias.write_text('Preferencias preservadas', encoding='utf-8')

            if tipo == 'powershell':
                formatos = p - {'maquina-de-edicao'}
                testar_painel(perfil, {'preferencias': {'formato': 'formato-ranking'}}, formatos, 'formato-ranking')
                testar_painel(perfil, {'formatos': [], 'preferencias': {'formato': 'formato-ranking'}}, set(), 'formato-ranking')
                # Nem mesmo um contexto contendo os 12 libera skills extras ausentes.
                testar_painel(perfil, {'formatos': sorted(p | e)}, formatos)

            instalar('order-bump')
            assert instaladas(perfil) == p | e
            assert hash_pasta(motor) == hash_motor, 'Complemento alterou o motor'
            if tipo == 'powershell':
                testar_painel(perfil, {}, (p | e) - {'maquina-de-edicao'})
            instalar('principal')
            instalar('order-bump')
            assert instaladas(perfil) == p | e
            assert hash_pasta(motor) == hash_motor
            assert pessoal.read_text(encoding='utf-8') == 'Estilo pessoal preservado'
            assert preferencias.read_text(encoding='utf-8') == 'Preferencias preservadas'
            assert {s.parent.name for s in (perfil / '.claude/skills-backup').glob('*/*/SKILL.md')} == p | e
            print(f'OK: {tipo}: dependencia, 7 -> 13 skills, atualizacao, backup e preferencias.')
        print('OK: painel mostra 6/12/zero, rejeita formatos ausentes e salva escolhas validas.')


if __name__ == '__main__':
    main()
