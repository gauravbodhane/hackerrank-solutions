# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp207/problem?isFullScreen=true
# Problem     LBP207
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-20, 08:57 a.m.
# ──────────────────────────────────────────────────


a = []
for i in range(3):
    a.append([int(i) for i in input().split()])
for i in range(3):
    s= 0
    for j in range(3):
        s = s+a[j][i]
    print(s)
