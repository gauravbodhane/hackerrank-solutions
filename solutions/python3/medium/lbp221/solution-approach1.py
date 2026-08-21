# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp221/problem?isFullScreen=true
# Problem     LBP221
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 09:06 p.m.
# Technique   nested-loop-matrix-comparison
# Time        O(1)
# Space       O(1)
# Insight     The program performs a cell-by-cell comparison of two 3x3 matrices and terminates early if any corresponding elements differ.
# Interview   Before: "How would you compare two fixed-size matrices for equality?" After: "I would iterate through each row and column index, comparing elements at each position. This approach runs in O(1) time since the matrix size is constant, ensuring all 9 elements are checked efficiently."
# Pitfalls    (1) The code assumes exactly three lines of input for each matrix, which may fail if the input format deviates from the specified 3x3 structure.  (2) The use of input().split() assumes space-separated integers, which will raise a ValueError if the input contains non-integer characters or unexpected delimiters.
# ──────────────────────────────────────────────────

flag = True
a = []
b = []
for i in range(3):
    a.append([int(x) for x in input().split()])
for i in range(3):
    b.append([int(x) for x in input().split()])
for i in range(3):
    for j in range(3):
        if a[i][j]!=b[i][j]:
            flag = False
            break
print('Yes' if flag else 'No')
            
