# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp180/problem?isFullScreen=true
# Problem     LBP180
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-10, 05:21 p.m.
# ──────────────────────────────────────────────────

n = int(input())
count = 0

while n > 0:
    if n % 2 == 1:
        count += 1
    n= n // 2
        
if count % 2 == 0:
    print('even')
else:
    print('odd')
