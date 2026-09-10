# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp180/problem?isFullScreen=true
# Problem     LBP180
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-10, 05:17 p.m.
# Technique   binary-string-count
# Time        O(log n)
# Space       O(log n)
# Insight     The parity of a decimal number is determined by checking if the count of set bits in its binary representation is divisible by two.
# Interview   Before: "How would you determine if a number has odd or even parity?" After: "I convert the integer to a binary string and count the occurrences of '1'. This approach runs in O(log n) time, where n is the input value, as the number of bits is logarithmic relative to the input magnitude."
# Pitfalls    (1) The solution assumes the input is a non-negative integer, as bin() behavior with negative numbers includes a sign prefix that might affect bit counting logic.  (2) Relying on string conversion for bit counting is less efficient than bitwise operations for very large integers.
# ──────────────────────────────────────────────────

n = int(input())

binary = bin(n)
ones = binary.count("1")

if ones % 2 == 0:
    print('even')
else:
    print('odd')
