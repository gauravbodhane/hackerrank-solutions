# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/lbp6222/challenges/lbp32/problem?isFullScreen=true
# Problem     LBP32
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-12, 05:25 p.m.
# ──────────────────────────────────────────────────

n = input() 
c = 0 
for i in n:
    if not i.isalnum():
        c+=1
print(c)
