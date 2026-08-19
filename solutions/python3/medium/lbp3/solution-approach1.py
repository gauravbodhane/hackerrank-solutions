# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp3/problem?isFullScreen=true
# Problem     LBP003
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-19, 11:47 a.m.
# Technique   boolean-logic-leap-year-check
# Time        O(1)
# Space       O(1)
# Insight     The code evaluates the leap year condition by checking if the year is divisible by four but not one hundred, or alternatively divisible by four hundred.
# Interview   Before: "How do you determine if a year is a leap year?" After: "I use a boolean expression to verify divisibility by 4 and 400, ensuring century years are handled correctly in O(1) time."
# Pitfalls    (1) Failing to prioritize the century year exception where years divisible by 100 must also be divisible by 400.  (2) Incorrectly using logical AND instead of OR when combining the century year condition with the standard leap year rule.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
# import calendar as cl 
# print(cl.isleap(int(input())))

n = int(input())
if (n%4==0 and n%100!=0) or (n%400==0):
    print("True")
else:
    print("False")
        
