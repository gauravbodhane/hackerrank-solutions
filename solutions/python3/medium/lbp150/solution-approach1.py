# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp150/problem?isFullScreen=true
# Problem     LBP150
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-19, 09:53 p.m.
# Technique   trial-division-factor-counting
# Time        O(N * M) where N is the array size and …
# Space       O(N) to store the input array
# Insight     The algorithm determines primality by counting the total number of divisors for each integer in the array and verifying that the count equals exactly two.
# Interview   Before: "How would you check if all numbers in a list are prime?" After: "I would iterate through the list and verify each number has exactly two divisors using trial division, resulting in O(N * M) time complexity, where M is the maximum value in the array."
# Pitfalls    (1) The algorithm incorrectly identifies 1 as non-prime by counting only one divisor, which is correct, but it is inefficient for large integers.  (2) The trial division loop runs up to n, which is significantly slower than checking up to the square root of n.
# ──────────────────────────────────────────────────

def isprime(n):
    f = 0 
    for i in range(1,n+1):
        if n % i ==0:
            f = f+1
    return f == 2
    
n = int(input())
l = [int(i) for i in input().split()]
c = 0
for i in l:
    if isprime(i):
        c= c+1 
print('true' if c == n else 'false')
