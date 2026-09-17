# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp265/problem?isFullScreen=true
# Problem     LBP265
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-17, 02:04 p.m.
# ──────────────────────────────────────────────────

n = int(input()) 
while n!=0:
    d = n%10
    print(d*d,end='')
    n = n//10
    
