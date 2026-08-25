# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp247/problem?isFullScreen=true
# Problem     LBP247
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-25, 11:55 a.m.
# ──────────────────────────────────────────────────

def isprime(n):
    f = 0
    for i in range(1,n+1):
        if n%i == 0:
            f =f +1 
    return f == 2
    
l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]
l3 = [int(i) for i in input().split()]
l =[l1,l2,l3]
s = 0
for i in range(3):
    for j in range(3):
        if isprime(l[i][j]):
            s =s +l[i][j]
print(s)
