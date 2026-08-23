# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp233/problem?isFullScreen=true
# Problem     LBP233
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-23, 01:48 p.m.
# Technique   in-place-column-swap
# Time        O(1)
# Space       O(1)
# Insight     The program performs an in-place swap of two specified columns across all three rows of a fixed 3x3 matrix using Python's tuple unpacking assignment.
# Interview   Before: "How would you swap two columns in a fixed 3x3 matrix?" After: "I would iterate through each row and swap the elements at indices m-1 and n-1. This approach is O(1) time and space, as the matrix size is constant."
# Pitfalls    (1) The code assumes 1-based indexing for input columns m and n, which requires subtracting one to access the correct 0-based list indices.  (2) The implementation is hardcoded for a 3x3 matrix and will fail if the input dimensions differ from the expected structure.
# ──────────────────────────────────────────────────


l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]
l3 = [int(i) for i in input().split()]
m = int(input())
n = int(input())
l = [l1,l2,l3]
for i in range(3):
    l[i][m-1],l[i][n-1] = l[i][n-1],l[i][m-1]
        
for i in range(3):
    for j in range(3):
        print(l[i][j],end=' ')
    print()
