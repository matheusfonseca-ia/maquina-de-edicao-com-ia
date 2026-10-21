# Reels com B-roll

Resumo: corte rápido, seus próprios clipes de apoio entrando por cima da fala e frases-chave empilhadas na legenda, com uma palavra grande em serifa laranja.

O visual descrito aqui (cores, fontes, materiais, legenda, música) é o **Original do formato**. Se a pessoa escolher outro estilo visual, o layout, as posições e o ritmo daqui continuam valendo e a aparência vem do estilo: siga `maquina-de-edicao/referencias/estilos-visuais.md`.

## Como fica

Vídeo vertical com cara de criador, sem gráfico nenhum. A pessoa fala pra câmera e, a cada ideia que dá pra mostrar, entra um clipe de apoio (B-roll) dela mesma: bastidor, rotina, tela do computador, lugar, produto. A legenda é pequena e limpa, mas nos momentos-chave a frase se empilha: uma palavra pequena em cima, e embaixo uma palavra grande em branco seguida de outra em serifa itálica laranja ("É o seu / **sistema.**").

## Escolhas que este formato já define

Proporção (vertical 9:16), nível (equivale ao Básico, mais os clipes de apoio), visual original da legenda (trocado se a pessoa escolher outro estilo visual; não tem gráficos), capa (sem caixa: o gancho é a própria legenda empilhada), verificação de fontes (desligada).

## Base técnica

- Vale: contato visual (bloco 3), pra decidir onde cobrir com B-roll quando a pessoa desvia o olhar.
- Não vale: layouts B e C, composições gráficas, câmera virtual, verificação de fontes.
- Render a 60 fps direto.

## Entradas extras

**Pasta `broll/`** dentro da pasta do projeto, com os clipes de apoio da pessoa (`.mp4`, `.mov`), verticais ou horizontais. Nomes descritivos ajudam ("computador-digitando.mp4", "cafe-manha.mov").

Na fase 0, se a pasta não existir ou estiver vazia, pergunte:

- **Vou colocar meus clipes na pasta `broll/` (Recomendado)**: espere a pessoa avisar que colocou e confira de novo.
- **Usar só imagens**: no lugar dos clipes, use imagens seguindo a ordem de origem de `formatos-prontos.md`, com um movimento lento de aproximação (escala 1 → 1,06 no trecho todo).
- **Sem B-roll**: o vídeo fica só com a câmera e a legenda empilhada.

### Como escolher os clipes

1. Rode `ffprobe` em cada clipe (orientação, duração).
2. Extraia 3 quadros de cada (início, meio, fim) e olhe o que mostram. Anote uma descrição curta de cada clipe em `edit/plano.md`.
3. Para cada frase da transcrição que dá pra ilustrar, case com o clipe que melhor mostra aquilo. Use o trecho mais estável do clipe (sem tremida, sem pessoa olhando pra câmera de outro vídeo).
4. Não repita o mesmo clipe, a não ser que a pasta tenha menos clipes que os pontos de B-roll. Nesse caso, use trechos diferentes do clipe.

## Ritmo e corte

- Cortes secos e rápidos. Reduza pausas acima de 180 ms pra cerca de 80 ms.
- B-roll cobre de 25% a 40% do tempo total, em inserções de 1,2 a 3 s.
- O áudio é sempre a voz da gravação principal. O áudio do clipe de apoio é descartado.
- Nunca coloque B-roll no gancho (primeira frase) nem na chamada pra ação: ali a pessoa aparece.
- Cada inserção começa e termina numa fronteira de palavra.

## Layouts

### A. Câmera cheia

Gravação em 1080 × 1920 por recorte proporcional, sem zoom.

### B-roll vertical

O clipe ocupa a tela inteira (recorte proporcional pra 1080 × 1920).

### B-roll horizontal

O clipe fica centralizado numa faixa de 1080 × 608 (y = 656 a 1264) sobre fundo preto puro. Não estique nem corte pra preencher a tela: o preto em cima e embaixo faz parte do visual.

## Direção visual

Sem cards, sem gráficos. O visual é a gravação, os clipes e a tipografia.

- Fontes: Inter (500, 600, 800) e Instrument Serif itálico, do Google Fonts, locais.
- Cor de destaque: laranja `#D9822B`.

## Gráficos

Nenhum além da legenda.

## Legendas

### Legenda normal

- Inter 600, 52 px, branca, sombra `0 3px 14px rgba(0,0,0,0.65)`, sem contorno.
- De 2 a 4 palavras por bloco.
- Posição: centralizada em x, centro do texto em y = 1130 (altura do peito) na câmera cheia e no B-roll vertical. No B-roll horizontal, y = 1180 (dentro da faixa, na parte de baixo).

### Frase empilhada (o destaque deste formato)

Uma vez a cada 6–10 segundos, na frase mais importante (a virada, a conclusão, o nome do passo):

- Linha de cima: 1 a 3 palavras em Inter 500, 46 px, branca, alinhada à esquerda do bloco.
- Linha de baixo: uma palavra em Inter 800, 120 px, branca, seguida de uma palavra em Instrument Serif itálico, 140 px, laranja `#D9822B`, com sombra `0 6px 28px rgba(0,0,0,0.55)`. As duas na mesma linha de base.
- O bloco inteiro fica centralizado em x, com o centro em y = 1180.
- Animação: a linha de cima aparece primeiro (fade 0,1 s), a palavra branca entra junto com a fala dela e a palavra laranja entra com subida de 20 px e fade em 0,25 s (power3.out), no instante em que é dita.
- Se a frase não couber em 1080 − 2 × 80 px, reduza o tamanho até caber (mínimo 90 px na linha de baixo).

Nunca duas frases empilhadas seguidas. Nunca empilhe artigo, preposição ou conjunção na linha de baixo.

## Capa e gancho

Sem caixa de título. No quadro 0 aparece, já pronta, a primeira frase empilhada do vídeo (a do gancho), pra servir de capa. Depois do quadro 0 ela some e volta no tempo certo.

## Chamada para ação

Se houver "comenta X": frase empilhada com "Comenta" em cima e a palavra X em laranja embaixo. Sem cartão.

## Áudio

- Música: lo-fi quente, 85–95 BPM, batida suave com chimbal discreto e acordes de piano elétrico abafados. ~−25 LUFS.
- Efeitos: só um "swish" curtinho e baixo (ruído filtrado, 120 ms, 18 dB abaixo do pico da voz) na entrada de cada frase empilhada. Nada nos cortes de B-roll. Sem riser.

## Saída

`edit/final.mp4`, 1080 × 1920, 60 fps, H.264 + AAC 48 kHz.

## Verificação do formato

- Nenhum B-roll no gancho nem na chamada pra ação.
- B-roll entre 25% e 40% do tempo.
- B-roll horizontal na faixa centralizada, com preto em cima e embaixo, sem distorção.
- Nenhum áudio dos clipes de apoio no mix.
- Frase empilhada sem cortar letra na borda e sem cobrir o rosto.
- No B-roll, nenhum quadro com a pessoa de outro clipe olhando pra lente enquanto a voz fala outra coisa.
