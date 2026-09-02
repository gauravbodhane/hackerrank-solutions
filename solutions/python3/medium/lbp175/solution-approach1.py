# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp175/problem?isFullScreen=true
# Problem     LBP175
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 08:29 a.m.
# ──────────────────────────────────────────────────

def isprime(n):
    f = 0
    for i in range(2,n):
        if n % i == 0:
            f = f +1
            break
    return f==0
        
n = int(input())
for i in range(2,n+1):
    if isprime(i):
        print(i,end=' ')
