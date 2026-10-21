---
name: maquina-de-edicao
description: Edita um vídeo falado (gravação bruta pra câmera) do começo ao fim usando código (FFmpeg, Python, Node e HyperFrames). Logo no começo a pessoa escolhe se quer editar do zero (respondendo algumas perguntas) ou com um formato pronto. No formato pronto ela escolhe primeiro o formato, entre 12 (Reels de Negócio, Reels com B-roll, Tela Dividida Explicativa, Ensaio Visual, Legenda Encaixada, Nuvem de Imagens, Recorte com Imagens, Telas em Profundidade, Formato Ranking, Cortes de Vídeo Longo, YouTube Educativo, Aula em Tela Dividida), e depois o estilo visual (Original do formato, Pixelado, Noite Laranja, Claro Tecnológico ou outro que ela criou). Edita sozinha, abre o resultado no HyperFrames Studio pra revisão e só exporta o MP4 depois da aprovação. Salva as preferências do vídeo aprovado e oferece repetir na próxima edição. Também guarda estilos copiados de vídeos de referência. Use quando o usuário chamar /maquina-de-edicao, disser "edita meu vídeo", "editar vídeo", "quero editar essa gravação", "transforma meu vídeo em reels", "quais formatos tem", "quais estilos de edição tem" ou pedir pra editar uma gravação bruta, e também quando pedir pra "analisar o estilo de edição desse vídeo", "salvar esse estilo", "copiar a edição desse reel" ou "criar um estilo visual novo".
---

# Máquina de Edição

Você vai transformar a gravação bruta do usuário num vídeo finalizado. Existem dois caminhos, e a pessoa escolhe logo no começo:

- **Do zero**: a pessoa responde algumas perguntas (proporção, nível, legenda, visual, música) e o vídeo sai do jeito que ela montou.
- **Formato pronto**: a pessoa escolhe **primeiro o formato** (a estrutura: um dos 12 formatos prontos, ou um estilo que ela copiou de um vídeo de referência) e **depois o estilo visual** (a aparência: cores, fontes, legenda, música). O vídeo sai naquele formato e naquele visual, quase sem perguntas.

Formato e estilo visual são independentes: qualquer formato combina com qualquer estilo visual. Ex: Formato Ranking + Pixelado = tier list com cara de videogame.

Cada formato pronto também é uma skill própria (ex: `/reels-de-negocio`). Quando a pessoa chama a skill do formato direto, ela cai aqui com o formato já escolhido e só escolhe o estilo visual.

O fluxo tem três fases:

1. **Entrevista**: entender como a pessoa quer o vídeo (poucas perguntas, todas com opção recomendada).
2. **Edição autônoma**: fazer tudo sozinho, sem novas perguntas, até o vídeo estar montado no HyperFrames Studio.
3. **Revisão e exportação**: a pessoa assiste no Studio, pede ajustes, e você só exporta o MP4 quando ela aprovar.

Depois da exportação, as preferências do vídeo aprovado ficam salvas. Na próxima edição, a skill oferece "Repetir o último vídeo" junto com os outros dois caminhos.

Fale com o usuário em português do Brasil, de forma simples e direta. A maioria dos alunos é iniciante: evite jargão técnico nas perguntas e nas mensagens de progresso.

Arquivos de apoio (leia antes da fase 2):

- `referencias/instrucoes-base.md`: as instruções completas de edição, divididas em blocos marcados por nível.
- `referencias/variacoes.md`: o que muda em cada bloco conforme as respostas (proporção horizontal, câmera vertical, visual, legendas, música, efeitos).
- `referencias/formatos-prontos.md`: o catálogo dos 12 formatos, onde fica cada um e como um formato se aplica por cima das instruções base.
- `referencias/estilos-visuais.md`: o que é um estilo visual, onde ficam, como aparecem na pergunta e como se aplicam por cima de um formato.
- `referencias/kit-noite.md`: o kit visual escuro (fundo preto, brilho laranja, cards de vidro, Inter + Instrument Serif) que vários formatos usam no visual original e o estilo Noite Laranja usa.

Formatos prontos: cada um numa pasta ao lado desta skill, `<pasta de skills>/<nome-do-formato>/formato.md` (a pasta de skills é a pasta-mãe desta). O catálogo está em `referencias/formatos-prontos.md`.

Estilos visuais: `estilos-visuais/*.md` dentro desta skill (os que vêm com a Máquina: Pixelado, Noite Laranja, Claro Tecnológico) e `~/.maquina-de-edicao/estilos-visuais/*.md` (os que a pessoa criou). Arquivos que começam com `_` são modelos e não aparecem na lista. Pra criar um estilo novo, o modelo é `estilos-visuais/_modelo.md`.

Preferências salvas do usuário (criado pela própria skill depois do primeiro vídeo aprovado):

- `~/.maquina-de-edicao/preferencias.md`: as escolhas da entrevista e os ajustes de gosto pessoal do último vídeo aprovado. Fica fora da pasta da skill pra não se perder quando a skill for atualizada. Formato na seção "Fase 5". Arquivos antigos podem ter a linha "Formato: Vertical 9:16": ela quer dizer a proporção.
- `~/.maquina-de-edicao/estilos/<nome>.md` (+ pasta `<nome>/` com quadros de referência): estilos copiados de vídeos de referência. Eles definem estrutura **e** aparência juntos, por isso aparecem na lista de formatos, como "seus estilos salvos". Cada arquivo começa com uma linha "Resumo:" e uma seção "Escolhas que este estilo já define". Como criar um: seção "Criar um estilo a partir de um vídeo de referência", no fim deste arquivo.

---

## Fase 0: Checar a pasta

Antes de qualquer pergunta, liste os arquivos da pasta atual.

- **Vídeo** (`.mp4`, `.mov`, `.mkv`, `.webm`, `.m4v`): se não houver, pare e explique que o vídeo bruto precisa estar nesta pasta. Se houver mais de um, pergunte qual editar.
- **Áudio** (`.wav`, `.mp3`, `.m4a`, `.aac`, `.flac`): se houver, pergunte o que é: "áudio limpo da minha voz (microfone/lapela)", "música que quero usar" ou "não usar".
- Rode `ffprobe` no vídeo e anote: orientação (horizontal ou vertical), resolução, fps e duração. Não pergunte a orientação da gravação ao usuário; detecte.
- Se o arquivo estiver corrompido ou ilegível, pare e avise.
- Verifique se existe `~/.maquina-de-edicao/preferencias.md`. Se existir, leia.
- Leia `referencias/formatos-prontos.md` e confira quais pastas de formato existem ao lado desta skill.
- Liste os estilos visuais (`estilos-visuais/*.md` desta skill e `~/.maquina-de-edicao/estilos-visuais/*.md`, sem os que começam com `_`). De cada um, leia só o título e as linhas "Resumo:" e "Combina com:".
- Liste os estilos salvos pela pessoa em `~/.maquina-de-edicao/estilos/*.md`. De cada um, leia só o título e a linha "Resumo:".
- **Se a skill foi chamada por uma skill de formato** (ex: a pessoa digitou `/reels-de-negocio`), o formato já está escolhido: pule a pergunta "Como quer editar este vídeo?" e a pergunta de formato, e siga direto pro passo 2 do "Caminho formato pronto" na fase 1.
- A pasta precisa ter o que o formato pede na seção "Entradas extras" do `formato.md` (ex: o Reels com B-roll procura uma pasta `broll/`). Essa checagem acontece depois que o formato é escolhido.

## Fase 1: Entrevista

### Como quer editar este vídeo?

A primeira pergunta é sempre **"Como quer editar este vídeo?"** (exceto quando a skill foi chamada por uma skill de formato). Opções:

- **Com um formato pronto**: escolhe o formato e depois o estilo visual, e o vídeo sai daquele jeito, quase sem perguntas.
- **Do zero**: você escolhe cada detalhe (proporção, nível, legenda, visual, música).
- **Repetir o último vídeo**: usa as preferências salvas (formato, estilo visual e ajustes). Só ofereça se existir `preferencias.md`.

Marque como "(Recomendado)" o "Repetir o último vídeo" se houver preferências salvas. Se não houver, marque "Com um formato pronto".

- "Repetir o último vídeo" → siga "Repetir o último vídeo (preferências salvas)" mais abaixo.
- "Do zero" → siga "Caminho do zero".
- "Com um formato pronto" → siga "Caminho formato pronto".

### Caminho formato pronto

**1. Qual formato.** Mostre o catálogo de `referencias/formatos-prontos.md` como uma lista numerada em texto (são mais de 4 opções, então não use a ferramenta de múltipla escolha aqui), separada em "Vertical 9:16" e "Horizontal 16:9", com o nome e a descrição curta de cada formato. No fim da lista, numa parte "Seus estilos salvos", acrescente os estilos que a pessoa copiou de vídeos de referência (`~/.maquina-de-edicao/estilos/`), com o nome e o resumo. Peça pra pessoa responder com o número ou o nome.

Ajude a escolher se a pessoa estiver em dúvida: olhe a duração e a orientação da gravação. Gravação acima de 10 minutos combina com Cortes de Vídeo Longo, YouTube Educativo ou Aula em Tela Dividida. Gravação curta combina com os formatos verticais.

**2. Ler o formato.** Leia o `formato.md` inteiro do formato escolhido (ou o arquivo do estilo salvo). Se ele tiver "Entradas extras", confira a pasta agora e siga o que ele manda quando faltar alguma coisa.

**3. Qual estilo visual.** Pergunte **"Qual estilo visual?"**, mostrando:

- **Original do formato**: o visual descrito no próprio `formato.md`. Descreva em poucas palavras o que é (ex: "preto com brilho laranja e cards de vidro").
- Um item por estilo visual listado na fase 0, com o nome e o resumo. Esconda o que for igual ao original do formato (ver `referencias/estilos-visuais.md`). Se o estilo tiver "Combina com" e o formato não estiver na lista, mostre mesmo assim, sem recomendar.

Marque como "(Recomendado)" o estilo visual das preferências salvas, se houver; se não, "Original do formato". Com até 4 opções, use a ferramenta de múltipla escolha; com mais, lista numerada em texto.

Se o escolhido no passo 1 foi um estilo salvo de vídeo de referência, ele já define a aparência: pule esta pergunta (a pessoa ainda pode pedir pra trocar o visual, e aí o estilo visual escolhido vale por cima do visual do estilo salvo).

Leia o arquivo inteiro do estilo visual escolhido (se não for o Original do formato) e a seção "Como aplicar um estilo visual a um formato" de `referencias/estilos-visuais.md`.

**4. Perguntas.** Não faça a "Padrão completo ou personalizar?" nem as perguntas listadas em "Escolhas que este formato já define". Faça só **uma rodada**, com as perguntas que ficam em aberto (normalmente estas):

- **Música de fundo?** Opções: "A do estilo (Recomendado)", que é o clima descrito no estilo visual (ou na seção Áudio do formato, no Original); "Usar a música que está na pasta" (só se houver arquivo de música); "Sem música".
- **Efeitos sonoros?** Opções: "Os do estilo (Recomendado)" ou "Nenhum".
- **Cor de destaque?** Opções: "A do estilo (Recomendado)" ou "A cor da minha marca" (peça o hex em seguida). Se as preferências salvas já tiverem cor de marca, a recomendada passa a ser essa.
- **Título de capa:** só se o formato tiver capa e a pessoa quiser escrever o próprio título. Pergunte: "Crio o título a partir do gancho (Recomendado)" ou "Eu escrevo".

Se a pessoa tiver preferências salvas com ajustes fixos, pergunte junto: "Aplicar seus ajustes fixos neste vídeo?" (ex: "legendas 15% maiores"). Recomende "Sim". Se o arquivo tiver uma seção `## Ajustes do formato <este formato>` ou `## Ajustes do estilo visual <este estilo>`, ela vale sempre que esse formato ou estilo for usado, sem perguntar. Mostre esses ajustes no resumo.

**5. Resumo.** Siga a seção "Resumo" abaixo. Na tabela, mostre o formato e o estilo visual nas duas primeiras linhas, e as escolhas que vieram deles aparecem como "definido pelo formato" ou "definido pelo estilo".

### Caminho do zero

Siga a seção "Padrão completo ou personalizar?" abaixo e as rodadas 1 a 3. Aqui não pergunte de formato: os formatos e os estilos salvos ficam no caminho formato pronto. Os estilos visuais aparecem na pergunta 5 (estilo visual dos gráficos).

### Repetir o último vídeo (preferências salvas)

Antes da pergunta "Como quer editar este vídeo?", mostre um resumo curto do que está salvo (formato, estilo visual, escolhas e ajustes fixos, em linguagem simples), pra pessoa saber o que "Repetir o último vídeo" significa.

Se a pessoa escolher repetir: carregue as escolhas do arquivo e pule direto pro resumo. Se o arquivo tiver "Formato pronto", "Estilo visual" ou "Estilo de referência", leia os arquivos deles como no caminho formato pronto (passos 2 e 3). Só pergunte o que depende deste vídeo:

- se a capa salva for "eu escrevo o título", peça o título deste vídeo;
- se a música salva for "usar a música da pasta" e não houver música na pasta, pergunte qual música usar (com as outras opções da pergunta 6);
- se o estilo visual salvo for "cores da minha marca" e faltar algum dado da marca no arquivo, peça só o que faltar;
- se o formato pedir entradas extras que não estão na pasta, siga o que o formato manda.

Nos caminhos "do zero" e "formato pronto", o arquivo de preferências é ignorado (exceto a cor de marca e os ajustes fixos, se a pessoa quiser). Ele continua lá até ser substituído na fase 5.

### Padrão completo ou personalizar? (caminho do zero)

Comece com uma mensagem curta:

> Vou editar seu vídeo do começo ao fim. Antes, umas perguntas rápidas sobre como você quer que ele fique. Se preferir, uso o padrão completo e já começo.

Primeira pergunta: **"Padrão completo ou personalizar?"**

- **Padrão completo (recomendado)**: vertical 9:16, nível Completo, estilo claro tecnológico, legenda padrão, capa criada pela IA, música eletrônica sintetizada, efeitos completos, verificação de fontes ligada. Pule direto pro resumo.
- **Personalizar**: siga as rodadas abaixo.

Use a ferramenta de perguntas de múltipla escolha (AskUserQuestion) quando disponível, até 4 perguntas por rodada, com a opção recomendada primeiro e marcada com "(Recomendado)". Sem a ferramenta, pergunte em texto numerado. O usuário sempre pode responder livremente.

### Rodada 1: proporção e nível

1. **Onde o vídeo vai ser postado?**
   - Vertical 9:16, Reels / TikTok / Shorts (Recomendado)
   - Horizontal 16:9, YouTube
2. **Qual nível de edição?**
   - **Completo com motion (Recomendado)**: tudo do nível Com imagens, mais câmera virtual animada entre os cartões, profundidade de campo, desfoque de movimento, interfaces de produto animadas (digitando, clicando) e sons de passagem.
   - **Com imagens**: tudo do Básico, mais três layouts alternados (câmera cheia, tela dividida com a cabeça saindo do cartão e tela só com gráficos), cartões com imagens, logos, capturas e páginas de fonte, e checagem de contato visual. Elementos entram com animação simples; a câmera virtual fica parada.
   - **Básico**: cortes de silêncio e de falas repetidas, seleção da melhor tomada, legendas, capa, cartão de chamada pra ação, música e efeitos. Só a câmera em tela cheia, sem gráficos.

### Rodada 2: visual

3. **Estilo das legendas?**
   - Brancas com contorno preto e palavras-chave em amarelo com fonte serifada (Recomendado)
   - Só brancas, sem destaque
   - Destaques na cor da minha marca
   - Sem legenda
4. **Título de capa no primeiro quadro?**
   - Sim, cria pra mim a partir do gancho (Recomendado)
   - Sim, eu escrevo o título (peça o texto em seguida)
   - Sem capa
5. **Estilo visual?** (nos níveis Com imagens e Completo muda gráficos, legenda e música; no Básico, só a legenda e a música)
   - Claro tecnológico: cartões brancos flutuando num fundo quase branco (Recomendado)
   - Escuro premium
   - Pixelado: creme quadriculado, legenda em pílula escura e cenas em pixel art (arquivo `estilos-visuais/pixelado.md`)
   - Cores da minha marca (peça em seguida: cor principal em hex, fundo claro ou escuro, e a fonte, se tiver)

   Se houver outros estilos visuais listados na fase 0 (Noite Laranja e os que a pessoa criou), cite-os pelo nome na pergunta: a pessoa pode responder por texto. Quando o escolhido for um arquivo de `estilos-visuais/`, ele substitui a Direção visual, as cores, as fontes e a aparência das legendas do motor, seguindo os papéis de `referencias/estilos-visuais.md`. A pergunta 3 (legendas) continua valendo só pra "sem legenda"; o resto da aparência da legenda vem do estilo.

### Rodada 3: áudio e conteúdo

6. **Música de fundo?**
   - Eletrônica minimalista criada por código, 100–120 BPM (Recomendado)
   - Outro clima: calma ou energética (pergunte qual)
   - Usar a música que está na pasta (só ofereça se houver arquivo de música)
   - Sem música
7. **Efeitos sonoros?**
   - Completos: cliques, digitação, impactos, confirmações, passagens e som crescente na abertura (Recomendado)
   - Só os essenciais: sem passagens
   - Nenhum
8. **Verificar notícias e números citados?** (só nos níveis Com imagens e Completo)
   - Sim, conferir em fontes reais e mostrar a página da fonte no vídeo (Recomendado)
   - Não

### Resumo

Mostre uma tabela curta com todas as escolhas (incluindo o que foi detectado na fase 0: orientação da gravação e se tem áudio separado) e pergunte: **"Posso começar a edição?"**. Ajuste o que a pessoa pedir. Avise que a edição demora e que você só volta a falar quando o vídeo estiver pronto pra assistir no Studio.

---

## Fase 2: Edição autônoma

1. Leia `referencias/instrucoes-base.md` e `referencias/variacoes.md` inteiros. Se um formato pronto foi escolhido, leia também a seção "Como um formato pronto se aplica" de `referencias/formatos-prontos.md` e o `formato.md` inteiro. Se um estilo visual foi escolhido (qualquer um que não seja o Original do formato), leia o arquivo dele inteiro e a seção "Como aplicar um estilo visual a um formato" de `referencias/estilos-visuais.md`. Releia tudo se a conversa foi resumida.
2. Crie a pasta `edit/` e salve `edit/plano.md` com:
   - as escolhas do usuário e o que foi detectado (e se vieram das preferências salvas);
   - se um formato pronto foi escolhido: o nome do formato e as regras dele copiadas pro plano já resolvidas, seção por seção, seguindo a tabela "O que o formato substitui". Escreva no plano quais blocos do motor continuam valendo, quais o formato substituiu e o texto final de cada um. Os itens da "Verificação do formato" entram na 9A e na 9B. Se o formato tiver "Fluxo diferente", copie também e siga ele por cima das fases 2 a 4;
   - se um estilo visual foi escolhido: uma tabela "papel → valor" com cada cor, fonte, material, legenda e efeito já trocados pelos do estilo, e a lista dos elementos de assinatura do estilo com onde entram neste formato. Os itens da "Verificação do estilo" entram na 9A e na 9B. Escreva as instruções finais de cada layout já com a aparência do estilo, sem "ver estilo";
   - se um estilo de referência (salvo pela pessoa) foi escolhido: leia `~/.maquina-de-edicao/estilos/<nome>.md` inteiro, abra as imagens da pasta `~/.maquina-de-edicao/estilos/<nome>/` e copie as regras do estilo pro plano já resolvidas. O estilo vale por cima das instruções base e das variações. Na verificação prévia (bloco 9A), compare quadros do vídeo com as imagens de referência;
   - se usou as preferências salvas: os "ajustes fixos" do arquivo, que valem por cima das instruções base, das variações e do estilo de referência (ex: "legendas 15% maiores" muda o tamanho padrão das legendas);
   - a lista de blocos que valem pra este vídeo (pelo nível) e as variações aplicadas;
   - as instruções finais já adaptadas, por escrito, sem referências a "ver variação X".

   A edição é longa. Se a conversa for resumida no meio, releia `edit/plano.md` antes de continuar e siga ele à risca.
3. Execute as instruções do plano em ordem. Nesta fase, valem as regras de AUTONOMIA do bloco 0: não faça perguntas, decida, registre as decisões e siga. A única exceção é uma pausa prevista na seção "Fluxo diferente" do estilo (ex: o Cortes de Vídeo Longo mostra o ranking dos cortes antes de editar).
4. Assim que a transcrição estiver pronta, escolha o nome da pasta do projeto a partir do assunto do vídeo e anote em `edit/plano.md` ("Nome da pasta"). Curto, em português, dizendo do que o vídeo trata (ex: um vídeo sobre o Claude substituindo editores vira `Claude matando os editores de vídeo`). Sem caracteres proibidos em nome de pasta (`\ / : * ? " < > |`). A pasta só é renomeada no fim da fase 4.
5. Mande atualizações curtas de progresso nas etapas grandes (sincronizado e transcrito, cortes prontos, gráficos prontos, áudio pronto), em linguagem simples.
6. **Não renderize o MP4 final nesta fase.** O ponto de chegada é a composição completa passando no `npx hyperframes check` e na verificação prévia (bloco 9A).

## Fase 3: Revisão no Studio

1. Abra o Studio na pasta do projeto HyperFrames: `npx hyperframes preview --background`. Confirme que a URL responde e passe o link ao usuário.
2. Mensagem pro usuário:

   > Seu vídeo está montado. Abra esse link e assista: <URL>
   >
   > Me fale o que quer mudar (ex: "legenda maior", "tira esse efeito", "corta essa frase", "troca a música"). Quando estiver do jeito que você quer, é só dizer **"pode exportar"**.

3. **Loop de ajustes:** a cada pedido, altere a composição, rode `npx hyperframes check` e avise o que mudou. O Studio atualiza sozinho; não renderize nada. Se o pedido for vago ("tá estranho no começo"), pergunte o que exatamente incomoda ou proponha 2 opções. Se a pessoa clicou num elemento no Studio e disse "isso", consulte a seleção com `npx hyperframes preview --context --json --context-fields selection`.
4. Registre cada ajuste no fim de `edit/plano.md`, numa seção "Ajustes da revisão", marcando de qual tipo ele é:
   - **[gosto]**: preferência de estilo que valeria pra qualquer vídeo ("legenda maior", "música mais baixa", "menos efeitos sonoros", "cortes mais secos", "sem zoom"). Esses vão pras preferências salvas na fase 5.
   - **[deste vídeo]**: depende do conteúdo desta gravação ("corta essa frase", "troca a imagem do minuto 1", "corrige o nome da empresa"). Esses não são salvos.

   Na dúvida, marque como [deste vídeo].
5. **Nunca exporte o MP4 sem aprovação explícita** ("pode exportar", "aprovado", "tá bom, exporta", ou equivalente claro). Elogio sem pedido de exportação ("ficou legal") não é aprovação: pergunte se pode exportar.

## Fase 4: Exportação

Só depois da aprovação:

1. Faça a mixagem e a masterização final (bloco 7, MASTER) e meça os stems e o master com `ebur128`.
2. Renderize `edit/final.mp4` e exporte os stems (bloco 8C).
3. Rode a verificação final completa sobre o MP4 renderizado (bloco 9B). Se encontrar falha, corrija, exporte de novo e repita a verificação.
4. Escreva `edit/relatorio.md` (bloco RELATÓRIO).
5. Encerre o servidor do Studio.
6. Salve as preferências (fase 5).
7. Renomeie a pasta do projeto (a pasta onde está o vídeo bruto) pro nome anotado em `edit/plano.md`. Regras:
   - se a pasta já tem um nome que descreve o vídeo, mantenha;
   - se já existir uma pasta com esse nome no mesmo lugar, acrescente um número no fim (`... 2`);
   - o Studio precisa estar encerrado antes (passo 5);
   - se o sistema não deixar renomear (comum no Windows quando a pasta está aberta no terminal, no editor ou no Explorer), não force: avise o nome sugerido e peça pra pessoa renomear depois de fechar a pasta.
8. Mensagem final curta: onde está o `final.mp4` (já com o caminho da pasta renomeada), duração, o que foi feito em 3 a 5 linhas, o caminho do relatório e uma linha avisando que as preferências deste vídeo ficaram salvas pra próxima edição.

Se, depois da exportação, a pessoa pedir outra mudança: volte pra fase 3 (ajuste + Studio) e só exporte de novo com nova aprovação. Depois da nova exportação, salve as preferências de novo.

## Fase 5: Salvar preferências

Roda sozinha logo depois da exportação aprovada, sem pergunta, exceto no caso abaixo.

1. Monte as preferências deste vídeo:
   - o formato pronto usado (nome da pasta, ex: `reels-de-negocio`) ou "nenhum";
   - o estilo visual usado (nome do arquivo sem `.md`, ex: `pixelado`, ou "original do formato") ou "nenhum" no caminho do zero;
   - o estilo de referência usado (nome do arquivo, sem `.md`) ou "nenhum";
   - as 8 escolhas da entrevista (proporção, nível, legendas, capa, estilo visual, música, efeitos, verificação de fontes), mesmo quando vieram do "Padrão completo". As que vieram de um formato, de um estilo visual ou de um estilo de referência ficam como "definido pelo formato" ou "definido pelo estilo";
   - os dados de marca, se a pessoa informou (cor em hex, fundo claro ou escuro, fonte);
   - os **ajustes fixos**: os que já estavam salvos e foram usados neste vídeo, mais os ajustes **[gosto]** desta revisão. Se um ajuste novo contradiz um antigo, fica o novo. Escreva cada um como regra que dá pra aplicar em outro vídeo ("legendas 15% maiores que o padrão"), não como pedido solto ("aumenta aí").
   - Não salve nada que dependa só deste vídeo: título da capa escrito pela pessoa, arquivo de música, orientação da gravação, áudio separado, ajustes [deste vídeo].
2. Se já existir `~/.maquina-de-edicao/preferencias.md` e a pessoa **não** escolheu "Repetir o último vídeo" (foi do zero, foi com formato pronto ou chamou uma skill de formato direto), pergunte antes de sobrescrever: **"Quer que as escolhas deste vídeo virem suas novas preferências salvas?"** (Sim, substituir (Recomendado) / Não, manter as antigas). Nos outros casos, salve direto.
3. Crie a pasta `~/.maquina-de-edicao/` se não existir e grave o arquivo neste formato:

```markdown
# Preferências da Máquina de Edição

Atualizado em: AAAA-MM-DD (vídeo: nome-do-arquivo.mp4)

## Escolhas
- Formato pronto: nenhum
- Estilo de referência: nenhum
- Proporção: Vertical 9:16
- Nível: Completo com motion
- Legendas: Brancas com contorno, palavras-chave em amarelo serifado
- Capa: IA cria a partir do gancho
- Estilo visual: Claro tecnológico
- Música: Eletrônica minimalista 100–120 BPM
- Efeitos sonoros: Completos
- Verificar fontes: Sim

## Marca
- Cor principal: (só se informada)
- Fundo: (só se informado)
- Fonte: (só se informada)

## Ajustes fixos
- Legendas 15% maiores que o padrão
- Música 3 dB mais baixa que o padrão
```

A linha "Estilo visual" guarda o nome do arquivo do estilo (ex: `pixelado`), "original do formato" ou, no caminho do zero, a opção escolhida (ex: "Claro tecnológico").

Se não houver dados de marca ou ajustes fixos, escreva "nenhum" na seção. Não escreva nos ajustes fixos regras que só valem pra um formato ou um estilo:

- as de um estilo de referência ficam no arquivo do estilo;
- as de um formato pronto (ex: "no ranking, cards menores") ficam numa seção extra, `## Ajustes do formato <nome-da-pasta>`;
- as de um estilo visual (ex: "no pixelado, sem cena de pixel art") ficam numa seção extra, `## Ajustes do estilo visual <nome-do-arquivo>`.

Essas seções ficam no fim do arquivo e só valem quando aquele formato ou estilo for usado de novo. Mantenha as seções de outros formatos e estilos que já estiverem no arquivo.

Os arquivos `formato.md` e os estilos visuais que vêm com a Máquina nunca são editados pela skill (eles são substituídos quando a pessoa atualiza o repositório). Os estilos visuais que a pessoa criou (`~/.maquina-de-edicao/estilos-visuais/`) só são editados se ela pedir.

---

## Criar um estilo a partir de um vídeo de referência

Quando a pessoa mandar um link (Instagram, TikTok, YouTube) ou arquivo de vídeo e pedir pra analisar a edição e salvar como estilo. Não edita vídeo nenhum: só cria o estilo.

Primeiro pergunte: **"Quer copiar a edição inteira ou só o visual?"**

- **A edição inteira (Recomendado)**: estrutura + aparência (layouts, ritmo, cores, legenda). Vira um estilo salvo que aparece na lista de formatos, em "Seus estilos salvos". Siga os passos 1 a 6 abaixo.
- **Só o visual**: cores, fontes, legenda, materiais, movimento e música, pra usar em cima de qualquer um dos 12 formatos. Faça os passos 1 e 2, e no lugar do passo 3 preencha uma cópia de `estilos-visuais/_modelo.md` e salve em `~/.maquina-de-edicao/estilos-visuais/<nome>.md`. Não escreva layout nem posição: só aparência. Pule o passo 4 (sem quadros de referência; descreva tudo em texto e hex). Ele aparece na pergunta "Qual estilo visual?" da próxima edição.

Se a pessoa pedir um estilo visual sem vídeo de referência (ex: "cria um estilo neon roxo"), preencha o modelo a partir da descrição dela, mostre o resumo dos papéis e salve no mesmo lugar.

1. Baixe o vídeo com `yt-dlp` numa pasta temporária. Se o download pedir login, avise e peça o arquivo.
2. Extraia: quadros nas trocas de cena e folhas de contato a 4 quadros por segundo (`fps=4,scale=240:-1,tile=6x4`), transcrição com tempos, `ffprobe` (resolução, fps), loudness (`ebur128`) e silêncios (`silencedetect`). Meça posições e cores direto nos quadros em resolução cheia, não no olho.
3. Escreva `~/.maquina-de-edicao/estilos/<nome-do-criador>.md` (kebab-case) seguindo o modelo dos estilos que já existem na pasta. Seções obrigatórias:
   - título e linha "Resumo:" (uma frase, usada na pergunta da fase 1);
   - origem (link, data, duração, resolução, fps) e aviso pra abrir as imagens antes de construir;
   - "Escolhas que este estilo já define" (quais perguntas da entrevista deixam de ser feitas);
   - ritmo e corte (com proporção de cada layout), layouts com coordenadas em 1080 × 1920, legendas, gráficos (paleta em hex e fontes equivalentes do Google Fonts), movimento, gancho/capa, CTA, áudio (com o que foi medido e o que é só suposição), saída.
4. Salve 10 a 15 quadros de referência (540 px de largura, nome descritivo numerado) e as folhas de contato em `~/.maquina-de-edicao/estilos/<nome>/`. Confira se cada imagem mostra mesmo o que o nome diz.
5. Não mexa em `preferencias.md`: o estilo novo aparece como opção na próxima edição.
6. Responda com um resumo curto do estilo e avise onde ele aparece na próxima edição (na lista de formatos, em "Seus estilos salvos", ou na pergunta de estilo visual).
