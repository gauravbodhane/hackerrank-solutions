# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp156/problem?isFullScreen=true
# Problem     LBP156
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-29, 08:43 a.m.
# Technique   direct-index-access
# Time        O(n)
# Space       O(n)
# Insight     The implementation iterates through the provided index array and prints the character at each specified position from the input string.
# Interview   Before: "How would you extract characters at specific indices from a string?" After: "I iterate through the index array and access the string directly, resulting in O(n) time complexity where n is the number of indices provided."
# Pitfalls    (1) The code assumes all indices in the array are within the valid bounds of the input string.  (2) The implementation does not convert the output to lowercase as required by the problem statement.  (3) The code fails if the input string contains spaces that are not accounted for by the index values.
# ──────────────────────────────────────────────────

s = input() 
n = int(input())
L = [int(i) for i in input().split()]
for i in range(n):
    print(s[L[i]],end='')
