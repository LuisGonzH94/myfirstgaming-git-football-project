import random

# letter 'x' will represent miss and letter 'o' will represent hit on token, and big 'G' will represent 'GOAL'!
#if 'o', then the player will either choose to find the goal by guessing from A to B on axis zero.
#Or player can choose to find another token. The faster the player find tokens, the higher chance to find the goal. 

hidden_dots = [[" "]*7 for x in range(7)]
visible_dots = [[" "]*6 for x in range(6)]

# 'G' for GOAL and 'M' for Miss(Redo)
#random.choice will be used to display goal as a 'G' or 'M'
g_m_goals = [["G"], ["M"]]
ran_c = random.choice(g_m_goals)

letter_to_num = {" ": 0, "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6}

#Created a function to display the football board.
#Noted %d and %s, which is for number and string. 
def display_board(board):
    print("   A| B | C | D | E | F")
    print("       ", ran_c)
    row_num = 1
    for row in board:
        print("%d|%s" %(row_num, "_|_".join(row)))
        row_num += 1
    return "Keep moving forward"
print(display_board(visible_dots))
