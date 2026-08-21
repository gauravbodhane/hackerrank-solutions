# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp207/problem?isFullScreen=true
# Problem     LBP207
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 08:59 a.m.
# ──────────────────────────────────────────────────

a = []
for i in range(3):
    a.append([int(i) for i in input().split()])

for  j in range(3):
    s= 0
    for i in range(3):
        s += a[i][j]
    print(s)
