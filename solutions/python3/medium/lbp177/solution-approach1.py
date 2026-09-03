# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp177/problem?isFullScreen=true
# Problem     LBP177
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-03, 06:11 p.m.
# Technique   isupper-isdigit-filter
# Time        O(N)
# Space       O(1)
# Insight     The program iterates through the input string and prints only characters that satisfy the condition of being either an uppercase letter or a digit.
# Interview   Before: "How do I extract the original message from the encrypted string?" After: "You can iterate through the string and filter for uppercase letters and digits, which runs in O(N) time and O(1) auxiliary space, effectively ignoring all lowercase letters and special characters."
# Pitfalls    (1) The code fails to handle empty input strings if the environment expects a specific output format for empty cases.  (2) The logic assumes the original message contains only uppercase letters and digits, ignoring potential whitespace characters that might be part of the original message.
# ──────────────────────────────────────────────────

n = input()

for ch in n:
    if ch.isupper() or ch.isdigit():
        print(ch,end='')
