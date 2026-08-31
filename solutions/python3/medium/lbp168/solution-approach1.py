# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp168/problem?isFullScreen=true
# Problem     LBP168
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-31, 02:33 p.m.
# Technique   list-slicing-comparison
# Time        O(N)
# Space       O(N)
# Insight     The program determines if an array is a palindrome by comparing the original list to its reversed copy created via slicing.
# Interview   Before: "How would you check if an array is a palindrome?" After: "I would compare the array to its reverse. This approach takes O(N) time and O(N) space, which is efficient for checking symmetry in an array of size N."
# Pitfalls    (1) The slicing operation creates a full copy of the list, which consumes O(N) additional space.  (2) The comparison L == L[::-1] relies on Python's list equality operator, which performs a full element-wise check.
# ──────────────────────────────────────────────────

n = int(input())
L=[int(i) for i in input().split()]
print("true" if L==L[::-1]else "false")
