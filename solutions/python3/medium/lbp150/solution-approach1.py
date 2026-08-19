# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp150/problem?isFullScreen=true
# Problem     LBP150
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-19, 09:53 p.m.
# ──────────────────────────────────────────────────

def isprime(n):
    f = 0 
    for i in range(1,n+1):
        if n % i ==0:
            f = f+1
    return f == 2
    
n = int(input())
l = [int(i) for i in input().split()]
c = 0
for i in l:
    if isprime(i):
        c= c+1 
print('true' if c == n else 'false')
