# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp251/problem?isFullScreen=true
# Problem     LBP251
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-15, 12:39 p.m.
# Technique   two-pass-linear-scan
# Time        O(N)
# Space       O(N)
# Insight     The algorithm maintains the relative order of elements by performing two separate linear passes over the input array, first printing non-multiples of ten and then printing multiples of ten.
# Interview   Before: "I could sort the array or use a partition function." After: "A two-pass approach is more efficient at O(N) time and O(N) space, ensuring the stable relative order required by the problem statement for multiples of ten."
# Pitfalls    (1) Failing to maintain the stable relative order of elements as explicitly required by the problem statement.  (2) Printing extra spaces or formatting errors that deviate from the expected output format of the updated array.
# ──────────────────────────────────────────────────

n = int(input())
L = [int(i) for i in input().split()]

for i in L:
    if i%10 != 0:
        print(i,end=' ') 

for i in L:
    if i%10 == 0:
        print(i,end=' ') 
