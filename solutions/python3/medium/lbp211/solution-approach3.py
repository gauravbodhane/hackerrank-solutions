# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp211/problem?isFullScreen=true
# Problem     LBP211
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 07:22 p.m.
# ──────────────────────────────────────────────────

n = []
for i in range(3):
    n.append([int (i) for i in input().split() ])
s =1
for i in range(3):
    if i==i:
        s*= n[i][i]
print(s)
