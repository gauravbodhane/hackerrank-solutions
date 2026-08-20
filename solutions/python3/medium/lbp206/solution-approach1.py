# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp206/problem?isFullScreen=true
# Problem     LBP206
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-20, 08:50 a.m.
# Technique   nested-loop-summation
# Time        O(N*M)
# Space       O(N*M)
# Insight     The program iterates through each row of the 3x3 matrix, accumulating the sum of elements in that row before printing the result.
# Interview   Before: "How would you calculate the sum of each row in a fixed 3x3 matrix?" After: "I would use nested loops to traverse the matrix row by row, maintaining a running sum for each row, resulting in O(N*M) time complexity where N and M are dimensions."
# Pitfalls    (1) The code assumes exactly three rows and three columns as per the problem statement, which will fail if the input dimensions vary.  (2) Using the same variable name 'i' for both the outer loop and the list comprehension inside the input loop may cause confusion, though it functions correctly in Python.
# ──────────────────────────────────────────────────


a = []
for i in range(3):
    a.append([int(i) for i in input().split()])
for i in range(3):
    s= 0
    for j in range(3):
        s = s+a[i][j]
    print(s)
