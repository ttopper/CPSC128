minesweeper_board = [
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 2, 'M', 2, 1, 1, 0, 0],
    [0, 1, 'M', 3, 2, 3, 'M', 1, 0, 0],
    [0, 1, 2, 2, 'M', 3, 2, 2, 1, 1],
    [0, 1, 1, 2, 1, 2, 'M', 2, 'M', 1],
    [0, 1, 'M', 1, 0, 1, 2, 3, 2, 1],
    [0, 2, 3, 2, 0, 0, 1, 'M', 1, 0],
    [0, 1, 'M', 1, 0, 1, 2, 2, 1, 0],
    [0, 1, 1, 1, 0, 1, 'M', 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0]
]

def display_board(minesweeper_board):
    '''A function that prints a minesweeper board (list of lists) in
    a human readable format.'''
    for r in range(len(minesweeper_board)):
        print()
        for c in range(len(minesweeper_board)):
            print(minesweeper_board[r][c], end = ' ')
    return None


def minesweeper_mistakes(minesweeper_board):
    '''Add comment here.'''
    pass

if __name__ == '__main__':
    display_board(minesweeper_board)
    print()
    print(minesweeper_mistakes(minesweeper_board))

            
