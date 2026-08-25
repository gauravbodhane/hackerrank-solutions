# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp241/problem?isFullScreen=true
# Problem     LBP241
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-25, 12:14 p.m.
# Technique   nested-loop-row-index-parity
# Time        O(1)
# Space       O(1)
# Insight     The algorithm iterates through a fixed 3x3 matrix and accumulates values only from rows where the index is even.
# Interview   Before: "How would you sum specific rows in a matrix?" After: "I iterate through the matrix and use the modulo operator on the row index to identify even rows, resulting in O(1) time complexity for a fixed 3x3 input."
# Pitfalls    (1) The code assumes a fixed 3x3 input size, which fails if the input matrix dimensions differ from the problem constraints.  (2) The logic relies on hardcoded input reading, which will raise an EOFError if fewer than three lines are provided.
# ──────────────────────────────────────────────────

l1 = [int (i) for i in input().split()]
l2 = [int (i) for i in input().split()]
l3 = [int (i) for i in input().split()]
l = [l1,l2,l3]
s = 0
for i in range(3):
    for j in range(3):
        if i%2==0:
            s = s +l[i][j]
print(s)
