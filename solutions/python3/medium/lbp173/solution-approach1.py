# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp173/problem?isFullScreen=true
# Problem     LBP173
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-02, 08:11 a.m.
# Technique   base-conversion-builtin
# Time        O(N)
# Space       O(N)
# Insight     The implementation leverages the built-in integer conversion function to interpret the input string as a base-17 number.
# Interview   Before: "How would you convert a custom base-17 string to decimal?" After: "I would use the built-in int function with a radix argument, which runs in O(N) time where N is the number of digits, handling the base-17 mapping automatically."
# Pitfalls    (1) The input string must only contain valid base-17 characters (0-9, A-G) or the int function will raise a ValueError.  (2) The problem constraints limit the input to a maximum of four digits, which this implementation handles implicitly.
# ──────────────────────────────────────────────────


print(int(input(),17))
