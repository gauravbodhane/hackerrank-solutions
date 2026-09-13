# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp198/problem?isFullScreen=true
# Problem     LBP198
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-13, 01:34 p.m.
# ──────────────────────────────────────────────────

n = int(input()[::-1])
while n!= 0:
    d = n% 10
    if d% 2 ==0:
        print(d+1,end='')
    else:
        print(d-1,end='')
    n = n//10
