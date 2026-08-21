# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp213/problem?isFullScreen=true
# Problem     LBP213
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 07:40 p.m.
# Technique   nested-loop-max-tracking
# Time        O(1)
# Space       O(1)
# Insight     The algorithm iterates through every element of the fixed 3x3 matrix to maintain a running maximum value.
# Interview   Before: "How would you find the largest value in a 3x3 grid?" After: "I would use nested loops to traverse the matrix, updating a tracker variable whenever a larger element is found, resulting in O(1) time and space complexity for this fixed-size input."
# Pitfalls    (1) Initializing the max variable to 0 fails if all matrix elements are negative integers.  (2) Hardcoding the range to 3 assumes the input strictly adheres to the 3x3 matrix constraint.
# ──────────────────────────────────────────────────

a = []

for i in range(3):
    a.append([int(x) for x in input().split()])

max = 0
for i in range(3):
    for j in range(3):
        if max<a[i][j]:
            max = a[i][j]
print(max)
