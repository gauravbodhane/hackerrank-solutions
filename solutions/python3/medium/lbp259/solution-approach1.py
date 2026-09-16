# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp259/problem?isFullScreen=true
# Problem     LBP259
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-16, 01:44 p.m.
# Technique   character-mapping-iteration
# Time        O(N)
# Space       O(1)
# Insight     The algorithm iterates through each character, preserving vowels while mapping consonants to the next immediate consonant in the alphabet, with 'z' wrapping to 'b'.
# Interview   Before: "How do you handle the consonant shift logic?" After: "I iterate through the string in O(N) time, checking if a character is a vowel or consonant. If it is a consonant, I increment the character code and skip any resulting vowels to ensure the next consonant is selected."
# Pitfalls    (1) Failing to account for the 'z' to 'b' wrap-around case explicitly before incrementing the character code.  (2) Incorrectly identifying vowels when the incremented character lands on a vowel, requiring a secondary skip to reach the next consonant.
# ──────────────────────────────────────────────────

n = input()
for i in n :
    if i in 'aeiou':
        print(i,end='')
    else:
        ch = i
        if ch == 'z':
            ch = 'a'
        ch = chr(ord(ch)+1)
        if ch in 'aeiou':
            print(chr(ord(ch)+1),end='')
        else:
            print(ch,end='')
