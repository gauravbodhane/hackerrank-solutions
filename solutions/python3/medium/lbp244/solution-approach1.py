# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp244/problem?isFullScreen=true
# Problem     LBP244
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-25, 11:35 a.m.
# Technique   nested-loop-modulo-indexing
# Time        O(1)
# Space       O(1)
# Insight     The algorithm iterates through a fixed 3x3 matrix and accumulates values located at odd column indices using the modulo operator.
# Interview   Before: "How would you sum specific columns in a matrix?" After: "I iterate through each row and column, checking if the column index is odd using j % 2 != 0. This approach runs in O(1) time for a fixed 3x3 matrix, effectively targeting indices 1, 3, and 5 if the matrix were larger."
# Pitfalls    (1) The code assumes a fixed 3x3 input size, which will fail if the input matrix dimensions differ from the expected constraints.  (2) The modulo operator j % 2 != 0 correctly identifies odd indices 1, 3, 5, but the hardcoded range(3) limits the summation to only index 1.
# ──────────────────────────────────────────────────

l1 = [int (i) for i in input().split()]
l2 = [int (i) for i in input().split()]
l3 = [int (i) for i in input().split()]
l = [l1,l2,l3]
s = 0
for i in range(3):
    for j in range(3):
        if j%2!=0:
            s = s +l[i][j]
print(s)
