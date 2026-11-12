# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/lbp6222/challenges/lbp33/problem?isFullScreen=true
# Problem     LBP33
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-12, 05:39 p.m.
# ──────────────────────────────────────────────────

n = input() 
g = 0
for i in n :
    if int(i) % 2 != 0:
        g += int(i) 
print(g)
