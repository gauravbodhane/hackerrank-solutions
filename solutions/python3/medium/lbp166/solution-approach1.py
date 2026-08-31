# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp166/problem?isFullScreen=true
# Problem     LBP166
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-31, 02:05 p.m.
# ──────────────────────────────────────────────────

n,m = (int(i) for i in input().split())
for i in range(n):
    l=[int(i) for i in input().split()]
    print(max(l),end=' ')
    
