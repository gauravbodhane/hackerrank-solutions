# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp223/problem?isFullScreen=true
# Problem     LBP223
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 09:23 p.m.
# ──────────────────────────────────────────────────

a = []
b = []
c = []
for i in range(3):
    a.append([int(i) for i in input().split()])
for i in range(3):
    b.append([int(i) for i in input().split()])
for i in range(3):
    cc=[]
    for j in range(3):
        cc.append(a[i][j]-b[i][j])
    c.append(cc)
for i in range(3):
    for j in range(3):
        print(c[i][j],end=' ')
    print()
