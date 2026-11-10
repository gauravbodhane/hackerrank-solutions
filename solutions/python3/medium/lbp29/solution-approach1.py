# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/lbp6222/challenges/lbp29/problem?isFullScreen=true
# Problem     LBP29
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-10, 04:24 p.m.
# ──────────────────────────────────────────────────

def isprime(n):
    f = 0
    for i in range(1,n+1):
        if n % i == 0:
            f += 1
    return f == 2
    
n = int(input())
print('true' if isprime(n) else 'false')
