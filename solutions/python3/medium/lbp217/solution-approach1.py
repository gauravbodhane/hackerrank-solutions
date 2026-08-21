# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp217/problem?isFullScreen=true
# Problem     LBP217
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 08:21 p.m.
# Technique   nested-loop-matrix-transpose
# Time        O(N^2)
# Space       O(N^2)
# Insight     The program iterates through the columns of the input matrix and prints the elements row by row to effectively swap the row and column indices.
# Interview   Before: "How would you flip a 3x3 matrix across its main diagonal?" After: "I would iterate through columns then rows, printing matrix[j][i] to achieve the transpose in O(N^2) time and O(N^2) space, where N is the dimension of the matrix."
# Pitfalls    (1) Failing to handle the input format correctly by assuming all numbers are on a single line instead of three separate lines.  (2) Incorrectly nesting the loops by using the row index as the outer loop instead of the column index, which prevents the transpose operation.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOU
a = []

for i in range(3):
    a.append([int(x) for x in input().split()])
for i in range(3):
    for j in range(3):
        print(a[j][i],end=' ')
    print()
