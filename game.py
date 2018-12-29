from UltimateGameBoard import UltimateGameBoard
from gameboard import Gameboard
from Comp import Computer
from player import Player

choice = 0
comp = Computer()
player = Player()

def print_menu():
    print("Hi! Welcome to the ultimate tic tac toe game!")
    print("""
    Menu
    --------------------------------------
    1. play regular tic tac toe 
    2. play ultimate tic tac toe
    3. Quit the game
    """
    )
    choice = int(input('What would you like to do?'))
    return choice

def play_again():
    repeat = input("Would you like to play again? (y/n)").lower()
    if repeat == 'y':
        return 1
    elif repeat == 'n':
        return 3
    else:
        return -1
def instructions():
    print("Ultimate Tic-Tac-Toe Game Instructions")
    print('''
    Ultimate Tic-Tac-Toe plays very similarly to regular Tic-Tac-Toe with a slight twist. 
    In order to capture a square on the board, you must win a game of regular Tic-Tac-Toe. 
    If you lose that game though, the square goes to the computer and it is their turn to play.
    The ultimate goal, Trying to get three squares in a row remains the same.
    Good Luck!!
    ''')


while choice != 3:
    choice = print_menu()
    if choice == 1:
        tic_tac_toe = Gameboard(comp, player)
        tic_tac_toe.choose_marker()
        tic_tac_toe.print_board()
        tic_tac_toe.playgame()
    elif choice == 2:
        tic_tac_toe = UltimateGameBoard(comp, player)
        instructions()
        tic_tac_toe.choose_marker()
        tic_tac_toe.print_board()
        tic_tac_toe.playgame()
    else:
        break
    choice = play_again()
    while choice == -1:
        print("Incorrect entry try again!")
        choice = play_again()
print("Game Ended!!")
    

