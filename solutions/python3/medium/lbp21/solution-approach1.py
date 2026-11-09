# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/lbp6222/challenges/lbp21/problem?isFullScreen=true
# Problem     LBP21
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-09, 04:13 p.m.
# ──────────────────────────────────────────────────

def isprime(n):
    f = 0
    for i in range(1,n+1):
        if n % i ==0:
            f+=1
    return f==2
n = input()
c = 0
for i in n:
    if isprime(int(i)):
        c +=int(i)
print(c)
