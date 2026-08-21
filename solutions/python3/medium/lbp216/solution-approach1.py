# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp216/problem?isFullScreen=true
# Problem     LBP216
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 08:03 p.m.
# ──────────────────────────────────────────────────

a = []

for i in range(3):
    a.append([int(x) for x in input().split()])
for i in range(3):
    min = a[i][0]
    for j in range(3):
        if min > a[i][j]:
            min = a[i][j]

    print(min) 
