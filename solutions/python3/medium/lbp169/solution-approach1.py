# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp169/problem?isFullScreen=true
# Problem     LBP169
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-31, 02:48 p.m.
# Technique   nested-loop-square-matrix-traversal
# Time        O(n)
# Space       O(n)
# Insight     The program calculates the square root of the input size to determine the dimensions of a square matrix and iterates through the array to print elements row by row.
# Interview   Before: "How would you reshape a flat array into a square matrix?" After: "I calculate the square root of the array length to determine the dimensions, then use nested loops to print elements in O(n) time, assuming the input size is a perfect square as per the constraints."
# Pitfalls    (1) The code assumes the input size is always a perfect square, which may cause index out of bounds errors if the input violates the constraint.  (2) The use of print with end=' ' results in a trailing space at the end of each row, which might fail strict output formatting requirements.
# ──────────────────────────────────────────────────

import math 
n= int(input())
m = math.isqrt(n) 
k = 0
l = [int(i) for i in input().split()]
for i in range(m):
    for j in range(m):
        print(l[k],end=' ')
        k = k+1
    print()
