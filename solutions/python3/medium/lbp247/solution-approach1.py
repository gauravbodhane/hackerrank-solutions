# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp247/problem?isFullScreen=true
# Problem     LBP247
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-25, 11:55 a.m.
# Technique   nested-loop-prime-summation
# Time        O(N^2 * M) where N is matrix dimension …
# Space       O(N^2)
# Insight     The program iterates through each element of the 3x3 matrix and adds the value to a running total if the element satisfies the primality condition defined by having exactly two divisors.
# Interview   Before: "How would you sum prime numbers in a 3x3 matrix?" After: "I would iterate through each cell and check primality by counting divisors up to the number itself. This approach runs in O(N^2 * M) time, where N is the matrix dimension and M is the maximum element value."
# Pitfalls    (1) The primality test fails for n=1 because the loop range(1, 2) counts only one divisor, correctly identifying it as non-prime.  (2) The primality test is inefficient for large numbers as it iterates up to n, resulting in O(n) complexity per check.
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
