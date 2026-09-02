# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp174/problem?isFullScreen=true
# Problem     LBP174
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 08:17 a.m.
# Technique   character-to-integer-mapping
# Time        O(N)
# Space       O(1)
# Insight     The algorithm iterates through each character of the input string and calculates its numeric value by subtracting the ASCII code of 'a' from the character's ASCII code.
# Interview   Before: "How would you convert a string of characters 'a-j' into their corresponding numeric digits '0-9'?" After: "I would iterate through the string and map each character to its integer equivalent using ASCII offsets, resulting in an O(N) time complexity where N is the length of the input string."
# Pitfalls    (1) The code assumes the input string only contains characters within the 'a-j' range as specified by the problem.  (2) The use of end='' in the print function prevents newline characters between digits, which may not be desired if the output format requires specific spacing.
# ──────────────────────────────────────────────────

n = input( )
for ch in n:
    print(ord(ch)- ord('a'),end='')
    
