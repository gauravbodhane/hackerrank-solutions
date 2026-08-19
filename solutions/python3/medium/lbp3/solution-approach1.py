# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/41dec30av2022/challenges/lbp3/problem?isFullScreen=true
# Problem     LBP003
# Difficulty  Medium
# Subdomain   N/A
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-08-19, 11:47 a.m.
# ──────────────────────────────────────────────────

# Enter your code here. Read input from STDIN. Print output to STDOUT
# import calendar as cl 
# print(cl.isleap(int(input())))

n = int(input())
if (n%4==0 and n%100!=0) or (n%400==0):
    print("True")
else:
    print("False")
        
