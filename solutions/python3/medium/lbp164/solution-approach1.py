# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp164/problem?isFullScreen=true
# Problem     LBP164
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-30, 04:16 p.m.
# ──────────────────────────────────────────────────

n = int(input())
l = [int(i) for i in input().split()]
print(l[1],end=' ')
for i in range(1,n-1):
    print(l[i-1]*l[i+1], end=' ')
print(l[n-2])
