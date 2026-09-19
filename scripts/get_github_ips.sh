#!/usr/bin/env bash

set -e

OUTPUT_DIR="dataset/data/github_ips/"
OUTPUT_FILE="$OUTPUT_DIR/github_ips.txt"
JSON_FILE="$OUTPUT_DIR/github_meta.json"

mkdir -p "$OUTPUT_DIR"

echo "[1/3] Получение данных GitHub Meta API..."

curl -L \
    -H "Accept: application/vnd.github+json" \
    https://api.github.com/meta \
    -o "$JSON_FILE"

echo "[2/3] Извлечение IP-диапазонов..."

jq -r '
    .git[]?,
    .web[]?,
    .api[]?
' "$JSON_FILE" | sort -u > "$OUTPUT_FILE"

echo "[3/3] Готово."

echo
echo "Количество диапазонов:"
wc -l "$OUTPUT_FILE"

echo
echo "Файл:"
echo "$OUTPUT_FILE"

echo
echo "Первые диапазоны:"
head "$OUTPUT_FILE"
