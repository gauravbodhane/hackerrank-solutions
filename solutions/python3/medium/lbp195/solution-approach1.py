# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp195/problem?isFullScreen=true
# Problem     LBP195
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-13, 01:01 p.m.
# Technique   conditional-range-mapping
# Time        O(1)
# Space       O(1)
# Insight     The code maps a single integer input to a specific rating category using nested conditional range checks.
# Interview   Before: "How would you categorize user points into ratings?" After: "I implemented a series of O(1) conditional checks to map the input points to their respective rating labels, ensuring all constraints from 30 to 100 are handled correctly."
# Pitfalls    (1) Failing to handle inputs outside the 30-100 range as specified in the problem constraints.  (2) Overlapping or missing integer values between the defined rating ranges.
# ──────────────────────────────────────────────────

n = int(input())
if n >= 30 and n <= 100:
    if n >= 30 and n<= 50:
        print('Average')
    elif n >= 51 and n <= 60:
        print('Good')
    elif n>= 61 and n <= 80:
        print('Excellent')
    elif n>= 81 and n <= 100:
        print('Outstanding')    
else:
    print('invalid')
