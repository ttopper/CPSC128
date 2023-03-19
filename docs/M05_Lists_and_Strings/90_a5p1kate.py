# a5p1xxxx.py
# 
# Determine if someone has won a game of Tic-Tac-Toe.
#
# My name
# Date

# The games we'll use to test our code:
GAMES = [
          [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],
          [['O','X',' '],['O','X',' '],[' ',' ',' ']],
          [['X','X',' '],['O',' ',' '],[' ','O',' ']],
          [['O','X',' '],['X','O',' '],[' ',' ',' ']],
          [['X',' ',' '],['O',' ','X'],[' ','O',' ']],
          [['X','O',' '],['X','O','O'],['X',' ','X']],
          [['X','O',' '],['O','O','X'],[' ','O','X']],
          [['X','O','O'],['O','X','O'],['X',' ','O']],
          [['X','X','X'],[' ','X','O'],[' ','O',' ']],
          [['X','O',' '],['O','O','O'],['X',' ','X']],
          [['X','O',' '],['O',' ','O'],['X','X','X']],
          [['X','O',' '],['O','X','O'],[' ',' ','X']],
          [['X',' ','O'],['O','O','X'],['O',' ','X']],
          [['X',' ','O'],['O',' ','X'],['O',' ','X']]
        ]
for game in GAMES:
    print('Testing ...')
    print('', game[0][0], '|', game[0][1], '|', game[0][2])
    print('---+---+---')
    print('', game[1][0], '|', game[1][1], '|', game[1][2])
    print('---+---+---')
    print('', game[2][0], '|', game[2][1], '|', game[2][2])
    
    #
    # Put your code here.
    #
    won = True
    winner = 'X'
    if won:
        print('Someone has won and it\'s', winner)
    else :
        print('No one has won.')
