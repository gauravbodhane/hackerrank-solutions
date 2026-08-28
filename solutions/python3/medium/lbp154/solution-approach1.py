# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp154/problem?isFullScreen=true
# Problem     LBP154
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-28, 02:12 p.m.
# ──────────────────────────────────────────────────

n = int(input())
x1,x2= (int(i) for i  in input().split())
L = [int(i) for i in input().split()]
for i in L:
    if abs(i)>= x1 and abs(i)<= x2:
        print(i,end=' ')
