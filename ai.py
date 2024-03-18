import sys
import time
import math
import random
import mancala
import random


# Random generator
def random_number_gen(board, player):
    valid_moves = available_positions(board, player)
    return random.choice(valid_moves)

# Available positions
def available_positions(board, player):
    if player == 0:
        pos_list = [i for i in range(mancala.STORE_1) if board[i] != 0]
    elif player == 1:
        pos_list = [i for i in range(mancala.STORE_1 + 1, mancala.STORE_2) if board[i] != 0]
    return pos_list


def utility_function(board, player):
    if mancala.winning_player(board) == 1:
        return (None, -100000000000000) if player else (None, 100000000000000)
    elif mancala.winning_player(board) == 2:
        return (None, 100000000000000) if player else (None, -100000000000000)
    else:
        return (None, 0)

# picks the best move based on the score calculated with the heuristic_2 function
def choose_best_pos(board, player):
    valid_locations = available_positions(board, player)
    best_score = -1000000
    best_pos = random.choice(valid_locations)
    for pos in valid_locations:
        # print("POS: " + str(pos))
        temp_board = board.copy()
        pl_temp = mancala.move_piece(pos, player, temp_board)
        score = fixed_heuristic( board, player)
        #use heuristic_2
        score = heuristic_2(temp_board, board, player)
        #score = heuristic(temp_board, player)
        # print("SCORE: " + str(score))
        # print("BEST SCORE: " + str(best_score))
        if(score > best_score):
            best_score = score
            best_pos = pos
    
    return best_pos, best_score

# return true if it is a terminal node and false if it is not
def terminal_node(board):
    return mancala.game_over(board)


######## HEURISTICS ###########

# evaluates how good is the move based in the number of seeds in the player deposit
def heuristic(board, player):
    return (board[mancala.STORE_2] - board[mancala.STORE_1]) if player else (board[mancala.STORE_1] - board[mancala.STORE_2])

# takes into account the change in the number of seeds in the player's store before and after the move, 
# as well as the difference in the number of seeds between the player's store and the opponent's store after the movement
def heuristic_2(board, old_board, player):
    score = 0
    store = mancala.STORE_1 if player == 1 else mancala.STORE_2

    if board[store] > old_board[store]:
        score += 12

    if board[store] > board[1 - store]:
        score += 10
    elif board[store] < board[1 - store]:
        score -= 8

    return score

def heuristic_3(board, old_board, player):
    score = 0
    opponent = (player + 1) % 2
    own_stones = sum(board[player * mancala.PITS_PER_PLAYER:(player + 1) * mancala.PITS_PER_PLAYER])
    opp_stones = sum(board[opponent * mancala.PITS_PER_PLAYER:(opponent + 1) * mancala.PITS_PER_PLAYER])

    # Check for multiple turns
    if board[mancala.STORE_1 if player == 0 else mancala.STORE_2] > old_board[mancala.STORE_1 if player == 0 else mancala.STORE_2]:
        score += 10 # bonus for getting an extra turn

    # Evaluate the score based on difference in number of stones in own storehouse and opponent's storehouse
    if player == 0:
        score += (board[mancala.STORE_1] - board[mancala.STORE_2]) * 3
    else:
        score += (board[mancala.STORE_2] - board[mancala.STORE_1]) * 3

    # Add a bonus for each pit that's empty on the player's side
    empty_pits = [i for i in range(player * mancala.PITS_PER_PLAYER, (player + 1) * mancala.PITS_PER_PLAYER) if board[i] == 0]
    score += len(empty_pits) * 5

    # Add a penalty for each pit that's empty on the opponent's side
    opp_empty_pits = [i for i in range(opponent * mancala.PITS_PER_PLAYER, (opponent + 1) * mancala.PITS_PER_PLAYER) if board[i] == 0]
    score -= len(opp_empty_pits) * 5

    # Add a bonus for the number of stones in the player's own side compared to the opponent's side
    if own_stones > opp_stones:
        score += 10

    return score

def heuristic_4(board, old_board, player):
    score = 0
    opponent = (player + 1) % 2
    own_store = board[mancala.STORE_1 if player == 0 else mancala.STORE_2]
    opp_store = board[mancala.STORE_1 if opponent == 0 else mancala.STORE_2]
    own_captured = board[mancala.STORE_2 if player == 0 else mancala.STORE_1] - old_board[mancala.STORE_2 if player == 0 else mancala.STORE_1]
    opp_captured = board[mancala.STORE_2 if opponent == 0 else mancala.STORE_1] - old_board[mancala.STORE_2 if opponent == 0 else mancala.STORE_1]
    # Evaluate the score based on the difference in the number of stones in the player's storehouse and opponent's storehouse
    score += (own_store - opp_store) * 2

    # Add a bonus for the number of stones captured
    score += own_captured * 5

    # Add a penalty for the number of stones captured by the opponent
    score -= opp_captured * 3

    return score

def heuristic_5(board, old_board, player):
    score = 0
    opponent = (player + 1) % 2

    # Count the number of stones on the player's side of the current board
    player_stones = sum(board[player * mancala.PITS_PER_PLAYER:(player + 1) * mancala.PITS_PER_PLAYER])

    # Count the number of stones on the opponent's side of the current board
    opponent_stones = sum(board[opponent * mancala.PITS_PER_PLAYER:(opponent + 1) * mancala.PITS_PER_PLAYER])

    # Count the number of stones on the player's side of the old board
    old_player_stones = sum(old_board[player * mancala.PITS_PER_PLAYER:(player + 1) * mancala.PITS_PER_PLAYER])

    # Count the number of stones on the opponent's side of the old board
    old_opponent_stones = sum(old_board[opponent * mancala.PITS_PER_PLAYER:(opponent + 1) * mancala.PITS_PER_PLAYER])

    # Compute the difference between the number of stones on the player's side in the current and old board
    player_stones_delta = player_stones - old_player_stones

    # Compute the difference between the number of stones on the opponent's side in the current and old board
    opponent_stones_delta = opponent_stones - old_opponent_stones

    # Evaluate the score based on the difference in the number of stones on the player's side and opponent's side
    score += (player_stones_delta - opponent_stones_delta)

    return score

def fixed_heuristic(board, player):
    """
    A simple heuristic that always returns the first legal move available
    """
    for i in range(len(board)):
        if board[i] > 0 and (player == 0 and i < len(board)//2) or (player == 1 and i >= len(board)//2 and i < len(board)-1):
            return i
    return None

################################

######## ALGORITHMS ##########

# minimax algorithm
def minimax(board, depth, maximizingPlayer, player):
    if depth == 0 or terminal_node(board):
        if terminal_node(board):
            return (None, utility_function(board, player)[1])
        else:
            #value = fixed_heuristic(board, player)
            value = heuristic(board, player)
            return(None, value)

    valid_locations = available_positions(board, player)
    if maximizingPlayer:
        best_pos = None
        value = -math.inf
        for pos in valid_locations:
            b_copy = board.copy()
            player_tmp = mancala.move_piece(pos, player, b_copy)
            new_score = minimax(b_copy, depth-1, player_tmp == player, player)[1]
            if new_score > value:
                value = new_score
                best_pos = pos
        return (best_pos, value)
    else:
        best_pos = None
        value = math.inf
        for pos in valid_locations:
            b_copy = board.copy()
            player_tmp = mancala.move_piece(pos, player, b_copy)
            new_score = minimax(b_copy, depth-1, player_tmp != player, player)[1]
            if new_score < value:
                value = new_score
                best_pos = pos
        return (best_pos, value)



# minimax algorithm with alpha beta pruning
def minimax_alpha_beta(board, old_board, depth, alpha, beta, maximizingPlayer, player):
    # Get a list of valid moves
    valid_moves = available_positions(board, player)
    # Check if the game has ended
    is_terminal = terminal_node(board)

    if (depth == 0 or is_terminal):
        # If the game has ended or the maximum search depth has been reached, return the utility or heuristic value
        if is_terminal:
            return utility_function(board, player)
        else:
            #value = heuristic_5(board,old_board, player)
            value = heuristic(board, player)
            #value = fixed_heuristic(board, player)
            return (None, value)

    if maximizingPlayer:
        # If it's the maximizing player's turn
        value = -math.inf
        best_move = random.choice(valid_moves)
        for move in valid_moves:
            # Make a copy of the board and apply the move
            b_copy = board.copy()
            
            player_tmp = mancala.move_piece(move, player, b_copy)
            # Recursively call minimax_alpha_beta with the new board state
            if player_tmp == player:
                new_score = minimax_alpha_beta(b_copy, board, depth-1, alpha, beta, True, player_tmp)[1]
            else:
                new_score = minimax_alpha_beta(b_copy, board, depth-1, alpha, beta, False, player_tmp)[1]
            # Update the best move and alpha value
            if new_score > value:
                value = new_score
                best_move = move
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return (best_move, value)
    else:
        # If it's the minimizing player's turn
        value = math.inf
        best_move = random.choice(valid_moves)
        for move in valid_moves:
            # Make a copy of the board and apply the move
            b_copy = board.copy()
            player_tmp = mancala.move_piece(move, player, b_copy)
            # Recursively call minimax_alpha_beta with the new board state
            if player_tmp != player:
                new_score = minimax_alpha_beta(b_copy, board, depth-1, alpha, beta, True, player_tmp)[1]
            else:
                new_score = minimax_alpha_beta(b_copy, board, depth-1, alpha, beta, False, player_tmp)[1]
            # Update the best move and beta value
            if new_score < value:
                value = new_score
                best_move = move
            beta = min(beta, value)
            if alpha >= beta:
                break
        return (best_move, value)


#################################