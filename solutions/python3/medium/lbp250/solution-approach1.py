# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp250/problem?isFullScreen=true
# Problem     LBP250	
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-25, 12:20 p.m.
# Technique   nested-loop-string-reversal
# Time        O(1)
# Space       O(1)
# Insight     The program iterates through a fixed 3x3 matrix and replaces each element with zero if its string representation is not equal to its reverse.
# Interview   Before: "How would you filter a matrix for palindromes?" After: "I would iterate through each cell, convert the integer to a string, and compare it with its reverse slice. This approach runs in O(1) time since the matrix size is constant."
# Pitfalls    (1) The code assumes exactly three lines of input, which will fail if the input format deviates from the specified 3x3 matrix.  (2) The string reversal check treats single-digit numbers as palindromes, which is consistent with the provided sample output.
# ──────────────────────────────────────────────────

l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]
l3 = [int(i) for i in input().split()]
l = [l1,l2,l3]
for i in range(3):
    for j in range(3):
        s = str(l[i][j])
        if s==s[::-1]:
            print(l[i][j],end=' ')
        else:
            print('0',end=' ')
    print()
