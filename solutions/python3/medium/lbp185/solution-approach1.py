# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp185/problem?isFullScreen=true
# Problem     LBP185
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-11, 10:56 a.m.
# ──────────────────────────────────────────────────

l = [int(i) for i in input().split()]

r = []
for i in range(0,len(l),2):
    r1 = l[i] -l[i+1]
    r.append(r1)
print(max(r))
