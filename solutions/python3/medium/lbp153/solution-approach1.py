# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp153/problem?isFullScreen=true
# Problem     LBP153
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-28, 01:43 p.m.
# ──────────────────────────────────────────────────

n = int(input())
L = [int(i) for i in input().split()]
c = 0
for i in range(0,n):
    for k in range(1,L[i]+1):
        if k*k == L[i]:
            c = c+1
print(c)  
