# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/lbp6222/challenges/lbp23/problem?isFullScreen=true
# Problem     LBP23
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-09, 04:33 p.m.
# ──────────────────────────────────────────────────

n = input()

s = 0
p = 1

for i in n:
    i = int(i)
    s = s + i
    p = p * i

if s + p == int(n):
    print("Yes")
else:
    print("No")
