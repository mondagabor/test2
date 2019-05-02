import random
MAP_SIZE = 5
matrix = [["⬚" for x in range (5)]for y in range (5)]

def draw_matrix():
    for i in range (5):
        for j in range (5):
            print (matrix[i][j], end=' ')
        print()
    print()
draw_matrix()



'''
def drawBoard(board):
    print(' ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2])
    print('-----------')
    print(' ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2])
    print('-----------')
    print(' ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2])

def randome(who_start_it):
    starter = random.randrange(1,2)
    if starter == 1:
        return player1
    else:X
        return player2
'''



def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'player1'
    else:
        return 'player2'

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Pick between X or O.')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def tie_check(board):
    return (board[0][0] != " " and board [0][1] != " " and board[0][2] != " " and
        board[1][0] != " " and board [1][1] != " " and board[1][2] != " " and
        board[2][0] != " " and board [2][1] != " " and board[2][2] != " " and
        board[0][0] != " " and board [1][0] != " " and board[2][0] != " " and
        board[0][1] != " " and board [1][1] != " " and board[2][1] != " " and
        board[0][2] != " " and board [1][2] != " " and board[2][2] != " "  and
        board[0][0] != " " and board [1][1] != " " and board[2][2] != " " and
        board[0][2] != " " and board [1][1] != " " and board[2][0] != " " )        

def win_check(board, letter):
    return ((board[0][0] == letter and board [0][1] == letter and board[0][2] == letter ) or
        (board[1][0] == letter and board [2][1] == letter and board[2][2] == letter ) or
        (board[0][0] == letter and board [1][1] == letter and board[1][2] == letter ) or
        (board[2][0] == letter and board [1][0] == letter and board[2][0] == letter ) or
        (board[0][1] == letter and board [1][1] == letter and board[2][1] == letter ) or
        (board[0][2] == letter and board [1][2] == letter and board[2][2] == letter ) or
        (board[0][0] == letter and board [1][1] == letter and board[2][2] == letter ) or
        (board[0][2] == letter and board [1][1] == letter and board[2][0] == letter ))



'''
def playermove1(board):
    player1 = input("Next move: ")
    if player1 == "11":
        if board[0][0] != " ":
            print ("This place is already taken! ")
            playermove1(board)
        else:
            board[0][0] = player1letter
            return board

    elif player1 == "12":
        if board[0][1] != " ":
            print ("This place is already taken! ")
            playermove1(board)
        else:
            board[0][1] = player1letter
            return board

    elif player1 == "13":
        if board[0][2] != " ":
            print ("This place is already taken! ")
            playermove1(board)
        else:
            board[0][2] = player1letter
            return board

    elif player1 == "21":
        if board[1][0] != " ":
            print ("This place is already taken! ")
            playermove1(board)
        else:
            board[1][0] = player1letter
            return board

    elif player1 == "22":
        if board[1][1] != " ":
            print ("This place is already taken! ")
            playermove1(board)
        else:
            board[1][1] = player1letter
            return board

    elif player1 == "23":
        if board[1][2] != " ":
            print ("This place is already taken! ")
            playermove1(board)
        else:
            board[1][2] = player1letter
            return board

    elif player1 == "31":
        if board[2][0] != " ":
            print ("This place is already taken! ")
            playermove1(board)
        else:
            board[2][0] = player1letter
            return board

    elif player1 == "32":
        if board[2][1] != " ":
            print ("This place is already taken! ")
            playermove1(board)
        else:
            board[2][1] = player1letter
            return board

    elif player1 == "33":
        if board[2][2] != " ":
            print ("This place is already taken! ")
            playermove1(board)
        else:
            board[2][2] = player1letter
            return board
    else:
        print("Out of range! ")
        playermove1(board)

def playermove2(board):
    player2 = input("Next move: ")
    if player2 == "11":
        if board[0][0] != " ":
            print ("This place is already taken! ")
            playermove2(board)
        else:
            board[0][0] = player2letter
            return board

    elif player2 == "12":
        if board[0][1] != " ":
            print ("This place is already taken! ")
            playermove2(board)
        else:
            board[0][1] = player2letter
            return board

    elif player2 == "13":
        if board[0][2] != " ":
            print ("This place is already taken! ")
            playermove2(board)
        else:
            board[0][2] = player2letter
            return board

    elif player2 == "21":
        if board[1][0] != " ":
            print ("This place is already taken! ")
            playermove2(board)
        else:
            board[1][0] = player2letter
            return board

    elif player2 == "22":
        if board[1][1] != " ":
            print ("This place is already taken! ")
            playermove2(board)
        else:
            board[1][1] = player2letter
            return board

    elif player2 == "23":
        if board[1][2] != " ":
            print ("This place is already taken! ")
            playermove2(board)
        else:
            board[1][2] = player2letter
            return board

    elif player2 == "31":
        if board[2][0] != " ":
            print ("This place is already taken! ")
            playermove2(board)
        else:
            board[2][0] = player2letter
            return board

    elif player2 == "32":
        if board[2][1] != " ":
            print ("This place is already taken! ")
            playermove2(board)
        else:
            board[2][1] = player2letter
            return board

    elif player2 == "33":
        if board[2][2] != " ":
            print ("This place is already taken! ")
            playermove2(board)
        else:
            board[2][2] = player2letter
            return board
    else:
        print("Out of range! ")
        playermove2(board)
print("Welcome! ")
'''
while True:
    board = [[" "," "," "],[" "," "," "],[" "," "," "]]
    player1letter, player2letter = inputPlayerLetter()   ###inputplayerletter == "x"
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')

    while True:
        if turn == 'player1':
            print ("player's 1 round! ")
            playermove1(board)
            drawBoard(board)

            if win_check(board, player1letter) == True:
                print(turn,"won the game!! ")
                break
            elif tie_check(board) == True:
                print ("Draw match! ")
                break
            else:
                turn = "player2"
                continue

        else:
            print ("player's 2 round! ")
            playermove2(board)
            drawBoard(board)
            if win_check(board, player2letter) == True:
                print(turn,"won the game!! ")
                break
            elif tie_check(board) == True:
                print ("Draw match!")
                break
            else:
                turn = "player1"
                continue

    answer = input("Would you like to restart?(yes or no) ")
    if answer == "y":
        continue
    else:
        break
      
print("Thanks for playing.")