# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp184/problem?isFullScreen=true
# Problem     LBP184
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-10, 06:51 p.m.
# Technique   sorting-and-index-comparison
# Time        O(n log n)
# Space       O(n)
# Insight     The algorithm identifies elements that remain at their original indices by comparing the input array with its sorted version.
# Interview   Before: "How would you count elements that stay in place after sorting?" After: "I compare the original array with a sorted copy, counting indices where values match. This takes O(n log n) time due to sorting and O(n) space to store the sorted array, handling any integer input size n."
# Pitfalls    (1) Failing to account for O(n log n) time complexity when n is large.  (2) Assuming the input array is already sorted or partially sorted.  (3) Misinterpreting the problem as requiring an in-place sort, which would modify the original indices.
# ──────────────────────────────────────────────────

n = int(input())
l = [int(i) for i in input().split()]
b = sorted(l)
c = 0 
for i in range(n):
    if l[i] == b[i]:
        c += 1
print(c)
