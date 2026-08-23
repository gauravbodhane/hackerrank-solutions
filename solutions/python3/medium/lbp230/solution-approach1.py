# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp230/problem?isFullScreen=true
# Problem     LBP230
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-23, 01:23 p.m.
# Technique   matrix-transpose-column-sort
# Time        O(1)
# Space       O(1)
# Insight     The program transposes the input matrix to isolate columns as rows, sorts each row in descending order, and then transposes the result back to restore the original column-wise structure.
# Interview   Before: "How would you sort columns independently in descending order?" After: "I transpose the matrix to treat columns as rows, sort them using O(N log N) per column, and transpose back. Since the matrix size is fixed at 3x3, the complexity is O(1)."
# Pitfalls    (1) The implementation assumes a fixed 3x3 input size, which will fail if the input matrix dimensions differ from the hardcoded range(3) loops.  (2) The nested print loops assume a square matrix, potentially causing index errors if the input is not exactly 3x3.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]
l3 = [int(i) for i in input().split()]
l = [l1,l2,l3]
ll =[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        ll[i][j] = l[j][i]
for i in range(3):
    ll[i].sort(reverse=True)
    
for i in range(3):
    for j in range(3):
        print(ll[j][i],end=' ')
    print()
