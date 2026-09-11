# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp190/problem?isFullScreen=true
# Problem     LBP190
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-11, 05:38 p.m.
# Technique   sorting-and-linear-scan
# Time        O(D log D) where D is the number of dig…
# Space       O(D)
# Insight     The algorithm sorts the ticket digits in ascending order and verifies that the absolute difference between every pair of adjacent sorted digits does not exceed two.
# Interview   Before: "How would you validate the ticket condition?" After: "I sort the digits in O(D log D) time and perform a linear scan to check if adjacent differences are at most two, ensuring O(D) space for the digit list."
# Pitfalls    (1) Failing to sort the digits first, as the problem explicitly requires checking the difference between adjacent digits in the sorted sequence.  (2) Incorrectly assuming the input is already sorted, which would lead to false negatives for unsorted ticket numbers.  (3) Misinterpreting the condition 'not more than 2' as strictly less than 2, whereas the problem allows a difference of exactly 2.
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
