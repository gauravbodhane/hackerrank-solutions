# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp267/problem?isFullScreen=true
# Problem     LBP267
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-17, 02:22 p.m.
# Technique   linear-search-perfect-square
# Time        O(sqrt(N))
# Space       O(1)
# Insight     The algorithm iterates through consecutive integers starting from one until the square of the current integer is greater than or equal to the input number.
# Interview   Before: "How would you find the smallest perfect square greater than or equal to N?" After: "I iterate through integers starting from one, squaring each until the result is at least N. This approach runs in O(sqrt(N)) time, which is efficient for finding the next perfect square."
# Pitfalls    (1) The loop condition i * i >= n correctly identifies the first perfect square greater than or equal to n, but it may return n itself if n is already a perfect square.  (2) The implementation lacks input validation for negative numbers, which could lead to unexpected behavior if the input is not a positive integer.
# ──────────────────────────────────────────────────

n = int(input())
i = 1
while True:
    if i * i>= n:
        print(i*i) 
        break
    i = i +1 
    
