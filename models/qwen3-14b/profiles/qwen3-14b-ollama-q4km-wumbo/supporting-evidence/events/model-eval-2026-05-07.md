
# qwen3-14b-wumbo Evaluation

Status: Good enough for daily local technical assistant use.

Strengths:
- Conservative Docker Compose workflows.
- Correct Arch/systemd tooling.
- Avoids major dangerous commands after prompt tuning.
- Good fit for homelab troubleshooting and command review.

Known caveats:
- Still review every command before running.
- May include noisy checks like pacman -Qkk.
- Arch News is better checked manually than via curl/grep.
- Keep context at 4096 for now.

Recommended role:
- Main technical/homelab model.
