# Nuvem de Imagens

Resumo: você em tela cheia e, acima da sua cabeça, grupos de imagens que aparecem e se sobrepõem conforme você fala, com uma legenda pequena, minúscula e discreta à esquerda.

## Como fica

Visual calmo e editorial. A pessoa fica na câmera o tempo todo, e o terço de cima da tela vira um mural: a cada ideia, uma imagem aparece; a próxima chega por cima, levemente deslocada, até formar um grupinho de 2 ou 3. Quando a ideia muda, o grupo some e começa outro. A legenda é pequena, em letra minúscula, alinhada à esquerda, sem destaque nenhum: quem chama atenção são as imagens.

## Escolhas que este estilo já define

Formato (vertical 9:16), nível (equivale ao Com imagens, só com o layout de câmera cheia), estilo das legendas, estilo visual, capa (primeiro grupo de imagens já montado + legenda), verificação de fontes (ligada só pra notícia ou número citado).

## Base técnica

- Vale: produtos citados (logo e interface viram imagens do grupo), fontes e verificação quando houver notícia.
- Não vale: layouts B e C, contato visual (a pessoa pode olhar pros lados à vontade), câmera virtual.
- Render a 60 fps direto.

## Entradas extras

Nenhuma obrigatória. Pasta `imagens/` tem prioridade. Siga a ordem de origem de `estilos-prontos.md`.

Este estilo usa **muitas** imagens (uma a cada 2–4 s de fala). Antes de construir, monte em `edit/plano.md` a lista de imagens com: tempo, palavra que a chama, origem e arquivo. Prefira fotos e capturas reais a cards de último recurso: se mais de 30% das imagens forem cards de último recurso, reduza o número de imagens (uma a cada 4–6 s) em vez de encher de card genérico.

## Ritmo e corte

Regras de limpeza do motor. Os cortes de frase não mudam nada na tela além da gravação: as imagens seguem a lógica das ideias, não dos cortes.

## Layouts

Só câmera cheia: gravação em 1080 × 1920 por recorte proporcional, sem zoom. Se o topo da cabeça estiver acima de y = 700, faça o recorte um pouco mais baixo (sem zoom, só posicionamento) pra liberar espaço em cima. Se não der, reduza a área das imagens.

### Área das imagens

Retângulo de x = 60 a 1020 e y = 180 a (topo da cabeça − 50). Normalmente y = 180 a 760.

## Direção visual

- Sem fundo extra: a própria gravação é o fundo.
- Fontes: Inter (500), local.
- Imagens: raio 6 px, sombra `0 24px 60px rgba(0,0,0,0.45)`, sem borda. Uma etiqueta minúscula no canto inferior esquerdo de cada imagem, em Inter 500 16 px, caixa alta, `rgba(255,255,255,0.7)`, dizendo de onde é ("FONTE: G1", "INSTAGRAM", "FOTO") só quando for imagem real de terceiro.

## Gráficos

### Grupo de imagens

- Cada grupo tem de 1 a 3 imagens e dura uma ideia (normalmente de 3 a 8 s).
- Tamanhos: a primeira imagem com 360 a 470 px de largura; as seguintes entre 280 e 390 px. Mantenha a proporção original de cada imagem (paisagem, quadrada ou retrato).
- Posições:
  - 1 imagem: centrada na área ou deslocada pra esquerda (x do centro entre 330 e 540).
  - 2 imagens: lado a lado com sobreposição de 0 a 60 px, a segunda 20 a 60 px mais baixa ou mais alta.
  - 3 imagens: duas em cima, uma embaixo no meio, sobrepondo as duas em 40–80 px.
- Varie as posições entre grupos: nunca dois grupos seguidos com o mesmo arranjo.
- Rotação: 0° (sem inclinação).

### Animação

- Cada imagem entra no instante da palavra que a chama: fade + escala 0,96 → 1 + subida de 16 px, em 0,4 s (power2.out).
- As imagens já presentes não se mexem quando uma nova chega.
- Troca de grupo: as imagens antigas saem juntas com fade de 0,2 s; o próximo grupo começa 0,1 s depois.
- Pausas de imagem: pode haver trechos curtos (1–2 s) sem imagem nenhuma entre grupos, pra respirar.

## Legendas

- Inter 500, 34 px, branca, **tudo minúsculo**, sem destaque, sombra `0 2px 10px rgba(0,0,0,0.6)`.
- Até 2 linhas de ~22 caracteres. Bloco de 3 a 7 palavras.
- **Alinhada à esquerda**, x = 70, com o topo do bloco em y = (topo da cabeça + 90), ao lado do rosto. Se o rosto estiver muito à esquerda, alinhe à direita em x = 1010.
- Pontuação mínima: tire pontos finais, mantenha interrogação.
- Entra e sai com fade de 0,1 s.

## Capa e gancho

No quadro 0: o primeiro grupo de imagens do vídeo já montado e a primeira legenda completa. Sem título extra. Escolha pra esse primeiro grupo a imagem mais forte do vídeo.

## Chamada para ação

Se houver "comenta X": uma imagem do grupo final é um card de comentário claro (Inter, fundo `#FFFFFF`, 420 × 140 px) com a palavra X, que aparece já escrita. Sem animação de digitação.

## Áudio

- Música: acústica e leve, 90–100 BPM, violão dedilhado ou piano com pad suave. ~−25 LUFS.
- Efeitos: um clique de papel bem baixo (16 dB abaixo do pico da voz) em cada imagem que entra. Sem riser.

## Saída

`edit/final.mp4`, 1080 × 1920, 60 fps, H.264 + AAC 48 kHz.

## Verificação do estilo

- Nenhuma imagem encostando ou cobrindo a cabeça.
- Nenhuma imagem cortada pela borda da tela.
- Imagens nítidas (sem upscale borrado acima de 1,5×).
- Cada imagem entra no máximo 2 quadros antes da palavra que a chama.
- Legenda sempre minúscula e sem cobrir o rosto.
- Origem de cada imagem no relatório.
