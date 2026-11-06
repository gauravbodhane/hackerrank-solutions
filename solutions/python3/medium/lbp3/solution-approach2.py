# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/lbp6222/challenges/lbp3/problem?isFullScreen=true
# Problem     LBP003
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-06, 10:26 p.m.
# ──────────────────────────────────────────────────

year = int(input())

if year % 400 == 0:
    print('True')
elif year % 4 == 0 and year % 100 != 0:
    print('True')
else:
    print('False')
