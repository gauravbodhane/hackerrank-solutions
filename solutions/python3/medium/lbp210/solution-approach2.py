# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/matrixtest/challenges/lbp210/problem?isFullScreen=true
# Problem     LBP210
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 09:04 a.m.
# ──────────────────────────────────────────────────

a = []
for i in range(3):
    a.append([int(i) for i in input().split()])
s = a[0][0] + a[2][2]
print(s)
