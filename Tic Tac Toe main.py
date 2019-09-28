
#Requirement list

#board
#display_board
#play_game
#player_input
#game_is_on
#repete it by using while
#handle_turn
#flip_player
#cheak_if_game_over
#cheak_for_winner
#cheak_if_tie
#implemeting while loop for avoiding error


print("\n\n")
print("-----X-------TIC--------O---------")
print("-----O-------TAC--------X---------")
print("-----X-------TOE--------O---------\n")
print(" \tLET'S  GET STARTED")

board=[
        '-','-','-',
        '-','-','-',
        '-','-','-',
]

#Global variable
game_is_on=True
current_player='X'
winner=None

#Displaying board
def display_board():
    print("\n")
    print(board[0]+" | " + board[1]+ " | " + board[2]+ " | "+"      1 | 2 | 3 |")
    print(board[3]+" | " + board[4]+ " | " + board[5] +" | "+"      4 | 5 | 6 |")
    print(board[6]+" | " + board[7]+ " | " + board[8] +" | "+"      7 | 8 | 9 |")
    print("\n")
display_board()

#Play_game is one of the main function when i will call it then it will start the game
def play_game():
    while game_is_on:
        handle_turn(current_player)
        if_game_over()
        flip_player()

    #Displaying winner or if tie
    if winner =='X' or winner=='O':
        print(winner+" HAS WON SO CONGRESS"+ " try next time "+current_player)
    else:
        print("Match Tie")

#Player's turn
def handle_turn(player):
    print(current_player,"'s turn")
    position=input("Enter a number from 1-9:")

    #Avoiding error if there will be any wrong input from user then
    valid=False
    while not valid:
        while position not in ["1","2","3","4","5","6","7",'8',"9"]:
            position=input("You can only input within this number [1-9]:")
        position = int(position) - 1
        if board[position] == '-':
            valid=True
        else:
            print("Don't put this number again you have already insert it...")
    #player input if [x or o]
    board[position]=player
    display_board()

#How a game will be over
def if_game_over():
    check_for_winner()
    check_if_tie()


#To check winner in row,column and diagonal wise
def check_for_winner():
    row_winner=check_row()
    column_winner=check_column()
    diagonal_winner=check_diagonal()

    global winner
    if row_winner:
        winner=row_winner
    elif column_winner:
        winner=column_winner
    elif diagonal_winner:
        winner=diagonal_winner
    else:
        winner=None

#checking winner in row wise
def check_row():
    global game_is_on
    row_1=board[0]==board[1]==board[2]!='-'
    row_2=board[3]==board[4]==board[5]!='-'
    row_3=board[6]==board[7]==board[8]!='-'

    if row_1 or row_2 or row_3:
        game_is_on=False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

#checking winner in column wise
def check_column():
    global game_is_on
    column_1=board[0]==board[3]==board[6]!='-'
    column_2=board[1]==board[4]==board[7]!='-'
    column_3=board[2]==board[5]==board[8]!='-'

    if column_1 or column_2 or column_3:
        game_is_on=False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

#checking winner in diagonal wise
def check_diagonal():
    global game_is_on
    diagonal_1=board[0]==board[4]==board[8]!='-'
    diagonal_2=board[6]==board[4]==board[2]!='-'

    if  diagonal_1 or  diagonal_2:
        game_is_on=False
    if  diagonal_1:
        return board[0]
    elif  diagonal_2:
        return board[6]
    return


#Fliping player
def flip_player():
    global current_player
    if current_player =='X':
        current_player='O'
    elif current_player=='O':
        current_player='X'
    else:
        return

#If match will be tie
def check_if_tie():
    global game_is_on
    if '-' not in board:
        game_is_on=False
    else:
        return

play_game()





