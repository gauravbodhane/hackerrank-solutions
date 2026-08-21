# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp214/problem?isFullScreen=true
# Problem     LBP214
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 07:47 p.m.
# Technique   nested-loop-min-scan
# Time        O(1)
# Space       O(1)
# Insight     The algorithm iterates through every element of the fixed 3x3 matrix to maintain a running minimum value.
# Interview   Before: "How would you find the minimum in a 3x3 matrix?" After: "I would use a nested loop to traverse all nine elements, updating a tracker variable. This approach runs in O(1) time since the matrix size is constant."
# Pitfalls    (1) Assuming the input matrix size is dynamic when the problem explicitly defines a 3x3 structure.  (2) Failing to handle potential input parsing errors if the matrix rows contain fewer than three integers.
# ──────────────────────────────────────────────────


a = []

for i in range(3):
    a.append([int(x) for x in input().split()])

min = a[0][0]
for i in range(3):
    for j in range(3):
        if min > a[i][j]:
            min = a[i][j]
print(min)
