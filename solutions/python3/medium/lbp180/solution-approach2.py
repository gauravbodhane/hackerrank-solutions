# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp180/problem?isFullScreen=true
# Problem     LBP180
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-10, 05:21 p.m.
# Technique   bit-counting-loop
# Time        O(log n)
# Space       O(1)
# Insight     The algorithm determines parity by iteratively extracting the least significant bit and counting the total number of set bits in the binary representation of the input integer.
# Interview   Before: "How do you determine if a number has odd or even parity?" After: "I count the set bits by repeatedly checking the remainder of division by two, resulting in O(log n) time complexity, which is efficient for any integer input."
# Pitfalls    (1) The loop condition n > 0 fails to process the input 0, which would incorrectly result in an even parity output.  (2) The logic assumes non-negative integer input, as negative numbers would cause an infinite loop with the current n // 2 implementation.
# ──────────────────────────────────────────────────

n = int(input())
count = 0

while n > 0:
    if n % 2 == 1:
        count += 1
    n= n // 2
        
if count % 2 == 0:
    print('even')
else:
    print('odd')
