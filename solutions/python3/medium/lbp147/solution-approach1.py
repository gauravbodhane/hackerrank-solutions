# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp147/problem?isFullScreen=true
# Problem     LBP147
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-19, 09:30 p.m.
# Technique   sorting-and-linear-scan
# Time        O(N log N)
# Space       O(N)
# Insight     The algorithm sorts the input array and identifies the first two non-negative integers to compute their sum.
# Interview   Before: "I would iterate through the list to find the two smallest values." After: "Sorting the array in O(N log N) time allows for a simple linear scan to find the two smallest positive integers, ensuring the sum is calculated efficiently even for large inputs."
# Pitfalls    (1) The code assumes the input contains at least two positive numbers, which may cause an IndexError if fewer than two exist.  (2) The logic fails to handle cases where the input array contains only one positive number or none at all.
# ──────────────────────────────────────────────────

n = int(input())
l = [int(i) for i in input().split()]
l.sort()
for i in range(n):
    if l[i] >= 0:
        print(l[i]+l[i+1])
        break
        
