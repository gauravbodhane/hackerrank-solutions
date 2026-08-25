# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp242/problem?isFullScreen=true
# Problem     LBP242
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-25, 11:33 a.m.
# Technique   nested-loop-row-index-parity
# Time        O(1)
# Space       O(1)
# Insight     The algorithm iterates through a fixed 3x3 matrix and accumulates the sum of elements only when the row index is odd.
# Interview   Before: "How would you sum specific rows in a matrix?" After: "I iterate through the rows and check if the index is odd using the modulo operator. This approach runs in O(1) time for a fixed 3x3 matrix, correctly targeting only the second row."
# Pitfalls    (1) Assuming the matrix size is dynamic when the problem constraints and code explicitly fix it to 3x3.  (2) Confusing 0-based indexing with 1-based indexing, which would lead to summing the wrong rows.
# ──────────────────────────────────────────────────

l1 = [int (i) for i in input().split()]
l2 = [int (i) for i in input().split()]
l3 = [int (i) for i in input().split()]
l = [l1,l2,l3]
s = 0
for i in range(3):
    for j in range(3):
        if i%2!=0:
            s = s +l[i][j]
print(s)
