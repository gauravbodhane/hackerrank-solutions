# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp254/problem?isFullScreen=true
# Problem     LBP254
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-15, 01:10 p.m.
# ──────────────────────────────────────────────────

n = int(input())
L = [int(i) for i in input().split()]

for i in L:
    c = 0
    while c<= i :
        if (c*c*c==i):
            print(i,end=' ')
            break
        c =c +1
