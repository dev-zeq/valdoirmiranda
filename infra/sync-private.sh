#!/usr/bin/env bash
set -euo pipefail

# Sincroniza os módulos privados (/var/www/valdoirmiranda-private) com a versão
# pública (/var/www/valdoirmiranda) após um `git pull`. Os arquivos privados são
# cópias manuais, não symlinks, e o destino é derivado do caminho de origem —
# 7d40d1ef04.html vai pra raiz, es/7d40d1ef04.html vai pra es/ etc. — para evitar
# copiar pro lugar errado (ex: sobrescrever o módulo PT com o EN).
#
# Uso (na VPS, depois do git pull):
#   /var/www/valdoirmiranda/infra/sync-private.sh

# Permite sobrescrever os caminhos para testes:
#   PUB=/tmp/pub PRIV=/tmp/priv infra/sync-private.sh
PUB="${PUB:-/var/www/valdoirmiranda}"
PRIV="${PRIV:-/var/www/valdoirmiranda-private}"

if [ ! -d "$PUB/.git" ]; then
  echo "Erro: $PUB não é um repositório git (execute o script na VPS)." >&2
  exit 1
fi

# Arquivos alterados no último pull (HEAD@{1}..HEAD). Sem histórico (primeiro
# pull), usa todos os arquivos rastreados.
changed="$(cd "$PUB" && git diff --name-only HEAD@{1} HEAD 2>/dev/null || true)"
if [ -z "$changed" ]; then
  changed="$(cd "$PUB" && git ls-files)"
fi

copied=0
skipped=0
while IFS= read -r f; do
  [ -n "$f" ] || continue
  src="$PUB/$f"
  [ -f "$src" ] || continue

  # Só sincroniza arquivos que já tenham espelho privado. Módulo novo precisa
  # ser copiado à mão uma vez (raiz, es/, en/) antes de passar a ser seguido.
  dst="$PRIV/$f"
  if [ ! -f "$dst" ]; then
    skipped=$((skipped+1))
    continue
  fi

  mkdir -p "$(dirname "$dst")"
  cp "$src" "$dst"
  echo "copiado: $f"
  copied=$((copied+1))
done <<< "$changed"

echo "sincronizados: $copied | sem espelho privado (ignorados): $skipped"
