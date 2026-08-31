# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp169/problem?isFullScreen=true
# Problem     LBP169
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-31, 02:48 p.m.
# ──────────────────────────────────────────────────

import math 
n= int(input())
m = math.isqrt(n) 
k = 0
l = [int(i) for i in input().split()]
for i in range(m):
    for j in range(m):
        print(l[k],end=' ')
        k = k+1
    print()
