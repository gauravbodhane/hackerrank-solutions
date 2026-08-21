# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp213/problem?isFullScreen=true
# Problem     LBP213
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 08:37 a.m.
# ──────────────────────────────────────────────────

a = []
for i in range(3):
    a.append([int(i)for i in input().split()])
max = a[0][0]
for i in range(3):
    for j in range(3):
        if max<a[i][j]:
            max = a[i][j]
print(max)
