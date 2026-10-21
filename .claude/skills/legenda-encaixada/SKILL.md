---
name: legenda-encaixada
description: Edita um vídeo falado no estilo Legenda Encaixada. Vídeo vertical 9:16 só com a câmera e a legenda; a frase se monta palavra por palavra e a palavra mais forte aparece gigante em serifa itálica laranja, com as outras encaixadas em volta. Faz parte da Máquina de Edição (precisa da skill maquina-de-edicao instalada). Use quando o usuário chamar /legenda-encaixada ou pedir pra editar um vídeo "no estilo Legenda Encaixada", "legenda encaixada", "legenda estilosa" ou "só legenda bonita".
---

# Legenda Encaixada

Estilo pronto da Máquina de Edição. Vídeo vertical 9:16 só com a câmera e a legenda: a frase se monta palavra por palavra e a palavra mais forte aparece gigante em serifa itálica laranja, com as outras encaixadas em volta.

Esta skill não tem um fluxo próprio: ela chama o motor da Máquina de Edição com este estilo já escolhido.

1. **Ache o motor.** Ele fica na pasta `maquina-de-edicao`, ao lado da pasta desta skill (as duas estão na mesma pasta de skills). Se não existir, pare e avise: "Esse estilo precisa da Máquina de Edição. Rode o instalador do repositório de novo (`instalar.ps1` no Windows ou `instalar.sh` no Mac) e abra o Claude Code de novo."
2. **Leia o `SKILL.md` do motor inteiro** e siga o fluxo dele do começo ao fim, com estas regras:
   - O estilo já está escolhido: **Legenda Encaixada** (pasta `legenda-encaixada`). Pule a pergunta "Como quer editar este vídeo?" e a lista de estilos. Vá direto pro "Caminho estilo pronto", a partir do passo 2.
   - A especificação do estilo é o arquivo `estilo.md` desta pasta. Leia inteiro antes da fase 1.
   - Todo o resto é igual ao motor: checar a pasta, a rodada curta de perguntas, a edição autônoma, a revisão no Studio, a exportação só depois da aprovação e as preferências salvas.
3. Se a pessoa pedir pra trocar de estilo no meio da conversa, volte pro motor e mostre a lista de estilos.
