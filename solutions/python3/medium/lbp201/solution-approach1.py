# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp201/problem?isFullScreen=true
# Problem     LBP201
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-20, 08:11 a.m.
# ──────────────────────────────────────────────────

n = int(input())
m = int(input())
a=[]
for i in range(n):
    a.append([int(i) for i in input().split()])
for i in range(n):
    for j in range(m):
        print(a[i][j],end=' ')
    print()
