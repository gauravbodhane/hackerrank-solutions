# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp181/problem?isFullScreen=true
# Problem     LBP181
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-11, 10:41 a.m.
# ──────────────────────────────────────────────────

n = input()

c = 0
for i in n :
    if n.count(i)==1:
        c =c+1
    if c == 2:
        print(i)
        break
