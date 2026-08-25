# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp248/problem?isFullScreen=true
# Problem     LBP248	
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-25, 12:06 p.m.
# Technique   nested-loop-digit-extraction
# Time        O(N*M*D)
# Space       O(N*M)
# Insight     The algorithm iterates through each matrix element, converts it to a string, and increments a counter for every character that matches the set of prime digits.
# Interview   Before: "How do you count prime digits in a matrix?" After: "I iterate through each cell, convert the integer to a string, and check each character against the set {2, 3, 5, 7}. This approach runs in O(N*M*D) time, where D is the number of digits per element."
# Pitfalls    (1) The code treats multi-digit numbers by checking each digit individually, which may lead to overcounting if the problem intended to check if the number itself is prime.  (2) The logic assumes all input elements are non-negative integers, as the string conversion of a negative sign would not match the prime digit set.
# ──────────────────────────────────────────────────

l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]
l3 = [int(i) for i in input().split()]
l = [l1,l2 , l3]
c = 0
for i in range(3):
    for j in range(3):
        for k in str(l[i][j]):
            if k in '2357':
                c =c +1
print(c)
