# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp212/problem?isFullScreen=true
# Problem     LBP212
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 08:28 a.m.
# Technique   anti-diagonal-product-iteration
# Time        O(1)
# Space       O(1)
# Insight     The code calculates the product of elements on the anti-diagonal of a 3x3 matrix by iterating through rows and accessing columns at index 2-i.
# Interview   Before: "How would you compute the product of the anti-diagonal in a fixed 3x3 matrix?" After: "I iterate through each row i and multiply the element at column 2-i, resulting in O(1) time and O(1) space complexity for this fixed-size input."
# Pitfalls    (1) The code assumes the input is strictly a 3x3 matrix as per the problem constraints.  (2) The index calculation 3-i-1 correctly targets columns 2, 1, and 0 for rows 0, 1, and 2 respectively.
# ──────────────────────────────────────────────────

a = []
for i in range(3):
    a.append([int(i) for i in input().split()]) 
s= 1
for i in range(3):
    s *= a[i][3-i-1] 
print(s)
