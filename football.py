import random

#Attributes to implement that will display our board.
hidden_bishops=[[" "]*7 for x in range(6)]
guess_pattern=[[" "]*7 for x in range(6)]

#Created a Dict to keep track of the values for our Keys (in this case letter).
letter_to_num = {" ": 0, "A":1,"B":2, "C":3,"D":4,"E":5,"F":6}

#Created a board that will display letter as colum and number as row, and the goal at the bottom. 
#'R' == the Rook
#%d and %s are used to print a number along with a string together. 
def print_board(board):
    print(" "*3, "|A|B|C|D|E|F|")
    row_num = 1
    for row in board:
        print("%d|>%s| <0" % (row_num, "|".join(row)))
        row_num +=1
    print("  >>>>>|_R_|<<<<<<")
  
def get_bishops_location():
    #Enter the row number between 1 to 6
    row = input("Please enter a row number: 1-6 ")
    while row not in "123456":
        print("Please enter a valid row number ")
        row = input("Please enter a row number 1-6 ")
    #Enter the column letter from A TO F
    column = input("Please enter a valid column letter: A-F ").upper()
    while column not in letter_to_num:
        print("Please enter a valid column letter ")
        column = input("Please enter a valid column letter: A-F ")
    return int(row)-1,letter_to_num[column]

# #Function that spawn bishop spots
def create_bishops(board):
    for bishop in range(7):
        bishop_r, bishop_cl = random.randint(1, 5), random.randint(1, 5)
        while board[bishop_r][bishop_cl] == "b":
            bishop_r, bishop_cl = random.randint(1, 5), random.randint(1, 5)
        board[bishop_r][bishop_cl] = "b"

#method to track turns
def count_found_bishops(board):
    count = 0
    for row in board:
        for column in row:
            if column == "b":
                count += 1
    return count

create_bishops(hidden_bishops)
turns = 21
goal_num = "137"
#Track the total of goals a player can make when finding a bishop at a time
score = 0
total_goals = []
print("Welcome to Football the 'Bishop' vs the 'Rook'")
while turns > 0:
    
    print_board(guess_pattern)
    row,column = get_bishops_location()
    lucky_goal_num = random.choice(goal_num)
    if guess_pattern[row][column] == "-":
        print(">> You already guessed that ")
    elif hidden_bishops[row][column] =='b':
        print(">> Great! You have found a bishop ")
        guess_pattern[row][column] = "b"

        guess_num = input("Enter a lucky number '1, 3 or 7' to score one goal ")
        if  guess_num == lucky_goal_num:
            print(">>|_o_| -> _|_GOAL_|_")
            print("**You got one extra turn** ")
            turns += 1
            score = 1
            total_goals.append(score)
        else:
            print(">>|_o_| -> _|_MISS_|_")
            print("The Rook is a brick wall" )
            turns -= 1
    else:
        print(">> Sorry,You missed")
        guess_pattern[row][column] = "-"
        turns -= 1                     

    if  count_found_bishops(guess_pattern) == 7:
        
        if  guess_num == lucky_goal_num:
            print("Congratulations you have found all Bishops ")
            print(">>|_o_| -> _|_GOAL_|_")
            print("You score a last minute goal ")
        else:
            print("Oops! you have found all Bishops; unfortunately...")
            print(">>|_o_| -> _|_MISS_|_")
            print("...you miss the last goal" )
        print(f"total goal: {sum(total_goals)}")
        break
    print(f" You have {turns} turns remaining ")
    
    if turns == 0:
        print("Game Over ")
        print(f"total goal: {sum(total_goals)}")
        break
