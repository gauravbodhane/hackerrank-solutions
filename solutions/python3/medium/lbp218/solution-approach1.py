# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp218/problem?isFullScreen=true
# Problem     LBP218
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 08:21 p.m.
# Technique   nested-loop-diagonal-sum
# Time        O(N^2)
# Space       O(N^2)
# Insight     The algorithm iterates through a 3x3 matrix and accumulates the values where the row index equals the column index.
# Interview   Before: "How would you calculate the trace of a square matrix?" After: "I iterate through the matrix and sum elements where row equals column, resulting in O(N^2) time complexity for an N by N matrix."
# Pitfalls    (1) The code assumes a fixed 3x3 input size as per the problem statement, which will fail if the input dimensions vary.  (2) Using nested loops to check i == j is less efficient than a single loop iterating through range(3) to access a[i][i].
# ──────────────────────────────────────────────────

a = []

for i in range(3):
    a.append([int(x) for x in input().split()])
s = 0
for i in range(3):
    for j in range(3):
        if i == j:
            s += a[j][i]
print(s)
    
    
