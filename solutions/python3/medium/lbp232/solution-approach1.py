# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp232/problem?isFullScreen=true
# Problem     LBP232
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-23, 01:43 p.m.
# Technique   list-index-swapping
# Time        O(1)
# Space       O(1)
# Insight     The program performs an in-place swap of two rows within a fixed 3x3 matrix using Python's tuple unpacking assignment.
# Interview   Before: "How would you swap two rows in a 3x3 matrix?" After: "I would use Python's tuple unpacking to swap the references in O(1) time, ensuring the indices m-1 and n-1 are correctly mapped to the 0-indexed list structure."
# Pitfalls    (1) The code assumes 1-based indexing for m and n, which will cause an IndexError if the input values are outside the range [1, 3].  (2) The implementation is hardcoded for a 3x3 matrix and will fail if the input matrix dimensions differ from the expected size.
# ──────────────────────────────────────────────────


l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]
l3 = [int(i) for i in input().split()]
m = int(input())
n = int(input())
l = [l1,l2,l3]
l[m-1],l[n-1] = l[n-1],l[m-1]
for i in range(3):
    for j in range(3):
        print(l[i][j],end=' ')
    print()
