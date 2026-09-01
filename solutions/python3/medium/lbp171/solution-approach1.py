# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp171/problem?isFullScreen=true
# Problem     LBP171
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-01, 10:25 a.m.
# Technique   hash-set-membership-check
# Time        O(K)
# Space       O(K)
# Insight     The program determines if an input string exists within a predefined list of language keywords using a membership operator.
# Interview   Before: "How would you check if a string is a reserved keyword?" After: "I would store the keywords in a set or list and perform an O(K) lookup, where K is the number of keywords, ensuring the input matches exactly."
# Pitfalls    (1) Failing to account for case sensitivity, as the problem implies exact string matching.  (2) Assuming the input might contain whitespace, which would cause the membership check to fail against the keyword list.
# ──────────────────────────────────────────────────

L= [
    "break",'case','continue','default','defer','else','for','func','goto','if','map','range','return','struct','type','var'
]
s= input()
print('true' if s in L else 'false')
