#!/usr/bin/env bash
# Instala a Máquina de Edição e os 12 formatos prontos no Claude Code (Mac e Linux).
# Uso, dentro da pasta do repositório:
#   bash instalar.sh
#
# Copia cada pasta de .claude/skills/ deste repositório para ~/.claude/skills/.
# Se já existir uma skill com o mesmo nome, a versão antiga vai para
# ~/.claude/skills-backup/<data>/ antes de ser substituída.
# Suas preferências e estilos salvos (~/.maquina-de-edicao/) não são tocados.

set -euo pipefail

raiz="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
origem="$raiz/.claude/skills"
destino="$HOME/.claude/skills"
backup="$HOME/.claude/skills-backup/$(date +%Y-%m-%d_%H-%M-%S)"

if [ ! -d "$origem" ]; then
  echo "Não achei a pasta .claude/skills ao lado deste script. Rode o instalador de dentro da pasta do repositório."
  exit 1
fi

mkdir -p "$destino"

total=0
fez_backup=0
for skill in "$origem"/*/; do
  nome="$(basename "$skill")"
  alvo="$destino/$nome"
  if [ -e "$alvo" ]; then
    mkdir -p "$backup"
    mv "$alvo" "$backup/$nome"
    fez_backup=1
  fi
  cp -R "$skill" "$alvo"
  echo "  ok  /$nome"
  total=$((total + 1))
done

echo ""
echo "Pronto! $total skills instaladas em $destino"
if [ "$fez_backup" = 1 ]; then
  echo "As versões antigas foram guardadas em $backup"
fi
echo ""
echo "Feche e abra o Claude Code de novo. Depois, na pasta do seu vídeo, digite:"
echo "  /maquina-de-edicao      (escolhe entre editar do zero ou com um formato pronto)"
echo "  /reels-de-negocio       (ou o nome de qualquer formato, pra ir direto)"
