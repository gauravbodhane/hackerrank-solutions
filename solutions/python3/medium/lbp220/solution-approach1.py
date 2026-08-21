# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp220/problem?isFullScreen=true
# Problem     LBP220
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 08:43 p.m.
# Technique   nested-loop-matrix-validation
# Time        O(1)
# Space       O(1)
# Insight     The algorithm verifies that all diagonal elements are one and all off-diagonal elements are zero within a fixed 3x3 matrix structure.
# Interview   Before: "How would you validate a square matrix?" After: "I iterate through each cell, checking if the diagonal indices match one and off-diagonal indices match zero. This approach runs in O(1) time for a fixed 3x3 matrix, ensuring all identity matrix properties are satisfied."
# Pitfalls    (1) Failing to account for the fixed 3x3 input size constraint when generalizing the logic.  (2) Incorrectly assuming the input format provides a single line instead of three separate lines for the matrix rows.
# ──────────────────────────────────────────────────

flag = True
a = []
for i in range(3):
    a.append([int(x) for x in input().split()])
for i in range(3):
    for j in range(3):
        if i==j and a[i][j]!=1:
            flag = False
            break
        if i!=j and a[i][j]!= 0:
            flag=False
            break
print('Yes' if flag else 'No')
            
