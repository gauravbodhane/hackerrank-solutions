# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp182/problem?isFullScreen=true
# Problem     LBP182
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-10, 05:47 p.m.
# ──────────────────────────────────────────────────

def isprime(n):
    f = 0 
    for i in range(1, n+1):
        if n % i ==0:
            f += 1
    return f == 2 
n = int(input())
l = [int(i) for i in input().split()]
c = 0
for i in l :
    if isprime(i):
        c += 1 
if c == 1 :
    print(0)
else:
    print(c)
