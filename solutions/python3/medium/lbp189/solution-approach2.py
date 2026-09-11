# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp189/problem?isFullScreen=true
# Problem     LBP189
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-11, 05:26 p.m.
# Technique   integer-reversal-arithmetic
# Time        O(log n)
# Space       O(1)
# Insight     The algorithm iteratively extracts the last digit of the integer using modulo and builds the reversed number by shifting existing digits left, maintaining the invariant that the sum of digits processed equals the original number's magnitude.
# Interview   Before: "How would you calculate the absolute difference between a number and its reverse?" After: "I used an O(log n) arithmetic approach to reverse the integer by repeatedly extracting digits, ensuring O(1) space complexity even for large inputs."
# Pitfalls    (1) Failing to handle the absolute value requirement, which results in negative differences for numbers where the reverse is smaller than the original.  (2) Assuming the input is always positive, though the loop condition n > 0 correctly handles positive integers as per the provided samples.
# ──────────────────────────────────────────────────

n = int(input())

original = n 
reverse = 0 
while n > 0:
    digit = n% 10 
    reverse = reverse * 10 + digit
    n = n // 10

diff = (reverse-original)
print(abs(diff))
