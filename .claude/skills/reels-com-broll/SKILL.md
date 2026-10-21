---
name: reels-com-broll
description: Edita um vídeo falado no estilo Reels com B-roll. Vídeo vertical 9:16 com corte rápido, os clipes de apoio da própria pessoa (pasta broll/) entrando por cima da fala e frases-chave empilhadas na legenda, com uma palavra grande em serifa laranja. Faz parte da Máquina de Edição (precisa da skill maquina-de-edicao instalada). Use quando o usuário chamar /reels-com-broll ou pedir pra editar um vídeo "no estilo Reels com B-roll", "reels com b-roll", "usar meus clipes de apoio" ou "reels de criador".
---

# Reels com B-roll

Estilo pronto da Máquina de Edição. Vídeo vertical 9:16 com corte rápido, os clipes de apoio da própria pessoa (pasta broll/) entrando por cima da fala e frases-chave empilhadas na legenda, com uma palavra grande em serifa laranja.

Esta skill não tem um fluxo próprio: ela chama o motor da Máquina de Edição com este estilo já escolhido.

1. **Ache o motor.** Ele fica na pasta `maquina-de-edicao`, ao lado da pasta desta skill (as duas estão na mesma pasta de skills). Se não existir, pare e avise: "Esse estilo precisa da Máquina de Edição. Rode o instalador do repositório de novo (`instalar.ps1` no Windows ou `instalar.sh` no Mac) e abra o Claude Code de novo."
2. **Leia o `SKILL.md` do motor inteiro** e siga o fluxo dele do começo ao fim, com estas regras:
   - O estilo já está escolhido: **Reels com B-roll** (pasta `reels-com-broll`). Pule a pergunta "Como quer editar este vídeo?" e a lista de estilos. Vá direto pro "Caminho estilo pronto", a partir do passo 2.
   - A especificação do estilo é o arquivo `estilo.md` desta pasta. Leia inteiro antes da fase 1.
   - Todo o resto é igual ao motor: checar a pasta, a rodada curta de perguntas, a edição autônoma, a revisão no Studio, a exportação só depois da aprovação e as preferências salvas.
3. Se a pessoa pedir pra trocar de estilo no meio da conversa, volte pro motor e mostre a lista de estilos.
