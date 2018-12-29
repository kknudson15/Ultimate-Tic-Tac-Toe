from gameboard import Gameboard
from Comp import Computer
from player import Player

class UltimateGameBoard:

    def __init__ (self, comp, player):
        '''
        Initializing the class and data members 
        inputs: computer object and player object
        Ouputs: none
        '''
        self.board = ['1','2','3','4','5','6','7','8','9']
        self.comp = comp
        self.player = player
        self.count = 0

    def print_board(self):
        '''
        Display function that outputs the gameboard to the 
        Inputs: list of the moves made so far in the game.
        Outputs: displays the game board to the terminal
        '''

        L1 = self.board[0]
        M1 = self.board[1]
        R1 = self.board[2]
        L2 = self.board[3]
        M2 = self.board[4]
        R2 = self.board[5]
        L3 = self.board[6]
        M3 = self.board[7]
        R3 = self.board[8]
        print(
        f"""
-----------------------------------------------------------
    board:
\t      |       |
\t  {L1}   |   {M1}   |    {R1}
\t______|_______|________
\t      |       |
\t  {L2}   |   {M2}   |    {R2}
\t______|_______|________
\t      |       |
\t  {L3}   |   {M3}   |    {R3}
\t      |       |

-----------------------------------------------------------
        """)

    def make_move(self, turn):
        '''
        Handles making moves on the board
        inputs: Which players turn it is as an integer
        Outputs: Alters that game board to reflect the move
        '''
        if turn == 1 and self.gameover() != True:
            move = self.player.make_move()
            if self.is_valid_move(move) == True:
                print(f"Playing game to capture square {move}!")
                game = 2
                comp = Computer()
                player = Player()
                tic_tac_toe = Gameboard(comp, player)
                tic_tac_toe.comp.set_marker(self.comp.get_marker())
                tic_tac_toe.player.set_marker(self.player.get_marker())
                tic_tac_toe.print_board()
                tic_tac_toe.playgame()
                if tic_tac_toe.declare_winner() == 1:
                    self.board[move-1] = self.player.get_marker()
                    self.count += 1
                elif tic_tac_toe.declare_winner() == -1:
                    self.board[move-1] = self.comp.get_marker()
                    self.count += 1
                else:
                    print ("It is a Tie! no one wins the square!")
            else:
                while(self.is_valid_move(move) == False):
                    print('Not a valid move! Try again!')
                    move = self.player.make_move()
                print(f"Playing game to capture square {move}!")
                game = 2
                comp = Computer()
                player = Player()
                tic_tac_toe = Gameboard(comp, player)
                tic_tac_toe.comp.set_marker(self.comp.get_marker())
                tic_tac_toe.player.set_marker(self.player.get_marker())
                tic_tac_toe.print_board()
                tic_tac_toe.playgame()
                if tic_tac_toe.declare_winner() == 1:
                    self.board[move-1] = self.player.get_marker()
                    self.count += 1
                elif tic_tac_toe.declare_winner() == -1:
                    self.board[move-1] = self.comp.get_marker()
                    self.count += 1
                else:
                    print ("It is a Tie! no one wins the square!")
        elif turn == 0 and self.gameover() != True:
            move1 = self.comp.make_move()
            if self.is_valid_move(move1) == True:
                print(f"Playing game to capture square {move1}!")
                game = 2
                comp = Computer()
                player = Player()
                tic_tac_toe = Gameboard(comp, player)
                tic_tac_toe.comp.set_marker(self.comp.get_marker())
                tic_tac_toe.player.set_marker(self.player.get_marker())
                tic_tac_toe.print_board()
                tic_tac_toe.playgame()
                if tic_tac_toe.declare_winner() == 1:
                    self.board[move1-1] = self.player.get_marker()
                    self.count += 1
                elif tic_tac_toe.declare_winner() == -1:
                    self.board[move1-1] = self.comp.get_marker()
                    self.count += 1
                else:
                    print ("It is a Tie! no one wins the square!")
            else:
                while(self.is_valid_move(move1) == False):
                    print('Computer is thinking...')
                    move1 = self.comp.make_move()
                print(f"Playing game to capture square {move1}!")
                game = 2
                comp = Computer()
                player = Player()
                tic_tac_toe = Gameboard(comp, player)
                tic_tac_toe.comp.set_marker(self.comp.get_marker())
                tic_tac_toe.player.set_marker(self.player.get_marker())
                tic_tac_toe.print_board()
                tic_tac_toe.playgame()
                if tic_tac_toe.declare_winner() == 1:
                    self.board[move1-1] = self.player.get_marker()
                    self.count += 1
                elif tic_tac_toe.declare_winner() == -1:
                    self.board[move1-1] = self.comp.get_marker()
                    self.count += 1
                else:
                    print ("No one wins the square!")
                print(f'\nThe computer moved to {move1}')

    def is_valid_move(self, move):
        '''
        Determines if a move is valid
        input: potential move to be made as an integer
        Ouput: Returns boolean corresponding to validity of move
        '''
        if move -1 > 8:
            return False
        elif self.board[move-1] == 'x' or self.board[move-1] == 'o':
            return False
        else:
            return True
    def winner(self, marker):
        '''
        Determines if a player has won the game
        Inputs: the player marker (x/o) that the function is checking for
        Outputs: Returns a boolean corresponding to whether or not a player has won
        '''
        if self.board[0] == marker and self.board[1] == marker and self.board[2] == marker:
            return True
        elif self.board[3] == marker and self.board[4] == marker and self.board[5] == marker:
            return True
        elif self.board[6] == marker and self.board[7] == marker and self.board[8] == marker:
            return True
        elif self.board[0] == marker and self.board[3] == marker and self.board[6] == marker:
            return True
        elif self.board[1] == marker and self.board[4] == marker and self.board[7] == marker:
            return True
        elif self.board[2] == marker and self.board[5] == marker and self.board[8] == marker:
            return True
        elif self.board[0] == marker and self.board[4] == marker and self.board[8] == marker:
            return True
        elif self.board[2] == marker and self.board[4] == marker and self.board[6] == marker:
            return True
        else:
            return False
    
    def gameover(self):
        '''
        Determines when the game is over
        Inputs: None 
        Oututs: Boolean corresponding to the game end conditions
        '''
        if self.count == 9:
            return True
        else:
            return (self.winner(self.player.get_marker()) or self.winner(self.comp.get_marker()))

    def declare_winner(self):
        '''
        Determines who won the game 
        Inputs: None 
        Ouputs: returns 1 if the human won, -1 if the computer won and 0 if there was a tie
        '''
        if(self.winner(self.player.get_marker())):
            return 1
        elif(self.winner(self.comp.get_marker())):
            return -1
        elif(self.count == 9):
            return 0

    def choose_marker(self):
        '''
        Assigns the markers to the player and computer
        Inputs/Outputs: none
        '''
        marker = input("would you like to play as X or O?").lower()
        while marker != 'x' and marker != 'o':
            print("Incorrect entry, please enter X or O")
            marker = input("would you like to play as X or O?").lower()
            self.player.set_marker(marker)
        if marker == 'x':
            self.comp.set_marker('o')
        elif marker == 'o':
            self.comp.set_marker('x')

    def playgame(self):
        '''
        Handles game play on this board 
        Inputs: None
        Ouputs: Returns True when the game ends
        '''
        move = 1
        while (self.gameover() == False):
            self.make_move(move)
            self.print_board()
            move = 1-move
            self.make_move(move)
            self.print_board()
            move = 1-move
        if self.declare_winner() == 1:
            print("Human Player has defeated the Computer!")
        elif self.declare_winner() == -1:
            print("Computer has defeated the Human Player")
        else:
            print("It is a Tie!!")
        return True

        

