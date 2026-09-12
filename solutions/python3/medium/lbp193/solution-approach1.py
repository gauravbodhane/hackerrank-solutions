# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp193/problem?isFullScreen=true
# Problem     LBP193
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-12, 12:44 p.m.
# Technique   linear-increment-search
# Time        O(1)
# Space       O(1)
# Insight     The algorithm iteratively increments the input integer until the remainder when divided by ten is zero.
# Interview   Before: "How would you round a number to the nearest multiple of ten?" After: "I would increment the value until the last digit is zero, which runs in O(1) time since the maximum distance to the next multiple of ten is nine."
# Pitfalls    (1) The implementation assumes the input is a non-negative integer as per the problem context.  (2) The loop will run indefinitely if the input is not a valid integer type.
# ──────────────────────────────────────────────────

n = int(input())
while True:
    if n % 10 == 0:
        print(n) 
        break
    else:
        n = n+1
