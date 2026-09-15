# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp251/problem?isFullScreen=true
# Problem     LBP251
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-15, 12:39 p.m.
# ──────────────────────────────────────────────────

n = int(input())
L = [int(i) for i in input().split()]

for i in L:
    if i%10 != 0:
        print(i,end=' ') 

for i in L:
    if i%10 == 0:
        print(i,end=' ') 
