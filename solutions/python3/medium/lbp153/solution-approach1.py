# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp153/problem?isFullScreen=true
# Problem     LBP153
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-28, 01:43 p.m.
# Technique   nested-loop-perfect-square-check
# Time        O(N * max(A))
# Space       O(N)
# Insight     The algorithm iterates through each plot area and checks if any integer k exists such that k squared equals the area.
# Interview   Before: "How would you count the number of square-shaped plots in a list?" After: "I iterate through each area and verify if it is a perfect square by checking all integers up to the area value, resulting in O(N * max(A)) time complexity."
# Pitfalls    (1) The nested loop approach is inefficient for large area values as it checks every integer up to the area.  (2) The code fails to handle non-positive area values correctly if they were present in the input.
# ──────────────────────────────────────────────────

n = int(input())
L = [int(i) for i in input().split()]
c = 0
for i in range(0,n):
    for k in range(1,L[i]+1):
        if k*k == L[i]:
            c = c+1
print(c)  
