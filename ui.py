import sys
import time
import math

import tkinter

import mancala_ui
import mancala
import ai


# self.root = tkinter.Tk()
# self.root.title("Mancala")

# size = w_width, w_height = 800, 600
# speed = [2, 2]
# white = '#FFFFFF'

# self.board = mancala_ui.init_self.board(mancala_ui.self.board_SIZE)
# self.canvas = tkinter.self.canvas(self.root, height = w_height, width = w_width, background='#CECDCD', highlightbackground='#CECDCD')
# self.canvas.pack()

import tkinter

class MancalaGame:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Mancala")

        self.size = self.w_width, self.w_height = 800, 600
        self.speed = [2, 2]
        self.white = '#FFFFFF'

        self.board = mancala_ui.init_board(mancala_ui.BOARD_SIZE)
        self.canvas = tkinter.Canvas(self.root, height=self.w_height, width=self.w_width, background='#CECDCD', highlightbackground='#CECDCD')
        self.canvas.pack()
        self.main_gui()

    def start(self):
        self.root.mainloop()
        

    # main function
    def main_gui(self):

        # Greatings
        self.canvas.create_text(400,75, text="Welcome to Mancala!", font=("Arial bold", 40), fill="black", anchor='center')
        self.canvas.create_text(400,350, text="Choose between the following options:", font=("Arial", 16), fill="black", anchor='center')

        # Mancala image
        img = tkinter.PhotoImage(file='mancala.png')


        # # TEST
        # self.entry = tkinter.Entry(self.root)
        # self.entry.pack()

        # button = tkinter.Button(self.root, text="Print Input", command=self.print_input)
        # button.pack()
        # Create a button widget
        button1 = tkinter.Button(self.canvas, text="Human vs Human", command=self.human_vs_human, highlightbackground='#CECDCD')
        button2 = tkinter.Button(self.canvas, text="Human vs AI", command=self.choose_levels_1, highlightbackground='#CECDCD')
        button3 = tkinter.Button(self.canvas, text="AI vs AI", command=self.choose_levels_2, highlightbackground='#CECDCD')

        # Add the button to the self.canvas
        self.canvas.create_window(400, 400, anchor=tkinter.CENTER, window=button1)
        self.canvas.create_window(400, 450, anchor=tkinter.CENTER, window=button2)
        self.canvas.create_window(400, 500, anchor=tkinter.CENTER, window=button3)

        # add image to the self.canvas
        self.canvas.create_image(400, 200, image=img)

        self.root.mainloop()

    # print self.board 
    def print_board(self, board):

        # self.board rectangle
        self.canvas.create_rectangle(50,150,750,400, fill='#EAE5E5', width=3)

        # draw self.board lines
        self.canvas.create_rectangle(100, 150, 700, 200, fill='#FFCC9B', width=3)
        self.canvas.create_rectangle(100, 350, 700, 400, fill='#B0D8FD',width=3)
        self.canvas.create_rectangle(100, 272, 700, 277, fill='black')
        self.canvas.create_rectangle(50, 150, 100, 400, fill='#FFCC9B', width=3)
        self.canvas.create_rectangle(700, 150, 750, 400, fill='#B0D8FD', width=3)
        #self.canvas.create_line(100, 150, 100, 400) # V
        self.canvas.create_line(200, 150, 200, 400)
        self.canvas.create_line(300, 150, 300, 400)
        self.canvas.create_line(400, 150, 400, 400)
        self.canvas.create_line(500, 150, 500, 400)
        self.canvas.create_line(600, 150, 600, 400)
        #self.canvas.create_line(700, 150, 700, 400) # V
        #self.canvas.create_line(100,200,700,200)
        #self.canvas.create_line(100,350,700,350)
        #self.canvas.create_line(100,272,700,272)
        #self.canvas.create_line(100,277,700,277)


        # draw self.board numbers
        self.canvas.create_text(650, 175, text="7")
        self.canvas.create_text(550, 175, text="8")
        self.canvas.create_text(450, 175, text="9")
        self.canvas.create_text(350, 175, text="10")
        self.canvas.create_text(250, 175, text="11")
        self.canvas.create_text(150, 175, text="12")
        self.canvas.create_text(650, 375, text="6")
        self.canvas.create_text(550, 375, text="5")
        self.canvas.create_text(450, 375, text="4")
        self.canvas.create_text(350, 375, text="3")
        self.canvas.create_text(250, 375, text="2")
        self.canvas.create_text(150, 375, text="1")

        # draw self.board values
        self.canvas.create_text(650, 235, text=int(self.board[7]), font=("Arial bold", 15))
        self.canvas.create_text(550, 235, text=int(self.board[8]), font=("Arial bold", 15))
        self.canvas.create_text(450, 235, text=int(self.board[9]), font=("Arial bold", 15))
        self.canvas.create_text(350, 235, text=int(self.board[10]), font=("Arial bold", 15))
        self.canvas.create_text(250, 235, text=int(self.board[11]), font=("Arial bold", 15))
        self.canvas.create_text(150, 235, text=int(self.board[12]), font=("Arial bold", 15))
        self.canvas.create_text(650, 315, text=int(self.board[5]), font=("Arial bold", 15))
        self.canvas.create_text(550, 315, text=int(self.board[4]), font=("Arial bold", 15))
        self.canvas.create_text(450, 315, text=int(self.board[3]), font=("Arial bold", 15))
        self.canvas.create_text(350, 315, text=int(self.board[2]), font=("Arial bold", 15))
        self.canvas.create_text(250, 315, text=int(self.board[1]), font=("Arial bold", 15))
        self.canvas.create_text(150, 315, text=int(self.board[0]), font=("Arial bold", 15))
        self.canvas.create_text(75, 275, text=int(self.board[13]), font=("Arial bold", 15))
        self.canvas.create_text(725, 275, text=int(self.board[6]), font=("Arial bold", 15))



    def print_input(self):
        self.text = int(self.entry.get())
        print(self.text)

    # Function to return the level after the click
    def click(self):
        if self.button5:
            self.level = 2
        if self.button6:
            self.level = 5
        if self.button7:
            self.level = 8
        return self.level
    
    # Function to return the level after the click
    def click_2(self):
        if self.button5:
            self.level1 = 2
            self.level2 = 2
        if self.button6:
            self.level1 = 2
            self.level2 = 5
        if self.button7:
            self.level1 = 2
            self.level2 = 8
        if self.button9:
            self.level1 = 5
            self.level2 = 2
        if self.button10:
            self.level1 = 8
            self.level2 = 2
        return self.level1, self.level2

    # Choose human vs AI levels
    def choose_levels_1(self):
        self.canvas.delete('all')
        self.canvas.create_text(400,350, text="Choose between the following difficulty levels:", font=("Arial", 16), fill="black", anchor='center')
        # Create a button widget
        self.button5 = tkinter.Button(self.canvas, text="Level Easy", command=self.human_vs_ai, highlightbackground='#CECDCD')
        self.button6 = tkinter.Button(self.canvas, text="Level Medium", command=self.human_vs_ai, highlightbackground='#CECDCD')
        self.button7 = tkinter.Button(self.canvas, text="Level Hard", command=self.human_vs_ai, highlightbackground='#CECDCD')
        # Add the button to the self.canvas
        self.canvas.create_window(400, 400, anchor=tkinter.CENTER, window=self.button5)
        self.canvas.create_window(400, 450, anchor=tkinter.CENTER, window=self.button6)
        self.canvas.create_window(400, 500, anchor=tkinter.CENTER, window=self.button7)

    # Choose AI vs AI levels
    def choose_levels_2(self):
        self.canvas.delete('all')
        self.canvas.create_text(400,200, text="Player 1 vs Player 2", font=("Arial bold", 40), fill="black", anchor='center')
        self.canvas.create_text(400,350, text="Choose between the following difficulty levels:", font=("Arial", 16), fill="black", anchor='center')
        # Create a button widget
        self.button5 = tkinter.Button(self.canvas, text="Level Easy vs Easy", command=self.ai_vs_ai, highlightbackground='#CECDCD')
        self.button6 = tkinter.Button(self.canvas, text="Level Easy vs Medium", command=self.ai_vs_ai, highlightbackground='#CECDCD')
        self.button7 = tkinter.Button(self.canvas, text="Level Easy vs Hard", command=self.ai_vs_ai, highlightbackground='#CECDCD')
        self.button9 = tkinter.Button(self.canvas, text="Level Medium vs Easy", command=self.ai_vs_ai, highlightbackground='#CECDCD')
        self.button10 = tkinter.Button(self.canvas, text="Level Hard vs Easy", command=self.ai_vs_ai, highlightbackground='#CECDCD')
        # Add the button to the self.canvas
        self.canvas.create_window(400, 400, anchor=tkinter.CENTER, window=self.button5)
        self.canvas.create_window(300, 450, anchor=tkinter.CENTER, window=self.button6)
        self.canvas.create_window(300, 500, anchor=tkinter.CENTER, window=self.button7)
        self.canvas.create_window(500, 450, anchor=tkinter.CENTER, window=self.button9)
        self.canvas.create_window(500, 500, anchor=tkinter.CENTER, window=self.button10)

    # Human vs Human game
    def human_vs_human(self):
        self.canvas.delete('all')
        self.print_board(self.board)
        player = 0
        winner = 0
        while(not mancala.game_over(self.board)):
            self.canvas.create_text(400, 50, text='Human vs Human', font=('Arial bold', 25))

            if player+1 == 1:
                p1 = self.canvas.create_text(700,450, text=f'Player {player+1} turn!')
            else:
                p2 = self.canvas.create_text(100,100, text=f'Player {player+1} turn!')
            teste = ai.available_positions(self.board, player)
            try:
                piece = mancala.parse_input(int(input("Choose your Piece: ")))
            except Exception:
                #mancala.self.print_board_cmd_line(self.board)
                print("INVALID INPUT!!")
                continue
            if(not mancala.is_valid_move(piece, player, self.board)):
                continue
            player = mancala.move_piece(piece, player, self.board)
            self.canvas.delete('all')
            self.print_board(self.board)
            self.canvas.update()
        winner = mancala.winning_player(self.board)
        print("GAME OVER")
        print("Number of seeds:")
        print("Player 1: " + str(self.board[mancala.STORE_1]))
        print("Player 2: " + str(self.board[mancala.STORE_2]))
        self.canvas.create_text(400,450, text='GAME OVER!', font=('Arial bold', 15))
        self.canvas.create_text(300,500, text=f'Player 1: {self.board[mancala_ui.STORE_1]} seeds')
        self.canvas.create_text(500, 500, text=f'Player 2: {self.board[mancala_ui.STORE_2]} seeds')
        self.canvas.delete(p1)
        self.canvas.delete(p2)

        if(winner != 0):
            print("Player " + str(winner) + " won the game!!!")
            self.canvas.create_text(400, 550, text=f"Player {winner} won the game!!!", font=('Arial bold', 20))
            print(f"Player {winner} won the game!!!")
        else:
            print("It's a draw!!")
            self.canvas.create_text(400, 550, text="It's a draw!!", font=('Arial bold', 20))

    # Human vs Pc game
    def human_vs_ai(self):
        self.canvas.delete('all')
        level = self.click()
        print(level)
        self.print_board(self.board)
        player = 0
        winner = 0
        while(not mancala_ui.game_over(self.board)):
            self.canvas.create_text(400, 50, text='Human vs AI', font=('Arial bold', 25))
            if(player == 0):
                p1 = self.canvas.create_text(700,450, text=f'Your turn!')
                while True:
                    try:
                        piece = mancala_ui.parse_input(int(input("Choose your Piece: ")))
                        if mancala_ui.is_valid_move(piece, player, self.board):
                            break
                        else:
                            print("Invalid move. Please choose another piece.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                        continue
                    
                player = mancala_ui.move_piece(piece, player, self.board)
                self.canvas.delete('all')
                self.print_board(self.board)
                self.canvas.update()
            elif(player == 1):
                p2 = self.canvas.create_text(100,100, text='Computer turn!')
                #piece, minimax_score = ai.minimax_alpha_beta(self.board, None, level, -math.inf, math.inf, True, player)
                piece, minimax_score = ai.minimax(self.board, level, True, player)
                print("Computer chooses piece " + str(piece))
                if(not mancala_ui.is_valid_move(piece, player, self.board)):
                    print("ERROR: Computer made an invalid move. Please fix the code.")
                player = mancala_ui.move_piece(piece, player, self.board)
                self.canvas.delete('all')
                self.print_board(self.board)
                self.canvas.update()
        self.canvas.delete(p1)
        self.canvas.delete(p2)
        winner = mancala_ui.winning_player(self.board)
        print("GAME OVER")
        print("Number of seeds:")
        print("You: " + str(self.board[mancala_ui.STORE_1]))
        print("Computer: " + str(self.board[mancala_ui.STORE_2]))
        self.canvas.create_text(400,450, text='GAME OVER!', font=('Arial bold', 15))
        self.canvas.create_text(300,500, text=f'Player 1: {self.board[6]} seeds')
        self.canvas.create_text(500, 500, text=f'Player 2: {self.board[13]} seeds')
        if winner == 1:
            self.canvas.create_text(400, 550, text='You won the game!', font=('Arial bold', 20))
        elif winner == 2:
            self.canvas.create_text(400, 550, text='The computer won the game!', font=('Arial bold', 20))
        else:
            self.canvas.create_text(400, 550, text="It's a draw!", font=('Arial bold', 20))

    # PC vs PC game
    def ai_vs_ai(self):
        self.canvas.delete('all')
        level1, level2 = self.click_2()
        print(level1)
        print(level2)
        self.canvas.create_text(400, 25, text='AI vs AI', font=('Arial bold', 20))
        """
        Runs a game of mancala between two AI players.
        """
        self.print_board(self.board)
        player = 0
        winner = 0
        moves_1 = []
        moves_2 = []
        while not mancala_ui.game_over(self.board):
            if player == 0:
                print("Player 1 turn!")
                #piece, minimax_score = ai.minimax(self.board, level2, True, player)
                
                piece, minimax_score = ai.minimax_alpha_beta(self.board, None, level1, -math.inf, math.inf, True, player)
                print("Player 1 choose: " + str(piece+1))
                moves_1.append(piece)
                if not mancala_ui.is_valid_move(piece, player, self.board):
                    print("Invalid move by Player 1, skipping turn")
                    continue
                player = mancala_ui.move_piece(piece, player, self.board)
                self.canvas.delete('all')
                self.print_board(self.board)
                self.canvas.create_text(400, 50, text='AI vs AI', font=('Arial bold', 25))
                p1 = self.canvas.create_text(700,450, text='Player 1 turn! ')
                self.canvas.update()
                time.sleep(2)
                self.canvas.update
            elif player == 1:
                print("Player 2 turn!")
                piece, minimax_score = ai.minimax(self.board, level2, True, player)
                #piece, minimax_score = ai.minimax(self.board, level2, True, player)
                #piece, minimax_score = ai.minimax_alpha_beta(self.board, None, level2, -math.inf, math.inf, True, player)
                print("Player 2 choose: " + str(piece))
                moves_2.append(piece)
                if not mancala_ui.is_valid_move(piece, player, self.board):
                    print("Invalid move by Player 2, skipping turn")
                    continue
                player = mancala_ui.move_piece(piece, player, self.board)
                self.canvas.delete('all')
                self.print_board(self.board)
                self.canvas.create_text(400, 50, text='AI vs AI', font=('Arial bold', 25))
                p2 = self.canvas.create_text(100,100, text='Player 2 turn!')
                self.canvas.update()
                time.sleep(2)
                self.canvas.update
        self.canvas.delete(p1)
        self.canvas.delete(p2)
        winner = mancala_ui.winning_player(self.board)
        print("GAME OVER")
        print("Number of seeds:")
        print("Player 1: " + str(self.board[mancala_ui.STORE_1]))
        print("Player 2: " + str(self.board[mancala_ui.STORE_2]))
        self.canvas.create_text(400,450, text='GAME OVER!', font=('Arial bold', 15))
        self.canvas.create_text(300,500, text=f'Player 1: {self.board[6]} seeds')
        self.canvas.create_text(500, 500,text=f'Player 2: {self.board[13]} seeds')
        if winner != 0:
            print("Player " + str(winner) + " won the game!!!")
            self.canvas.create_text(400, 550, text=f"Player {winner} won the game!!!", font=('Arial bold', 20))
        else:
            print("It's a draw!!")
            self.canvas.create_text(400, 550, text="It's a draw!!", font=('Arial bold', 20))
        print(moves_1)
        print(moves_2)


# mancala = MancalaGame()
# mancala.start()