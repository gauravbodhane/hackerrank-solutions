# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp203/problem?isFullScreen=true
# Problem     LBP203
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-20, 08:32 a.m.
# Technique   nested-loop-matrix-traversal
# Time        O(1)
# Space       O(1)
# Insight     The algorithm iterates through every element of the fixed 3x3 matrix and accumulates the value into a running sum if the element is divisible by two.
# Interview   Before: "How would you sum specific elements in a 2D array?" After: "I iterate through the 3x3 matrix using nested loops, checking each element with the modulo operator. This approach runs in O(1) time since the matrix size is constant, effectively handling all even integers including zero."
# Pitfalls    (1) Assuming the input matrix size is dynamic when the problem explicitly defines a 3x3 matrix.  (2) Failing to account for zero as an even number, which is correctly handled by the modulo operator in this implementation.
# ──────────────────────────────────────────────────


a=[]
for i in range(3):
    a.append([int (i) for i in input().split()])
s = 0
for i in range(3):
    for j in range(3):
        if a[i][j]%2==0:
            s = s+a[i][j]
print(s)
