#!/bin/bash

set -e

TARGETS="dataset/data/targets.txt"
OUTPUT_DIR="dataset/data/raw"
OUTPUT="$OUTPUT_DIR/nmap_result.xml"

mkdir -p "$OUTPUT_DIR"

if [ ! -f "$TARGETS" ]; then
    echo "Ошибка: файл $TARGETS не найден."
    exit 1
fi

echo "=== Nmap scan ==="
echo "Targets: $TARGETS"
echo "Output: $OUTPUT"

sudo nmap \
    -iL "$TARGETS" \
    -sV \
    -sC \
    -oX "$OUTPUT"

echo "Nmap завершён."
echo "Результат сохранён в: $OUTPUT"
