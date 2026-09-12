# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp191/problem?isFullScreen=true
# Problem     LBP191
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-12, 12:10 p.m.
# Technique   iterative-digit-sum-reduction
# Time        O(log N)
# Space       O(1)
# Insight     The algorithm repeatedly computes the sum of digits of the application ID until the result falls within the range [1, 26], mapping the final value to its corresponding uppercase letter.
# Interview   Before: "How do I map a numeric ID to a letter set?" After: "I iteratively sum the digits until the value is between 1 and 26, then use ASCII conversion. This runs in O(log N) time, where N is the application ID, as the sum of digits decreases logarithmically."
# Pitfalls    (1) Failing to handle cases where the initial sum of digits exceeds 26, requiring multiple iterations.  (2) Incorrectly mapping the numeric range 1-26 to ASCII characters by using the wrong offset for 'A'.
# ──────────────────────────────────────────────────

def sum(n):
    sum=0
    while n!= 0:
        d = n% 10 
        sum = sum +d
        n = n// 10
    return sum

n = int(input())
while True:
    if n>=1 and n <= 26:
        print(chr(n+64))
        break
    else:
        n = sum(n)
        
