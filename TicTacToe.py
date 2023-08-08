#1 Set up a board
from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[1]+'|'+board[2]+'|'+board[3])

#2 Take in a player input and assign their marker as 'X' or 'O'

def player_input():
    
    marker = ''
    
    # Keep asking player 1 to choose X or O
    
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()
    
    # Assign player 2, the opposite marker 
    
    player1 = marker 
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
        
    return (player1,player2)

#3 takes in the board list object, a marker ('X' or 'O'), and a desired position and assign to the board

def place_marker(board, marker, position):
    
    board[position] = marker

#4 takes in a board and a mark (X or O) and then checks to see if that mark has won

def win_check(board, mark):
    
    # Win TIC TAC TOE? 
    
    # All ROWS, and check to see if they all share the same marker?
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[7] == mark and board[8] == mark and board[9] == mark) or
    
    # All COLLUMNS, check to see if marker matches 
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    
    # 2 DIAGONALS, check to see match
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[1] == mark and board[5] == mark and board[9] == mark)) 

#5 Randomly decide which player goes first

import random

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player1'
    else:
        return 'Player2'

#6 Check whether a space on the board is freely available

def space_check(board, position):
    
    return board[position] == ' '

#7 Checks if the board is full

def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False 
        
    # Board is full if we return TRUE
    return True 

#8 Asks for a player's next position and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use

def player_choice(board):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position: (1-9) '))
    
    return position

#9 Asks the player if they want to play again

def replay():
    
    choice = input('Play again? Enter Yes or No')
    
    return choice == 'Yes'

#10 Compile all the functions

print('Welcome to Tic Tac Toe!')

while True: 
    
     #Play the game 
        
    ## Set everyyhing up (board<whos first, choose markers X,O)
    
    the_board = [' ']*10
    
    player1_marker,player2_marker = player_input()
   
    turn = choose_first()
    print(turn+' will go first')
    
    play_game = input('Ready to play? y or n? ')
    
    if play_game == 'y':
        game_on = True 
    else:
        game_on = False
    
    ## Game Play
    
    while game_on:
        if turn == 'Player1':
            #Player1's turn.
            
            # Show the board
            display_board(the_board)
            
            # Choose a position 
            position = player_choice(the_board)
            
            # Place the marker on the position 
            place_marker(the_board,player1_marker,position)
            
            # Check if they won 
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TILE GAME!!')
                    break
                else:
                    turn = 'Player2'
        
        else:
            
            # Show the board
            display_board(the_board)
            
            # Choose a position 
            position = player_choice(the_board)
            
            # Place the marker on the position 
            place_marker(the_board,player2_marker,position)
            
            # Check if they won 
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TILE GAME!!')
                    break
                else:
                    turn = 'Player1'       
        
    if not replay():
        break
