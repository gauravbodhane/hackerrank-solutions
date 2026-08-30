# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp165/problem?isFullScreen=true
# Problem     LBP165
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-30, 04:23 p.m.
# Technique   sorting-index-access
# Time        O(N log N)
# Space       O(N)
# Insight     The code sorts the array in ascending order and accesses the second minimum element at index 1 and the third largest element at index N-3.
# Interview   Before: "How would you find the sum of the second minimum and third largest elements?" After: "I sort the array in O(N log N) time and access indices 1 and N-3, assuming N is at least 3 as implied by the problem constraints."
# Pitfalls    (1) The code assumes N is at least 3, which will cause an IndexError for smaller arrays.  (2) The logic fails if the array contains duplicate values, as it treats them as distinct positions in the sorted order.
# ──────────────────────────────────────────────────

n = int(input())
l =[int(i) for i in input().split()]
l.sort()
print(l[2-1]+l[n-3])
