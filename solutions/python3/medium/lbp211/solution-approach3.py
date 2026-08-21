# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp211/problem?isFullScreen=true
# Problem     LBP211
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 07:22 p.m.
# Technique   diagonal-product-iteration
# Time        O(1)
# Space       O(1)
# Insight     The program calculates the product of the main diagonal elements of a fixed 3x3 matrix by iterating through indices where the row and column are equal.
# Interview   Before: "How would you compute the product of a matrix diagonal?" After: "I iterate through the 3x3 matrix using a single loop, multiplying elements where row equals column index, resulting in O(1) time and O(1) space complexity for this fixed-size input."
# Pitfalls    (1) The code assumes a fixed 3x3 input size, which will fail if the input matrix dimensions differ from the expected 3x3 format.  (2) The logic relies on the input being provided as three separate lines, which may cause errors if the input format deviates from the expected structure.
# ──────────────────────────────────────────────────

n = []
for i in range(3):
    n.append([int (i) for i in input().split() ])
s =1
for i in range(3):
    if i==i:
        s*= n[i][i]
print(s)
