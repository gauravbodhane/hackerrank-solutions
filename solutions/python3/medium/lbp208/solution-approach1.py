# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp208/problem?isFullScreen=true
# Problem     LBP208
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-20, 09:00 a.m.
# ──────────────────────────────────────────────────


a = []
for i in range(3):
    a.append([int(i) for i in input().split()])
s =0
for i in range(3):
    for j in range(3):
        if i==j:
            s = s+a[i][j]
print(s)
