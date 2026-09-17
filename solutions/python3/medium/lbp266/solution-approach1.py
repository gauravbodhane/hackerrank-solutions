# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp266/problem?isFullScreen=true
# Problem     LBP266
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-17, 02:12 p.m.
# ──────────────────────────────────────────────────

import re
n = input()
print('true'if re.fullmatch('[a-zA-Z_][a-zA-Z0-9_]+',n) else 'false')
