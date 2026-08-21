# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp219/problem?isFullScreen=true
# Problem     LBP219
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 08:35 p.m.
# Technique   nested-loop-matrix-traversal
# Time        O(1)
# Space       O(1)
# Insight     The algorithm iterates through every element of the 3x3 matrix, incrementing the odd counter for non-zero remainders and the even counter for non-zero values divisible by two.
# Interview   Before: "How do you count parity in a fixed-size matrix while ignoring zeros?" After: "I iterate through the 3x3 grid using nested loops, applying conditional checks for parity and zero-exclusion, resulting in O(1) time and space complexity."
# Pitfalls    (1) Failing to exclude zero from the even count, as the problem explicitly requires ignoring zero values.  (2) Assuming the input matrix size is variable when the problem constraints specify a fixed 3x3 matrix.
# ──────────────────────────────────────────────────

a = []

for i in range(3):
    a.append([int(x) for x in input().split()])
even = 0
odd = 0
for i in range(3):
    for j in range(3):
        if a[i][j]%2 == 0 and a[i][j]!= 0:
            even = even+ 1 
        if a[i][j]%2!= 0:
            odd = odd+ 1

print(odd)
print(even)
