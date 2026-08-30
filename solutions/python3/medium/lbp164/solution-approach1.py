# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp164/problem?isFullScreen=true
# Problem     LBP164
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-30, 04:16 p.m.
# Technique   linear-scan-boundary-handling
# Time        O(n)
# Space       O(n)
# Insight     The algorithm updates each internal element by multiplying its immediate neighbors while explicitly printing the first and last elements as boundary cases.
# Interview   Before: "How would you update each element to the product of its neighbors?" After: "I would handle the boundaries separately and iterate through the middle, resulting in O(n) time and O(n) space complexity, ensuring the first and last elements are correctly preserved as per the problem constraints."
# Pitfalls    (1) Failing to handle the first and last elements separately leads to index out of bounds errors.  (2) Assuming the input array size is always greater than one, which is required for the logic to function correctly.
# ──────────────────────────────────────────────────

n = int(input())
l = [int(i) for i in input().split()]
print(l[1],end=' ')
for i in range(1,n-1):
    print(l[i-1]*l[i+1], end=' ')
print(l[n-2])
