# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp219/problem?isFullScreen=true
# Problem     LBP219
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 08:35 p.m.
# ──────────────────────────────────────────────────

a = []

for i in range(3):
    a.append([int(x) for x in input().split()])
even = 0
odd = 0
for i in range(3):
    for j in range(3):
        if a[i][j]%2 == 0 and a[i][j]!= 0:
            even = even+ 1 
        if a[i][j]%2!= 0:
            odd = odd+ 1

print(odd)
print(even)
