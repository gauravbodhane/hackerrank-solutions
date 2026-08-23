# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp232/problem?isFullScreen=true
# Problem     LBP232
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-23, 01:43 p.m.
# ──────────────────────────────────────────────────


l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]
l3 = [int(i) for i in input().split()]
m = int(input())
n = int(input())
l = [l1,l2,l3]
l[m-1],l[n-1] = l[n-1],l[m-1]
for i in range(3):
    for j in range(3):
        print(l[i][j],end=' ')
    print()
