# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp158/problem?isFullScreen=true
# Problem     LBP158
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-29, 09:20 a.m.
# Technique   linear-scan-sign-comparison
# Time        O(n)
# Space       O(n)
# Insight     The algorithm iterates through the array and sets a flag to false if any two adjacent elements share the same sign.
# Pitfalls    (1) The code treats zero as a non-positive number, which may cause unexpected results if the input contains zeros.  (2) The loop range(0, n-1) correctly avoids an index out of bounds error by stopping at the second-to-last element.
# ──────────────────────────────────────────────────

n = int(input())
L=[int(i) for i in input().split()]
flag = True
for i in range(0,n-1):
    if L[i] > 0 and L[i+1] > 0:
        flag = False
        break
    if L[i]<0 and L[i+1]<0:
        flag =False
        break
print(str(flag).lower())
