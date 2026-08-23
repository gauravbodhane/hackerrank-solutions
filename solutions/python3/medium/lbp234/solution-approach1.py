# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp234/problem?isFullScreen=true
# Problem     LBP234
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-23, 02:11 p.m.
# Technique   in-place-diagonal-swap
# Time        O(1)
# Space       O(1)
# Insight     The algorithm performs an in-place swap of the primary and secondary diagonal elements for each row in a 3x3 matrix.
# Interview   Before: "How would you swap the diagonals of a 3x3 matrix?" After: "I iterate through each row and swap the elements at index i and 2-i, resulting in O(1) time and space complexity for this fixed-size input."
# Pitfalls    (1) Swapping the center element (1,1) with itself when i=1, which is redundant but harmless.  (2) Incorrectly calculating the secondary diagonal index as 3-i instead of 3-i-1, leading to an IndexError.
# ──────────────────────────────────────────────────

l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]
l3 = [int(i) for i in input().split()]

l = [l1,l2,l3]
for i in range(3):
    l[i][i] , l[i][3-i-1] = l[i][3-i-1], l[i][i]
for i in range(3):
    for j in range(3):
        print(l[i][j],end=' ')
    print()
