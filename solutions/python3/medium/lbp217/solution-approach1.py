# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp217/problem?isFullScreen=true
# Problem     LBP217
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-14, 11:29 p.m.
# ──────────────────────────────────────────────────

a = []

for i in range(3):
    a.append([int(x) for x in input().split()])
    
for i in range(3):
    for j in range(3):
        print(a[j][i],end=' ')
    print()
