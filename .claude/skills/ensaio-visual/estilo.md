# Ensaio Visual

Resumo: preto e laranja com cara de documentário; você recortado sobre um fundo escuro com brilho laranja embaixo, e as provas (posts, notícias, números, antes e depois) aparecendo em cards brancos acima da sua cabeça.

## Como fica

A pessoa aparece recortada (sem o fundo real) sobre preto, com um brilho laranja quente subindo de baixo, como luz de palco. Acima da cabeça, cards brancos com as provas do que ela está dizendo: um post, a manchete de uma notícia, um número gigante, um quadro de antes e depois. A legenda fica pequena logo acima da cabeça. No gancho, um título grande em serifa itálica atravessa o peito da pessoa.

## Escolhas que este estilo já define

Formato (vertical 9:16), nível (equivale ao Com imagens, sem câmera virtual), estilo das legendas, estilo visual, capa (título em serifa sobre o peito), verificação de fontes (ligada).

## Base técnica

- Vale: contato visual (bloco 3), produtos citados, fontes e verificação (as provas precisam ser reais ou claramente ilustrativas).
- Remoção de fundo no vídeo inteiro (`npx hyperframes remove-background` ou equivalente). Confira bordas de cabelo e ombros em quadros de movimento.
- Não vale: layouts B e C do motor, câmera virtual, desfoque de movimento.
- Render a 60 fps direto.

## Entradas extras

Nenhuma obrigatória. Se houver pasta `imagens/`, os arquivos dela têm prioridade como provas.

## Ritmo e corte

- Regras de limpeza do motor.
- A posição e a escala da pessoa mudam a cada corte de frase (ver Layouts), o que dá ritmo mesmo sem trocar de tela.

## Layouts

Um layout só, com três enquadramentos da pessoa recortada que se alternam a cada corte:

| Enquadramento | Escala | Topo da cabeça | x do centro do corpo |
|---|---|---|---|
| Médio | corpo com 760 px de largura de ombros | y = 760 | 540 |
| Fechado | ombros com 900 px | y = 620 | 540 |
| Deslocado | ombros com 640 px | y = 1100 | 300 ou 780 (alterna) |

- O corpo sempre encosta na borda de baixo da tela.
- Nunca o mesmo enquadramento em dois trechos seguidos.
- Quando a prova é larga (antes e depois, dois cards), use Médio. Quando a prova é um card só, use Deslocado, com o card do lado oposto ao corpo.

### Fundo

- Preto `#000000`.
- Brilho laranja embaixo: elipse de 1400 × 700 px centrada em (540, 1920), de `rgba(204,116,48,0.55)` no centro a transparente, desfoque de 160 px. Atrás da pessoa.
- Um segundo brilho, mais fraco (`rgba(204,116,48,0.18)`), atrás do card de prova quando houver.

## Direção visual

- Fontes: Inter (400, 600, 700) e Instrument Serif itálico, locais.
- Laranja: `#CC7430`. Texto sobre preto: `#FFFFFF`.
- Cards de prova: **brancos**, `#FFFFFF`, raio 10 px, sombra `0 30px 80px rgba(0,0,0,0.6)`, padding de 32 px. Texto dentro em `#111111`.
- Acima de cada card, um rótulo pequeno em Inter 500 22 px `#A1A1AA`, dizendo o que é ("Post de exemplo, @seuperfil", "Matéria", "Antes", "Depois").

## Gráficos

As provas ficam entre y = 100 e y = (topo da cabeça − 60). Tipos:

- **Post de rede social** (480 × 470 px): avatar, nome, @, texto em Inter 400 28 px, imagem, linha de curtidas. Use o post real se for citado; se for um exemplo, deixe claro no rótulo "Post de exemplo".
- **Manchete de notícia** (560 × 420 px): nome do site em caixa alta (Inter 700 20 px), manchete em serifa (Instrument Serif 400, 48 px, `#111`), autor, imagem e linhas cinza. Use a página real da fonte quando a fala citar notícia (captura nítida, recortada no card).
- **Número gigante**: sem card. Número em Inter 700, 260 px, laranja `#CC7430`, com rótulo em Inter 600 40 px branco embaixo ("clientes novos"). Fica ao lado do card anterior, se houver.
- **Passos**: cards brancos estreitos (220 × 420 px) lado a lado, cada um com uma etiqueta preta no topo ("Gancho", "História", "Oferta"), aparecendo conforme a fala.
- **Antes e depois**: dois cards de 400 × 410 px lado a lado, rótulos "Antes" e "Depois" em etiquetas pretas, número grande dentro (Inter 700 120 px, preto no antes e laranja no depois) e um mini gráfico de linha.
- **Logo de produto**: logo oficial dentro de um card branco quadrado de 300 px.

Entrada dos cards: subida de 50 px + fade em 0,45 s (power3.out), com leve rotação de −2° a 2° que se endireita. Cada card fica até a ideia mudar; ao mudar, corte seco.

## Legendas

- Inter 700, 50 px, branca, sombra `0 4px 16px rgba(0,0,0,0.7)`.
- De 2 a 4 palavras por bloco.
- Centralizada no x da pessoa, com o centro 70 px acima do topo da cabeça (entre o card de prova e a cabeça). Se não couber, vai pra 60 px abaixo do card.
- Destaque a cada 2–3 blocos: uma palavra em Instrument Serif itálico laranja, 1,15× o tamanho.

## Capa e gancho

Durante o gancho (até o fim da primeira frase), com o enquadramento Médio:

- Título em duas palavras grandes atravessando o peito, centro em y = 1370: a primeira em Instrument Serif itálico branco, a segunda em Instrument Serif itálico laranja, 150 px, com sombra `0 8px 40px rgba(0,0,0,0.6)`.
- Embaixo, uma linha em Inter 700 46 px branca com o resto da ideia ("Posta todo dia / Ainda sem clientes").
- O título está completo no quadro 0 e fica até o primeiro corte depois do gancho.

## Chamada para ação

Se houver "comenta X": card branco de comentário (580 × 200 px) acima da cabeça, com avatar, a palavra X sendo digitada com cursor e um "Publicar" preto clicado no fim. Sem chamada na fala, não crie.

## Áudio

- Música: cinematográfica e escura, 70–85 BPM, pad grave contínuo, pulso de sintetizador suave e uma textura de piano espaçada. Sem bateria marcada. ~−25 LUFS.
- Efeitos: "papel" curto (ruído filtrado em banda média, 90 ms) na entrada de cada card de prova, "pop" grave no número gigante. Riser grave terminando no fim do gancho.

## Saída

`edit/final.mp4`, 1080 × 1920, 60 fps, H.264 + AAC 48 kHz.

## Verificação do estilo

- Recorte sem halo ou serrilhado visível em cabelo e ombros, inclusive em movimento.
- Nenhum card de prova encostando na cabeça ou cortado pela borda da tela.
- Provas reais conferidas (bloco de fontes) e exemplos marcados como "de exemplo" no rótulo.
- Enquadramento diferente a cada corte.
- Brilho laranja sempre atrás da pessoa, nunca por cima.
