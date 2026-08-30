# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp162/problem?isFullScreen=true
# Problem     LBP162
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-30, 01:57 p.m.
# ──────────────────────────────────────────────────

n = int(input())
l =[int(i) for i in input().split()]
c = 0
sc = 0
for i in l:
    x=str(i).count('5')
    if c <= x:
        c = x 
        element = i 
    if x == 0:
        sc = sc+1
if sc != n :
    print(element)
else:
    print(l[0])
        
