import sys
import math
import time
import resource
import mancala
import ai
import pandas as pd


def human_vs_ai(board, level):
    mancala.print_board_cmd_line(board)
    player = 0
    winner = 0
    moves = []
    while(not mancala.game_over(board)):
        if(player == 0):
            print("Player " + str(player + 1) + " turn!")
            try:
                piece = mancala.parse_input(int(input("Choose your Piece: ")))
            except Exception:
                mancala.print_board_cmd_line(board)
                print("INVALID INPUT!!")
                continue
            if(not mancala.is_valid_move(piece, player, board)):
                continue
            player = mancala.move_piece(piece, player, board)
            mancala.print_board_cmd_line(board)
        elif(player == 1):
            print("Player " + str(player + 1) + " turn!")
            tic = time.clock()
            piece, minimax_score = ai.minimax_alpha_beta(board, None, level, -math.inf, math.inf, True, player)
            toc = time.clock()
            print("CHOOSEN POS: " + str(piece))
            print("Processing Time: " + str(toc-tic))
            if(not mancala.is_valid_move(piece, player, board)):
                continue
            player = mancala.move_piece(piece, player, board)
            moves.append(piece)
            mancala.print_board_cmd_line(board)
            time.sleep(1)

    
    winner = mancala.winning_player(board)
    print("GAME OVER")
    print("Number of seeds:")
    print("Player 1: " + str(board[mancala.STORE_1]))
    print("Player 2: " + str(board[mancala.STORE_2]) + " | Moves Done: " + str(moves))
    if(winner != 0):
        print("Player " + str(winner) + " won the game!!!")
    else:
        print("It's a draw!!")

def ai_vs_ai(board, level1, level2):
    mancala.print_board_cmd_line(board)
    player = 0
    winner = 0
    moves_1 = []
    moves_2 = []
    # time_1 = []
    # time_2 = []
    while(not mancala.game_over(board)):
        if(player == 0):
            # print("Player 1 turn!")
            # print(player)
            #tic1 = time.clock()
            piece = ai.random_number_gen(board, player)
            piece, minimax_score = ai.minimax(board, level1, True, player)
            #piece, minimax_score = ai.minimax_alpha_beta(board, None, level1, -math.inf, math.inf, True, player)
            if(not mancala.is_valid_move(piece, player, board)):
                continue
            player = mancala.move_piece(piece, player, board)
            moves_1.append(piece)
            
        
        elif(player == 1):
            # print("Player 2 turn!")
            #tic2 = time.clock()
            piece = ai.random_number_gen(board, player)
            #piece, minimax_score = ai.minimax(board, level2, True, player)
            piece, minimax_score = ai.minimax_alpha_beta(board, None, level2, -math.inf, math.inf, True, player)
            if(not mancala.is_valid_move(piece, player, board)):
                continue
            player = mancala.move_piece(piece, player, board)
            moves_2.append(piece)
           
    
    winner = mancala.winning_player(board)
    print("GAME OVER")
    print('Moves from Player 1: ' + str(moves_1))
    print('Moves from Player 2: ' + str(moves_2))
    if(winner != 0):
        print("Player " + str(winner) + " won the game!")
    else:
        print("It's a draw!!")
    return winner, moves_1, moves_2

#function to call ai_vs_ai 10 times and return the number of wins for each player
def pc_vs_pc_10_times(level1, level2):
    i = 0
    win = 0
    win_count = 0
    p1_wins = 0
    p2_wins = 0
    time_start = time.time()
    while(i<10):
        board = mancala.init_board(mancala.BOARD_SIZE)
        win, m1, m2 = ai_vs_ai(board, level1, level2)
        #if player 1 wins
        if(win == 1):
            p1_wins += 1
            i += 1
        #if player 2 wins
        elif(win == 2):
            p2_wins += 1
            i += 1
        #if it's a draw
        else:
            i += 1
    time_end = time.time()
    memory_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    
    time_spent = time_end - time_start


    print("Player 1 wins: " + str(p1_wins))
    print("Player 2 wins: " + str(p2_wins))


    

    return p1_wins, p2_wins, memory_usage, time_spent, m1, m2


p1_25, p2_25, mu25, t_25, m1_25, m2_25 = pc_vs_pc_10_times(5,2) 
p1_28, p2_28, mu28, t_28, m1_28, m2_28 = pc_vs_pc_10_times(2,8) 
p1_58, p2_58, mu58, t_58, m1_58, m2_58 = pc_vs_pc_10_times(5,8) 


#### MINIMAX TESTS ####

# #With No Alpha-Beta Pruning - Heuristic 1
# print(f"With depth 2 and 5 - Player 1 wins: {p1_25} | Player 2 wins: {p2_25} | Memory Usage: {mu25} bytes")
# print(f"With depth 2 and 8 - Player 1 wins: {p1_28} | Player 2 wins: {p2_28} | Memory Usage: {mu28} bytes")
# print(f"With depth 5 and 8 - Player 1 wins: {p1_58} | Player 2 wins: {p2_58} | Memory Usage: {mu58} bytes")

# #With No Alpha-Beta Pruning - Heuristic 2
# print(f"With depth 2 and 5 - Player 1 wins: {p1_25} | Player 2 wins: {p2_25} | Memory Usage: {mu25} bytes")
# print(f"With depth 2 and 8 - Player 1 wins: {p1_28} | Player 2 wins: {p2_28} | Memory Usage: {mu28} bytes")
# print(f"With depth 5 and 8 - Player 1 wins: {p1_58} | Player 2 wins: {p2_58} | Memory Usage: {mu58} bytes")

# #With No Alpha-Beta Pruning - Heuristic 3
# print(f"With depth 2 and 5 - Player 1 wins: {p1_25} | Player 2 wins: {p2_25} | Memory Usage: {mu25} bytes")
# print(f"With depth 2 and 8 - Player 1 wins: {p1_28} | Player 2 wins: {p2_28} | Memory Usage: {mu28} bytes")
# print(f"With depth 5 and 8 - Player 1 wins: {p1_58} | Player 2 wins: {p2_58} | Memory Usage: {mu58} bytes")

# #With No Alpha-Beta Pruning - Heuristic 4
# print(f"With depth 2 and 5 - Player 1 wins: {p1_25} | Player 2 wins: {p2_25} | Memory Usage: {mu25} bytes")
# print(f"With depth 2 and 8 - Player 1 wins: {p1_28} | Player 2 wins: {p2_28} | Memory Usage: {mu28} bytes")
# print(f"With depth 5 and 8 - Player 1 wins: {p1_58} | Player 2 wins: {p2_58} | Memory Usage: {mu58} bytes")

# #With No Alpha-Beta Pruning - Heuristic 5
# print(f"With depth 2 and 5 - Player 1 wins: {p1_25} | Player 2 wins: {p2_25} | Memory Usage: {mu25} bytes")
# print(f"With depth 2 and 8 - Player 1 wins: {p1_28} | Player 2 wins: {p2_28} | Memory Usage: {mu28} bytes")
# print(f"With depth 5 and 8 - Player 1 wins: {p1_58} | Player 2 wins: {p2_58} | Memory Usage: {mu58} bytes")

#### MINIMAX WITH ALPHA-BETA PRUNING TESTS ####

#With Alpha-Beta Pruning - Heuristic 1
print(f"With depth 5 and 2 - Player 1 wins: {p1_25} | Player 2 wins: {p2_25} | Memory Usage: {mu25} bytes | Time: {t_25} | Moves_1: {m1_25} | Moves_2: {m2_25}")
print(f"With depth 2 and 8 - Player 1 wins: {p1_28} | Player 2 wins: {p2_28} | Memory Usage: {mu28} bytes | Time: {t_28} | Moves_1: {m1_28} | Moves_2: {m2_28}")
print(f"With depth 5 and 8 - Player 1 wins: {p1_58} | Player 2 wins: {p2_58} | Memory Usage: {mu58} bytes | Time: {t_58} | Moves_1: {m1_58} | Moves_2: {m2_58}")

#With Alpha-Beta Pruning - Heuristic 2
# print(f"With depth 2 and 5 - Player 1 wins: {p1_25} | Player 2 wins: {p2_25} | Memory Usage: {mu25} bytes")
# print(f"With depth 2 and 8 - Player 1 wins: {p1_28} | Player 2 wins: {p2_28} | Memory Usage: {mu28} bytes")
# print(f"With depth 5 and 8 - Player 1 wins: {p1_58} | Player 2 wins: {p2_58} | Memory Usage: {mu58} bytes")

#With Alpha-Beta Pruning - Heuristic 3
# print(f"With depth 2 and 5 - Player 1 wins: {p1_25} | Player 2 wins: {p2_25} | Memory Usage: {mu25} bytes")
# print(f"With depth 2 and 8 - Player 1 wins: {p1_28} | Player 2 wins: {p2_28} | Memory Usage: {mu28} bytes")
# print(f"With depth 5 and 8 - Player 1 wins: {p1_58} | Player 2 wins: {p2_58} | Memory Usage: {mu58} bytes")

#With Alpha-Beta Pruning - Heuristic 4
# print(f"With depth 2 and 5 - Player 1 wins: {p1_25} | Player 2 wins: {p2_25} | Memory Usage: {mu25} bytes")
# print(f"With depth 2 and 8 - Player 1 wins: {p1_28} | Player 2 wins: {p2_28} | Memory Usage: {mu28} bytes")
# print(f"With depth 5 and 8 - Player 1 wins: {p1_58} | Player 2 wins: {p2_58} | Memory Usage: {mu58} bytes")

#With Alpha-Beta Pruning - Heuristic 5
# print(f"With depth 2 and 5 - Player 1 wins: {p1_25} | Player 2 wins: {p2_25} | Memory Usage: {mu25} bytes")
# print(f"With depth 2 and 8 - Player 1 wins: {p1_28} | Player 2 wins: {p2_28} | Memory Usage: {mu28} bytes")
# print(f"With depth 5 and 8 - Player 1 wins: {p1_58} | Player 2 wins: {p2_58} | Memory Usage: {mu58} bytes")

 
alpha_beta_data = {
    'Player_1_wins': [p1_25,p1_28,p1_58], # minimax
    'Player_2_wins': [p2_25,p2_28,p2_58], # alpha-beta
    'Memory_usage': [mu25,mu28,mu58],
    'Time':[t_25,t_28,t_58],
    'Moves_1':[m1_25,m1_28,m1_58],
    'Moves_2':[m2_25,m2_28,m2_58],
    'Algorithm':['minimax_ab_52_1','minimax_ab_28_1','minimax_ab_58_1',]
}

df1 = pd.DataFrame(alpha_beta_data)
print(df1)
df1.to_csv('minimax_alphabeta_1.csv')