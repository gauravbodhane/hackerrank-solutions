# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp229/problem?isFullScreen=true
# Problem     LBP229
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-23, 01:19 p.m.
# ──────────────────────────────────────────────────


l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]
l3 = [int(i) for i in input().split()]
l = [l1,l2,l3]
ll =[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        ll[i][j] = l[j][i]
for i in range(3):
    ll[i].sort()
    
for i in range(3):
    for j in range(3):
        print(ll[j][i],end=' ')
    print()
