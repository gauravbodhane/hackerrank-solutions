# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp252/problem?isFullScreen=true
# Problem     LBP252	
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-09-15, 12:48 p.m.
# ──────────────────────────────────────────────────

n = int(input())
if n >= 30 and n<= 100:
    if n>= 30 and n<= 50:
        print('D')
    elif n>= 51 and n<= 60:
        print('C')
    elif n>= 61 and n<= 80:
        print('B')
    elif n>= 81 and n<= 100:
        print('A') 
    
else:
    print('invalide')
