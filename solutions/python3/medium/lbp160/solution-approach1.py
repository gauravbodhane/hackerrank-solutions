# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp160/problem?isFullScreen=true
# Problem     LBP160
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-29, 09:57 a.m.
# Technique   linear-scan-digit-intersection
# Time        O(N * D)
# Space       O(D)
# Insight     The algorithm verifies that every adjacent pair in the array shares at least one common digit by incrementing a counter for each successful match and comparing the final count to the total number of pairs.
# Interview   Before: "How do you check if adjacent numbers share a digit?" After: "I convert each number to a string and check for character intersection. This runs in O(N * D) time, where N is the array size and D is the maximum number of digits in an element."
# Pitfalls    (1) The code assumes the input array size n is at least 1, as range(n-1) will not execute for n=1, resulting in a count of 0 which correctly returns true.  (2) The logic relies on string conversion, which is efficient for small integers but may be slower for extremely large numbers.
# ──────────────────────────────────────────────────

n = int(input())
l = [int(i) for i in input().split()]
c = 0
for i in range(n-1):
    for j in str(l[i]):
        if j in  str(l[i+1]):
            c = c +1
            break
print(str(c==n-1).lower())
