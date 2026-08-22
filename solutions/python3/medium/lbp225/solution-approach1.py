# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp225/problem?isFullScreen=true
# Problem     LBP225
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-22, 08:43 a.m.
# ──────────────────────────────────────────────────

l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]
l3 = [int(i) for i in input().split()]
l = [l1,l2,l3]
ll= []
for i in range(3):
    for j in range(3):
        ll.append(l[i][j])
ll.sort()
k = 0
for i in range(3):
    for j in range(3):
        l[i][j]=ll[k]
        k= k +1
        
for i in range(3):
    for j in range(3):
        print(l[i][j],end=' ')
    print()
