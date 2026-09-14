# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp215/problem?isFullScreen=true
# Problem     LBP215
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-14, 11:09 p.m.
# Technique   row-wise-max-extraction
# Time        O(N*M)
# Space       O(N*M)
# Insight     The program iterates through each row of a fixed 3x3 matrix and computes the maximum value using the built-in max function.
# Interview   Before: "How would you find the largest value in every row of a matrix?" After: "I would iterate through each row and apply the max function, resulting in O(N*M) time complexity for an N by M matrix."
# Pitfalls    (1) The code assumes exactly three lines of input, which will fail if the input matrix size deviates from the 3x3 requirement.  (2) Using input().split() without error handling will raise a ValueError if any row contains non-integer characters.
# ──────────────────────────────────────────────────

l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]
l3 = [int(i) for i in input().split()]

l = [l1,l2,l3]

for i in range(3):
    g = max(l[i])
    print(g)
