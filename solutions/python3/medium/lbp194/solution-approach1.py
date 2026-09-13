# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp194/problem?isFullScreen=true
# Problem     LBP194
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-13, 12:56 p.m.
# Technique   character-case-inversion-scan
# Time        O(N)
# Space       O(N)
# Insight     The algorithm iterates through each character of the input string, applying a constant-time ASCII offset to toggle the case of alphabetic characters while preserving non-alphabetic characters.
# Interview   Before: "How would you swap the case of every character in a string?" After: "I iterate through the string and use ASCII arithmetic to flip the case of letters, resulting in O(N) time and O(N) space complexity for the new string."
# Pitfalls    (1) Assuming the input contains only alphabetic characters when the problem does not explicitly restrict non-alphabetic input.  (2) Failing to account for the ASCII difference of 32 between uppercase and lowercase letters.
# ──────────────────────────────────────────────────

n = input() 
result = ''
for ch in n:
    if 'a'<=ch<='z':
        result+= chr(ord(ch)-32)
    elif 'A'<=ch<='Z':
        result+= chr(ord(ch)+ 32)
    else:
        result += ch
print(result)
