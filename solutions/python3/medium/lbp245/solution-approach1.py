# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp245/problem?isFullScreen=true
# Problem     LBP245	
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-25, 11:39 a.m.
# Technique   nested-loop-parity-sum
# Time        O(1)
# Space       O(1)
# Insight     The algorithm iterates through a fixed 3x3 matrix and accumulates elements where the sum of the row index and column index is even.
# Interview   Before: "How would you sum elements at even-parity indices in a 3x3 matrix?" After: "I iterate through all indices i and j, checking if (i+j) % 2 == 0. This approach runs in O(1) time and O(1) space, as the matrix size is constant."
# Pitfalls    (1) Misinterpreting the parity condition as checking if only the row or column index is even instead of their sum.  (2) Assuming the input matrix size is dynamic when the problem explicitly defines a 3x3 matrix.
# ──────────────────────────────────────────────────

l1 = [int (i) for i in input().split()]
l2 = [int (i) for i in input().split()]
l3 = [int (i) for i in input().split()]
l = [l1,l2,l3]
s = 0
for i in range(3):
    for j in range(3):
        if (i+j) % 2== 0:
        
            s = s +l[i][j]
print(s)
