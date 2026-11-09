# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/lbp6222/challenges/lbp22/problem?isFullScreen=true
# Problem     LBP22
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-09, 04:16 p.m.
# ──────────────────────────────────────────────────

n = input()
c = 0
for i in n:
    c+=int(i)
if int(n) % c == 0:
    print('Yes')
else:
    print('No')
