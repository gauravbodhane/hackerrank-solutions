# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/lbp6222/challenges/lbp16/problem?isFullScreen=true
# Problem     LBP16
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-08, 03:25 p.m.
# ──────────────────────────────────────────────────

n = input()
n1 = input() 
c = 0
for i in n:
    if n1 in i :
        c+= 1
print(c)
