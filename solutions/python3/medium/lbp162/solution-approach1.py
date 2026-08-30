# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp162/problem?isFullScreen=true
# Problem     LBP162
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-30, 01:57 p.m.
# Technique   frequency-counting-linear-scan
# Time        O(N * D)
# Space       O(N)
# Insight     The algorithm tracks the maximum frequency of the digit five and updates the candidate number whenever a higher or equal frequency is encountered, defaulting to the first element if no fives exist.
# Interview   Before: "How do you find the luckiest number based on digit frequency?" After: "I iterate through the array, counting occurrences of '5' in each number. By updating the candidate on greater-than-or-equal counts, I ensure the last occurrence is selected in O(N * D) time, where D is the number of digits."
# Pitfalls    (1) The logic uses a non-strict inequality (c <= x) to ensure the last occurrence is selected, which might be misinterpreted as selecting the first occurrence.  (2) The condition sc == n correctly identifies the case where no fives exist, but relies on a counter that increments for every number without a five.  (3) The code assumes the input array is non-empty, which is consistent with the problem context but lacks an explicit check for empty input.
# ──────────────────────────────────────────────────

n = int(input())
l =[int(i) for i in input().split()]
c = 0
sc = 0
for i in l:
    x=str(i).count('5')
    if c <= x:
        c = x 
        element = i 
    if x == 0:
        sc = sc+1
if sc != n :
    print(element)
else:
    print(l[0])
        
