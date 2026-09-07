# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp179/problem?isFullScreen=true
# Problem     LBP179
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-07, 08:24 a.m.
# ──────────────────────────────────────────────────

n = int(input())
L = [int(i) for i in input().split()]
even = sorted([i for i in L if i % 2 == 0])
odd = sorted([i for i in L if i % 2 != 0])

result = []

for i in range(n):
    if i < len(even):
        result.append(even[i])
    if i < len(odd):
        result.append(odd[i])
        
print(*result)
