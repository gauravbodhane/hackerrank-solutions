# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp230/problem?isFullScreen=true
# Problem     LBP230
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-23, 01:23 p.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]
l3 = [int(i) for i in input().split()]
l = [l1,l2,l3]
ll =[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        ll[i][j] = l[j][i]
for i in range(3):
    ll[i].sort(reverse=True)
    
for i in range(3):
    for j in range(3):
        print(ll[j][i],end=' ')
    print()
