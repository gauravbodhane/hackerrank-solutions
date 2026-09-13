# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp199/problem?isFullScreen=true
# Problem     LBP199
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-13, 01:58 p.m.
# ──────────────────────────────────────────────────

n = int(input())
l =[int(i) for i in input().split()]
k = int(input())
s = 0
for i in l:
    s =s+i//k
print(s)
