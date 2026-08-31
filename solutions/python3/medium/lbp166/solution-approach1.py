# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp166/problem?isFullScreen=true
# Problem     LBP166
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-31, 02:05 p.m.
# Technique   row-wise-maximum-scan
# Time        O(N * M)
# Space       O(M)
# Insight     The algorithm processes each of the N product rows independently to identify and print the maximum value within each day's M-length record.
# Interview   Before: "How would you find the maximum revenue per day given a matrix of N products and M days?" After: "I iterate through each of the N rows, calculating the maximum of the M elements in O(N * M) time, ensuring each day's peak revenue is identified efficiently."
# Pitfalls    (1) The code assumes the input structure provides N rows of M integers, which may fail if the input format deviates from the expected N by M matrix.  (2) Using print with end=' ' may leave a trailing space, which might be rejected by strict output format checkers.
# ──────────────────────────────────────────────────

n,m = (int(i) for i in input().split())
for i in range(n):
    l=[int(i) for i in input().split()]
    print(max(l),end=' ')
    
