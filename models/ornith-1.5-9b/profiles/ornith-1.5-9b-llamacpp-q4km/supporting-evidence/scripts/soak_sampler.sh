#!/usr/bin/env bash
# Phase 9 soak sampler: 70 iterations x 30 s = 35 min coverage
cd <USER_HOME>/Projects/local-llm/evals/ornith-1.5-9b
for i in $(seq 1 70); do
  ts=$(date +%s)
  line=$(nvidia-smi --query-gpu=memory.used,temperature.gpu,utilization.gpu --format=csv,noheader,nounits | tr ', ' ',')
  echo "$ts,$line" >> results/soak/gpu_sample.csv
  pid=$(pgrep -f 'llama-server.*8931' | head -1)
  if [ -n "$pid" ]; then
    rss=$(awk '/VmRSS/{print $2}' /proc/$pid/status 2>/dev/null)
    echo "$ts,$rss" >> results/soak/rss_sample.csv
  fi
  sleep 30
done
echo SAMPLER_DONE
