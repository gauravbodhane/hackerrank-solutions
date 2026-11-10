# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/lbp6222/challenges/lbp27/problem?isFullScreen=true
# Problem     LBP27
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-10, 04:14 p.m.
# ──────────────────────────────────────────────────

i = int(input())
j = int(input())
k = int(input())
s=0
for x in range(i,j+1):
    s += x
for x in range(j-1,k-1,-1):
    s+= x
print(s)
