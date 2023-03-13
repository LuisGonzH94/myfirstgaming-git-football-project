#Started all over again because I did not want to copy and paste from other coders that create the battleship game. 
#Although, I am doing some research since there are some functions I need to keep practicing. 
#However, this file is not a battleship game; it is a football game where the user will need to find the hidden players('O') and score. 
#Rules: a) Find the 5 players. b) If one player is found, then the user can shoot to goal. Else, user can try finding another player until getting 5.
#c) Turns will vary depending on how fast the user find the hidden players. One player found, one extra turn to shoot to goal.
#d) Last, The higher goals, the better chance to beat the game. Choices will be on for user to decide. Get goals, or find all players first. 

import random
#Created a board 1x6 that goes through A-F
print(" |A|B|C|D|E|F|")

for x in range(1, 7):
    row = ""
    for y in range(6):
        col = "_|"
        row = row + col
    print(x, row)

#Goal setup, using random.choice
goal_t = "T"
goal_u = "Y"
ran_goal = random.choice([goal_t, goal_u])

shoot = "Y"
for goal in ran_goal:
    r1 = ran_goal 
    print("7","---", r1, "-----")   
points = 0
if shoot == r1:
    print("GOAL!, You score 1 point")
    points += 1
else:
    print("It's a miss")
    points -= 0
    
print("Your current points: ", points) 
    

