# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp256/problem?isFullScreen=true
# Problem     LBP256
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-16, 01:02 p.m.
# Technique   digit-extraction-modulo-loop
# Time        O(log n)
# Space       O(1)
# Insight     The algorithm iterates through each digit of the input integer by repeatedly applying modulo and integer division operations, incrementing a counter whenever an even digit is encountered.
# Interview   Before: "How do I count even digits in a number?" After: "I extract each digit using modulo 10 and check parity, which runs in O(log n) time where n is the input value. This handles the input as a numeric type rather than a string."
# Pitfalls    (1) The loop condition n != 0 fails to count even digits if the input is exactly 0, as the loop body never executes.  (2) The algorithm assumes the input is a positive integer and may behave unexpectedly if negative numbers are provided due to the behavior of the modulo operator.
# ──────────────────────────────────────────────────

n = int(input())
c = 0
while n!= 0:
    d = n%10
    if d % 2==0:
        c = c+1
    n = n//10
    
print(c)
