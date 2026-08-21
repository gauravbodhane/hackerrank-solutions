# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp208/problem?isFullScreen=true
# Problem     LBP208
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 08:51 a.m.
# ──────────────────────────────────────────────────

a = [] 
for i in range(3):
    a.append([int(i) for i in input().split()])
s = 0
for i in range(3):
    s += a[i][i]
print(s)
