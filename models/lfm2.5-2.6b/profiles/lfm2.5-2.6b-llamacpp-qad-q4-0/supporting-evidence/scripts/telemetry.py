#!/usr/bin/env python3
import csv, datetime, subprocess, sys, time
out = sys.argv[1]
interval = float(sys.argv[2]) if len(sys.argv) > 2 else 2.0
fields = "timestamp,index,memory.used,memory.free,utilization.gpu,power.draw,temperature.gpu,pstate"
with open(out, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(fields.split(","))
    f.flush()
    print(f"telemetry-ready {out}", flush=True)
    while True:
        now = datetime.datetime.now(datetime.timezone.utc).isoformat()
        result = subprocess.run([
            "nvidia-smi", "--query-gpu=index,memory.used,memory.free,utilization.gpu,power.draw,temperature.gpu,pstate", "--format=csv,noheader,nounits"
        ], capture_output=True, text=True, check=False)
        for line in result.stdout.splitlines():
            writer.writerow([now] + [x.strip() for x in line.split(",")])
        f.flush()
        time.sleep(interval)
