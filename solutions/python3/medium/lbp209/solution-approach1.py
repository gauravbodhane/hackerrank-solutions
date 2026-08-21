# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp209/problem?isFullScreen=true
# Problem     LBP209
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 07:55 a.m.
# Technique   anti-diagonal-summation
# Time        O(1)
# Space       O(1)
# Insight     The algorithm iterates through each row index i and adds the element at column index 2-i to the running sum to calculate the anti-diagonal total.
# Interview   Before: "How would you sum the anti-diagonal of a 3x3 matrix?" After: "I iterate through rows 0 to 2, accessing column 2-i for each row. This O(1) approach efficiently targets the anti-diagonal elements in a fixed-size 3x3 matrix."
# Pitfalls    (1) The code assumes a fixed 3x3 input size and will fail if the input matrix dimensions differ.  (2) The index calculation 3-i-1 assumes zero-based indexing and will cause an IndexError if the matrix is smaller than 3x3.
# ──────────────────────────────────────────────────

a = []
for i in range(3):
    a.append([int(i) for i in input().split()])
s = 0
for i in range(3):
    s+= a[i][3-i-1]
print(s)
