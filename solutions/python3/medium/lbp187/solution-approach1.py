# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp187/problem?isFullScreen=true
# Problem     LBP187
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-11, 05:06 p.m.
# Technique   negative-indexing-tuple-unpacking
# Time        O(1)
# Space       O(1)
# Insight     The implementation uses negative indexing to access the last two characters of the input string and prints them in reversed order separated by a comma.
# Interview   Before: "How would you extract and reorder the final two characters of a string?" After: "I used negative indexing to access the last two characters in O(1) time, ensuring the solution handles strings of length at least two as implied by the problem constraints."
# Pitfalls    (1) The code will raise an IndexError if the input string has a length of less than two.  (2) The implementation assumes the input string contains at least two characters as per the implicit problem constraints.
# ──────────────────────────────────────────────────

n = input()
g = (n[-1],n[-2])

print(*g,sep=",")
