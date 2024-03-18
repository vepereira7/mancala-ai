import time
import sys
import math

BOARD_SIZE = 14

STORE_1 = 6  # deposit position for player 1
STORE_2 = 13 # deposit position for player 2
WINNING_SCORE = 25
PITS_PER_PLAYER = 6

# Opposite positions on board
opposite = {
    0 : 12,
    1 : 11,
    2 : 10,
    3 : 9,
    4 : 8,
    5 : 7,
    7 : 5,
    8 : 4,
    9 : 3,
    10 : 2,
    11 : 1,
    12 : 0,
}



# Initiate the board for the given size
def init_board(size):
    board = [0] * size
    for i in range(size):
        if(i != STORE_1 and i != (STORE_2)):
            board[i] = 4
    return board

# Verifies if the board is in a final state, wich means the game is over
def game_over(board):
    count1 = 0
    count2 = 0
    for i in range(len(board)):
        if(i >= 0 and i < STORE_1):
            if(board[i] == 0):
                count1 += 1
        if(i > STORE_1 and i < STORE_2):
            if(board[i] == 0):
                count2 += 1

    if(count1 == 6):
        for i in range(7,13):
            board[STORE_2] += board[i]
        return True
    elif(count2 == 6):
        for i in range(0,STORE_1):
            board[STORE_1] += board[i]
        return True
    else:
        return False

# Return the winning player
def winning_player(board):
    if(board[STORE_1] > board[STORE_2]):
        return 1
    elif(board[STORE_1] < board[STORE_2]):
        return 2
    else:
        return 0    
    
# Parses the user input to use in the index board
def parse_input(inpt):
    if(inpt > 0 and inpt <= STORE_1):
        return inpt - 1
    elif(inpt > STORE_1 and inpt < STORE_2):
        return inpt
    else:
        return

# Handles the logic for the case of a player eats the seeds of the opponent
def eat_seeds(pos, player, board):
    global opposite

    if(player == 0):
        if(board[opposite[pos]] != 0):
            board[STORE_1] += (board[pos]+board[opposite[pos]])
            board[pos] = 0
            board[opposite[pos]] = 0

    if(player == 1):
        if(board[opposite[pos]] != 0):
            board[STORE_2] += (board[pos]+board[opposite[pos]])
            board[pos] = 0
            board[opposite[pos]] = 0


# Handles the logic for moving pieces in the board
def move_piece(pos, player, board):
    i = 0
    if(player == 0):
        hand = board[pos]
        board[pos] = 0
        i = pos+1
        while(hand > 0):
            if(i == STORE_2):
                i = 0
            if(hand == 1 and board[i] == 0 and (i >= 0 and i < STORE_1)):
                board[i] += 1
                eat_seeds(i, player, board)
                hand -= 1
            elif(hand == 1 and i == STORE_1):
                board[i] += 1
                return player
            else:
                board[i] += 1
                hand -= 1
                i += 1

    if(player == 1):
        hand = board[pos]
        board[pos] = 0
        i = pos+1
        while(hand > 0):
            if(i == STORE_1):
                i += 1
            if(i > STORE_2):
                i = 0
            if(hand == 1 and board[i] == 0 and (i > STORE_1 and i < STORE_2)):
                board[i] += 1
                eat_seeds(i, player, board)
                hand -= 1
            elif(hand == 1 and i == STORE_2):
                board[i] += 1
                return player
            else:
                board[i] += 1
                hand -= 1
                i += 1

    player += 1
    player = player % 2
    return player



# Verifies if the user input move is valid
def is_valid_move(pos, player, board):
    if(pos == None):
        print("INVALID INPUT!!")
        return False
    if(player == 0):
        if(pos < 0 or pos > 6):
            print("You must choose between 1 - 6")
            return False
        if(board[pos] == 0):
            print("Empty house, choose another!")
            return False

    elif(player == 1):
        if(pos < 7 or pos > 12):
            print("You must choose between 7 - 12")
            return False
        if(board[pos] == 0):
            print("Empty house, choose another!")
            return False
    
    return True


# Print to the screen the board
def print_board_cmd_line(board):
    print("\n------12----11----10----09----08----07-----")
    st = "|  |"
    i = 0
    j = 0
    w = len(board)-1
    while(w > 6):
        if(w != (len(board)-1)):  
            if(board[w] > 9):
                st += " |" + str(board[w]) + "| "
            else:
                st += " |0" + str(board[w]) + "| "
        w -= 1
   
    if(board[(len(board)-1)] > 9):
        st += "|  |\n|" + str(board[(len(board)-1)]) + "|"
    else:
        st += "|  |\n|0" + str(board[(len(board)-1)]) + "|"
    while(j < 6):
        st += "      "
        j += 1
    if(board[6] > 9):
        st += "|" + str(board[6]) + "|\n|  |"
    else:
        st += "|0" + str(board[6]) + "|\n|  |"

    while(i < 7):
        if(i != 6):
            if(board[i] > 9):
                st += " |" + str(board[i]) + "| "
            else:
                st += " |0" + str(board[i]) + "| "
        i += 1
    st += "|  |"
    print(st)
    print("------01----02----03----04----05----06-----\n")

