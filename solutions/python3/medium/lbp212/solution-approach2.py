# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp212/problem?isFullScreen=true
# Problem     LBP212
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-22, 08:04 a.m.
# ──────────────────────────────────────────────────

a = []

for i in range(3):
    a.append([int(x) for x in input().split()])

s = 1

for i in range(3):
    s = s * a[i][3-i-1]

print(s)
