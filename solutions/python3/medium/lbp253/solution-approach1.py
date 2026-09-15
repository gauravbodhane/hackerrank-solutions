# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp253/problem?isFullScreen=true
# Problem     LBP253
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-15, 01:01 p.m.
# Technique   iterative-pair-swapping
# Time        O(n)
# Space       O(n)
# Insight     The algorithm iterates through the list in steps of two, swapping adjacent elements until it reaches the end or leaves the final element unchanged if the list length is odd.
# Interview   Before: "How would you decrypt a sequence by swapping consecutive pairs?" After: "I iterate through the list with a step of two, swapping indices i and i+1. This runs in O(n) time and O(n) space, correctly handling odd-length lists by leaving the last element in place."
# Pitfalls    (1) The code assumes the input list contains exactly n elements, which may cause an IndexError if the input line has fewer than n integers.  (2) The logic fails if n is 0, as the range or loop conditions might not handle empty input correctly depending on the input stream.  (3) The use of print with end=' ' results in a trailing space, which might violate strict output formatting requirements.
# ──────────────────────────────────────────────────

n = int(input())
L = [int(i) for i in input().split()]

if n% 2==0:
    i = 0
    while i<n:
        print(L[i+1], L[i],end=' ')
        i = i+2
else :
    i = 0
    while i<n-1:
        print(L[i+1],L[i],end=' ')
        i= i+2
    print(L[n-1])
