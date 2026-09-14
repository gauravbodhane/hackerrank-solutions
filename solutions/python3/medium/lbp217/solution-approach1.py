# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp217/problem?isFullScreen=true
# Problem     LBP217
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-14, 11:29 p.m.
# Technique   nested-loop-matrix-transpose
# Time        O(N^2)
# Space       O(N^2)
# Insight     The program reads a 3x3 matrix into a list of lists and iterates through columns then rows to print the transposed elements.
# Interview   Before: "How would you transpose a fixed-size matrix?" After: "I would use nested loops to swap indices, accessing a[j][i] instead of a[i][j]. This approach runs in O(N^2) time and O(N^2) space, where N is the dimension of the matrix."
# Pitfalls    (1) The code assumes exactly three lines of input, which will fail if the input contains fewer than three rows.  (2) The nested loops are hardcoded for a 3x3 matrix and will not work for matrices of different dimensions.  (3) The use of print(..., end=' ') followed by print() may result in trailing spaces at the end of each row.
# ──────────────────────────────────────────────────

a = []

for i in range(3):
    a.append([int(x) for x in input().split()])
    
for i in range(3):
    for j in range(3):
        print(a[j][i],end=' ')
    print()
