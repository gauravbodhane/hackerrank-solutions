# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp179/problem?isFullScreen=true
# Problem     LBP179
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-07, 08:24 a.m.
# Technique   sorting-and-interleaving-lists
# Time        O(N log N)
# Space       O(N)
# Insight     The implementation separates elements into sorted even and odd lists, then interleaves them by iterating up to the input size n to ensure all elements are included in the final result.
# Interview   Before: "How would you rearrange an array to alternate even and odd numbers in increasing order?" After: "I sorted the even and odd numbers separately and interleaved them, resulting in O(N log N) time complexity, which handles the alternating requirement efficiently for any input size n."
# Pitfalls    (1) Failing to handle cases where the count of even and odd numbers is unequal, which the loop bounds correctly manage by checking list lengths.  (2) Assuming the input array is already sorted, which would lead to incorrect interleaving since the problem requires increasing order.
# ──────────────────────────────────────────────────

n = int(input())
L = [int(i) for i in input().split()]
even = sorted([i for i in L if i % 2 == 0])
odd = sorted([i for i in L if i % 2 != 0])

result = []

for i in range(n):
    if i < len(even):
        result.append(even[i])
    if i < len(odd):
        result.append(odd[i])
        
print(*result)
