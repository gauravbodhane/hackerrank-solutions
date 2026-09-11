# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp186/problem?isFullScreen=true
# Problem     LBP186
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-11, 11:10 a.m.
# ──────────────────────────────────────────────────

n = int(input())
l = [int(i) for i in input().split()]
l.sort()
g = n//2
r = l[:g] + l[g:][::-1]
print(*r)
