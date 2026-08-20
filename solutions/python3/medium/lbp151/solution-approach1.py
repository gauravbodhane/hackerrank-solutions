# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp151/problem?isFullScreen=true
# Problem     LBP151
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-20, 10:20 p.m.
# Technique   linear-scan-adjacent-difference
# Time        O(n)
# Space       O(n)
# Insight     The algorithm iterates through the array once, accumulating the absolute difference between each pair of adjacent elements.
# Interview   Before: "I would use a nested loop to compare every pair." After: "I can compute the sum of adjacent distances in O(n) time by iterating once and calculating the absolute difference between index i and i+1, which handles the array size constraint efficiently."
# Pitfalls    (1) Accessing l[i+1] when i reaches n-1 would cause an index out of bounds error, which is prevented by the range(n-1) loop limit.  (2) Failing to use the absolute value function would result in incorrect sums for descending sequences.
# ──────────────────────────────────────────────────

n = int(input())
l = [int (i) for i in input().split()]
s = 0
for i in range(n-1):
    s += abs(l[i] - l[i+1])
print(s)
