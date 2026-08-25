# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp249/problem?isFullScreen=true
# Problem     LBP249	
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-25, 12:13 p.m.
# Technique   nested-loop-string-reversal
# Time        O(N*M*D)
# Space       O(N*M)
# Insight     The program iterates through each integer in the 3x3 matrix, converts it to a string, reverses the character sequence using slicing, and prints the result.
# Interview   Before: "How would you reverse the digits of every number in a 3x3 matrix?" After: "I would iterate through each row and column, convert each integer to a string, and use slicing to reverse it. This approach runs in O(N*M*D) time, where D is the number of digits."
# Pitfalls    (1) The code assumes exactly three lines of input, which may fail if the input format deviates from the specified 3x3 matrix structure.  (2) Using string reversal on negative integers would place the minus sign at the end of the number, which may not be the intended mathematical behavior.
# ──────────────────────────────────────────────────

l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]
l3 = [int(i) for i in input().split()]
l = [l1,l2,l3]
for i in range(3):
    for j in range(3):
        print(str(l[i][j])[::-1],end= ' ')
    print()
