# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp213/problem?isFullScreen=true
# Problem     LBP213
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-21, 08:37 a.m.
# Technique   nested-loop-max-tracking
# Time        O(1)
# Space       O(1)
# Insight     The algorithm iterates through every element of the fixed 3x3 matrix to maintain a running maximum value.
# Interview   Before: "How would you find the largest value in a 3x3 grid?" After: "I iterate through all nine elements using nested loops, updating a tracker variable whenever a larger value is found, resulting in O(1) time and space complexity for this fixed-size input."
# Pitfalls    (1) Using a variable name like max that shadows the built-in Python max function.  (2) Assuming the input will always contain exactly nine integers across three lines as specified.
# ──────────────────────────────────────────────────

a = []
for i in range(3):
    a.append([int(i)for i in input().split()])
max = a[0][0]
for i in range(3):
    for j in range(3):
        if max<a[i][j]:
            max = a[i][j]
print(max)
