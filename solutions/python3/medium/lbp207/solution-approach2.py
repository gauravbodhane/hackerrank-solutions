# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp207/problem?isFullScreen=true
# Problem     LBP207
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 08:59 a.m.
# Technique   nested-loop-column-sum
# Time        O(N^2)
# Space       O(N^2)
# Insight     The algorithm iterates through each column index and accumulates values from every row at that specific column index to compute the total sum.
# Interview   Before: "How would you calculate the sum of each column in a 3x3 matrix?" After: "I iterate through columns first, then rows, resulting in O(N^2) time complexity, where N is the dimension of the matrix."
# Pitfalls    (1) Assuming the input matrix is always 3x3 when the logic could be generalized to N x M.  (2) Incorrectly nesting the loops by iterating over rows in the outer loop instead of columns.
# ──────────────────────────────────────────────────

a = []
for i in range(3):
    a.append([int(i) for i in input().split()])

for  j in range(3):
    s= 0
    for i in range(3):
        s += a[i][j]
    print(s)
