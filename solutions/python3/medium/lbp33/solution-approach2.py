# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/lbp6222/challenges/lbp33/problem?isFullScreen=true
# Problem     LBP33
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-12, 05:40 p.m.
# ──────────────────────────────────────────────────

n = input() 
print(sum(int(x) for x in n if int(x) % 2 != 0))
