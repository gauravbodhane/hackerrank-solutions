# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp195/problem?isFullScreen=true
# Problem     LBP195
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-13, 01:01 p.m.
# ──────────────────────────────────────────────────

n = int(input())
if n >= 30 and n <= 100:
    if n >= 30 and n<= 50:
        print('Average')
    elif n >= 51 and n <= 60:
        print('Good')
    elif n>= 61 and n <= 80:
        print('Excellent')
    elif n>= 81 and n <= 100:
        print('Outstanding')    
else:
    print('invalid')
