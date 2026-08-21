# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp210/problem?isFullScreen=true
# Problem     LBP210
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 09:04 a.m.
# Technique   fixed-index-matrix-access
# Time        O(1)
# Space       O(1)
# Insight     The program extracts the first element at index [0][0] and the last element at index [2][2] from a fixed 3x3 matrix to compute their sum.
# Interview   Before: "How would you sum the corners of a 3x3 matrix?" After: "I would access the top-left and bottom-right indices directly, which is an O(1) operation, assuming the input is guaranteed to be a 3x3 matrix as specified."
# Pitfalls    (1) The code assumes a fixed 3x3 matrix size and will raise an IndexError if the input contains fewer than three rows or columns.  (2) The implementation does not validate input format, potentially causing a ValueError if non-integer values are provided.
# ──────────────────────────────────────────────────

a = []
for i in range(3):
    a.append([int(i) for i in input().split()])
s = a[0][0] + a[2][2]
print(s)
