# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp215/problem?isFullScreen=true
# Problem     LBP215
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 07:59 p.m.
# ──────────────────────────────────────────────────

a = []

for i in range(3):
    a.append([int(x) for x in input().split()])

for i in range(3):
    max = a[i][0]
    for j in range(3):
        if max < a[i][j]:
            max = a[i][j]
    print(max)
