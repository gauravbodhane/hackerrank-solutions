# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp255/problem?isFullScreen=true
# Problem     LBP255
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-15, 01:25 p.m.
# Technique   string-reversal-subtraction
# Time        O(D)
# Space       O(D)
# Insight     The algorithm calculates the difference between the input integer and its reversed string representation by casting both to integers.
# Interview   Before: "How would you calculate the difference between a number and its reverse?" After: "I convert the number to a string, reverse it using slicing, and subtract the integer values. This runs in O(D) time, where D is the number of digits, handling both positive and negative inputs correctly."
# Pitfalls    (1) The code fails if the input contains non-numeric characters, as int() will raise a ValueError.  (2) The slicing approach n[::-1] does not handle negative signs correctly if the input is negative, as the minus sign moves to the end of the string.
# ──────────────────────────────────────────────────

n = input()

print(int(n)-int(n[::-1]))
