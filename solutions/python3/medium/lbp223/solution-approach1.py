# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp223/problem?isFullScreen=true
# Problem     LBP223
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 09:23 p.m.
# Technique   nested-loop-matrix-subtraction
# Time        O(1)
# Space       O(1)
# Insight     The program performs element-wise subtraction of two fixed 3x3 matrices by iterating through row and column indices.
# Interview   Before: "How would you subtract two matrices?" After: "I would iterate through each row and column to compute the difference of corresponding elements, resulting in O(1) time complexity since the matrix size is fixed at 3x3."
# Pitfalls    (1) The code assumes the input always provides exactly three rows and three columns as specified in the problem constraints.  (2) The use of print with end=' ' results in a trailing space at the end of each row, which may be sensitive in strict output formatting.
# ──────────────────────────────────────────────────

a = []
b = []
c = []
for i in range(3):
    a.append([int(i) for i in input().split()])
for i in range(3):
    b.append([int(i) for i in input().split()])
for i in range(3):
    cc=[]
    for j in range(3):
        cc.append(a[i][j]-b[i][j])
    c.append(cc)
for i in range(3):
    for j in range(3):
        print(c[i][j],end=' ')
    print()
