# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp156/problem?isFullScreen=true
# Problem     LBP156
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-29, 08:43 a.m.
# ──────────────────────────────────────────────────

s = input() 
n = int(input())
L = [int(i) for i in input().split()]
for i in range(n):
    print(s[L[i]],end='')
