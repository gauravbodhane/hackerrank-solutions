# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp157/problem?isFullScreen=true
# Problem     LBP157
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-29, 09:02 a.m.
# ──────────────────────────────────────────────────

n = int(input())
L = [int(i) for i in input().split()]
flag=False
for i in L:
    if '7' in str(i) :
        flag=True
        break
print('Boom!' if flag else 'there is no 7 in the array')
