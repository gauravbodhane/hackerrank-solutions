# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp1/problem?isFullScreen=true
# Problem     LBP001
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-19, 11:46 a.m.
# Technique   conditional-parity-check
# Time        O(1)
# Space       O(1)
# Insight     The program validates the input against the constraint n >= 0 before applying the modulo operator to determine parity.
# Interview   Before: "How would you classify an integer as even or odd?" After: "I check if the input is negative to handle the invalid case, then use the modulo operator for O(1) time complexity, ensuring the n >= 0 constraint is satisfied."
# Pitfalls    (1) Failing to handle the n < 0 constraint results in incorrect output for negative integers.  (2) Assuming all integers are valid without checking the n >= 0 constraint defined in the problem statement.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
print("invalid" if n <0 else ("even" if n%2==0 else "odd") )
