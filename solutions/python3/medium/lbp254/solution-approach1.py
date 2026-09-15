# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp254/problem?isFullScreen=true
# Problem     LBP254
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-15, 01:10 p.m.
# Technique   brute-force-cube-check
# Time        O(N * max(price)^(1/3))
# Space       O(N)
# Insight     The algorithm iterates through each product price and performs a linear search to verify if the cube of any integer equals the given price.
# Interview   Before: "How would you identify perfect cubes in a list?" After: "I iterate through each number and check if any integer cubed matches the value, resulting in O(N * max(price)^(1/3)) time complexity, which is sufficient for small price values."
# Pitfalls    (1) The linear search for the cube root is inefficient for very large price values.  (2) The code prints each perfect cube found instead of returning the total count as requested by the problem description.
# ──────────────────────────────────────────────────

n = int(input())
L = [int(i) for i in input().split()]

for i in L:
    c = 0
    while c<= i :
        if (c*c*c==i):
            print(i,end=' ')
            break
        c =c +1
