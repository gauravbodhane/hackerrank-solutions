# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/lbp6222/challenges/lbp12/problem?isFullScreen=true
# Problem     LBP12
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-08, 03:06 p.m.
# ──────────────────────────────────────────────────

n = input()
count=0
for i in n :
    if i in '369':
        count+= int(i)
print(count)
