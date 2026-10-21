# Aula em Tela Dividida

Resumo: aula em 16:9 com um documento de anotações (gerado a partir da sua fala) rolando à esquerda, acompanhando o que você explica, e você à direita; o documento também é entregue como arquivo pra seus alunos.

O visual descrito aqui (cores, fontes, materiais, legenda, música) é o **Original do formato**. Se a pessoa escolher outro estilo visual, o layout, as posições e o ritmo daqui continuam valendo e a aparência vem do estilo: siga `maquina-de-edicao/referencias/estilos-visuais.md`.

## Como fica

O lado esquerdo é uma página branca, como um documento bem diagramado: título com uma palavra em serifa laranja, seções, etiquetas laranja "Passo 1", diagramas simples (caixas ligadas por setas), uma faixa preta com a frase-chave e, no fim, um checklist. A página rola sozinha acompanhando a fala, e o trecho que a pessoa está explicando ganha marca-texto. O lado direito é a pessoa. De vez em quando a pessoa vai pra tela cheia, com um card pequeno no canto (por exemplo, um player com a barra dividida nas etapas da aula).

O documento é gerado pela skill a partir da transcrição e sai também como `documento-da-aula.html` e `.pdf`, pronto pra virar material da aula.

## Escolhas que este formato já define

Proporção (horizontal 16:9), nível (equivale ao Com imagens, com layout próprio), legendas (sem legenda na tela; entrega `.srt`), visual original (cores, fontes e materiais, trocados se a pessoa escolher outro estilo visual), capa (sem capa), verificação de fontes (ligada só pra número ou notícia citados).

## Base técnica

- Vale: contato visual (bloco 3, só pra decidir quando usar tela cheia), produtos citados, fontes e verificação.
- Proporções gerais de "Formato horizontal 16:9" de `variacoes.md`; layouts deste arquivo.
- Não vale: layouts B e C do motor, câmera virtual, capa, cartão de chamada pra ação.
- Render no fps da gravação (60 ou 30).

## Entradas extras

Opcional: se a pessoa tiver um roteiro ou anotações da aula (`roteiro.md`, `.txt`, `.docx` ou `.pdf` na pasta), use como base do documento e confira contra a fala. Sem roteiro, o documento sai só da transcrição.

## Fluxo diferente

Uma etapa a mais na fase 2, logo depois da transcrição e dos cortes:

**Fase 2a: escrever o documento da aula.**

1. Divida a aula em seções pelo assunto.
2. Escreva o documento em HTML (uma página única, rolando), em português, com as palavras da pessoa (resuma, mas não invente conceito que ela não falou):
   - cabeçalho pequeno (nome do curso ou "Aula", se a fala citar), título da aula com **uma** palavra em serifa itálica laranja, e uma linha de subtítulo;
   - um bloco "É pra você se..." quando a pessoa disser pra quem é;
   - uma seção por assunto: título (Inter 700), uma ou duas frases de resumo, e bullets curtos;
   - **diagrama** sempre que a fala descrever uma sequência ou relação: caixas com borda preta ligadas por setas laranja (ex: Gancho → História → Oferta), com a última caixa preenchida de preto;
   - **etiquetas de passo** ("Passo 1", "Passo 2") em caixinhas laranja antes de cada passo;
   - **faixa-chave**: faixa preta com a frase mais importante da seção em branco e uma palavra em laranja (no máximo uma por seção);
   - **checklist** ou plano no fim, se a aula terminar com tarefa (grade de dias, lista de verificação);
   - "Diagnóstico" ou "Erros comuns" se a pessoa falar disso.
3. Grave em `edit/documento-da-aula.html` e anote em `edit/plano.md` o mapa **tempo da fala → elemento do documento** (qual seção, qual bullet, qual caixa do diagrama corresponde a cada trecho).

Na fase 4, exporte também `edit/documento-da-aula.pdf` (A4, mesma diagramação, sem a animação).

## Ritmo e corte

- Limpeza mais suave que o motor: reduza pausas acima de 400 ms pra ~200 ms. Aula precisa de respiro.
- Proporção: 80% dividido, 20% tela cheia.

## Layouts

Tela de 1920 × 1080.

### A. Dividido (principal)

- **Documento** à esquerda: x = 0 a 845, fundo `#FFFFFF`, sem borda. O conteúdo tem margens de 56 px. Uma sombra fina na divisa (`4px 0 24px rgba(0,0,0,0.25)`).
- **Pessoa** à direita: x = 845 a 1920, gravação recortada pra 1075 × 1080 com o rosto centralizado. Etiqueta minúscula opcional no canto superior direito com o nome da pessoa (Inter 600 16 px, caixa alta, `rgba(255,255,255,0.7)`), só se ela disser o nome.

### B. Tela cheia com card

Gravação em tela cheia e um card de vidro escuro (Kit Noite) de 420 × 300 px no canto esquerdo (x = 80, y = 220), mostrando o progresso da aula: um mini player com o título da aula e uma barra dividida nas etapas (ex: "Gancho · História · Oferta"), com a etapa atual em laranja e as passadas preenchidas. Notificação pequena por cima quando a fala citar um resultado ("Nova call agendada").

### Regras de distribuição

- Abertura: B por 5–10 s, depois A.
- Quando a pessoa conta uma história, dá uma opinião ou fala diretamente com o aluno: B.
- Explicação de conteúdo: A.
- Encerramento: B.

## Direção visual

### Documento

- Fontes: **Playfair Display** 700 (título da aula), **Instrument Serif** itálico (palavra destacada do título e destaques), **Inter** 400/600/700 (todo o resto). Locais.
- Texto `#111111`, secundário `#6B6B6B`, laranja `#C8662A`, marca-texto `#FDE68A`, faixa-chave `#111111`.
- Tamanhos (no vídeo, a 845 px de largura): título 56 px, títulos de seção 30 px, texto 20 px, bullets 19 px, etiquetas 14 px em caixa alta. Nada abaixo de 14 px.
- Espaçamento generoso: 48 px entre seções.

### Card do modo tela cheia

Kit Noite (`maquina-de-edicao/referencias/kit-noite.md`).

## Gráficos

### Rolagem sincronizada

- O documento rola pra manter o elemento que está sendo falado entre y = 180 e y = 520 da tela.
- Rolagem suave (0,8–1,2 s, power2.inOut), só quando o elemento atual sair dessa faixa. Nunca rolagem contínua.
- O elemento atual recebe marca-texto amarelo (fundo `#FDE68A` atrás do texto) que se "desenha" da esquerda pra direita em 0,4 s quando a fala chega nele, e fica até a fala passar pro próximo.
- Elementos ainda não falados aparecem normalmente (o documento já está todo escrito), mas os diagramas se montam na hora: cada caixa aparece quando é citada, e a seta até ela se desenha em 0,3 s.
- Ao voltar de B pra A, o documento está na posição certa pro trecho atual.

## Legendas

Nenhuma legenda na tela. Gere `edit/legendas.srt` como no YouTube Educativo (até 2 linhas de 42 caracteres).

## Capa e gancho

Sem capa. O quadro 0 é o início da aula.

## Chamada para ação

Sem cartão. Se a aula termina indicando a próxima ("continua no episódio 2"), o documento tem uma linha final com isso.

## Áudio

- Música: opcional e mínima. Padrão: **sem música** durante a explicação; um pad suave de 4 s só na abertura e no encerramento (~−30 LUFS). Se a pessoa escolheu a música do formato, é isso.
- Efeitos: um "tic" de papel bem baixo (18 dB abaixo do pico da voz) quando uma caixa de diagrama aparece. Nada mais.

## Saída

- `edit/final.mp4`, 1920 × 1080, fps da gravação, H.264 + AAC 48 kHz.
- `edit/documento-da-aula.html` e `edit/documento-da-aula.pdf`.
- `edit/legendas.srt`.

## Verificação do formato

- Todo conceito do documento foi falado na aula (nada inventado).
- O marca-texto está no elemento certo em 5 pontos espalhados pelo vídeo.
- Texto do documento legível no vídeo (nada abaixo de 14 px, contraste alto).
- O PDF abre e tem a mesma estrutura do HTML.
- Nenhuma rolagem durante a fala de uma mesma frase curta (sem "pula-pula").
