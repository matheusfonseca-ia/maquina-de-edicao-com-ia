---
name: formato-ranking
description: Edita um vídeo falado no estilo Formato Ranking. Vídeo vertical 9:16 com uma tier list (S a F) na frente do peito que se preenche conforme a pessoa ranqueia cada item; o item entra como card grande e voa pra fileira da nota. Faz parte da Máquina de Edição (precisa da skill maquina-de-edicao instalada). Use quando o usuário chamar /formato-ranking ou pedir pra editar um vídeo "no estilo Formato Ranking", "formato ranking", "tier list" ou "vídeo de ranking".
---

# Formato Ranking

Estilo pronto da Máquina de Edição. Vídeo vertical 9:16 com uma tier list (S a F) na frente do peito que se preenche conforme a pessoa ranqueia cada item: o item entra como card grande e voa pra fileira da nota.

Esta skill não tem um fluxo próprio: ela chama o motor da Máquina de Edição com este estilo já escolhido.

1. **Ache o motor.** Ele fica na pasta `maquina-de-edicao`, ao lado da pasta desta skill (as duas estão na mesma pasta de skills). Se não existir, pare e avise: "Esse estilo precisa da Máquina de Edição. Rode o instalador do repositório de novo (`instalar.ps1` no Windows ou `instalar.sh` no Mac) e abra o Claude Code de novo."
2. **Leia o `SKILL.md` do motor inteiro** e siga o fluxo dele do começo ao fim, com estas regras:
   - O estilo já está escolhido: **Formato Ranking** (pasta `formato-ranking`). Pule a pergunta "Como quer editar este vídeo?" e a lista de estilos. Vá direto pro "Caminho estilo pronto", a partir do passo 2.
   - A especificação do estilo é o arquivo `estilo.md` desta pasta. Leia inteiro antes da fase 1.
   - Todo o resto é igual ao motor: checar a pasta, a rodada curta de perguntas, a edição autônoma, a revisão no Studio, a exportação só depois da aprovação e as preferências salvas.
3. Se a pessoa pedir pra trocar de estilo no meio da conversa, volte pro motor e mostre a lista de estilos.
