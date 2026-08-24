# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp235/problem?isFullScreen=true
# Problem     LBP235
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-24, 02:16 p.m.
# ──────────────────────────────────────────────────

l1 = [int (i) for i in input().split()]
l2 = [int (i) for i in input().split()]
l3 = [int (i) for i in input().split()]
l = [l1,l2,l3]
flag = True
for i in range(3):
    for j in range(3):
        if j<i and l[i][j]!= 0:
            flag=False
print('Yes' if  flag else 'No')
