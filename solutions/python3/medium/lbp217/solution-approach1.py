# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp217/problem?isFullScreen=true
# Problem     LBP217
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 08:21 p.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOU
a = []

for i in range(3):
    a.append([int(x) for x in input().split()])
for i in range(3):
    for j in range(3):
        print(a[j][i],end=' ')
    print()
