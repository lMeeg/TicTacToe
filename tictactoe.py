import math

def display_board(board):
    blankBoard="""
___________________
|     |     |     |
|  7  |  8  |  9  |
|     |     |     |
|-----------------|
|     |     |     |
|  4  |  5  |  6  |
|     |     |     |
|-----------------|
|     |     |     |
|  1  |  2  |  3  |
|     |     |     |
|-----------------|
"""

    for i in range(1,10):
        if (board[i] == 'O' or board[i] == 'X'):
            blankBoard = blankBoard.replace(str(i), board[i])
        else:
            blankBoard = blankBoard.replace(str(i), ' ')
    print(blankBoard)

def player_input():
    player1 = input("Pick a marker 'X' or 'O' ")

    while True:
        if player1.upper() == 'X':
            player2='O'
            print("You are " + player1 + ". Computer is " + player2)
            return player1.upper(),player2
        elif player1.upper() == 'O':
            player2='X'
            print("You are " + player1 + ". Computer is " + player2)
            return player1.upper(),player2
        else:
            player1 = input("Pick a marker 'X' or 'O' ")

def place_marker(board, marker, position):
    board[position] = marker
    return board

def space_check(board, position):
    return board[position] == '#'

def full_board_check(board):
    return len([x for x in board if x == '#']) == 1

def win_check(board, mark):
    if board[1] == board[2] == board[3] == mark:
        return True
    if board[4] == board[5] == board[6] == mark:
        return True
    if board[7] == board[8] == board[9] == mark:
        return True
    if board[1] == board[4] == board[7] == mark:
        return True
    if board[2] == board[5] == board[8] == mark:
        return True
    if board[3] == board[6] == board[9] == mark:
        return True
    if board[1] == board[5] == board[9] == mark:
        return True
    if board[3] == board[5] == board[7] == mark:
        return True
    return False

def player_choice(board, player):
    if player == 'human':
        choice = input("Choose an empty space between 1 and 9 : ")
        while not space_check(board, int(choice)):
            choice = input("This space isn't free. Choose again : ")
    else:
        choice = minimax(board, player)['position']
    return int(choice)


def replay():
    playAgain = input("Do you want to play again (y/n) ? ")
    if playAgain.lower() == 'y':
        return True
    if playAgain.lower() == 'n':
        return False
    
def minimax(board, player):
    if win_check(board, player):
        return {'score': 10}
    elif win_check(board, switch_player(player)):
        return {'score': -10}
    elif full_board_check(board):
        return {'score': 0}

    moves = []
    for i in range(1, 10):
        if space_check(board, i):
            move = {'position': i}

            board_copy = board.copy()
            board_copy[i] = player

            if player == 'computer':
                result = minimax(board_copy, 'human')
                move['score'] = result['score']
            else:
                result = minimax(board_copy, 'computer')
                move['score'] = result['score']

            moves.append(move)

    best_move = None
    if player == 'computer':
        best_score = -10000
        for move in moves:
            if move['score'] > best_score:
                best_score = move['score']
                best_move = move
    else:
        best_score = 10000
        for move in moves:
            if move['score'] < best_score:
                best_score = move['score']
                best_move = move

    return best_move

def switch_player(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'

print('Welcome to Tic Tac Toe!')

while True:
    board = ['#'] * 10
    player1_marker, player2_marker = player_input()

    if player1_marker == 'X':
        turn = 'human'
    else:
        turn = 'computer'

    play_game = input("Are you ready to play? Enter Yes or No: ")

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'human':
            display_board(board)
            position = player_choice(board, 'human')
            place_marker(board, player1_marker, position)

            if win_check(board, player1_marker):
                display_board(board)
                print("You have won the game")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("The game is a draw")
                    break
                else:
                    turn = 'computer'
        else:
            position = player_choice(board, 'computer')
            place_marker(board, player2_marker, position)

            if win_check(board, player2_marker):
                display_board(board)
                print("The computer has won the game")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("The game is a draw")
                    break
                else:
                    turn = 'human'

    if not replay():
        break 