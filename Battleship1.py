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
#print ship_row
#print ship_col

turn = 0

for turn in range(4):

    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Col: "))


    #This checks if you guessed correctly.
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulation! You sank my battleship"
        break

    else:

        #This checks if you guessed within the 5x5 grid.
        if guess_col not in range(0, len(board)) or guess_row not in range(0, len(board)):
            print "Oops, that's not even in the ocean."

        #This checks if you have already guessed in that location.
        elif board[guess_col][guess_row] == "X":
            print "You guessed that one already."

        #This tell you, you missed and it marks that spot as "X".
        else:
            print "You missed my battleship!"
            board[guess_col][guess_row] = "X"

        turn += 1
        print "Your turn is %s" % turn

        #TODO: delete this turn in final code
        print turn
        print_board(board)

        if turn == 4:
            print "Game is over! You have run out of turns."
            print "Game Over"

'''


You can also add on to your Battleship! program to make it more complex and fun to play.
Here are some ideas for enhancements—maybe you can think of some more!

1.
    Make multiple battleships: you'll need to be careful because you need to make sure
    that you don’t place battleships on top of each other on the game board.
    You'll also want to make sure that you balance the size of the board with
    the number of ships so the game is still challenging and fun to play.

2.
    Make battleships of different sizes: this is trickier than it sounds.
    All the parts of the battleship need to be vertically or horizontally
    touching and you’ll need to make sure you don’t accidentally place part
    of a ship off the side of the board.

3.
    Make your game a two-player game.

4.
    Use functions to allow your game to have more features like rematches, statistics and more!

Some of these options will be easier after we cover loops in the next lesson.
Think about coming back to Battleship! after a few more lessons
and see what other changes you can make!


'''
