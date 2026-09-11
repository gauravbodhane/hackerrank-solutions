# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp185/problem?isFullScreen=true
# Problem     LBP185
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-11, 10:56 a.m.
# Technique   list-comprehension-max-reduction
# Time        O(n)
# Space       O(n)
# Insight     The code calculates the savings for each friend by subtracting the expenditure at the odd index from the salary at the preceding even index and identifies the maximum value.
# Interview   Before: "How would you find the maximum savings from a flat list of salary-expenditure pairs?" After: "I iterate through the list with a step of two to compute each difference in O(n) time and O(n) space, then return the maximum value found."
# Pitfalls    (1) The code assumes the input list length is always a multiple of two, which may cause an IndexError if the input contains an odd number of elements.  (2) The code assumes the input contains at least two elements, as an empty list would cause max() to raise a ValueError.
# ──────────────────────────────────────────────────

l = [int(i) for i in input().split()]

r = []
for i in range(0,len(l),2):
    r1 = l[i] -l[i+1]
    r.append(r1)
print(max(r))
