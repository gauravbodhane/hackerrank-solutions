# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp237/problem?isFullScreen=true
# Problem     LBP237
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-24, 07:18 p.m.
# Technique   nested-loop-scalar-multiplication
# Time        O(1)
# Space       O(1)
# Insight     The program processes a fixed 3x3 matrix by iterating through each element and multiplying it by the provided scalar value.
# Interview   Before: "How would you perform scalar multiplication on a 3x3 matrix?" After: "I would iterate through each row and column using nested loops to multiply every element by the scalar, resulting in O(1) time complexity for this fixed-size input."
# Pitfalls    (1) The code assumes exactly nine integers are provided for the matrix, which may fail if the input format deviates from the expected 3x3 structure.  (2) The use of print with end=' ' may leave a trailing space at the end of each row, which might be rejected by strict output checkers.
# ──────────────────────────────────────────────────

l1 = [int (i) for i in input().split()]
l2 = [int (i) for i in input().split()]
l3 = [int (i) for i in input().split()]
l = [l1,l2,l3]
l4 = int(input()) 
for i in range(3):
    for j in range(3):
        print(l[i][j]*l4,end=' ')
    print()
