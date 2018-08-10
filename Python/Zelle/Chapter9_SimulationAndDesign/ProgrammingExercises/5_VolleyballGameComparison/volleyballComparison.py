# volleyballComparison.py
# A program that compares two scoring systems of a volleyball game.
"""Design and implement a system that compares regular volleyball games to 
those using rally scoring. Your program should be able to investigate whether
rally scoring magnifies, reduces, or has no effect on the relative advantage
enjoyed by the better team."""

from random import random
import volleyball
import volleyballRallyScoring

def main():
	
    printIntro()
    probA, probB, n = getInputs()
    # Get the number of games won by rally scoring.
    winsARally, winsBRally = volleyballRallyScoring.simNGames(n, probA, probB)
    # Get the number of games won by traditional scoring.
    winsATrad, winsBTrad = volleyball.simNGames(n, probA, probB)
    printSummary(winsARally, winsBRally, winsATrad, winsBTrad, n)

def printIntro():
	
    print("This program simulates a game of volleyball between two \
teams called 'A' and 'B'. The abilities of each team is indicated by a \
probability (a number betweeen 0 and 1) that the team wins the point when \
serving. Team A always has the first serve.")

def getInputs():
	# Returns the three simulation parameters.
    a = b = 0
    while a + b != 1:
        print("Team A and Team B probability of winning added together \
must equal 1.")
        while True:
            try:
                a = float(input("What is the probability Team A \
                wins a serve? "))
            except (SyntaxError, NameError, TypeError, ValueError):
                print("You have to enter a decimal between 0 and 1.")
                continue
            if a > 1 or a < 0:
                print("You have to enter a decimal between 0 and 1.")
                continue
            else: break

        while True:
            try:
                b = float(input("What is the probability Team B \
                wins a serve? "))
            except (SyntaxError, NameError, TypeError, ValueError):
                print("You have to enter a decimal between 0 and 1.")
                continue
            if a > 1 or a < 0:
                print("You have to enter a decimal between 0 and 1.")
                continue
            else: break

    n = 0
    while n < 1:
        try:
            n = int(input("How many games to simulate? "))
        except (SyntaxError, NameError, TypeError, ValueError):
            print("You have to enter a whole number.")
            continue
        if n < 1:
            print("You have to simulate at least one game.")
            continue
    return a, b, n

def simNGames(n, probA, probB):
# Simulates n games of racquetball between players whos
# 	abilities are represented by the probability of winning a serve.
# Returns number of wins for A and B

    winsA = winsB = 0

    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def simOneGame(probA, probB):
    # Simulates a single game of volleyball between teams whose
    # 	abilities are represented by the probability of winning a serve.
    # Returns final scores for teams A and B

    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"           
    return scoreA, scoreB

def gameOver(a, b):
    # a and b represent scores for a volleyball game
    # Returns True if the game is over, otherwise False.
    if a >= 15 and a > b + 2:
        return True
    elif b >= 15 and b > a + 2:
        return True
    else:
        return False
	
def printSummary(winsARally, winsBRally, winsATrad, winsBTrad, n):
    # Prints a summary of wins by game type

    print("\nGames simulated:", n)
    print("Rally scoring wins for team A: {0} ({1:0.1%})"\
    .format(winsARally, winsARally/n))
    print("Traditional scoring wins for team A: {0} ({1:0.1%})"\
    .format(winsATrad, winsATrad/n))
    print("\nRally scoring wins for team B: {0} ({1:0.1%})"\
    .format(winsBRally, winsBRally/n))
    print("Traditional scoring wins for team B: {0} ({1:0.1%})"\
    .format(winsBTrad, winsBTrad/n))
	
if __name__ == '__main__': main()
