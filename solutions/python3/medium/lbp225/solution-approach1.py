# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp225/problem?isFullScreen=true
# Problem     LBP225
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-22, 08:43 a.m.
# Technique   flatten-sort-reconstruct
# Time        O(N log N)
# Space       O(N)
# Insight     The algorithm flattens the 3x3 matrix into a single list, sorts the elements in ascending order, and then maps them back into the original matrix structure.
# Interview   Before: "How would you sort a 3x3 matrix?" After: "I would flatten the matrix into a 1D array, sort it in O(N log N) time, and refill the matrix, where N is the total number of elements."
# Pitfalls    (1) The implementation assumes a fixed 3x3 matrix size, which will fail if the input dimensions differ from the hardcoded loops.  (2) The use of nested loops for input reading and output printing is rigid and does not handle dynamic matrix sizes.
# ──────────────────────────────────────────────────

l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]
l3 = [int(i) for i in input().split()]
l = [l1,l2,l3]
ll= []
for i in range(3):
    for j in range(3):
        ll.append(l[i][j])
ll.sort()
k = 0
for i in range(3):
    for j in range(3):
        l[i][j]=ll[k]
        k= k +1
        
for i in range(3):
    for j in range(3):
        print(l[i][j],end=' ')
    print()
