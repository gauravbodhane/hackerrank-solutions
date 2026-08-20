# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp152/problem?isFullScreen=true
# Problem     LBP152
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-20, 10:28 p.m.
# Technique   list-partitioning-by-parity
# Time        O(N)
# Space       O(N)
# Insight     The algorithm partitions the input list into two separate lists based on parity and concatenates them to ensure all even numbers precede all odd numbers.
# Interview   Before: "How would you reorder an array to group evens before odds?" After: "I would iterate through the list once, collecting evens and odds into separate buffers, then concatenate them. This approach achieves O(N) time and O(N) space complexity, handling the N size constraint efficiently."
# Pitfalls    (1) Failing to handle the input format where the first integer is the array size and the subsequent integers are the array elements.  (2) Assuming the relative order of elements within the even or odd groups must be sorted, which is not required by the problem statement.
# ──────────────────────────────────────────────────

n = int(input())
l = [int(i) for i in input().split()]
even = []
odd = []
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)   
a = even + odd
print(*a)
