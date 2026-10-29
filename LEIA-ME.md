# Máquina de Edição com IA — pacote principal

Inclui a Máquina de Edição e seis formatos, cada um com sua própria skill:

| Comando | Como fica |
|---|---|
| `/reels-de-negocio` | Alterna câmera cheia, tela dividida e animações |
| `/reels-com-broll` | Cortes rápidos, clipes de apoio e frases em destaque |
| `/tela-dividida-explicativa` | Você embaixo e explicações animadas em cima |
| `/ensaio-visual` | Você recortado com notícias, números e provas visuais |
| `/recorte-com-imagens` | Você na frente de imagens que mudam com a fala |
| `/telas-em-profundidade` | Interfaces animadas atrás de você, com profundidade |

Os seis formatos são verticais (Reels, TikTok e Shorts). O caminho **Do zero** também permite editar gravações horizontais. Pixelado, Noite Laranja e Claro Tecnológico vêm incluídos e podem ser combinados com qualquer formato.

## Instalar

Extraia o ZIP inteiro, incluindo a pasta `.claude`, e abra um terminal nesta pasta.

Windows (PowerShell):

```powershell
powershell -ExecutionPolicy Bypass -File .\instalar.ps1
```

Mac/Linux:

```bash
bash instalar.sh
```

O instalador copia sete skills para `~/.claude/skills/` (o motor e os seis formatos). Se houver versões antigas das mesmas skills, elas ficam em `~/.claude/skills-backup/`. Preferências, estilos pessoais e outros formatos já instalados são preservados.

Feche e abra o Claude Code depois da instalação.

## Editar

Crie uma pasta própria para cada vídeo, fora desta pasta de instalação, e coloque a gravação nela. Abra o Claude Code nessa pasta e digite `/maquina-de-edicao` ou o comando de um formato. É necessário acesso ao Claude Code.

Na primeira edição, o Claude confere Node.js, FFmpeg, Python e HyperFrames e orienta a instalação do que faltar. Um painel local abre no navegador para você escolher o formato e o visual. Depois da montagem, assista no HyperFrames Studio e peça ajustes. Para gerar o MP4 final, diga **pode exportar**. A saída fica em `edit/final.mp4`.

## Atualizar e adicionar formatos

Baixe a nova versão do seu pacote, extraia e rode o instalador novamente. Quem comprou o complemento instala o ZIP de seis formatos extras depois do principal; os novos comandos aparecem no mesmo painel.
