# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp215/problem?isFullScreen=true
# Problem     LBP215
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 07:59 p.m.
# Technique   nested-loop-row-max
# Time        O(N*M)
# Space       O(N*M)
# Insight     The algorithm iterates through each row of the 3x3 matrix and maintains a running maximum value to identify the largest element in that specific row.
# Interview   Before: "How would you find the maximum in each row of a matrix?" After: "I iterate through each row and track the maximum element, resulting in O(N*M) time complexity for an N by M matrix, which is optimal for visiting every element once."
# Pitfalls    (1) The code assumes a fixed 3x3 input size, which will fail if the input matrix dimensions differ from the hardcoded range.  (2) Using 'max' as a variable name shadows the built-in Python max() function, which is poor practice.
# ──────────────────────────────────────────────────

a = []

for i in range(3):
    a.append([int(x) for x in input().split()])

for i in range(3):
    max = a[i][0]
    for j in range(3):
        if max < a[i][j]:
            max = a[i][j]
    print(max)
