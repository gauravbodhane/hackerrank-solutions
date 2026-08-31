# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp167/problem?isFullScreen=true
# Problem     LBP167
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-31, 02:26 p.m.
# ──────────────────────────────────────────────────

import math 

def count(n):
    c= 0
    while str(n).endswith('0'):
        c +=1 
        n = n//10
    return c
n = int(input())
print(count(math.factorial(n)))
