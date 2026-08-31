# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp167/problem?isFullScreen=true
# Problem     LBP167
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-31, 02:26 p.m.
# Technique   factorial-trailing-zero-counting
# Time        O(N log N)
# Space       O(N log N)
# Insight     The algorithm calculates the full factorial of the input number and iteratively strips trailing zeros by checking the string representation of the resulting integer.
# Interview   Before: "I should count factors of 5 in the prime factorization of n! to find trailing zeros." After: "The current approach computes the full factorial, which takes O(N log N) time and space, and then counts trailing zeros by string manipulation, which is inefficient for large inputs."
# Pitfalls    (1) Calculating the full factorial of large numbers leads to memory exhaustion and performance degradation.  (2) String conversion of extremely large integers is computationally expensive compared to mathematical division.  (3) The approach fails to utilize Legendre's formula, which provides a more efficient O(log N) solution for counting trailing zeros.
# ──────────────────────────────────────────────────

import math 

def count(n):
    c= 0
    while str(n).endswith('0'):
        c +=1 
        n = n//10
    return c
n = int(input())
print(count(math.factorial(n)))
