# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp253/problem?isFullScreen=true
# Problem     LBP253
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-15, 01:01 p.m.
# ──────────────────────────────────────────────────

n = int(input())
L = [int(i) for i in input().split()]

if n% 2==0:
    i = 0
    while i<n:
        print(L[i+1], L[i],end=' ')
        i = i+2
else :
    i = 0
    while i<n-1:
        print(L[i+1],L[i],end=' ')
        i= i+2
    print(L[n-1])
