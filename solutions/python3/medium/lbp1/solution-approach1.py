# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/lbp6222/challenges/lbp1/problem?isFullScreen=true
# Problem     LBP001
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-05, 05:18 p.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

if n < 0 :
    print('invalid')
elif n %2==0:
    print('even')
else:
    print('odd')
