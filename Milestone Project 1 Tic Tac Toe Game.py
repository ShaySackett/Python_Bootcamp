import random

def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


def player_input(first_player):
    marker = ' '

    while marker != 'X' and marker != 'O':
        marker = input(f'Player {first_player}, choose X or O: ')

    if first_player == 1:
        if marker == 'X':
            player1 = 'X'
            player2 = 'O'
        else:
            player1 = 'O'
            player2 = 'X'
    else:
        if marker == 'X':
            player2 = 'X'
            player1 = 'O'
        else:
            player2 = 'O'
            player1 = 'X'

    return (player1, player2)

def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    # Check horizontal portion of board:
    row_1 = [board[7], board[8], board[9]]
    row_2 = [board[4], board[5], board[6]]
    row_3 = [board[1], board[2], board[3]]

    # check verticals:
    col_1 = [board[7], board[4], board[1]]
    col_2 = [board[8], board[5], board[2]]
    col_3 = [board[9], board[6], board[3]]

    # check diagonals:
    diag_1 = [board[7], board[5], board[3]]
    diag_2 = [board[9], board[5], board[1]]

    lists_to_check = [row_1, row_2, row_3, col_1, col_2, col_3, diag_1, diag_2]

    for line in lists_to_check:  # loop through all combinations of lines and columns
        if [mark] * 3 == line:
            return True
    else:
        return False


def choose_first():
    player_choice = random.randint(1, 2)

    print(f'I have decided player {player_choice} will go first!')

    return player_choice

def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for index in range(1, len(board)):
        if board[index] == ' ':
            return False
    else:
        return True


def player_choice(board):
    position = False
    while position != True:

        new_position = int(input("Choose a location to mark (1-9): "))
        if space_check(board, new_position):
            return new_position
            break

        else:
            print("That is not a valid position")


def replay():
    replay = input("Would you like to play again? (Y or N)")

    if replay == 'Y':
        return True
    elif replay == 'N':
        return False



while True:

    # Set the game up here
    game_on = True
    new_game = True
    while game_on:

        if new_game:
            print('Welcome to Tic Tac Toe!')
            print('Locations on the board correspond to their position 1-9 on keyboard numpads')
            game_board = [' '] * 10
            next_player_move = choose_first()
            player_1, player_2 = player_input(next_player_move)
            new_game = False

        print('\n'*100)
        display_board(game_board)

        # Player 1 Turn
        if next_player_move == 1:
            print('Player 1: ')
            loc = player_choice(game_board)
            place_marker(game_board, player_1, loc)
            next_player_move = 2
        # Player2 Turn
        else:
            print('Player 2: ')
            loc = player_choice(game_board)
            place_marker(game_board, player_2, loc)
            next_player_move = 1

        if win_check(game_board, player_1):
            print('\n'*100)
            display_board(game_board)  # display gameboard again so player can see winning move
            print('Player 1 wins!! Congratulations!!')
            break
        elif win_check(game_board, player_2):
            print('\n'*100)
            display_board(game_board)
            print('Player 2 wins!! Congratulations!!')
            break
        elif full_board_check(game_board):
            print('\n'*100)
            display_board(game_board)
            print('Board is full! TIE!')
            break

    if not replay():
        print("Bye!")
        break