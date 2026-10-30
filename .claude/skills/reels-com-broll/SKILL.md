---
name: reels-com-broll
description: Edita um vídeo falado no formato Reels com B-roll. Vídeo vertical 9:16 com corte rápido, clipes de apoio (os da pessoa ou buscados na internet) entrando por cima da fala e frases-chave empilhadas na legenda. Depois de escolher o formato, a pessoa escolhe o estilo visual (original do formato, Pixelado, Noite Laranja, Claro Tecnológico ou um que ela criou). Faz parte da Máquina de Edição (precisa da skill maquina-de-edicao instalada). Use quando o usuário chamar /reels-com-broll ou pedir pra editar um vídeo "no formato Reels com B-roll", "reels com b-roll", "usar meus clipes de apoio" ou "reels de criador".
---

# Reels com B-roll

Formato pronto da Máquina de Edição. Vídeo vertical 9:16 com corte rápido, clipes de apoio (os da pessoa ou buscados na internet) entrando por cima da fala e frases-chave empilhadas na legenda.

Esta skill não tem um fluxo próprio: ela chama o motor da Máquina de Edição com este formato já escolhido.

1. **Ache o motor.** Ele fica na pasta `maquina-de-edicao`, ao lado da pasta desta skill (as duas estão na mesma pasta de skills). Se não existir, pare e avise: "Esse formato precisa da Máquina de Edição. Rode o instalador do pacote principal da Máquina de Edição (`instalar.ps1` no Windows ou `instalar.sh` no Mac) e abra o Claude Code de novo."
2. **Leia o `SKILL.md` do motor inteiro** e siga o fluxo dele do começo ao fim, com estas regras:
   - O formato já está escolhido: **Reels com B-roll** (pasta `reels-com-broll`). Pule a pergunta "Como quer editar este vídeo?" e a lista de formatos. Vá direto pro "Caminho formato pronto", a partir do passo 2.
   - A especificação do formato é o arquivo `formato.md` desta pasta. Leia inteiro antes da fase 1.
   - A pergunta "Qual estilo visual?" (passo 3) continua: é ela que define a aparência do vídeo.
   - **Centralização obrigatória em todos os vídeos:** mantenha o centro da cabeça exatamente no centro horizontal da área visível reservada à pessoa (tela inteira ou janela da câmera), sem desvio para a esquerda ou direita. Reenquadre cada tomada e acompanhe movimentos. Esta regra prevalece sobre posições do `formato.md`, estilos e preferências; confira antes do Studio e no MP4 final. Siga o bloco 2A das instruções base do motor.
   - Todo o resto é igual ao motor: checar a pasta, a rodada curta de perguntas, a edição autônoma, a revisão no Studio, a exportação só depois da aprovação e as preferências salvas.
3. Se a pessoa pedir pra trocar de formato no meio da conversa, volte pro motor e mostre a lista de formatos.
