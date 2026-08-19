# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp148/problem?isFullScreen=true
# Problem     LBP148
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-19, 09:35 p.m.
# Technique   list-slicing-and-conditional-check
# Time        O(m)
# Space       O(m)
# Insight     The implementation uses list slicing to extract the final m elements if m is less than or equal to the array size, otherwise it outputs zero.
# Pitfalls    (1) Failing to handle the case where m exceeds the array size, which requires returning 0 per the problem constraints.  (2) Incorrectly calculating the slice index as n-m, which relies on the input size n being provided correctly.
# ──────────────────────────────────────────────────

n = int(input())
l = [int(i) for i in input().split()]
m = int(input())
if m <= n:
    for i in l[n-m:]:
        print(i,end=' ')
else :
    print(0)
