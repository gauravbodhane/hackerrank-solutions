# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp259/problem?isFullScreen=true
# Problem     LBP259
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-16, 01:36 p.m.
# Technique   character-mapping-iteration
# Time        O(N)
# Space       O(1)
# Insight     The algorithm iterates through each character, preserving vowels while mapping consonants to the next immediate consonant in the alphabet, with 'z' wrapping to 'b'.
# Interview   Before: "How would you transform characters based on vowel/consonant status?" After: "I iterate through the string in O(N) time, checking if each character is a vowel to retain it or shifting consonants to the next valid consonant, handling the 'z' to 'b' wrap-around case."
# Pitfalls    (1) The logic fails to correctly handle the 'z' to 'b' transition because the code increments 'z' to '{' before the vowel check.  (2) The implementation incorrectly treats 'a' as a consonant after the 'z' to 'a' assignment, leading to an incorrect shift to 'b' instead of the next consonant.
# ──────────────────────────────────────────────────

n = input()
for i  in n:
    if i in 'aeiou':
        print(i , end='')
    else:
        ch = i  
        if ch =='z':

            ch ='a' 
        ch = chr(ord(ch)+1)
        if ch in 'aeiou':
            print(chr(ord(ch)+1),end='')
        else:
            print(ch,end='')
