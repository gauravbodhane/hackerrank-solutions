# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp189/problem?isFullScreen=true
# Problem     LBP189
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-11, 05:26 p.m.
# ──────────────────────────────────────────────────

n = int(input())

original = n 
reverse = 0 
while n > 0:
    digit = n% 10 
    reverse = reverse * 10 + digit
    n = n // 10

diff = (reverse-original)
print(abs(diff))
