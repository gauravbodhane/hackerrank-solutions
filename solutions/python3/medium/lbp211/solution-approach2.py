# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp211/problem?isFullScreen=true
# Problem     LBP211
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 09:06 a.m.
# Technique   diagonal-product-iteration
# Time        O(1)
# Space       O(1)
# Insight     The program calculates the product of the main diagonal elements of a fixed 3x3 matrix by iterating through indices where row and column coordinates are identical.
# Interview   Before: "How would you compute the product of a matrix diagonal?" After: "I iterate through the 3x3 matrix using a single loop to access elements at [j][j], resulting in O(1) time and space complexity for this fixed-size input."
# Pitfalls    (1) The code assumes a fixed 3x3 input size, which will fail if the input matrix dimensions differ from the expected 3x3 format.  (2) The logic assumes the input contains exactly three lines of three integers, which may cause an EOFError or index error if the input is malformed.
# ──────────────────────────────────────────────────

a = []
for i in range(3):
    a.append([int(i) for i in input().split()])
s = 1
for  j in range(3):
    if j==j:
        s *= a[j][j]
        
print(s)
