# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp163/problem?isFullScreen=true
# Problem     LBP163
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-30, 02:06 p.m.
# Technique   linear-scan-frequency-count
# Time        O(n^2)
# Space       O(1)
# Insight     The algorithm iterates through the input list and identifies the unique element by checking if its total count within the list equals one.
# Interview   Before: "I could use a hash map to track frequencies in linear time." After: "This implementation uses a nested count approach, resulting in O(n^2) time complexity, which is acceptable given the constraints but less efficient than a frequency map for large inputs."
# Pitfalls    (1) The O(n^2) time complexity may cause a timeout on large input arrays.  (2) The count method iterates over the entire list for every element, leading to redundant calculations.
# ──────────────────────────────────────────────────

n = int(input())
l = [int(i) for i in input().split() ]
for i in l:
    t =l.count(i)
    if t== 1:
        print(i)
