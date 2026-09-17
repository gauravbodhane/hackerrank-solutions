# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp262/problem?isFullScreen=true
# Problem     LBP262
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-17, 01:43 p.m.
# Technique   modular-arithmetic-check
# Time        O(1)
# Space       O(1)
# Insight     The code verifies if the last digit of the cube of an integer matches the integer itself by checking the remainder of the cube when divided by ten.
# Interview   Before: "How do you check if a number's cube ends with the number itself?" After: "I use the modulo operator to isolate the last digit of the cube, which runs in O(1) time and O(1) space, effectively validating the condition for any integer input."
# Pitfalls    (1) The code only checks the last digit, which is insufficient for multi-digit numbers where the entire suffix must match the original number.  (2) The logic fails for any input greater than nine because the modulo ten operation only compares the last digit rather than the full trailing sequence.
# ──────────────────────────────────────────────────

n = int(input())
print('true' if n**3%10==n else 'false') 
