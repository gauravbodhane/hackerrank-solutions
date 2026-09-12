# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp191/problem?isFullScreen=true
# Problem     LBP191
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-12, 12:10 p.m.
# ──────────────────────────────────────────────────

def sum(n):
    sum=0
    while n!= 0:
        d = n% 10 
        sum = sum +d
        n = n// 10
    return sum

n = int(input())
while True:
    if n>=1 and n <= 26:
        print(chr(n+64))
        break
    else:
        n = sum(n)
        
