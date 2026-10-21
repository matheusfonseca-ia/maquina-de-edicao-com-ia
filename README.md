# Máquina de Edição com IA + 12 Estilos Prontos

Edite seus vídeos com o Claude Code sem abrir app de edição. Você coloca a gravação numa pasta, digita um comando e o Claude corta, legenda, monta os gráficos, coloca música e efeitos e te mostra o vídeo pronto pra aprovar.

Este repositório tem tudo:

- **`/maquina-de-edicao`**: a skill principal. Ela pergunta se você quer editar **do zero** (escolhendo cada detalhe) ou **com um estilo pronto**.
- **12 estilos prontos**, cada um com o próprio comando. Se você já sabe o estilo, digita o nome dele e vai direto.

## Os 12 estilos

### Vertical 9:16 (Reels, TikTok, Shorts)

| Comando | Como o vídeo sai |
|---|---|
| `/reels-de-negocio` | Alterna câmera cheia, tela dividida e animação em tela cheia a cada corte |
| `/reels-com-broll` | Corte rápido, seus clipes de apoio e frases-chave empilhadas na legenda |
| `/tela-dividida-explicativa` | Você embaixo e a explicação em cima, com cards de vidro, contadores e gráficos que se desenham |
| `/ensaio-visual` | Preto e laranja, você recortado e as provas aparecendo acima de você |
| `/legenda-encaixada` | Uma palavra gigante em destaque e o resto da frase encaixado em volta |
| `/nuvem-de-imagens` | Grupos de imagens acima da sua cabeça, legenda pequena e discreta |
| `/recorte-com-imagens` | Você recortado na frente de imagens em tela cheia que trocam a cada ideia |
| `/telas-em-profundidade` | Você em tela cheia com interfaces e telas reais atrás da sua cabeça |
| `/formato-ranking` | Tier list que vai se preenchendo conforme você ranqueia |
| `/cortes-de-video-longo` | Entra um vídeo longo ou uma call, saem cortes verticais ranqueados |

### Horizontal 16:9 (YouTube)

| Comando | Como o vídeo sai |
|---|---|
| `/youtube-educativo` | Vídeo longo com cards, tela dividida e animações explicativas |
| `/aula-em-tela-dividida` | O documento da aula rola na esquerda e você fica na direita (o documento sai em PDF também) |

## O que você precisa

- Um computador Windows ou Mac.
- **Claude Code** num plano pago do Claude.
- **Git** pra baixar o repositório (no Windows: [git-scm.com](https://git-scm.com); no Mac já vem instalado ou é instalado na primeira vez que você usar).
- Node.js, FFmpeg, Python e HyperFrames: na primeira edição, o próprio Claude confere o que falta no seu computador e te guia pra instalar. Tudo isso é gratuito.

## Instalação

Abra o terminal e rode:

**Windows (PowerShell)**

```powershell
git clone <LINK-DO-REPOSITORIO> maquina-de-edicao
cd maquina-de-edicao
powershell -ExecutionPolicy Bypass -File .\instalar.ps1
```

**Mac**

```bash
git clone <LINK-DO-REPOSITORIO> maquina-de-edicao
cd maquina-de-edicao
bash instalar.sh
```

O instalador copia as 13 skills pra pasta de skills do Claude Code no seu computador (`~/.claude/skills/`), e aí elas funcionam em qualquer pasta. Se você já tinha uma versão antiga da Máquina de Edição, ela é guardada em `~/.claude/skills-backup/` antes da troca. Suas preferências e estilos salvos não são apagados.

Depois de instalar, **feche e abra o Claude Code de novo**.

## Como usar

1. Crie uma pasta pro vídeo e coloque a gravação bruta dentro (e o áudio do microfone, se gravou separado).
2. Abra o Claude Code nessa pasta.
3. Digite `/maquina-de-edicao` e escolha **do zero** ou **estilo pronto**. Ou digite direto o comando do estilo, por exemplo `/ensaio-visual`.
4. Responda as perguntas rápidas (no estilo pronto são só música, efeitos e cor de destaque).
5. Espere. Quando o vídeo estiver montado, o Claude te passa um link do **HyperFrames Studio** pra assistir.
6. Peça os ajustes que quiser, em português normal ("legenda maior", "tira esse efeito", "corta essa frase").
7. Quando estiver bom, diga **"pode exportar"**. O vídeo final sai em `edit/final.mp4`.

O que você aprovar fica salvo. No próximo vídeo, dá pra escolher "Repetir o último vídeo" e pular as perguntas.

### Alguns estilos pedem coisas a mais na pasta

- **Reels com B-roll**: coloque seus clipes de apoio numa pasta `broll/` dentro da pasta do vídeo.
- **Nuvem de Imagens**, **Recorte com Imagens**, **Ensaio Visual** e **Formato Ranking**: se quiser usar suas próprias imagens, coloque numa pasta `imagens/` (com nomes que digam o que é cada uma). Sem isso, o Claude busca logos, páginas e imagens reais do que você citou.
- **Aula em Tela Dividida**: se tiver o roteiro da aula, coloque na pasta. O documento da aula fica mais fiel.
- **Cortes de Vídeo Longo**: o Claude te mostra o ranking dos melhores trechos antes de editar, e você aprova ou troca.

## Quer seu próprio estilo?

Mande o link de um reel que você gosta e peça pra Máquina **"analisar o estilo de edição desse vídeo e salvar"**. Ele vira um estilo seu e aparece na lista junto com os 12.

Você também pode pedir pro Claude mudar um estilo pronto do seu jeito ("no Reels de Negócio, quero a legenda amarela"). O ajuste fica salvo pras próximas vezes que você usar aquele estilo.

## Atualizar

Quando sair uma versão nova, rode dentro da pasta do repositório:

```bash
git pull
```

E rode o instalador de novo.

## Problemas comuns

- **O comando não aparece no Claude Code**: feche e abra o Claude Code depois de instalar. Confira se a pasta `~/.claude/skills/maquina-de-edicao` existe.
- **"Esse estilo precisa da Máquina de Edição"**: o motor não foi instalado junto. Rode o instalador de novo.
- **No Windows, "a execução de scripts foi desabilitada"**: use o comando completo `powershell -ExecutionPolicy Bypass -File .\instalar.ps1`.
- **A renderização está lenta**: é normal no primeiro vídeo (o Claude instala as ferramentas). Estilos com recorte do fundo (Ensaio Visual, Recorte com Imagens, Telas em Profundidade) demoram mais que os outros.
