# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp260/problem?isFullScreen=true
# Problem     LBP260
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-16, 02:51 p.m.
# Technique   factorial-last-non-zero-digit
# Time        O(n)
# Space       O(n)
# Insight     The code calculates the factorial of the input and extracts the last non-zero digit by checking if the last digit is zero and dividing by ten if necessary.
# Interview   Before: "How would you find the last non-zero digit of a factorial?" After: "I compute the full factorial in O(n) time and check the last digit; if it is zero, I perform integer division by ten to isolate the preceding digit, which is O(n) space due to Python's arbitrary-precision integers."
# Pitfalls    (1) The implementation uses math.factorial which consumes O(n) space for large inputs, potentially causing memory issues.  (2) The logic only checks the last digit for zero, which fails if the last two digits are zero, such as in 10! = 3628800.
# ──────────────────────────────────────────────────

import math
n = int(input())
f = math.factorial(n) 
if f% 10 == 0:
    print((f//10)%10)
else:
    print(f%10)
