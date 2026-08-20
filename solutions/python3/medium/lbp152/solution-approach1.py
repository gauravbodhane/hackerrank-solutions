# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp152/problem?isFullScreen=true
# Problem     LBP152
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-20, 10:28 p.m.
# ──────────────────────────────────────────────────

n = int(input())
l = [int(i) for i in input().split()]
even = []
odd = []
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)   
a = even + odd
print(*a)
