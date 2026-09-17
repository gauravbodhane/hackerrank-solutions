# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp265/problem?isFullScreen=true
# Problem     LBP265
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-17, 02:04 p.m.
# Technique   modulo-division-digit-extraction
# Time        O(d)
# Space       O(1)
# Insight     The algorithm extracts each digit from the input number using modulo and integer division, squares the digit, and prints it immediately, effectively reversing the number while performing the transformation.
# Interview   Before: "How would you transform and reverse a number's digits?" After: "I use modulo and integer division to process digits in O(d) time, where d is the number of digits. This approach avoids string conversion and handles the reversal naturally by printing digits as they are extracted from the end."
# Pitfalls    (1) The code fails to handle the input constraint requiring numbers to have at least two digits, as it processes single-digit inputs without restriction.
# ──────────────────────────────────────────────────

n = int(input()) 
while n!=0:
    d = n%10
    print(d*d,end='')
    n = n//10
    
