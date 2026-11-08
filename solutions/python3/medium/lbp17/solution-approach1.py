# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/lbp6222/challenges/lbp17/problem?isFullScreen=true
# Problem     LBP17
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-08, 03:31 p.m.
# ──────────────────────────────────────────────────

def pali(n):
    if n == n[::-1]:
        return 'Yes'
    else:
        return 'No'
n = input() 
print(pali(n))
