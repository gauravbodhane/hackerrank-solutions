# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp176/problem?isFullScreen=true
# Problem     LBP176
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-03, 06:01 p.m.
# ──────────────────────────────────────────────────

a, b = (int(i) for i in input().split())

while b != 0:
    a , b = b , a%b
print(a)
