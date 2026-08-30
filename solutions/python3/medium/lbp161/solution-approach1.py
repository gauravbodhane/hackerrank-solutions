# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp161/problem?isFullScreen=true
# Problem     LBP161
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-30, 12:08 p.m.
# Technique   sorting-and-linear-scan
# Time        O(N log N)
# Space       O(N)
# Insight     The algorithm determines if a combined array forms a consecutive sequence by sorting the elements and verifying that every adjacent pair has a difference of exactly one.
# Interview   Before: "How would you check if two arrays form a consecutive sequence?" After: "I would concatenate and sort the arrays in O(N log N) time, then verify that each adjacent element pair has a difference of one to ensure no gaps exist in the sequence."
# Pitfalls    (1) The logic fails if the input arrays contain duplicate values, as the difference between adjacent elements would be zero instead of one.  (2) The code assumes the input arrays are non-empty, as an empty input would cause an index error or incorrect comparison logic.
# ──────────────────────────────────────────────────

n1 = int(input())
l1 = [int(i) for i in input().split()]
n2 = int(input())
l2 = [int(i) for i in input().split()]
l3 = l1 +l2
l3.sort()
c = 0
for i in range(0,(n1+n2)-1):
    if l3[i]+1 ==l3[i+1]:
        c=c+1
print(str(c==(n1+n2)-1).lower())
        
