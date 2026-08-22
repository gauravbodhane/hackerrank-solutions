# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp212/problem?isFullScreen=true
# Problem     LBP212
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-22, 08:04 a.m.
# Technique   anti-diagonal-product-iteration
# Time        O(1)
# Space       O(1)
# Insight     The algorithm calculates the product of elements on the anti-diagonal of a 3x3 matrix by accessing indices where the column index is defined as n-i-1.
# Interview   Before: "How would you compute the product of the secondary diagonal in a fixed-size matrix?" After: "I iterate through the rows and multiply the element at index [i][n-i-1], resulting in O(1) time complexity for a 3x3 matrix."
# Pitfalls    (1) The code assumes a fixed 3x3 input size and will raise an IndexError if the input matrix dimensions are smaller than 3x3.  (2) The logic relies on the input being provided as three separate lines of space-separated integers, which may fail if the input format deviates.
# ──────────────────────────────────────────────────

a = []

for i in range(3):
    a.append([int(x) for x in input().split()])

s = 1

for i in range(3):
    s = s * a[i][3-i-1]

print(s)
