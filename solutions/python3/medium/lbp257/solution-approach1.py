# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp257/problem?isFullScreen=true
# Problem     LBP257
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-16, 01:21 p.m.
# ──────────────────────────────────────────────────

n = int(input())
a1 = -1
a2 = 1
sum = 0
for i in range(1,n+1):
    a3 = a1 + a2
    sum = sum + a3 
    a1 , a2 = a2, a3
print(sum)
