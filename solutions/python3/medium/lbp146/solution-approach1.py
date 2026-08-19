# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp146/problem?isFullScreen=true
# Problem     LBP146
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-19, 09:25 p.m.
# ──────────────────────────────────────────────────

n = int(input())
l = [int(i) for i in input().split()]
c =0 
s = 0
for i in l:
    if i > 0 :
        c =c +1
    else:
        s =s+i
if n!= 0:
    print(c,s)  
else:
    print(' ')
