# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp227/problem?isFullScreen=true
# Problem     LBP227
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-22, 09:08 a.m.
# Technique   row-wise-sorting
# Time        O(R * C log C)
# Space       O(R * C)
# Insight     The program organizes a fixed 3x3 matrix by sorting each row independently in ascending order using the built-in sort method.
# Interview   Before: "How would you sort elements within each row of a matrix?" After: "I would iterate through each row and apply a sorting algorithm, resulting in O(R * C log C) time complexity, where R is the number of rows and C is the number of columns."
# Pitfalls    (1) The code assumes a fixed 3x3 input size, which will fail if the input matrix dimensions differ from the hardcoded range.  (2) The use of print with end=' ' followed by print() may introduce trailing spaces that could cause formatting errors in strict online judges.
# ──────────────────────────────────────────────────

l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]
l3 = [int(i) for i in input().split()]
l = [l1,l2,l3]
for i in range(3):
    l[i].sort()
    
for i in range(3):
    for j in range(3):
        print(l[i][j],end=' ')
    print()
