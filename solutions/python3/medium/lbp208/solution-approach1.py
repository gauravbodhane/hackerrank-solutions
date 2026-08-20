# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp208/problem?isFullScreen=true
# Problem     LBP208
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-20, 09:00 a.m.
# Technique   nested-loop-diagonal-sum
# Time        O(N^2)
# Space       O(N^2)
# Insight     The algorithm iterates through a 3x3 matrix and accumulates values where the row index equals the column index.
# Interview   Before: "I could iterate through every element and check if i equals j." After: "Since the matrix is fixed at 3x3, this O(N^2) approach is efficient, though one could optimize to O(N) by accessing a[i][i] directly in a single loop."
# Pitfalls    (1) Assuming the input matrix is always 3x3 as per the problem statement, which may fail if the input size varies.  (2) Using nested loops to check i == j instead of directly accessing diagonal elements, which is less efficient.
# ──────────────────────────────────────────────────


a = []
for i in range(3):
    a.append([int(i) for i in input().split()])
s =0
for i in range(3):
    for j in range(3):
        if i==j:
            s = s+a[i][j]
print(s)
