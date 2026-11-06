# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/lbp6222/challenges/lbp4/problem?isFullScreen=true
# Problem     LBP004
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-06, 10:34 p.m.
# ──────────────────────────────────────────────────

n = int(input())
if n >= 30 and n <= 100:
    if n >= 30 and n <= 50:
        print('D')
    elif n >= 51 and n <= 60:
        print('C')
    elif n >= 61 and n <= 80:
        print('B')
    elif n >= 81 and n <= 100:
        print('A')
else:
    print('invalid')
    
       
