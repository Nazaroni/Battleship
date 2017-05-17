from random import randint

#game board "Ocean"
board = []

for _ in range(0, 5):
    board.append(["O"] * 5)


def print_board(board):
    for row in board:
        print " ".join(row)


def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

turn = 0

for turn in range(4):

    turn += 1


    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Col: "))


    #This checks if you guessed correctly
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulation! You sank my battleship"

    else:

        if guess_col and guess_row not in range(0, len(board) -1):
            print "Oops, that's not even in the ocean."

        elif board[guess_col][guess_row] == "X":
            print "You guessed that one already."

        else:
            print "You missed my battleship!"
            board[guess_col][guess_row] = "X"

        print "Your turn is %s" % turn
        print turn
        print_board(board)
