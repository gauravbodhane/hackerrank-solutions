# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp177/problem?isFullScreen=true
# Problem     LBP177
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-03, 06:11 p.m.
# ──────────────────────────────────────────────────

n = input()

for ch in n:
    if ch.isupper() or ch.isdigit():
        print(ch,end='')
