# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp226/problem?isFullScreen=true
# Problem     LBP226
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-22, 08:50 a.m.
# Technique   flatten-sort-reverse-fill
# Time        O(N log N)
# Space       O(N)
# Insight     The implementation flattens the 3x3 matrix into a list, sorts it in ascending order, and then populates the matrix in reverse order to achieve a descending sort.
# Interview   Before: "How would you sort a 2D matrix in descending order?" After: "I flatten the matrix into a 1D array, sort it, and map it back in reverse. This approach runs in O(N log N) time, where N is the total number of elements, effectively handling the 3x3 grid constraints."
# Pitfalls    (1) The code assumes a fixed 3x3 input size, which will fail if the input matrix dimensions differ from the hardcoded loops.  (2) The use of hardcoded nested loops for input reading and printing limits the solution to exactly 3x3 matrices as per the sample.
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
k =len(ll)-1
for i in range(3):
    for j in range(3):
        l[i][j]=ll[k]
        k= k - 1
        
for i in range(3):
    for j in range(3):
        print(l[i][j],end=' ')
    print()
