# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp240/problem?isFullScreen=true
# Problem     LBP240
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-25, 11:19 a.m.
# ──────────────────────────────────────────────────

l1 = [int (i) for i in input().split()]
l2 = [int (i) for i in input().split()]
l3 = [int (i) for i in input().split()]
l =[l1,l2,l3]
for i in range(3):
    for j in range(3):
        print(l[i][j]* l[i][j],end=' ')
    print()
