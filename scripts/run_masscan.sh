#!/bin/bash

set -e

TARGETS="dataset/data/targets.txt"
OUTPUT_DIR="dataset/data/raw"
OUTPUT="$OUTPUT_DIR/masscan_output.txt"

mkdir -p "$OUTPUT_DIR"

if [ ! -f "$TARGETS" ]; then
    echo "Ошибка: файл $TARGETS не найден."
    exit 1
fi

echo "=== Masscan scan ==="
echo "Targets: $TARGETS"
echo "Output: $OUTPUT"

sudo masscan \
    -iL "$TARGETS" \
    -p 1-1000 \
    --rate 100 \
    -oG "$OUTPUT"

echo "Masscan завершён."
echo "Результат сохранён в: $OUTPUT"
