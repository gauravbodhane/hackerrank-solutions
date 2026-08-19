# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp149/problem?isFullScreen=true
# Problem     LBP149
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-19, 09:42 p.m.
# Technique   linear-scan-neighbor-comparison
# Time        O(n)
# Space       O(n)
# Insight     The algorithm iterates through the array from the second element to the second-to-last element, identifying local maxima by comparing each element strictly against its immediate left and right neighbors.
# Interview   Before: "How would you find all local peaks in an array?" After: "I iterate from index 1 to n-2, checking if the current element is strictly greater than both neighbors. This O(n) approach correctly ignores boundary elements as required by the problem statement."
# Pitfalls    (1) The loop range(1, len(l)-1) correctly excludes boundary elements, but failing to account for this range would lead to index out of bounds errors.  (2) The strict inequality condition l[i] > l[i-1] and l[i] > l[i+1] correctly ignores plateaus where adjacent elements are equal.
# ──────────────────────────────────────────────────

n = int(input())
l = [int(i) for i in input().split()]
for i in range(1,len(l)-1):
    if l[i]>l[i-1] and l[i]>l[i+1]:
        print(l[i],end=' ')
