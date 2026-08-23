# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp229/problem?isFullScreen=true
# Problem     LBP229
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-23, 01:19 p.m.
# Technique   matrix-transpose-column-sort
# Time        O(1)
# Space       O(1)
# Insight     The program transposes the 3x3 matrix to isolate columns as rows, sorts each row independently, and then transposes the result back to restore the original column-wise structure.
# Interview   Before: "How would you sort columns in a fixed 3x3 matrix?" After: "I transpose the matrix to treat columns as rows, sort them in O(1) time, and transpose back to output the result."
# Pitfalls    (1) The code assumes a fixed 3x3 input size, which will fail if the input dimensions differ from the hardcoded range(3) loops.  (2) The nested loops for printing use ll[j][i] which relies on the specific 3x3 structure to correctly map the sorted values back to their original column positions.
# ──────────────────────────────────────────────────


l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]
l3 = [int(i) for i in input().split()]
l = [l1,l2,l3]
ll =[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        ll[i][j] = l[j][i]
for i in range(3):
    ll[i].sort()
    
for i in range(3):
    for j in range(3):
        print(ll[j][i],end=' ')
    print()
