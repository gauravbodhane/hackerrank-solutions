# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp148/problem?isFullScreen=true
# Problem     LBP148
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-19, 09:35 p.m.
# ──────────────────────────────────────────────────

n = int(input())
l = [int(i) for i in input().split()]
m = int(input())
if m <= n:
    for i in l[n-m:]:
        print(i,end=' ')
else :
    print(0)
