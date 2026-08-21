# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp222/problem?isFullScreen=true
# Problem     LBP222
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 09:15 p.m.
# ──────────────────────────────────────────────────


a = []
b = []
c= []
for i in range(3):
    a.append([int(x) for x in input().split()])
for i in range(3):
    b.append([int(x) for x in input().split()])
for i in range(3):
    cc=[]
    for j in range(3):
        cc.append(a[i][j]+b[i][j])
    c.append(cc)
for i in range(3):
    for j in range(3):
        print(c[i][j],end=' ')
    print()
