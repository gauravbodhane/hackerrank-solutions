# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp198/problem?isFullScreen=true
# Problem     LBP198
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-13, 01:34 p.m.
# Technique   digit-extraction-reverse-processing
# Time        O(d)
# Space       O(1)
# Insight     The algorithm processes digits in reverse order by repeatedly extracting the last digit using modulo and integer division until the number is exhausted.
# Interview   Before: "How would you transform each digit of an integer based on its parity?" After: "I would extract digits from right to left using modulo 10, apply the parity rules, and print them, resulting in O(d) time complexity where d is the number of digits."
# Pitfalls    (1) Reversing the input string before processing causes the output to be printed in the original order, which may be unexpected if the logic required a different sequence.  (2) The use of end='' in the print function prevents newline characters, which might fail if the problem expects a specific output format per line.
# ──────────────────────────────────────────────────

n = int(input()[::-1])
while n!= 0:
    d = n% 10
    if d% 2 ==0:
        print(d+1,end='')
    else:
        print(d-1,end='')
    n = n//10
