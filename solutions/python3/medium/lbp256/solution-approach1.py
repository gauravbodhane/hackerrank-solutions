# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp256/problem?isFullScreen=true
# Problem     LBP256
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-16, 01:02 p.m.
# ──────────────────────────────────────────────────

n = int(input())
c = 0
while n!= 0:
    d = n%10
    if d % 2==0:
        c = c+1
    n = n//10
    
print(c)
