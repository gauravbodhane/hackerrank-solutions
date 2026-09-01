# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp172/problem?isFullScreen=true
# Problem     LBP172
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-01, 11:00 a.m.
# ──────────────────────────────────────────────────

n = input()
n = int(n[::-1])
L =[]
while n!= 0:
    L.append(n%10)
    n = n//10
index = 0
se = 0
so = 0
while index<len(L):
    if index%2==0:
        se = se + L[index]
    else :
        so = so + L[index]
    index = index + 1
print(so - se)
