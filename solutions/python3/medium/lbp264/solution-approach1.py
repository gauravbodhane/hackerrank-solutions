# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp264/problem?isFullScreen=true
# Problem     LBP264
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-17, 02:01 p.m.
# Technique   modular-exponentiation-via-built-in
# Time        O(log m)
# Space       O(1)
# Insight     The last digit of a power is equivalent to the result of the base raised to the exponent modulo ten.
# Interview   Before: "I would use a loop to multiply the base b times." After: "Using the built-in exponentiation operator with modulo is more efficient, achieving O(log m) time complexity while correctly handling large exponents."
# Pitfalls    (1) The solution assumes the input base and exponent are non-negative integers as implied by the problem context.  (2) Large exponents may cause memory issues if calculated fully before applying the modulo operator in languages without arbitrary-precision integers.
# ──────────────────────────────────────────────────

n , m = (int(i) for i in input().split())
print((n**m)%10)
