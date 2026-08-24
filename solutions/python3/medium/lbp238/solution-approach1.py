# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp238/problem?isFullScreen=true
# Problem     LBP238
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-24, 07:26 p.m.
# Technique   nested-loop-matrix-comparison
# Time        O(1)
# Space       O(1)
# Insight     The algorithm verifies symmetry by counting the number of elements that satisfy the condition A[i][j] == A[j][i] and checking if the total count equals the square of the matrix dimension.
# Interview   Before: "How would you check if a 3x3 matrix is symmetric?" After: "I compare each element at (i, j) with its transpose counterpart at (j, i). Since the matrix is fixed at 3x3, this runs in O(1) time and space, ensuring all nine positions match."
# Pitfalls    (1) The code assumes the input is always a 3x3 matrix, which may fail if the input dimensions vary.  (2) The logic relies on a counter reaching exactly nine, which is only valid for a 3x3 matrix as specified in the problem constraints.
# ──────────────────────────────────────────────────

l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]
l3 = [int(i) for i in input().split()]
l = [l1,l2,l3]
c = 0
for i in range(3):
    for j in range(3):
        if l[i][j] == l[j][i]:
            c = c+1
print('Yes' if c==9 else 'No')
