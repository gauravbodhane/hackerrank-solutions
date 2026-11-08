# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/lbp6222/challenges/lbp11/problem?isFullScreen=true
# Problem     LBP11
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-08, 03:03 p.m.
# ──────────────────────────────────────────────────

def isprime(n):
    f = 0
    for i in range(1,n+1):
        if n% i == 0:
            f=f+1
    return f == 2


n = input()
sum =0 
for i in n:
    if isprime(int(i)):
        sum += int(i)
print(sum)
    
