# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp221/problem?isFullScreen=true
# Problem     LBP221
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 09:06 p.m.
# ──────────────────────────────────────────────────

flag = True
a = []
b = []
for i in range(3):
    a.append([int(x) for x in input().split()])
for i in range(3):
    b.append([int(x) for x in input().split()])
for i in range(3):
    for j in range(3):
        if a[i][j]!=b[i][j]:
            flag = False
            break
print('Yes' if flag else 'No')
            
