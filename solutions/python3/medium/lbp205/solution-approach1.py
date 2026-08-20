# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp205/problem?isFullScreen=true
# Problem     LBP205
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-20, 08:45 a.m.
# Technique   brute-force-prime-check
# Time        O(N^2 * M)
# Space       O(N^2)
# Insight     The program iterates through every element in the 3x3 matrix and adds it to the total sum if the element has exactly two divisors.
# Interview   Before: "How would you sum prime numbers in a matrix?" After: "I would iterate through each cell and verify primality by counting divisors, resulting in O(N^2 * M) time complexity, where M is the maximum value in the matrix."
# Pitfalls    (1) The isprime function incorrectly identifies 1 as a non-prime by checking for exactly two divisors, which is correct, but it is inefficient for large inputs.  (2) The nested loops are hardcoded for a 3x3 matrix, which will fail if the input dimensions deviate from the problem statement's constraints.  (3) The primality test uses an O(N) approach per element, which is inefficient compared to O(sqrt(N)) trial division.
# ──────────────────────────────────────────────────

def isprime(n):
    f = 0
    for i in range(1,n+1):
        if n%i==0:
            f = f+1
    return f==2
a = []
for i in range(3):
    a.append([int(i) for i in input().split()])
s= 0
for i in range(3):
    for j in range(3):
        if isprime(a[i][j]):
            s=s+a[i][j] 
print(s)
