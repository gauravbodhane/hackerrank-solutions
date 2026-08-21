# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp211/problem?isFullScreen=true
# Problem     LBP211
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 08:22 a.m.
# ──────────────────────────────────────────────────

a =[]
for i in range(3):
    a.append([int(i) for i in input().split()])
s =1
for i in range(3):
    
    if i ==i:
        s *=a[i][i]
print(s)
