# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp263/problem?isFullScreen=true
# Problem     LBP263
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-17, 01:51 p.m.
# Technique   string-indexing-with-bounds-check
# Time        O(1)
# Space       O(N)
# Insight     The code converts the input number to a string and accesses the character at the index corresponding to the one-based position k minus one, returning -1 if the index is out of bounds.
# Interview   Before: "I would iterate through the digits to find the kth one." After: "Converting the number to a string allows O(1) access to the kth digit, provided the index is within the string length, resulting in O(N) space complexity for the string representation."
# Pitfalls    (1) The code uses s < len(n) as the condition, which incorrectly returns -1 when s equals the length of the string.  (2) The implementation fails to handle cases where the input number is negative, as the minus sign would be treated as a character.
# ──────────────────────────────────────────────────

n = input() 
s = int(input())
print(n[s-1] if s<len(n) else '-1')    
