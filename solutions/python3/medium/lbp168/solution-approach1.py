# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp168/problem?isFullScreen=true
# Problem     LBP168
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-31, 02:33 p.m.
# ──────────────────────────────────────────────────

n = int(input())
L=[int(i) for i in input().split()]
print("true" if L==L[::-1]else "false")
