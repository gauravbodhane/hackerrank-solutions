# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp228/problem?isFullScreen=true
# Problem     LBP228
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-22, 09:07 a.m.
# Technique   row-wise-sorting-in-place
# Time        O(N log N) where N is the number of col…
# Space       O(N) to store the matrix rows
# Insight     The program independently sorts each of the three predefined rows in descending order using the built-in sort method before printing the resulting matrix.
# Interview   Before: "How would you sort a 3x3 matrix row-wise in descending order?" After: "I would sort each row individually using a descending sort function, resulting in O(N log N) time complexity per row, where N is the number of elements in each row."
# Pitfalls    (1) The code assumes a fixed 3x3 matrix structure, which will fail if the input contains a different number of rows or columns.  (2) Using print with end=' ' results in a trailing space at the end of each row, which may violate strict output formatting requirements.
# ──────────────────────────────────────────────────

l1 = [int (i) for i in input().split()]
l2 = [int (i) for i in input().split()]
l3 = [int (i) for i in input().split()]
l1.sort(reverse=True)
l2.sort(reverse=True)
l3.sort(reverse=True)
l = [l1,l2,l3]
for i in range(3):
    for j in range(3):
        print(l[i][j],end=' ')
    print()
