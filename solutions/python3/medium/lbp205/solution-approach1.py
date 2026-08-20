# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp205/problem?isFullScreen=true
# Problem     LBP205
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-20, 08:45 a.m.
# ──────────────────────────────────────────────────

def isprime(n):
    f = 0
    for i in range(1,n+1):
        if n%i==0:
            f = f+1
    return f==2
a = []
for i in range(3):
    a.append([int(i) for i in input().split()])
s= 0
for i in range(3):
    for j in range(3):
        if isprime(a[i][j]):
            s=s+a[i][j] 
print(s)
