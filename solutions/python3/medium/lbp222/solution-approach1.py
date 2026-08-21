# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp222/problem?isFullScreen=true
# Problem     LBP222
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 09:15 p.m.
# Technique   nested-loop-matrix-addition
# Time        O(1)
# Space       O(1)
# Insight     The program performs element-wise addition of two fixed 3x3 matrices by iterating through row and column indices.
# Interview   Before: "How would you add two matrices?" After: "I would iterate through each row and column index to sum corresponding elements, resulting in O(1) time and space complexity since the matrix size is fixed at 3x3."
# Pitfalls    (1) The code assumes exactly three lines of input for each matrix, which may fail if the input format deviates from the 3x3 specification.  (2) Using print with end=' ' results in a trailing space at the end of each row, which might be rejected by strict output checkers.
# ──────────────────────────────────────────────────


a = []
b = []
c= []
for i in range(3):
    a.append([int(x) for x in input().split()])
for i in range(3):
    b.append([int(x) for x in input().split()])
for i in range(3):
    cc=[]
    for j in range(3):
        cc.append(a[i][j]+b[i][j])
    c.append(cc)
for i in range(3):
    for j in range(3):
        print(c[i][j],end=' ')
    print()
