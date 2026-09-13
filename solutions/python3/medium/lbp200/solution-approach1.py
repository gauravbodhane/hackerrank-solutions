# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp200/problem?isFullScreen=true
# Problem     LBP200
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-13, 02:00 p.m.
# Technique   linear-sum-of-remainders
# Time        O(N)
# Space       O(N)
# Insight     The algorithm iterates through the input list once, calculating the remainder of each element divided by K and accumulating these values into a running sum.
# Interview   Before: "How would you calculate the sum of remainders for a list of N numbers?" After: "I would iterate through the list once, applying the modulo operator to each element and summing the results, achieving O(N) time complexity and O(N) space complexity for the input storage."
# Pitfalls    (1) The code assumes K is non-zero, as division by zero will raise a ZeroDivisionError.  (2) The input format expects N, then the list, then K, which may cause errors if the input stream is not ordered exactly as specified.
# ──────────────────────────────────────────────────

n = int(input())
l =[int(i) for i in input().split()]
k = int(input())
s = 0
for i in l:
    s =s+i%k
print(s)
