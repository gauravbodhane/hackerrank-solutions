# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp240/problem?isFullScreen=true
# Problem     LBP240
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-25, 11:19 a.m.
# Technique   nested-loop-matrix-traversal
# Time        O(1)
# Space       O(1)
# Insight     The program iterates through a fixed 3x3 matrix structure and prints the square of each element using nested loops.
# Interview   Before: "How would you square every element in a 3x3 matrix?" After: "I would use nested loops to traverse the 3x3 grid, squaring each element in O(1) time since the matrix size is constant."
# Pitfalls    (1) The code assumes exactly three lines of input, which will fail if the input format deviates from the specified 3x3 matrix.  (2) The use of print with end=' ' may result in trailing spaces at the end of each row, which might be rejected by strict output checkers.
# ──────────────────────────────────────────────────

l1 = [int (i) for i in input().split()]
l2 = [int (i) for i in input().split()]
l3 = [int (i) for i in input().split()]
l =[l1,l2,l3]
for i in range(3):
    for j in range(3):
        print(l[i][j]* l[i][j],end=' ')
    print()
