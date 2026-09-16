# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp258/problem?isFullScreen=true
# Problem     LBP258
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-16, 01:20 p.m.
# ──────────────────────────────────────────────────

n = input()
c = 0 
for i in n:
    if i.isdigit():
        c += 1
print(c)
