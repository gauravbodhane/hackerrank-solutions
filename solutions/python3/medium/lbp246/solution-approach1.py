# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp246/problem?isFullScreen=true
# Problem     LBP246
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-25, 11:44 a.m.
# Technique   nested-loop-parity-sum
# Time        O(1)
# Space       O(1)
# Insight     The algorithm iterates through a fixed 3x3 matrix and accumulates values where the sum of the current row index and column index is odd.
# Interview   Before: "How would you sum elements at odd-indexed positions in a 3x3 matrix?" After: "I iterate through all indices (i, j) and check if (i + j) % 2 != 0. This approach runs in O(1) time and O(1) space, as the matrix size is constant."
# Pitfalls    (1) Incorrectly assuming the matrix dimensions are dynamic when the problem specifies a 3x3 matrix.  (2) Confusing the parity of the sum of indices with the parity of the element values themselves.
# ──────────────────────────────────────────────────

l1 = [int (i) for i in input().split()]
l2 = [int (i) for i in input().split()]
l3 = [int (i) for i in input().split()]
l = [l1,l2,l3]
s = 0
for i in range(3):
    for j in range(3):
        if (i+j)%2!=0:
            s = s +l[i][j]
print(s)
