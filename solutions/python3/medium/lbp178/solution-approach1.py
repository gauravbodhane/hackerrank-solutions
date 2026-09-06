# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp178/problem?isFullScreen=true
# Problem     LBP178
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-06, 03:31 p.m.
# ──────────────────────────────────────────────────

w1,w2,w3,l1,l2 = (int(i) for i in input().split())

if ((w1 <= l2 and w2 +w3 <= l1) or(w2 <= l2 and w1 +w3 <= l1)or (w3 <= l2 and w1 +w2 <= l1)):
    print('Yes')
else:
    print('No')
