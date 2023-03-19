# boggle.py
#
# Generate a random 4x4 boggle board for play and print it.
# There are three options printing the board.
#
# Kate Chatfield-Reed (from J Hudson)
# Winter 2023


from random import choice

# Set board size
NUM_ROWS = 4
NUM_COLS = 4

# Create an empty board
board = []
for row in range(NUM_ROWS):
    board.append([""]* NUM_COLS)

print(board)

# Pick a new random character for each position on the board
for row in range(NUM_ROWS):
    for col in range(NUM_COLS):
        board[row][col] = choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

print(board)

##for row in board:
##    print(row)
##
##for row in board:
##	output = ''
##	for letter in row:
##		output += letter + ' '
##	print(output)

