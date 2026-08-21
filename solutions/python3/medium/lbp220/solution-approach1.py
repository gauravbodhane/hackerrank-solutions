# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp220/problem?isFullScreen=true
# Problem     LBP220
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 08:43 p.m.
# ──────────────────────────────────────────────────

flag = True
a = []
for i in range(3):
    a.append([int(x) for x in input().split()])
for i in range(3):
    for j in range(3):
        if i==j and a[i][j]!=1:
            flag = False
            break
        if i!=j and a[i][j]!= 0:
            flag=False
            break
print('Yes' if flag else 'No')
            
