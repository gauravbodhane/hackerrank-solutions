# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp170/problem?isFullScreen=true
# Problem     LBP170
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-31, 02:54 p.m.
# ──────────────────────────────────────────────────

n, m = (int(i) for i in input().split())
for i in range(n):
    L = [int(i) for i in input().split()]
    for j in L:
        print(j,end=' ')
