# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp2/problem?isFullScreen=true
# Problem     LBP002
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-19, 11:47 a.m.
# Technique   nested-conditional-logic
# Time        O(1)
# Space       O(1)
# Insight     The code evaluates the parity and range of the integer n to determine the output based on four distinct conditional branches.
# Interview   Before: "How would you classify an integer based on parity and range?" After: "I used nested if-else statements to check the parity and range constraints, resulting in O(1) time complexity, ensuring the solution handles the 1 to 100 range efficiently."
# Pitfalls    (1) Failing to account for the inclusive range boundaries 2, 5, 6, and 20 as specified in the problem.  (2) Incorrectly ordering the conditional checks, which could lead to overlapping logic for even numbers.  (3) Omitting the input validation check for the constraint 1 <= n <= 100.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
if n>=1 and n<=100:
    if n%2!=0:
        print("Weird")
    else:
        if n>=2 and n<=5:
            print("Not Weird")
        elif n>=6 and n<=20:
            print("Weird")
        else:
            print("Not Weird")
