import random

MAP_SIZE = 3

def draw_matrix():
    for i in range(MAP_SIZE):
        for j in range(MAP_SIZE):
            print(matrix[i][j], end=' ')
        print()
    print()

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'player1'
    else:
        return 'player2'


def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
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
        board[0][2] != " " and board [1][2] != " " and board[2][2] != " " and
        board[0][0] != " " and board [1][1] != " " and board[2][2] != " " and
        board[0][2] != " " and board [1][1] != " " and board[2][0] != " " )        


def win_check(board, letter):
    return ((board[0][0] == letter and board [0][1] == letter and board[0][2] == letter ) or
        (board[1][0] == letter and board [1][1] == letter and board[1][2] == letter ) or
        (board[2][0] == letter and board [2][1] == letter and board[2][2] == letter ) or
        (board[0][0] == letter and board [1][0] == letter and board[2][0] == letter ) or
        (board[0][1] == letter and board [1][1] == letter and board[2][1] == letter ) or
        (board[0][2] == letter and board [1][2] == letter and board[2][2] == letter ) or
        (board[0][0] == letter and board [1][1] == letter and board[2][2] == letter ) or
        (board[0][2] == letter and board [1][1] == letter and board[2][0] == letter ))

def turne(playerletter):
    if playerletter == "x":
        return "x"
    else:
        return "o"

def playermove():
    valt = []
    valt = list(input("move: "))
    valt1 = int(valt[0])
    valt2 = int(valt[1])
    matrix[valt1][valt2] = playerletter


def change_turn(turn):
    if turn == "player1":
        return "player2"
    else:
        return "player1"

print("Welcome in tic tac toe! ")

while True:
    matrix = [["⬚" for x in range (MAP_SIZE)]for y in range (MAP_SIZE)]
    player1letter, player2letter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    playerletter = None

    while True:
        playerletter = turne(playerletter)
        print ("player's "+ turn + " round! ")
        playermove()
        win_check()
        if win_check(matrix, playerletter) == True:
            print(turn,"won the game!! ")
            break
        elif tie_check() == True:
            print ("Draw match! ")
            break
        else:
            turn = change_turn(turn)
            continue

    answer = input("would you like to restart?(yes or no) ")
    if answer == "y":
        continue
    else:
        break
      
        
print("thanks for the game!! :)")
