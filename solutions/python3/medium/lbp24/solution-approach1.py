# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/lbp6222/challenges/lbp24/problem?isFullScreen=true
# Problem     LBP24
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-09, 04:37 p.m.
# ──────────────────────────────────────────────────

n = int(input() )
n1 = int(input() )

s = 0
for i in range(n,n1+1):
    if i % 2 == 0:
        s += i
        
print(s)
