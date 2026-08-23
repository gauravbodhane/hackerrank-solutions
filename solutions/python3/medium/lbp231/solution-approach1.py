# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp231/problem?isFullScreen=true
# Problem     LBP231
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-23, 01:29 p.m.
# Technique   matrix-zero-counting
# Time        O(N*M)
# Space       O(N*M)
# Insight     The algorithm determines if a matrix is sparse by counting the total number of zero elements and comparing that count against the threshold of five.
# Interview   Before: "How do you identify a sparse matrix?" After: "A sparse matrix is defined by having a majority of zero elements. By iterating through the 3x3 grid and counting zeros, we check if the count is at least five, resulting in O(1) time complexity for this fixed-size input."
# Pitfalls    (1) The code assumes a fixed 3x3 input size, which fails if the input matrix dimensions differ from the hardcoded structure.  (2) The definition of majority is strictly interpreted as count >= 5, which may not align with definitions requiring strictly more than half the elements.
# ──────────────────────────────────────────────────


l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]
l3 = [int(i) for i in input().split()]
l = [l1,l2,l3]
counter = 0
for i in l:
    counter= counter+i.count(0)
print('Yes' if counter>= 5 else 'No')
