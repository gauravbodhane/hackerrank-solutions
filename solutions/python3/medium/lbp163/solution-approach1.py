# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp163/problem?isFullScreen=true
# Problem     LBP163
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-30, 02:06 p.m.
# ──────────────────────────────────────────────────

n = int(input())
l = [int(i) for i in input().split() ]
for i in l:
    t =l.count(i)
    if t== 1:
        print(i)
