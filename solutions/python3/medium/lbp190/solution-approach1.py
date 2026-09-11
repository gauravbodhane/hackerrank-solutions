# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp190/problem?isFullScreen=true
# Problem     LBP190
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-11, 05:38 p.m.
# ──────────────────────────────────────────────────

n = input()

digit = list(n) 
digit.sort()

for i in range(len(digit)-1):
    if int(digit[i+1]) - int(digit[i])> 2:
        print('No')
        break
else:
    print('Yes')
