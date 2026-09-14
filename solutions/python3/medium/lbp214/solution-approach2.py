# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp214/problem?isFullScreen=true
# Problem     LBP214
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-14, 11:05 p.m.
# ──────────────────────────────────────────────────

m = []
 
for i in range(3):
    m += [int(x) for x in input().split()]
print(min(m))
