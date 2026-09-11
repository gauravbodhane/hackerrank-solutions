# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp189/problem?isFullScreen=true
# Problem     LBP189
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-11, 05:19 p.m.
# Technique   string-reversal-conversion
# Time        O(D)
# Space       O(D)
# Insight     The program calculates the absolute difference between an integer and its reversed digit representation by converting the input to a string, reversing it, and performing arithmetic on the integer casts.
# Interview   Before: "How would you find the difference between a number and its reverse?" After: "I convert the number to a string to reverse it in O(D) time, where D is the number of digits, then subtract the integer values to find the absolute difference."
# Pitfalls    (1) The code assumes the input is a valid integer string and will raise a ValueError if non-numeric characters are provided.  (2) Leading zeros in the reversed number are handled correctly by the int() constructor, but this might be unexpected if the problem required preserving string formatting.
# ──────────────────────────────────────────────────

n = input()

g = n[::-1]

g1 = int(g)
n2 = int(n) 
print(abs(g1-n2))

