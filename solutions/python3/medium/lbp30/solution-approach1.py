# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/lbp6222/challenges/lbp30/problem?isFullScreen=true
# Problem     LBP30
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-10, 04:33 p.m.
# ──────────────────────────────────────────────────

def palli(n):
    rev = ''
    for i in n:
        rev = i + rev 
    if n == rev :
        print('valid')
    else:
        print('invalid')
        
n = input()

palli(n)
