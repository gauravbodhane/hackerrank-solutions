# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp182/problem?isFullScreen=true
# Problem     LBP182
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-10, 05:47 p.m.
# Technique   prime-counting-linear-scan
# Time        O(N * M) where M is the maximum value i…
# Space       O(N)
# Insight     The implementation counts the total number of prime integers in the input array and returns that count if it is not equal to one, rather than calculating the difference between the largest and smallest primes.
# Interview   Before: "How do you find the difference between the largest and smallest primes?" After: "The current implementation counts primes in O(N*M) time, but it fails to calculate the difference as requested, returning the count instead of the range of prime values."
# Pitfalls    (1) The code returns the count of primes instead of the absolute difference between the largest and smallest prime numbers as required by the problem statement.  (2) The isprime function uses an O(N) trial division approach which is inefficient for large integers.  (3) The logic incorrectly handles the case where there are zero primes by returning zero, which happens to match the requirement for one or fewer primes.
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
