# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp201/problem?isFullScreen=true
# Problem     LBP201
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-20, 08:11 a.m.
# Technique   nested-loop-matrix-traversal
# Time        O(n * m)
# Space       O(n * m)
# Insight     The program reads n rows of m integers into a nested list structure and iterates through the indices to print each element followed by a space.
# Interview   Before: "How would you print a 2D array?" After: "I would use nested loops to traverse the n by m matrix, resulting in O(n * m) time complexity, ensuring each element is printed in row-major order as required by the constraints."
# Pitfalls    (1) The code uses a list comprehension with the variable i inside the loop, which shadows the outer loop variable i.  (2) The print statement adds a trailing space after every element, which might be sensitive depending on strict output formatting requirements.  (3) The input reading assumes each row is provided on a new line, which may fail if the input format deviates from the expected structure.
# ──────────────────────────────────────────────────

n = int(input())
m = int(input())
a=[]
for i in range(n):
    a.append([int(i) for i in input().split()])
for i in range(n):
    for j in range(m):
        print(a[i][j],end=' ')
    print()
