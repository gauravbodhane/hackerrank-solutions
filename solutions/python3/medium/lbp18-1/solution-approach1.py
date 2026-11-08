# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/lbp6222/challenges/lbp18-1/problem?isFullScreen=true
# Problem     LBP18 1
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-11-08, 03:35 p.m.
# ──────────────────────────────────────────────────

def birthdaycheck(month,day):
    if month == 'july' and day == 5:
        return 1
    else:
        return 0 
    
month= input() 
day  = int(input()) 

print(birthdaycheck(month,day))
