# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp248/problem?isFullScreen=true
# Problem     LBP248	
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-25, 12:06 p.m.
# ──────────────────────────────────────────────────

l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]
l3 = [int(i) for i in input().split()]
l = [l1,l2 , l3]
c = 0
for i in range(3):
    for j in range(3):
        for k in str(l[i][j]):
            if k in '2357':
                c =c +1
print(c)
