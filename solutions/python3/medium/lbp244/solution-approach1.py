# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp244/problem?isFullScreen=true
# Problem     LBP244
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-25, 11:35 a.m.
# ──────────────────────────────────────────────────

l1 = [int (i) for i in input().split()]
l2 = [int (i) for i in input().split()]
l3 = [int (i) for i in input().split()]
l = [l1,l2,l3]
s = 0
for i in range(3):
    for j in range(3):
        if j%2!=0:
            s = s +l[i][j]
print(s)
