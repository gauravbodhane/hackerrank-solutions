# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp252/problem?isFullScreen=true
# Problem     LBP252	
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-15, 12:48 p.m.
# Technique   conditional-range-mapping
# Time        O(1)
# Space       O(1)
# Insight     The algorithm maps an integer input to a specific character grade based on defined inclusive range boundaries.
# Interview   Before: "How would you categorize a score into grades?" After: "I used a series of conditional checks to map the input to the correct grade in O(1) time, ensuring the input falls within the valid 30-100 range specified in the problem."
# Pitfalls    (1) The code prints 'invalide' for inputs outside the 30-100 range, which may not match expected behavior if the problem implies only valid inputs.  (2) The logic relies on hardcoded inclusive boundaries that do not account for potential gaps between ranges like 50 and 51.
# ──────────────────────────────────────────────────

n = int(input())
if n >= 30 and n<= 100:
    if n>= 30 and n<= 50:
        print('D')
    elif n>= 51 and n<= 60:
        print('C')
    elif n>= 61 and n<= 80:
        print('B')
    elif n>= 81 and n<= 100:
        print('A') 
    
else:
    print('invalide')
