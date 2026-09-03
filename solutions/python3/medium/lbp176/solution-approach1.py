# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp176/problem?isFullScreen=true
# Problem     LBP176
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-03, 06:01 p.m.
# Technique   euclidean-algorithm-iterative
# Time        O(log(min(a, b)))
# Space       O(1)
# Insight     The algorithm iteratively replaces the larger number with the remainder of the division until the remainder becomes zero, leaving the greatest common divisor in the first variable.
# Interview   Before: "How would you find the greatest common divisor of two integers?" After: "I would use the Euclidean algorithm, which repeatedly applies the modulo operator to reduce the numbers. This approach is highly efficient with a time complexity of O(log(min(a, b))) and handles any two positive integers provided in the input."
# Pitfalls    (1) Failing to handle the case where one input is zero, although the Euclidean algorithm naturally returns the non-zero value as the GCD.  (2) Assuming the input order matters, whereas the algorithm correctly swaps values if the first integer is smaller than the second.
# ──────────────────────────────────────────────────

a, b = (int(i) for i in input().split())

while b != 0:
    a , b = b , a%b
print(a)
