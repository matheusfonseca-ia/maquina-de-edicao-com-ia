# Reels de Negócio + Pixelado

Quando a pessoa escolhe o formato **Reels de Negócio** com o estilo visual **Pixelado**, o vídeo segue **este arquivo**, não os layouts do `formato.md`. É o formato dos reels do Matheus editados no estilo Opus Jake (os que foram aprovados sem correção): tela dividida com a câmera embaixo, gráfico em tela cheia e cena em pixel art em tela cheia, alternando a cada frase, e cada frase virando uma cena que mostra literalmente o que está sendo dito.

Prioridade: este arquivo vale por cima do `formato.md` do Reels de Negócio e por cima do `estilos-visuais/pixelado.md`. Onde este arquivo não fala nada, vale o `pixelado.md` (paleta, fontes, repertório de motions, peças) e depois o motor. Ajustes fixos salvos e observações da pessoa continuam valendo por cima de tudo.

Do `formato.md` só continuam: vertical 1080 × 1920, 60 fps, base técnica (contato visual, produtos citados, fontes e verificação), silêncios secos e a saída. **Não usar** do `formato.md`: câmera cheia, gancho com cards atrás da cabeça, título de capa em duas linhas, tela dividida meio a meio, legenda de uma palavra por vez, pílula de notificação no CTA, Kit Noite.

## Cenas-modelo

A pasta `cenas-modelo/` (ao lado deste arquivo) tem cenas HyperFrames de vídeos aprovados neste formato. **Abra as do tipo de cada cena antes de construir** e copie a estrutura, as convenções e o acabamento, trocando o conteúdo. O `cenas-modelo/LEIA.md` diz o que cada uma mostra.

## A ideia central

**Cada frase falada vira uma pequena cena que mostra literalmente o que está sendo dito.** "Respostas ruins" vira um cemitério de lápides; "faz 100 versões" vira o mascote se multiplicando até uma grade de 10 × 10 com contador "×100"; "grátis" vira um carimbo verde batendo sobre a página do repositório; "o Claude matou o Instagram" vira o mascote com uma espada cortando o celular, a tela trincando e uma lápide com o logo do Instagram. Não existe cartão genérico com ícone e título.

**Cada efeito acontece na palavra que o nomeia** (o carimbo "GRÁTIS" bate em "gratuito", o contador sobe em "onze", o interruptor liga em "conectar"). Use os tempos das palavras na faixa final.

Antes de construir, escreva em `edit/plano.md` a tabela **"# · início · fim · layout · frase · metáfora visual"** do vídeo inteiro, com os tempos das palavras que disparam cada efeito. Se não achar metáfora pra uma frase, use a peça real (print da página, terminal, chat, repositório) com uma ação em cima (cursor, risco, contorno, carimbo).

## Layouts (1080 × 1920)

**A câmera nunca fica em tela cheia.** Três layouts, trocados sempre por **corte seco**:

### D. Dividido (o principal, ~50–60% do vídeo)

- **Faixa de cima (y 0 a 770):** fundo creme `#EFEDEB` com grade bem fraca (linhas de 2 px a cada 90 px, `#E6E4E1`: `background-image: linear-gradient(#e6e4e1 2px, transparent 2px), linear-gradient(90deg, #e6e4e1 2px, transparent 2px); background-size: 90px 90px; background-position: -1px -1px`).
- **Cartão:** x 90 a 990 (900 px), y 255 a 700 (445 px), raio 28, fundo `#F9F8F6`, sombra `0 18px 40px rgba(0,0,0,.10)`. Pode crescer pra cima até y ≈ 200, **nunca abaixo de y 700**. Selos, chips e cursores podem ficar fora do cartão, na faixa creme, sempre acima de y 700. O conteúdo do cartão muda a cada frase.
- **Câmera (y 770 a 1920):** largura total, **borda reta**, sem moldura, sem cartão arredondado, sem cabeça saindo pra fora. Corte horizontal seco entre o creme e o vídeo. O vídeo é posicionado pra que os olhos fiquem em ~y 1180 (com enquadramento de selfie comum, o topo do vídeo de 1080 × 1920 fica em ~y 500 e só aparece a parte abaixo de 770). Enquadramento fixo: sem zoom, sem punch-in, sem acompanhamento de cabeça.

### F. Gráfico cheio (~25–40%)

- Fundo creme quadriculado na tela inteira, opaco (sem câmera).
- Elemento principal em x 90 a 990. Conteúdo em duas zonas: **acima da legenda (y 200 a 700)** e **abaixo (y 830 a 1500)**. Terminal ou print grande podem descer até y ≈ 1440.

### P. Pixel art cheia (~10–15%, 1 ou 2 por vídeo, no clímax)

- Cena pixel art opaca em 1080 × 1920 (cenário + personagens em sprite andando, se multiplicando, se enfrentando, caindo).
- HUD em Silkscreen dentro de caixa preta `#151513` com borda `#3A3836`; número em dourado `#E8B547` (contador descendo ou subindo, "VENCEDOR" com confete).
- Deixe a faixa y 721 a 807 sem nada importante (é da legenda).

### Distribuição

- **Gancho: D**, com a cena mais forte e mais estranha do vídeo, com bastante ação (ex: celular com o feed → mascote salta com espada → corte diagonal → tela trinca com glitch → lápide "RIP" → carimbo "MORTO"). Nunca gancho em câmera cheia, nunca título de capa: o quadro 0 já é o dividido com a cena começando e a primeira legenda.
- **CTA: D**, com o cartão do CTA na faixa de cima (acima da cabeça), do momento em que a pessoa fala "comenta X" até o fim.
- **Clímax** (a virada, o resultado, a briga, a comparação): P.
- O resto alterna D e F. **Dois trechos seguidos nunca usam o mesmo layout.**
- Estrutura típica: gancho (D) → nome do produto ou da ideia (cartão de produto) → como funciona (alterna F e D) → clímax (P) → benefício (antes riscado, depois aparecendo) → como instalar ou usar (print → seta → chat) → CTA (D).

## Ritmo

- Uma cena nova a cada **1,3 a 3 s** de fala (≈ uma por frase ou meia frase). Nenhuma cena passa de 5 s, a não ser o CTA.
- Dentro da cena, algo muda a cada **0,3 a 0,6 s** (elemento entra, contador sobe, risco é desenhado, palavra é digitada). A tela nunca fica parada.
- Cortes de silêncio secos: nenhuma pausa acima de 150 ms na voz (alvo ~110 ms).
- Tomadas repetidas: use a última tomada completa de cada frase.

## Legenda

- **Pílula escura** `#3A3836` a 92%, raio 12, altura 86, folga lateral 34; a largura acompanha o texto (até ~840 px).
- **JetBrains Mono ExtraBold (800), caixa alta**, branco, 52 px, `letter-spacing: 0.08em`.
- **2 a 3 palavras por bloco**, troca seca, sem animação de entrada, sem palavra por palavra, sem cor de destaque.
- **Posição fixa em todos os layouts:** centro em x 540, y 764 (pílula de y 721 a 807), na emenda do dividido (metade sobre o creme, metade sobre a câmera). Nunca muda de lugar.
- Começa no quadro 0. Mantém apóstrofo e interrogação; sem ponto final.

## Peças e movimento

Paleta, fontes e repertório de motions: os do `pixelado.md` (multiplicação com contador, cartão de produto, print real, carimbo, terminal, chat, anotação à mão, cartão de tarefa, personagens cercando, mini cartões, linha de etapas, cartas, etiquetas de crítica em pixel, cronômetro, fluxo de instalação, duelo e vencedor). Além disso:

- **Mascote do Claude Code** quando o assunto é Claude (12 × 8 blocos, terracota `#D97757`, olhos pretos):
  ```
  ..BBBBBBBB..
  ..BBBBBBBB..
  ..BEBBBBEB..
  BBBEBBBBEBBB
  BBBBBBBBBBBB
  ..BBBBBBBB..
  ..B.B..B.B..
  ..B.B..B.B..
  ```
  Acessórios (espada, lupa, café, viseira) em blocos extras. Assunto sem mascote próprio: mascote pixel simples ligado ao tema.
- **Marca citada na fala usa o logo oficial** (Claude, Instagram, GitHub, X…), nunca um personagem ou texto genérico no lugar. Logos em SVG oficial (ex: Simple Icons) dentro de `projeto/assets/img/`.
- **Perfis de terceiros** são genéricos (avatar de cor lisa com inicial, "@perfil_exemplo"). O perfil da pessoa (foto e @) aparece quando a fala diz "sua conta", "seu perfil" e no CTA: peça a foto de perfil se não estiver na pasta.
- **Simetria:** elementos de cada cena alinhados de forma simétrica e harmônica, mesma linha de base, mesmas distâncias do eixo x 540.
- Entradas: `opacity 0 → 1`, subida de 10 px, escala 0,96 → 1, 0,25 s, `power2.out`. Texto digitado letra a letra com cursor de bloco (passos de 0,03 a 0,05 s). Contadores rolando. Grades em cascata (20 a 30 ms). Traços com `stroke-dashoffset` (~0,3 s). Carimbo: escala 1,6 → 1, girado −8 a −12°, tremida curta.
- Sem câmera virtual, sem desfoque de movimento, sem whip pan. **O quadro 0 de cada cena já mostra conteúdo útil** (corte seco), nunca o cartão vazio.
- Valores ilustrativos (curtidas, notas, contadores que não estão na fala) são permitidos se forem claramente ilustrativos e registrados no relatório; números ditos na fala aparecem como foram ditos.

## CTA

Dividido. Cartão na faixa de cima com duas linhas numeradas por círculos terracota:

1. Foto de perfil da pessoa com anel de story + "Seguir" (Inter 700) + @perfil, e botão azul "Seguir" que vira "Seguindo" cinza.
2. "Comente" + campo onde a palavra-chave é digitada em caixa alta, com contorno terracota.

Embaixo, pequeno: "✈ Te envio na DM". Na palavra "DM" (ou "direct"), uma notificação de DM chega acima do cartão. Fica até o fim. Modelo: `cenas-modelo/cta.html`.

## Montagem (HyperFrames)

- `index.html` 1080 × 1920, 60 fps. Faixa 0: câmera cortada contínua, visível só na janela y 770 a 1920 (as cenas D pintam só y 0 a 770 e deixam o resto transparente; F e P cobrem a tela). Faixa 2: uma sub-composição por cena (`compositions/c01-<nome>.html`…). Faixa 4: legendas (`compositions/legendas.html`). Depois as faixas de áudio.
- Contrato de cada cena (o que faz as cenas-modelo funcionarem):
  - `<template>` com `<style>`, `#root` e `<script>` dentro; `#root` com `data-composition-id`, `data-width="1080"`, `data-height="1920"`, `data-duration` = duração da cena. Tempo local = tempo global − início da cena.
  - Um único `gsap.timeline({ paused: true })` registrado em `window.__timelines["<id>"]`, terminando com `tl.set({}, {}, <duração>)`.
  - **Prefixe todas as classes, ids e nomes de fonte com o id da cena** (`c07-…`, `"C07 Inter"`): os estilos de todas as cenas se juntam numa página só.
  - Fontes locais por `@font-face` (`../assets/fonts/`): JetBrains Mono, Inter, Newsreader, Silkscreen, Caveat.
  - Estados iniciais com `gsap.set(...)` antes da timeline (um `tl.set` na posição 0 não aparece no quadro 0). Cuidado com `tl.fromTo`: o "from" é aplicado no quadro 0 da cena; use só se o "from" for invisível, ou `immediateRender: false`.
  - Proibido: `Math.random` (use gerador com semente fixa), relógio, rede, `repeat: -1`. Pixel art de cenário num `<canvas>` pequeno com `image-rendering: pixelated`; personagens animados como grade de `div`s de 12 px ou mais.
  - Nenhum texto gráfico menor que 30 px (rótulo mono secundário: 26 px no mínimo). Contraste mínimo 3:1.
- Vídeo com muitas cenas: dá pra dividir a construção entre ajudantes em paralelo (4 a 6 cenas cada), todos com o mesmo guia (`edit/work/brief-cenas.md` com o contrato acima, a geometria, as peças comuns do vídeo e os tempos das palavras) e as cenas-modelo.

## Áudio

- Clima da música e efeitos: os do `pixelado.md`, filtrados pelos ajustes fixos da pessoa.
- Riser curto terminando exatamente no fim do gancho.
- Cada cena lista seus eventos de som (tempo global + tipo: pop, carimbo, clique, confirmação, moeda, 8 bits…) e o motor mixa tudo num `sfx.wav`.

## Verificação (além da do motor)

- Câmera só embaixo, com borda reta em y 770; nunca em tela cheia.
- Nenhum par de cenas seguidas com o mesmo layout; os três layouts aparecem (P pelo menos uma vez, no máximo duas).
- Nas cenas D, nada abaixo de y 700 além da câmera.
- Legenda fixa em y 764 em todos os quadros, sem cobrir nada importante; quadro 0 com cena + legenda.
- Cada efeito na palavra que o nomeia (confira 3 ou 4 nos quadros).
- Cortes de cena conferidos nos dois lados em quadros reais: a cena nova aparece desde o primeiro quadro previsto.
- Compare snapshots com as cenas-modelo: mesmo acabamento (hierarquia, alinhamento simétrico, nada cortado, texto legível).
