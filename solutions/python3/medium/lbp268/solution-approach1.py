# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp268/problem?isFullScreen=true
# Problem     LBP268
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-17, 02:24 p.m.
# Technique   arithmetic-absolute-difference
# Time        O(1)
# Space       O(1)
# Insight     The program calculates the absolute difference between the sum and the product of two integers using the built-in abs function.
# Interview   Before: "How would you compute the absolute difference between two arithmetic operations?" After: "I compute the sum and product, then apply the absolute value function to their difference, resulting in O(1) time and space complexity."
# Pitfalls    (1) Failing to use the abs function will result in negative values when the product exceeds the sum.  (2) Assuming the inputs are on the same line when the problem implies separate input calls.
# ──────────────────────────────────────────────────

a = int(input())
b = int(input())

print(abs((a+b)-(a*b)))
