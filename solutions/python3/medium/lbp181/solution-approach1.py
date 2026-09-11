# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp181/problem?isFullScreen=true
# Problem     LBP181
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-11, 10:41 a.m.
# Technique   frequency-count-linear-scan
# Time        O(N^2)
# Space       O(1)
# Insight     The algorithm iterates through the string and increments a counter whenever a character appears exactly once, terminating and printing the character when the counter reaches two.
# Interview   Before: "How would you find the second unique character?" After: "I would use a frequency map to achieve O(N) time, whereas this O(N^2) approach uses string count repeatedly, which is inefficient for large strings."
# Pitfalls    (1) The use of string.count() inside a loop results in O(N^2) time complexity, which may cause a timeout on large input strings.  (2) The code fails to produce any output if the string contains fewer than two non-repeating characters.
# ──────────────────────────────────────────────────

n = input()

c = 0
for i in n :
    if n.count(i)==1:
        c =c+1
    if c == 2:
        print(i)
        break
