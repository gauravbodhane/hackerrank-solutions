# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp147/problem?isFullScreen=true
# Problem     LBP147
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-19, 09:30 p.m.
# ──────────────────────────────────────────────────

n = int(input())
l = [int(i) for i in input().split()]
l.sort()
for i in range(n):
    if l[i] >= 0:
        print(l[i]+l[i+1])
        break
        
