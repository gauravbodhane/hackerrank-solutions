# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp184/problem?isFullScreen=true
# Problem     LBP184
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-10, 06:51 p.m.
# ──────────────────────────────────────────────────

n = int(input())
l = [int(i) for i in input().split()]
b = sorted(l)
c = 0 
for i in range(n):
    if l[i] == b[i]:
        c += 1
print(c)
