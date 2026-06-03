#!/usr/bin/env bash
set -euo pipefail
cd /root/awesome-niche-tools
mkdir -p insights shifts memory/agents || true

# Create metrics file for archivist runs
cat > memory/agents/archivist.json <<'EOF'
{
  "agent_id": "archivist",
  "enabled": true,
  "last_shift": {
    "date": null,
    "status": "none",
    "branch": "",
    "outputs_generated": 0
  },
  "metrics": {
    "total_shifts": 0,
    "successful_shifts": 0,
    "failed_shifts": 0,
    "weeks_tracked": 0,
    "categories_tracked": 0,
    "repeat_winners_identified": 0
  },
  "updated_at": null
}
EOF

echo '{"total":"0","new":"0","categories":0,"failures":0}' > shifts/latest-metrics.json

# Initialize empty baselines for first Archivist run
cat > insights/trends.md <<'EOF'
# Trends

No data yet. This file will be updated after the first Archivist run.
EOF

cat > insights/emerging-categories.md <<'EOF'
# Emerging Categories

No data yet. This file will be updated after the first Archivist run.
EOF

cat > insights/declining-categories.md <<'EOF'
# Declining Categories

No data yet. This file will be updated after the first Archivist run.
EOF

cat > insights/repeat-winners.md <<'EOF'
# Repeat Winners

Requires 3+ weeks of vibe-coder weekly digest data to calculate repeat wins.
EOF
