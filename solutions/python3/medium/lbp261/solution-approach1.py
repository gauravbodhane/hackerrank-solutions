# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp261/problem?isFullScreen=true
# Problem     LBP261
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-16, 02:58 p.m.
# Technique   binary-string-count
# Time        O(log n)
# Space       O(log n)
# Insight     The solution converts the integer to its binary string representation and counts the occurrences of the character '1'.
# Interview   Before: "How would you count set bits in an integer?" After: "I used Python's built-in bin() function to convert the integer to a string, then counted the '1' characters, resulting in O(log n) time complexity where n is the input value."
# Pitfalls    (1) The bin() function includes a '0b' prefix in the string, but counting '1's remains accurate as '0b' contains no '1's.  (2) The solution assumes non-negative integer input as per the problem context, as bin() on negative integers includes a '-' sign.
# ──────────────────────────────────────────────────

n = int(input())
s = bin(n) 
print(s.count('1'))
