# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp155/problem?isFullScreen=true
# Problem     LBP155
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-28, 02:28 p.m.
# ──────────────────────────────────────────────────

n = int(input())
s = int(input())
L = [int(i) for i in input().split()]
L.sort()
print(L[s-1])
