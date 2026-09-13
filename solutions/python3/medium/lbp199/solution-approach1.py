# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp199/problem?isFullScreen=true
# Problem     LBP199
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-13, 01:58 p.m.
# Technique   linear-sum-of-quotients
# Time        O(N)
# Space       O(N)
# Insight     The algorithm computes the total score by iterating through the input list and accumulating the integer division result of each element by the divisor k.
# Interview   Before: "I would use a loop to divide each element by k and sum them up." After: "I implemented an O(N) solution that iterates through the list once, performing integer division on each element to calculate the total score, ensuring efficiency for large input sizes."
# Pitfalls    (1) The code assumes k is non-zero, as division by zero will raise a ZeroDivisionError.  (2) The problem specifies positive numbers, so negative inputs or zero in the list may lead to unexpected quotient results.
# ──────────────────────────────────────────────────

n = int(input())
l =[int(i) for i in input().split()]
k = int(input())
s = 0
for i in l:
    s =s+i//k
print(s)
