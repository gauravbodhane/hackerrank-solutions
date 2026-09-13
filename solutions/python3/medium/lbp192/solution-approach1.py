# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp192/problem?isFullScreen=true
# Problem     LBP192
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-13, 12:55 p.m.
# Technique   brute-force-digit-sum-check
# Time        O(N log N)
# Space       O(1)
# Insight     The program iterates through every integer from 2 to N and verifies if the sum of the cubes of its digits equals the integer itself.
# Interview   Before: "How would you identify Armstrong numbers up to N?" After: "I iterate from 2 to N, calculating the sum of cubed digits for each. This approach runs in O(N log N) time, where log N represents the number of digits in each integer."
# Pitfalls    (1) The range function range(2, n+1) correctly includes N, but failing to account for the upper bound N would violate the problem requirement.  (2) The sum function uses integer division n // 10, which is correct for base-10 digit extraction but would fail if the input were not a positive integer.
# ──────────────────────────────────────────────────

def sum(n):
    s = 0
    while n!= 0:
        d = n % 10
        s =s + (d*d*d)
        n = n // 10
    return s 
n = int(input())
for i in range(2,n+1):
    if i == sum(i):
        print(i,end=' ')
