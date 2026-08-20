# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp207/problem?isFullScreen=true
# Problem     LBP207
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-20, 08:57 a.m.
# Technique   nested-loop-column-sum
# Time        O(N^2)
# Space       O(N^2)
# Insight     The algorithm iterates through columns by fixing the column index in the outer loop and traversing rows in the inner loop to accumulate the sum.
# Interview   Before: "How would you calculate the sum of each column in a 3x3 matrix?" After: "I iterate through each column index first, then sum the elements across rows, resulting in O(N^2) time complexity for an N by N matrix."
# Pitfalls    (1) Swapping the inner and outer loop indices results in row-wise sums instead of column-wise sums.  (2) Hardcoding the range to 3 assumes the input is strictly a 3x3 matrix as per the problem statement.
# ──────────────────────────────────────────────────


a = []
for i in range(3):
    a.append([int(i) for i in input().split()])
for i in range(3):
    s= 0
    for j in range(3):
        s = s+a[j][i]
    print(s)
