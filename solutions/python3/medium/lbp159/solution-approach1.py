# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp159/problem?isFullScreen=true
# Problem     LBP159
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-29, 09:22 a.m.
# Technique   boolean-membership-check
# Time        O(n)
# Space       O(n)
# Insight     The code determines if all elements in the list are truthy by verifying that zero is not present in the input array.
# Interview   Before: "How would you check if every element in an array is non-zero?" After: "I would use the 'not in' operator to check for zero, which runs in O(n) time and O(n) space, effectively validating the truthiness of all elements in the list."
# Pitfalls    (1) Assuming the function checks for all falsy values instead of specifically checking for zero as defined by the problem constraints.  (2) Failing to account for the O(n) space complexity required to store the input list before performing the membership check.
# ──────────────────────────────────────────────────

n = int(input())
L = [int(i) for i in input().split()]
print(str(0 not in L).lower())
