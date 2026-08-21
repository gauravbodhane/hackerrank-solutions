# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp214/problem?isFullScreen=true
# Problem     LBP214
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 07:47 p.m.
# ──────────────────────────────────────────────────


a = []

for i in range(3):
    a.append([int(x) for x in input().split()])

min = a[0][0]
for i in range(3):
    for j in range(3):
        if min > a[i][j]:
            min = a[i][j]
print(min)
