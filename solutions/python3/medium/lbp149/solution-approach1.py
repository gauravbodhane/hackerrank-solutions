# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp149/problem?isFullScreen=true
# Problem     LBP149
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-19, 09:42 p.m.
# ──────────────────────────────────────────────────

n = int(input())
l = [int(i) for i in input().split()]
for i in range(1,len(l)-1):
    if l[i]>l[i-1] and l[i]>l[i+1]:
        print(l[i],end=' ')
