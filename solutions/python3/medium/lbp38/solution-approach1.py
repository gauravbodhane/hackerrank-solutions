# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/lbp6222/challenges/lbp38/problem?isFullScreen=true
# Problem     LBP38
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-12, 10:29 p.m.
# ──────────────────────────────────────────────────

s = input()

count = 0

for ch in s:
    if not (ch.isalnum() or ch.isspace()):
        count += 1

print(count)
