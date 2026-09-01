# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp172/problem?isFullScreen=true
# Problem     LBP172
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-01, 11:00 a.m.
# Technique   digit-reversal-and-parity-summation
# Time        O(D)
# Space       O(D)
# Insight     The code reverses the input number to map digits to zero-based indices, where even indices correspond to odd positions and odd indices correspond to even positions in the original number.
# Interview   Before: "How would you calculate the difference between sums of digits at odd and even positions?" After: "I reverse the number to store digits in a list, then iterate through indices to sum them by parity. This approach runs in O(D) time and space, where D is the number of digits."
# Pitfalls    (1) The code treats the first digit (index 0) as an even position, which may conflict with standard 1-based positional definitions.  (2) The logic fails for an input of 0 because the while loop condition n != 0 prevents the list from being populated.  (3) Reversing the number as a string and then converting to int removes leading zeros, which could affect positional parity if the input format implies fixed-length strings.
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
