# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp192/problem?isFullScreen=true
# Problem     LBP192
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-13, 12:55 p.m.
# ──────────────────────────────────────────────────

def sum(n):
    s = 0
    while n!= 0:
        d = n % 10
        s =s + (d*d*d)
        n = n // 10
    return s 
n = int(input())
for i in range(2,n+1):
    if i == sum(i):
        print(i,end=' ')
