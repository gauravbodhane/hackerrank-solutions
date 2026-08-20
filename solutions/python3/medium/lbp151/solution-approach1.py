# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp151/problem?isFullScreen=true
# Problem     LBP151
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-20, 10:20 p.m.
# ──────────────────────────────────────────────────

n = int(input())
l = [int (i) for i in input().split()]
s = 0
for i in range(n-1):
    s += abs(l[i] - l[i+1])
print(s)
