# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp250/problem?isFullScreen=true
# Problem     LBP250	
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-25, 12:20 p.m.
# ──────────────────────────────────────────────────

l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]
l3 = [int(i) for i in input().split()]
l = [l1,l2,l3]
for i in range(3):
    for j in range(3):
        s = str(l[i][j])
        if s==s[::-1]:
            print(l[i][j],end=' ')
        else:
            print('0',end=' ')
    print()
