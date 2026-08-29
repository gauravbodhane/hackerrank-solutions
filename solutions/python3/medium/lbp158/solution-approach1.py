# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp158/problem?isFullScreen=true
# Problem     LBP158
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-29, 09:20 a.m.
# ──────────────────────────────────────────────────

n = int(input())
L=[int(i) for i in input().split()]
flag = True
for i in range(0,n-1):
    if L[i] > 0 and L[i+1] > 0:
        flag = False
        break
    if L[i]<0 and L[i+1]<0:
        flag =False
        break
print(str(flag).lower())
