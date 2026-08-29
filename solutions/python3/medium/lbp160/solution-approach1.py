# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp160/problem?isFullScreen=true
# Problem     LBP160
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-29, 09:57 a.m.
# ──────────────────────────────────────────────────

n = int(input())
l = [int(i) for i in input().split()]
c = 0
for i in range(n-1):
    for j in str(l[i]):
        if j in  str(l[i+1]):
            c = c +1
            break
print(str(c==n-1).lower())
