# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/lbp6222/challenges/lbp10/problem?isFullScreen=true
# Problem     LBP010
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-08, 02:55 p.m.
# ──────────────────────────────────────────────────

n = input() 
sum = 0
for i in n :
    if int(i)% 2 != 0:
        sum+= int(i)
print(sum)
