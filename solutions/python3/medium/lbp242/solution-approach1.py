# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp242/problem?isFullScreen=true
# Problem     LBP242
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-25, 11:33 a.m.
# ──────────────────────────────────────────────────

l1 = [int (i) for i in input().split()]
l2 = [int (i) for i in input().split()]
l3 = [int (i) for i in input().split()]
l = [l1,l2,l3]
s = 0
for i in range(3):
    for j in range(3):
        if i%2!=0:
            s = s +l[i][j]
print(s)
