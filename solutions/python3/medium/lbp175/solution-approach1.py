# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp175/problem?isFullScreen=true
# Problem     LBP175
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 08:29 a.m.
# Technique   trial-division-loop
# Time        O(n^2)
# Space       O(1)
# Insight     The program iterates through every integer from two to n, checking for primality by testing divisibility against all integers up to the number itself.
# Interview   Before: "How would you print all primes up to n?" After: "I would iterate from two to n and check each for factors. This approach has O(n^2) time complexity, which is sufficient for small n as specified in the problem constraints."
# Pitfalls    (1) The trial division loop checks up to n-1, which is inefficient compared to checking up to the square root of n.  (2) The code fails to handle inputs less than two, as the range(2, n+1) will be empty and produce no output.
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
