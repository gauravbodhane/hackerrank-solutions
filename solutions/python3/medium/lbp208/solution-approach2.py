# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp208/problem?isFullScreen=true
# Problem     LBP208
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 08:51 a.m.
# Technique   diagonal-sum-iteration
# Time        O(1)
# Space       O(1)
# Insight     The algorithm iterates through the indices of a fixed 3x3 matrix to accumulate values where the row index equals the column index.
# Interview   Before: "How would you sum the main diagonal of a square matrix?" After: "I would iterate through the indices from 0 to n-1 and sum elements at [i][i], resulting in O(n) time complexity for an n x n matrix, or O(1) for this specific 3x3 case."
# Pitfalls    (1) The code assumes a fixed 3x3 input size, which will fail if the input matrix dimensions differ from the expected constraints.  (2) The input reading logic assumes each row is provided on a new line, which may cause errors if the input format deviates from the expected structure.
# ──────────────────────────────────────────────────

a = [] 
for i in range(3):
    a.append([int(i) for i in input().split()])
s = 0
for i in range(3):
    s += a[i][i]
print(s)
