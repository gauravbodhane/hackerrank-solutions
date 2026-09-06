# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp178/problem?isFullScreen=true
# Problem     LBP178
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-06, 03:31 p.m.
# Technique   brute-force-permutation-check
# Time        O(1)
# Space       O(1)
# Insight     The algorithm determines if any of the three luggage items can serve as the single cabin bag while the remaining two fit within the check-in weight limit.
# Interview   Before: "How do you verify if three items fit into two distinct capacity constraints?" After: "By checking all three permutations of assigning one item to the cabin limit and two to the check-in limit, we achieve O(1) time and space complexity."
# Pitfalls    (1) Failing to account for all three possible assignments of luggage to the cabin bag.  (2) Assuming the order of input weights corresponds to a fixed assignment of cabin versus check-in bags.
# ──────────────────────────────────────────────────

w1,w2,w3,l1,l2 = (int(i) for i in input().split())

if ((w1 <= l2 and w2 +w3 <= l1) or(w2 <= l2 and w1 +w3 <= l1)or (w3 <= l2 and w1 +w2 <= l1)):
    print('Yes')
else:
    print('No')
