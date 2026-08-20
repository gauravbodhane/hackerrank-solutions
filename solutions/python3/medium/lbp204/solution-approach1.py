# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp204/problem?isFullScreen=true
# Problem     LBP204
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-20, 08:39 a.m.
# Technique   nested-loop-matrix-traversal
# Time        O(1)
# Space       O(1)
# Insight     The algorithm iterates through every cell of the fixed 3x3 matrix and accumulates the value into a running sum if the element is odd.
# Interview   Before: "How would you sum specific elements in a 2D array?" After: "I iterate through the 3x3 matrix using nested loops, checking each element with the modulo operator. This approach runs in O(1) time and O(1) space, as the matrix size is constant."
# Pitfalls    (1) Assuming the input matrix size is dynamic when the problem constraints strictly define a 3x3 matrix.  (2) Failing to handle non-integer inputs if the input format deviates from the specified integer matrix structure.
# ──────────────────────────────────────────────────

a = []
for i in range(3):
    a.append([int(i) for i in input().split()])
s= 0
for i in range(3):
    for j in range(3):
        if a[i][j]%2 != 0:
            s=s+a[i][j] 
print(s)
