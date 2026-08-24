# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp236/problem?isFullScreen=true
# Problem     LBP236
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-24, 07:11 p.m.
# Technique   nested-loop-upper-triangle-check
# Time        O(1)
# Space       O(1)
# Insight     The algorithm verifies that all elements above the main diagonal, where the column index exceeds the row index, are equal to zero.
# Interview   Before: "How do you validate a lower triangular matrix?" After: "I iterate through the 3x3 matrix and ensure every element where j > i is zero, resulting in O(1) time and space complexity for this fixed-size input."
# Pitfalls    (1) Confusing the condition j > i with j < i, which would incorrectly check for an upper triangular matrix instead.  (2) Assuming the input matrix size is dynamic when the problem constraints and implementation specifically target a 3x3 matrix.
# ──────────────────────────────────────────────────

l1 = [int (i) for i in input().split()]
l2 = [int (i) for i in input().split()]
l3 = [int (i) for i in input().split()]
l = [l1,l2,l3]
flag = True
for i in range(3):
    for j in range(3):
        if j>i and l[i][j] != 0:
            flag= False
print('Yes' if flag else 'No')
