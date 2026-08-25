# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp243/problem?isFullScreen=true
# Problem     LBP243
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-25, 11:34 a.m.
# Technique   nested-loop-modulo-indexing
# Time        O(1)
# Space       O(1)
# Insight     The algorithm iterates through every element of the 3x3 matrix and accumulates values where the column index is even.
# Interview   Before: "How would you sum specific columns in a fixed-size matrix?" After: "I iterate through the 3x3 grid using nested loops and apply a modulo operator to identify even-indexed columns, resulting in O(1) time and space complexity."
# Pitfalls    (1) Assuming the input matrix size is dynamic when the problem explicitly defines a 3x3 matrix.  (2) Confusing row-major indexing with column-major indexing when calculating the sum of even-indexed columns.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
l1 = [int (i) for i in input().split()]
l2 = [int (i) for i in input().split()]
l3 = [int (i) for i in input().split()]
l = [l1,l2,l3]
s = 0
for i in range(3):
    for j in range(3):
        if j%2==0:
            s = s +l[i][j]
print(s)
