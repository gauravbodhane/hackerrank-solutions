# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp211/problem?isFullScreen=true
# Problem     LBP211
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 08:22 a.m.
# Technique   diagonal-product-iteration
# Time        O(1)
# Space       O(1)
# Insight     The program calculates the product of the main diagonal elements of a 3x3 matrix by iterating through indices where row and column coordinates are identical.
# Interview   Before: "How do you compute the product of a matrix diagonal?" After: "I iterate through the 3x3 matrix and multiply elements where the row index equals the column index, resulting in O(1) time complexity for this fixed-size input."
# Pitfalls    (1) The code assumes a fixed 3x3 input size, which will fail if the input matrix dimensions differ from the hardcoded range(3) loops.  (2) The condition if i == i is redundant and does not validate the matrix structure or handle non-square inputs.
# ──────────────────────────────────────────────────

a =[]
for i in range(3):
    a.append([int(i) for i in input().split()])
s =1
for i in range(3):
    
    if i ==i:
        s *=a[i][i]
print(s)
