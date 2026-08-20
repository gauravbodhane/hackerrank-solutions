# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp206/problem?isFullScreen=true
# Problem     LBP206
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-20, 08:50 a.m.
# ──────────────────────────────────────────────────


a = []
for i in range(3):
    a.append([int(i) for i in input().split()])
for i in range(3):
    s= 0
    for j in range(3):
        s = s+a[i][j]
    print(s)
