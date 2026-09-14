# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp216/problem?isFullScreen=true
# Problem     LBP216
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-14, 11:12 p.m.
# ──────────────────────────────────────────────────

l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]
l3 = [int(i) for i in input().split()]

l = [l1,l2,l3]

for i in range(3):
    g = min(l[i])
    print(g)
