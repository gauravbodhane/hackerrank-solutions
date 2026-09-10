# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp180/problem?isFullScreen=true
# Problem     LBP180
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-10, 05:17 p.m.
# ──────────────────────────────────────────────────

n = int(input())

binary = bin(n)
ones = binary.count("1")

if ones % 2 == 0:
    print('even')
else:
    print('odd')
