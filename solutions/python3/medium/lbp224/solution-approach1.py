# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp224/problem?isFullScreen=true
# Problem     LBP224 
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-22, 08:30 a.m.
# Technique   triple-nested-loop-matrix-multiplication
# Time        O(1)
# Space       O(1)
# Insight     The algorithm computes the product of two 3x3 matrices by iterating through each row of the first matrix and each column of the second matrix to calculate the dot product for each cell.
# Interview   Before: "How would you multiply two matrices?" After: "I would use three nested loops to compute the dot product of rows and columns, resulting in O(1) time complexity since the input size is fixed at 3x3."
# Pitfalls    (1) The code assumes exactly 3x3 input matrices as per the problem constraints and will fail if the input dimensions differ.  (2) The use of a fixed 3x3 result matrix prevents the program from handling dynamic matrix sizes.
# ──────────────────────────────────────────────────


a = []
b = []
c = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    a.append([int (i) for i in input().split()])
for i in range(3):
    b.append([int (i) for i in input().split()])
    
    
for i in range(3):
    for j in range(3):
        for k in range(3):
            c[i][j]= c[i][j]+(a[i][k]*b[k][j])
   
for i  in range(3):
    for j in range(3):
        print(c[i][j],end=' ')
    print()
