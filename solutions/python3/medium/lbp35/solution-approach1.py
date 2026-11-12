# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/lbp6222/challenges/lbp35/problem?isFullScreen=true
# Problem     LBP35
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-12, 06:05 p.m.
# ──────────────────────────────────────────────────

def isprime(n):
    return n in (1,2,3,5,7)
    
n = int(input()) 
s = 0

while n > 0 :
    d = n% 10
    if not isprime(d):
        s+= d 
    n = n// 10
print(s)
