# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp165/problem?isFullScreen=true
# Problem     LBP165
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-30, 04:23 p.m.
# ──────────────────────────────────────────────────

n = int(input())
l =[int(i) for i in input().split()]
l.sort()
print(l[2-1]+l[n-3])
