# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp218/problem?isFullScreen=true
# Problem     LBP218
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 08:21 p.m.
# ──────────────────────────────────────────────────

a = []

for i in range(3):
    a.append([int(x) for x in input().split()])
s = 0
for i in range(3):
    for j in range(3):
        if i == j:
            s += a[j][i]
print(s)
    
    
