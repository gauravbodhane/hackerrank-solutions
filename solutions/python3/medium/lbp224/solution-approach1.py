# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp224/problem?isFullScreen=true
# Problem     LBP224 
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-22, 08:30 a.m.
# ──────────────────────────────────────────────────


a = []
b = []
c = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    a.append([int (i) for i in input().split()])
for i in range(3):
    b.append([int (i) for i in input().split()])
    
    
for i in range(3):
    for j in range(3):
        for k in range(3):
            c[i][j]= c[i][j]+(a[i][k]*b[k][j])
   
for i  in range(3):
    for j in range(3):
        print(c[i][j],end=' ')
    print()
