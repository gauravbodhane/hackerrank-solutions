# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp202/problem?isFullScreen=true
# Problem     LBP202
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-20, 08:27 a.m.
# Technique   nested-loop-summation
# Time        O(n * m)
# Space       O(n * m)
# Insight     The algorithm iterates through each row and column of the matrix to accumulate the total sum of all elements into a single variable.
# Interview   Before: "How would you calculate the sum of a 2D array?" After: "I would use nested loops to traverse the n by m matrix, resulting in O(n * m) time complexity, which is optimal for visiting every element once."
# Pitfalls    (1) The input reading logic assumes each row contains exactly m integers, which may fail if the input format is inconsistent.  (2) The variable name i is reused in the list comprehension, which shadows the outer loop variable i in the matrix construction.
# ──────────────────────────────────────────────────

n = int(input())
m = int(input())

a = []
for i in range(n):
    a.append([int(i) for i in input().split()])
    
s = 0
for i in range(n):
    for j in range(m):
        s=s+a[i][j]
print(s)
