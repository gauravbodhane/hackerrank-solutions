# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp157/problem?isFullScreen=true
# Problem     LBP157
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-29, 09:02 a.m.
# Technique   string-conversion-membership-check
# Time        O(N * D)
# Space       O(N)
# Insight     The algorithm iterates through the list, converting each integer to a string to check for the presence of the character '7' as a substring.
# Interview   Before: "How would you detect if a specific digit exists within any number in an array?" After: "I convert each integer to a string and check for the character '7'. This approach runs in O(N * D) time, where N is the array size and D is the maximum number of digits."
# Pitfalls    (1) Converting integers to strings is necessary because the 'in' operator on integers checks for value equality rather than digit presence.  (2) The logic fails if the input array is empty, though the problem constraints imply valid input.
# ──────────────────────────────────────────────────

n = int(input())
L = [int(i) for i in input().split()]
flag=False
for i in L:
    if '7' in str(i) :
        flag=True
        break
print('Boom!' if flag else 'there is no 7 in the array')
