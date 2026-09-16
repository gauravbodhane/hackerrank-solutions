# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp260/problem?isFullScreen=true
# Problem     LBP260
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-16, 02:51 p.m.
# ──────────────────────────────────────────────────

import math
n = int(input())
f = math.factorial(n) 
if f% 10 == 0:
    print((f//10)%10)
else:
    print(f%10)
