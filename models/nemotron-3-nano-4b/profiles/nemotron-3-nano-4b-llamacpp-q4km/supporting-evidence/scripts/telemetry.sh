#!/bin/bash
# Lightweight continuous telemetry: VRAM/temp/power + journal error scan
OUT="$1"; INTERVAL="${2:-10}"
while true; do
  echo "$(date -u +%FT%TZ),"$(nvidia-smi --query-gpu=temperature.gpu,power.draw,memory.used,utilization.gpu --format=csv,noheader)"" >> "$OUT/telemetry.csv"
  sleep "$INTERVAL"
done
