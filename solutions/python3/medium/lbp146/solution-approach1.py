# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp146/problem?isFullScreen=true
# Problem     LBP146
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-19, 09:25 p.m.
# Technique   linear-scan-accumulator
# Time        O(n)
# Space       O(n)
# Insight     The algorithm iterates through the input list once, incrementing a counter for positive integers and accumulating the sum of non-positive integers.
# Interview   Before: "How would you count positives and sum negatives in one pass?" After: "I iterate through the array once, maintaining a counter and a running sum, resulting in O(n) time and O(n) space complexity, while correctly handling the empty input case by printing a space."
# Pitfalls    (1) The code treats zero as a negative number by adding it to the sum, which is consistent with the rule that zero is not positive.  (2) The code prints a space for an empty input array instead of returning an empty array, as specified by the problem constraints.
# ──────────────────────────────────────────────────

n = int(input())
l = [int(i) for i in input().split()]
c =0 
s = 0
for i in l:
    if i > 0 :
        c =c +1
    else:
        s =s+i
if n!= 0:
    print(c,s)  
else:
    print(' ')
