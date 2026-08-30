# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp161/problem?isFullScreen=true
# Problem     LBP161
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-30, 12:08 p.m.
# ──────────────────────────────────────────────────

n1 = int(input())
l1 = [int(i) for i in input().split()]
n2 = int(input())
l2 = [int(i) for i in input().split()]
l3 = l1 +l2
l3.sort()
c = 0
for i in range(0,(n1+n2)-1):
    if l3[i]+1 ==l3[i+1]:
        c=c+1
print(str(c==(n1+n2)-1).lower())
        
