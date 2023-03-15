#Started all over again because I did not want to copy and paste from other coders that create the battleship game. 
#Although, I am doing some research since there are some functions I need to keep practicing. 
#However, this file is not a battleship game; it is a football game where the user will need to find the hidden players('O') and score. 
#Rules: a) Find the 5 players. b) If one player is found, then the user can shoot to goal. Else, user can try finding another player until getting 5.
#c) Turns will vary depending on how fast the user find the hidden players. One player found, one extra turn to shoot to goal.
#d) Last, The higher goals, the better chance to beat the game. Choices will be on for user to decide. Get goals, or find all players first. 

from random import randint

hidden_bishops=[[" "]*7 for x in range(6)]
guess_pattern=[[" "]*7 for x in range(6)]

letter_to_num={" ": 0, "A":1,"B":2, "C":3,"D":4,"E":5,"F":6}

def print_board(board):
    print(" "*3, "|A|B|C|D|E|F|")
    net = "  >>>>>|_R_|<<<<<<"
    row_num= 1
    for row in board:
        print("%d|>%s|<" % (row_num, "|".join(row)))
        row_num +=1
    print(net)
  
def get_bishops_location():
    #Enter the row number between 1 to 6
    row=input('Please enter a row number: 1-6 ')
    while row not in '123456':
        print("Please enter a valid row number ")
        row=input('Please enter a ship row 1-6 ')
    #Enter the column letter from A TO F
    column=input("Please enter a column letter: A-F ").upper()
    while column not in letter_to_num:
        print("Please enter a valid column letter ")
        column=input("Please enter a ship column A-F ")
    return int(row)-1,letter_to_num[column]

# #Function that creates bishop spots
def create_ships(board):
    for bishop in range(5):
        bishop_r, bishop_cl= randint(1,5), randint(1,5)
        while board[bishop_r][bishop_cl] =='B':
            bishop_r, bishop_cl= randint(1,5), randint(1,5)
        board[bishop_r][bishop_cl] = 'B'

def count_hit_ships(board):
    count=0
    for row in board:
        for column in row:
            if column=='B':
                count+=1
    return count

create_ships(hidden_bishops)
turns = 50
goal = 0
score = 0
total_goals = [0]
print("Welcome to Football the 'Bishop' vs the 'Rool'")
while turns > 0:
    
    print_board(guess_pattern)
    row,column = get_bishops_location()
    goal = randint (1, 3)
    if guess_pattern[row][column] == '-':
        print(' You already guessed that ')
    elif hidden_bishops[row][column] =='B':
        print(' Congratulations you have found a bishop ')
        guess_pattern[row][column] = 'B'

        guess_num = input("Enter a number from 1 to 3 to score one goal ")
        while goal == 0:
         print("  >>>>>|_K_|<<<<<<")
        if  goal == 1:
            print("|__|" + "|_o_|")
            print("GOOOAAALLL! - You got one extra point ")
            turns += 1
            score += 1
            total_goals.append(score)
        else:
            print("|_K_|" + "|_x_|")
            print("You miss! The Rook is a brick wall" )
            turns -= 1
    else:
        print('Sorry,You missed')
        guess_pattern[row][column] = '-'
        turns -= 1                     

    if  count_hit_ships(guess_pattern) == 5:
        print("Congratulations you have found all Bishops ")
        if  goal == 1:
            print("|__|" + "|_o_|")
            print("GOOOAAALLL! - Last minute goal ")
        else:
            print("|_K_|" + "|_x_|")
            print("You miss last goal" )
        print(f"total goal: {sum(total_goals)}")
        break
    print(' You have ' +str(turns) + ' turns remaining ')

    if turns == 0:
        print('Game Over ')
        break