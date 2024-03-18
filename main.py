import sys
import time
import math

import tkinter

import mancala
import ai
import ui




# human vs human player mode in command line
def human_vs_human(board):
    mancala.print_board_cmd_line(board)
    player = 0
    winner = 0
    while(not mancala.game_over(board)):
        print("Player " + str(player + 1) + " turn!")
        teste = ai.available_positions(board, player)
        try:
            piece = mancala.parse_input(int(input("Choose your Seeds: ")))
        except Exception:
            mancala.print_board_cmd_line(board)
            print("Invalid Input!")
            continue
        if(not mancala.is_valid_move(piece, player, board)):
            continue
        player = mancala.move_piece(piece, player, board)
        mancala.print_board_cmd_line(board)
    
    winner = mancala.winning_player(board)
    print("GAME OVER")
    print("Number of seeds:")
    print("Player 1: " + str(board[mancala.STORE_1]))
    print("Player 2: " + str(board[mancala.STORE_2]))
    if(winner != 0):
        print("Player " + str(winner) + " won the game!!!")
    else:
        print("It's a draw!!")


def human_vs_ai(board, level):
    mancala.print_board_cmd_line(board)
    player = 0
    winner = 0
    while(not mancala.game_over(board)):
        if(player == 0):
            print("Your turn!")
            while True:
                try:
                    piece = mancala.parse_input(int(input("Choose your Seeds: ")))
                    if mancala.is_valid_move(piece, player, board):
                        break
                    else:
                        print("Invalid move. Please choose another piece.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
                
            player = mancala.move_piece(piece, player, board)
            mancala.print_board_cmd_line(board)
        elif(player == 1):
            print("Computer turn!")
            piece, minimax_score = ai.minimax_alpha_beta(board, None, level, -math.inf, math.inf, True, player)
            print("Computer chooses piece " + str(piece))
            if(not mancala.is_valid_move(piece, player, board)):
                print("ERROR: Ai made an incorrect move! It seems to be a code bug.")
            player = mancala.move_piece(piece, player, board)
            mancala.print_board_cmd_line(board)

    winner = mancala.winning_player(board)
    print("GAME OVER!")
    print("Number of seeds:")
    print("You: " + str(board[mancala.STORE_1]))
    print("Computer: " + str(board[mancala.STORE_2]))
    if(winner != 0):
        print("Congratulations! You won the game!" if winner == 1 else "You lost! The computer won the game!")
    else:
        print("It's a draw!")

    

def ai_vs_ai(board, level1, level2):
    """
    Runs a game of mancala between two AI players.
    """
    mancala.print_board_cmd_line(board)
    player = 0
    winner = 0
    while not mancala.game_over(board):
        if player == 0:
            print("Player 1 turn!")
            piece, minimax_score = ai.minimax_alpha_beta(board, None, level1, -math.inf, math.inf, True, player)
            print("Player 1 choose: " + str(piece+1))
            if not mancala.is_valid_move(piece, player, board):
                print("Invalid move by Player 1, skipping turn")
                continue
            player = mancala.move_piece(piece, player, board)
            mancala.print_board_cmd_line(board)
        elif player == 1:
            print("Player 2 turn!")
            piece, minimax_score = ai.minimax_alpha_beta(board, None, level2, -math.inf, math.inf, True, player)
            print("Player 2 choose: " + str(piece))
            if not mancala.is_valid_move(piece, player, board):
                print("Invalid move by Player 2, skipping turn")
                continue
            player = mancala.move_piece(piece, player, board)
            mancala.print_board_cmd_line(board)

    winner = mancala.winning_player(board)
    print("GAME OVER")
    print("Number of seeds:")
    print("Player 1: " + str(board[mancala.STORE_1]))
    print("Player 2: " + str(board[mancala.STORE_2]))
    if winner != 0:
        print("Player " + str(winner) + " won the game!!!")
    else:
        print("It's a draw!!")



# Play the game in the command line
def main_cmd_line_game():
    print("\n\n\n\n\nChoose your mode:\n")
    print("1 - Player vs Player")
    print("2 - Player vs PC")
    print("3 - PC vs PC")
    print("4 - Exit")
    while(True):
        try:
            user = int(input("Select: "))
            if(user == 1 or user == 2 or user == 3 or user == 4):
                break
            else:
                print("Choose between 1, 2, 3 and 4!")
                continue
        except Exception:
            print("Invalid Input!")
            continue
    if(user == 4):
        return
    board = mancala.init_board(mancala.BOARD_SIZE)
    if(user == 1):
        human_vs_human(board)
    elif(user == 2):
        print("Choose the difficulty level:")
        print("1 - Easy")
        print("2 - Medium")
        print("3 - Hard")
        print("4 - Exit")
        while(True):
            try:
                level = int(input("Select: "))
                if(level == 1 or level == 2 or level == 3 or level == 4):
                    break
                else:
                    print("Choose between 1, 2 and 3!")
                    continue
            except Exception:
                print("Invalid Input!")
                continue
        if(level == 1):
            human_vs_ai(board, 2)
        elif(level == 2):
            human_vs_ai(board, 5)
        elif(level == 3):
            human_vs_ai(board, 8)
        else:
            return

    else:
        while(True):
            print("Choose the difficulty level for pc 1:")
            print("1 - Easy")
            print("2 - Medium")
            print("3 - Hard")
            print("4 - Exit")
            try:
                level1 = int(input("Select: "))
                if(level1 == 1 or level1 == 2 or level1 == 3 or level1 == 4):
                    break
                else:
                    print("Choose between 1, 2, 3 or 4!")
                    continue
            except Exception:
                print("Invalid Input!")
                continue

        while(True):
            print("Choose the difficulty level for pc 2:")
            print("1 - Easy")
            print("2 - Medium")
            print("3 - Hard")
            print("4 - Exit")
            try:
                level2 = int(input("Select: "))
                if(level2 == 1 or level2 == 2 or level2 == 3 or level2 == 4):
                    break
                else:
                    print("Choose between 1, 2, 3 or 4!")
                    continue
            except Exception:
                print("Invalid Input!")
                continue
        
        if(level1 == 1):
            pc_1 = 2
        elif(level1 == 2):
            pc_1 = 5
        elif(level1 == 3):
            pc_1 = 8
        else:
            return

        if(level2 == 1):
            pc_2 = 2
        elif(level2 == 2):
            pc_2 = 5
        elif(level2 == 3):
            pc_2 = 8
        else:
            return
        
        ai_vs_ai(board, pc_1, pc_2)


# Chooses between the graphical interface and the terminal interface
def term_or_gui():
    while(True):
        print("\n\n\nMANCALA BOARD GAME")
        print("\nSelect one of the options:")
        print("1 - Run the Game on Terminal")
        print("2 - Run the Game on Graphical Interface")
        print("0 - Exit Command Line Menu")
        while(True):
            try:
                user = int(input("Select: "))
                if(user == 1 or user == 2 or user == 0):
                    break
                else:
                    print("Choose 0, 1!")
                    continue
            except Exception:
                print("Invalid Input!")
                continue
        if(user == 1):
            main_cmd_line_game()
        elif( user == 2):
            mancala = ui.MancalaGame()
            mancala.start()
        else:
            break



term_or_gui()