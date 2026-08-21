# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp216/problem?isFullScreen=true
# Problem     LBP216
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 08:03 p.m.
# Technique   nested-loop-row-minimum
# Time        O(N*M)
# Space       O(N*M)
# Insight     The algorithm iterates through each row of the 3x3 matrix and maintains a running minimum value to identify the smallest element in that specific row.
# Interview   Before: "How would you find the minimum in each row?" After: "I iterate through each row and track the minimum element, resulting in O(N*M) time complexity for an N by M matrix, which is efficient for this 3x3 input."
# Pitfalls    (1) Assuming the input matrix is always 3x3 when the logic could be generalized to N by M.  (2) Failing to handle potential empty input lines if the matrix dimensions are not strictly 3x3 as specified.
# ──────────────────────────────────────────────────

a = []

for i in range(3):
    a.append([int(x) for x in input().split()])
for i in range(3):
    min = a[i][0]
    for j in range(3):
        if min > a[i][j]:
            min = a[i][j]

    print(min) 
