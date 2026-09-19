#!/bin/bash

set -e

TARGETS="dataset/data/targets.txt"
OUTPUT_DIR="dataset/data/raw"
OUTPUT="$OUTPUT_DIR/nikto_report.html"

mkdir -p "$OUTPUT_DIR"

if [ ! -f "$TARGETS" ]; then
    echo "Ошибка: файл $TARGETS не найден."
    exit 1
fi

echo "=== Nikto scan ==="
echo "Targets: $TARGETS"
echo "Output: $OUTPUT"

cat > "$OUTPUT" <<EOF
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Nikto Scan Report</title>
</head>
<body>
<h1>Nikto Scan Report</h1>
EOF

while IFS= read -r target; do

    # Пропускаем пустые строки
    if [ -z "$target" ]; then
        continue
    fi

    # Пропускаем комментарии
    if [[ "$target" == \#* ]]; then
        continue
    fi

    echo "Scanning target: $target"

    echo "<h2>Target: $target</h2>" >> "$OUTPUT"

    nikto -h "$target" -output - 2>&1 >> "$OUTPUT"

    echo "<hr>" >> "$OUTPUT"

done < "$TARGETS"

cat >> "$OUTPUT" <<EOF
</body>
</html>
EOF

echo "Nikto завершён."
echo "Результат сохранён в: $OUTPUT"
