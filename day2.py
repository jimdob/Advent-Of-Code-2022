#Advent of Code 2022 Day 2 Solution

'''
Rock, Paper, Scissors

The winner of the whole tournament is the player with the highest score.
Your total score is the sum of your scores for each round. 
The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

A=Rock
B=Paper
C=Scissors

X=Rock
Y=Paper
Z=Scissors
'''


with open('day2input.txt') as f:

    stratGuide = [choice.split(' ') for choice in f.read().splitlines()]
    #print(stratGuide)

    #PART 1
    #Find the total score if everything goes exactly according to your strategy guide.

    def determineP1Score(x,y):
        if y == 'X': score=1
        if y == 'Y': score=2
        if y == 'Z': score=3

        match x,y:
            case 'A','X':   #rock vs rock
                score += 3
            case 'A','Y':   #rock vs paper
                score += 6  
            case 'A','Z':   #rock vs scissors
                score += 0  
            case 'B','X':   #paper vs rock
                score += 0  
            case 'B','Y':   #paper vs paper
                score += 3  
            case 'B','Z':   #paper vs scissors
                score += 6  
            case 'C','X':   #scissors vs rock
                score += 6  
            case 'C','Y':   #scissors vs paper
                score += 0  
            case 'C','Z':   #scissors vs scissors
                score += 3  
        return score
    
    p1Score = 0
    for game in stratGuide:
        x = game[0]
        y = game[1]
        p1Score += determineP1Score(x,y)
    print('The total score for part 1 is:',p1Score)


    #PART 2

    def determineP2Score(x,y):
        #Based on second column. Indicates loss, draw, or win (x, y, z respectively)
        if y == 'X': score=0
        if y == 'Y': score=3
        if y == 'Z': score=6

        match x,y:
            case 'A','X':   #lose vs rock
                score += 3
            case 'A','Y':   #draw vs rock
                score += 1  
            case 'A','Z':   #win vs rock
                score += 2  
            case 'B','X':   #lose vs paper
                score += 1  
            case 'B','Y':   #draw vs paper
                score += 2  
            case 'B','Z':   #win vs paper
                score += 3  
            case 'C','X':   #lose vs scissors
                score += 2  
            case 'C','Y':   #draw vs scissors
                score += 3  
            case 'C','Z':   #win vs scissors
                score += 1  
        return score
    
    p2Score = 0
    for game2 in stratGuide:
        x = game2[0]
        y = game2[1]
        p2Score += determineP2Score(x,y)
    print('The total score for part 2 is:',p2Score)
