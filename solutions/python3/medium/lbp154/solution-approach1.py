# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp154/problem?isFullScreen=true
# Problem     LBP154
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-28, 02:12 p.m.
# Technique   linear-scan-absolute-range-filter
# Time        O(N)
# Space       O(N)
# Insight     The algorithm iterates through the list of distances and prints each value whose absolute magnitude falls within the inclusive range defined by the provided start and end distance bounds.
# Interview   Before: "How do we filter employees by distance?" After: "We perform a linear scan in O(N) time, checking if the absolute value of each distance lies within [x1, x2]. If no values match, the output remains empty, which is the expected behavior for this range query."
# Pitfalls    (1) The code fails to output -1 when no employees fall within the specified range, contradicting the problem statement requirement.  (2) The use of abs(i) assumes the range bounds x1 and x2 are non-negative, which may lead to incorrect filtering if negative bounds are provided.
# ──────────────────────────────────────────────────

n = int(input())
x1,x2= (int(i) for i  in input().split())
L = [int(i) for i in input().split()]
for i in L:
    if abs(i)>= x1 and abs(i)<= x2:
        print(i,end=' ')
