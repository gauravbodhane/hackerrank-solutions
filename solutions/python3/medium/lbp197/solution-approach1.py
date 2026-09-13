# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp197/problem?isFullScreen=true
# Problem     LBP197
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-13, 01:19 p.m.
# Technique   stack-simulation-via-lookahead
# Time        O(N+M)
# Space       O(N+M)
# Insight     The implementation constructs two lists by appending characters that are not followed by a backspace character, effectively ignoring the actual backspace logic defined in the problem.
# Interview   Before: "I will use a stack to process the backspaces." After: "Actually, the provided code uses a lookahead scan to filter characters, resulting in O(N+M) time and space complexity, though it fails to correctly simulate the backspace behavior described in the problem statement."
# Pitfalls    (1) The code fails to handle consecutive backspaces or backspaces at the end of the string because it only checks the immediate next character.  (2) The logic incorrectly ignores the actual removal of characters, as it only checks if the current and next characters are not '#'.  (3) The implementation does not account for the requirement that a backspace removes the previous character, instead treating '#' as a simple filter.
# ──────────────────────────────────────────────────

s1 = input()
s2 = input()
s3 = []
s4 = []
for i in range(len(s1)-1):
    if s1[i] != '#' and s1[i+1] !='#':
        s3.append(s1[i])

for i in range(len(s2)-1):
    if s2[i] != '#' and s2[i+1] !='#':
        s4.append(s2[i])

print('1' if s3==s4 else '0')
