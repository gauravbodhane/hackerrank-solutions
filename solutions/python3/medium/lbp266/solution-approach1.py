# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp266/problem?isFullScreen=true
# Problem     LBP266
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-17, 02:12 p.m.
# Technique   regex-fullmatch-validation
# Time        O(N)
# Space       O(1)
# Insight     The implementation validates the string against a regular expression pattern that enforces the starting character constraint and the allowed character set for the entire string.
# Interview   Before: "How would you validate a variable name?" After: "I used a regex pattern to ensure the string starts with a letter or underscore and contains only alphanumeric characters or underscores, achieving O(N) time complexity for a string of length N."
# Pitfalls    (1) The regex pattern [a-zA-Z_][a-zA-Z0-9_]+ requires at least two characters, failing single-character valid variable names like 'a'.  (2) The regex pattern does not account for empty strings, which are implicitly rejected by the + quantifier.
# ──────────────────────────────────────────────────

import re
n = input()
print('true'if re.fullmatch('[a-zA-Z_][a-zA-Z0-9_]+',n) else 'false')
