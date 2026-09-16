# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp259/problem?isFullScreen=true
# Problem     LBP259
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-16, 01:44 p.m.
# ──────────────────────────────────────────────────

n = input()
for i in n :
    if i in 'aeiou':
        print(i,end='')
    else:
        ch = i
        if ch == 'z':
            ch = 'a'
        ch = chr(ord(ch)+1)
        if ch in 'aeiou':
            print(chr(ord(ch)+1),end='')
        else:
            print(ch,end='')
