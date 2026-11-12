# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/lbp6222/challenges/lbp31/problem?isFullScreen=true
# Problem     LBP31
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-12, 05:21 p.m.
# ──────────────────────────────────────────────────

i = input()
j = input()
k = input() 

n1 = min(i[0]+j[0]+k[0])
n2 = min(i[1]+j[1]+k[1])
n3 = min(i[2]+j[2]+k[2])

mx = max(i+j+k)

print(mx+n1+n2+n3)
