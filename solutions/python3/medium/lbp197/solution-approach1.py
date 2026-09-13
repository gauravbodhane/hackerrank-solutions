# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp197/problem?isFullScreen=true
# Problem     LBP197
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-13, 01:19 p.m.
# ──────────────────────────────────────────────────

s1 = input()
s2 = input()
s3 = []
s4 = []
for i in range(len(s1)-1):
    if s1[i] != '#' and s1[i+1] !='#':
        s3.append(s1[i])

for i in range(len(s2)-1):
    if s2[i] != '#' and s2[i+1] !='#':
        s4.append(s2[i])

print('1' if s3==s4 else '0')
