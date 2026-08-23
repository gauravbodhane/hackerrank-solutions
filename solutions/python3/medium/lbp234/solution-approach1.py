# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp234/problem?isFullScreen=true
# Problem     LBP234
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-23, 02:11 p.m.
# ──────────────────────────────────────────────────

l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]
l3 = [int(i) for i in input().split()]

l = [l1,l2,l3]
for i in range(3):
    l[i][i] , l[i][3-i-1] = l[i][3-i-1], l[i][i]
for i in range(3):
    for j in range(3):
        print(l[i][j],end=' ')
    print()
