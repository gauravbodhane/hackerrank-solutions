# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp194/problem?isFullScreen=true
# Problem     LBP194
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-13, 12:56 p.m.
# ──────────────────────────────────────────────────

n = input() 
result = ''
for ch in n:
    if 'a'<=ch<='z':
        result+= chr(ord(ch)-32)
    elif 'A'<=ch<='Z':
        result+= chr(ord(ch)+ 32)
    else:
        result += ch
print(result)
