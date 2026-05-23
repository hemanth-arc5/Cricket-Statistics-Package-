from cricketstats import *
 
print("\n=== USING INSTALLED PACKAGE ===")

print("\nBATTING")
print("Batting Average:", batting_average(7000, 150))
print("Strike Rate:", strike_rate(100, 70))
print("Highest Score:", highest_score([55, 88, 145, 67]))

print("\nBOWLING")
print("Economy Rate:", economy_rate(55, 10))
print("Bowling Average:", bowling_average(300, 18))
print("Best Figures:", best_figures([(2, 30), (6, 25), (5, 18)]))

print("\nTEAM")
print("Players:", show_players())
print("Team Score:", team_score([100, 110, 90, 75]))