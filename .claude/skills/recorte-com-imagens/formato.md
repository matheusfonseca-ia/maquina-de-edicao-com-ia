# Recorte com Imagens

Resumo: você recortado (sem o fundo da gravação) na frente de imagens em tela cheia que trocam a cada ideia, mudando de tamanho e de lugar na tela, com legenda condensada no meio.

O visual descrito aqui (cores, fontes, materiais, legenda, música) é o **Original do formato**. Se a pessoa escolher outro estilo visual, o layout, as posições e o ritmo daqui continuam valendo e a aparência vem do estilo: siga `maquina-de-edicao/referencias/estilos-visuais.md`.

## Como fica

O fundo real da gravação some. Atrás da pessoa, uma imagem ocupa a tela inteira e troca a cada ideia: um lugar, um objeto, uma tela, um gráfico. A pessoa também muda: às vezes grande e centralizada, às vezes pequena num canto, como se fosse colada sobre a imagem. A legenda é condensada, branca, com sombra, no meio da tela. O gancho abre com um mosaico de 4 imagens e um título em caixa branca.

## Escolhas que este formato já define

Proporção (vertical 9:16), nível (equivale ao Com imagens, com um layout próprio), visual original da legenda e dos gráficos (trocado se a pessoa escolher outro estilo visual), capa (mosaico + título em caixa branca), verificação de fontes (ligada só pra notícia ou número citado).

## Base técnica

- Remoção de fundo no vídeo inteiro (`npx hyperframes remove-background` ou equivalente). Confira cabelo, ombros e mãos em movimento.
- Vale: produtos citados, fontes e verificação quando houver notícia.
- Não vale: layouts B e C do motor, câmera virtual, contato visual obrigatório.
- Render a 60 fps direto.

## Entradas extras

Nenhuma obrigatória. Pasta `imagens/` tem prioridade; depois, a ordem de origem de `formatos-prontos.md`.

As imagens aqui ocupam a tela inteira, então precisam de resolução: mínimo 1080 px no lado menor depois do recorte pra 9:16. Imagens horizontais pequenas viram fundo desfocado (ver Gráficos).

## Ritmo e corte

- Regras de limpeza do motor.
- Uma imagem de fundo nova a cada ideia: normalmente a cada 2,5 a 5 s. Nunca a mesma imagem por mais de 7 s.
- A pessoa muda de enquadramento junto com a troca de fundo.

## Layouts

### A. Recorte sobre imagem (principal)

Camadas, de trás pra frente:

1. Imagem de fundo em 1080 × 1920 (recorte proporcional, sem distorção).
2. Escurecimento leve: `rgba(0,0,0,0.18)` na tela toda, mais um gradiente de transparente (y = 1200) a `rgba(0,0,0,0.35)` (y = 1920).
3. A pessoa recortada, com sombra suave atrás (`drop-shadow(0 20px 50px rgba(0,0,0,0.45))`).
4. Legenda.

Enquadramentos da pessoa (alterne; nunca o mesmo duas vezes seguidas):

| Nome | Largura dos ombros | Posição |
|---|---|---|
| Grande central | 900 px | centrada em x, corpo encostando na borda de baixo |
| Pequena no canto de cima | 420 px | x do centro = 260 ou 820, cortada logo abaixo dos ombros com borda reta em y = 720 |
| Média lateral | 560 px | x do centro = 330 ou 750, corpo encostando na borda de baixo |
| Pequena no meio | 420 px | centrada, cortada abaixo dos ombros em y = 1230 |

Quando a pessoa fica "pequena e cortada", o corte de baixo é uma linha reta (como uma foto colada), não um degradê.

### B. Mosaico (só no gancho)

Grade 2 × 2 de imagens (cada uma 540 × 960) na tela toda, sem espaço entre elas, com a pessoa recortada Grande central por cima e o título do gancho (ver Capa).

## Direção visual

- Fontes: **Oswald** 300 e 500 (condensada, Google Fonts) pras legendas; **Inter** 700 pro título do gancho. Locais.
- Texto branco `#FFFFFF`.
- Nenhum elemento gráfico além da legenda e do título.

## Gráficos

### Imagens de fundo

- Uma por ideia. Case pela palavra que mais "desenha" a ideia (lugar, objeto, ação, resultado).
- Imagem pequena ou horizontal: use como fundo uma cópia ampliada e desfocada (40 px, brilho 0,8) e, por cima, a imagem nítida centralizada num retângulo de 1000 px de largura com raio 12 px, entre y = 200 e y = 900. Nesse caso a pessoa usa o enquadramento Média lateral ou Pequena no meio.
- Movimento leve em todas: aproximação lenta de 1 → 1,05 durante o trecho (linear). Nunca movimento rápido.
- Troca de imagem: corte seco junto com a troca de enquadramento da pessoa, numa fronteira de palavra.

## Legendas

- Oswald 300, 58 px, branca, sombra `0 3px 14px rgba(0,0,0,0.7)`, `letter-spacing: 0.01em`.
- Frase de 3 a 6 palavras, em uma linha (quebra em duas só se passar de 960 px).
- Centralizada em x, centro em y = 960 (meio da tela). Se a pessoa estiver "pequena no meio", a legenda vai pra y = 1320.
- Sem palavra de destaque. Sem caixa alta.

## Capa e gancho

Durante a primeira frase, layout Mosaico:

- Título em caixa branca centrada em y ≈ 480: duas linhas em Inter 700, 64 px, texto `#111111`, cada linha numa caixa branca própria justa ao texto (padding 12 × 22 px, raio 14 px), as caixas com 6 px de espaço entre si.
- Embaixo, uma linha pequena entre parênteses em Inter 500 34 px branca com sombra, complementando ("(não é o seu conteúdo)").
- No quadro 0 o título já está completo. Ele fica até o fim do gancho.

## Chamada para ação

Se houver "comenta X": no último trecho, a legenda vira "comenta X" com X em Oswald 500 72 px. Sem cartão.

## Áudio

- Música: indie eletrônica com textura, 95–105 BPM, batida leve, sintetizador quente e um arpejo discreto. ~−24 LUFS.
- Efeitos: um "tchk" de corte de filme bem baixo (ruído curto filtrado, 60 ms, 18 dB abaixo do pico da voz) nas trocas de imagem, respeitando no máximo 1 a cada 0,6 s. Riser curto terminando no fim do gancho.

## Saída

`edit/final.mp4`, 1080 × 1920, 60 fps, H.264 + AAC 48 kHz.

## Verificação do formato

- Recorte limpo em todos os enquadramentos, sem halo e sem pedaços do fundo real.
- Nenhuma imagem de fundo esticada ou pixelada.
- Troca de imagem e de enquadramento no mesmo quadro.
- Legenda legível sobre todas as imagens (se o fundo for muito claro naquela área, aumente o escurecimento só naquele trecho).
- Origem de cada imagem no relatório.
