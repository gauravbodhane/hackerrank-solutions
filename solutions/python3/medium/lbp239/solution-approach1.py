# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp239/problem?isFullScreen=true
# Problem     LBP239
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-24, 07:31 p.m.
# Technique   nested-loop-diagonal-filter
# Time        O(1)
# Space       O(1)
# Insight     The implementation iterates through a fixed 3x3 matrix and prints the element at index [i][j] only when the row index equals the column index, otherwise printing two spaces.
# Interview   Before: "I would iterate through the matrix and print every element." After: "I filter for diagonal elements where row equals column, resulting in O(1) time complexity for this fixed 3x3 input size."
# Pitfalls    (1) The code prints two spaces for non-diagonal elements instead of skipping them, which may violate strict output formatting requirements.  (2) The implementation is hardcoded for a 3x3 matrix and will fail if the input dimensions differ from the problem constraints.
# ──────────────────────────────────────────────────


l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]
l3 = [int(i) for i in input().split()]
l = [l1,l2,l3]
for i in range(3):
    for j in range(3):
        if i==j :
            print(l[i][j],end=' ')
        else :
            print('  ',end='')
    print()
