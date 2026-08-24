# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp238/problem?isFullScreen=true
# Problem     LBP238
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-24, 07:26 p.m.
# ──────────────────────────────────────────────────

l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]
l3 = [int(i) for i in input().split()]
l = [l1,l2,l3]
c = 0
for i in range(3):
    for j in range(3):
        if l[i][j] == l[j][i]:
            c = c+1
print('Yes' if c==9 else 'No')
