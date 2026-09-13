# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp196/problem?isFullScreen=true
# Problem     LBP196
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-13, 01:05 p.m.
# Technique   built-in-modular-exponentiation
# Time        O(log e)
# Space       O(1)
# Insight     The implementation utilizes Python's arbitrary-precision integer arithmetic to compute the modular exponentiation directly.
# Interview   Before: "How would you compute b raised to the power of e modulo m?" After: "I would use the built-in pow(b, e, m) function, which performs modular exponentiation in O(log e) time, ensuring efficiency even for very large exponents."
# Pitfalls    (1) Using the ** operator followed by % instead of the three-argument pow(b, e, m) function can lead to memory exhaustion for extremely large exponents.  (2) The code assumes positive integer inputs as per the problem statement and does not handle potential division by zero if m is zero.
# ──────────────────────────────────────────────────

b,e,m = (int(i) for i in input().split())

print(int(b**e%m))
