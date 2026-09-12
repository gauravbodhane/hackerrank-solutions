# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp193/problem?isFullScreen=true
# Problem     LBP193
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-12, 12:44 p.m.
# ──────────────────────────────────────────────────

n = int(input())
while True:
    if n % 10 == 0:
        print(n) 
        break
    else:
        n = n+1
