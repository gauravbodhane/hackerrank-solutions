# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp235/problem?isFullScreen=true
# Problem     LBP235
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-24, 02:16 p.m.
# Technique   nested-loop-zero-check
# Time        O(1)
# Space       O(1)
# Insight     The algorithm verifies an upper triangular matrix by ensuring all elements below the main diagonal, where the row index exceeds the column index, are equal to zero.
# Interview   Before: "How do you validate an upper triangular matrix?" After: "I iterate through the 3x3 matrix and check if any element at row i and column j is non-zero when i > j. This O(1) approach confirms the property by verifying the lower triangle contains only zeros."
# Pitfalls    (1) Confusing the condition j < i with i < j, which would incorrectly check for a lower triangular matrix instead of an upper triangular one.  (2) Assuming the input matrix size is dynamic when the problem statement and code explicitly constrain it to a 3x3 matrix.
# ──────────────────────────────────────────────────

l1 = [int (i) for i in input().split()]
l2 = [int (i) for i in input().split()]
l3 = [int (i) for i in input().split()]
l = [l1,l2,l3]
flag = True
for i in range(3):
    for j in range(3):
        if j<i and l[i][j]!= 0:
            flag=False
print('Yes' if  flag else 'No')
