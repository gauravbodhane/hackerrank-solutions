# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp186/problem?isFullScreen=true
# Problem     LBP186
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-11, 11:10 a.m.
# Technique   slicing-and-reverse-sort
# Time        O(N log N)
# Space       O(N)
# Insight     The algorithm sorts the entire list and then reverses the second half to satisfy the ascending-descending requirement.
# Interview   Before: "How would you sort the first half ascending and the second half descending?" After: "I sort the entire array in O(N log N) time, then reverse the second half, which takes O(N) time, resulting in an overall O(N log N) complexity for any N."
# Pitfalls    (1) The implementation assumes K is always N//2, which may not match requirements if K is provided as a separate input.  (2) The code fails if the input list is empty, as the slicing logic assumes at least one element exists.
# ──────────────────────────────────────────────────

n = int(input())
l = [int(i) for i in input().split()]
l.sort()
g = n//2
r = l[:g] + l[g:][::-1]
print(*r)
