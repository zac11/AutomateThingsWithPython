"""
This is the code for the Tic Tac Toe game set up
"""

"""
This is the board structure
"""
theTicTacToeBoard={
    'top-L':'', 'top-M':'', 'top-R':'',
    'mid-L':'', 'mid-M':'', 'mid-R':'',
    'low-L':'', 'low-M':'', 'low-R':''}


"""
This method is for printing the board
"""
def printboard(board):
    print(board['top-L']+'     |'+board['top-M']+'     |'+board['top-R'])
    print('-----+-----+-----')
    print(board['mid-L']+'     |'+board['mid-M']+'     |'+board['mid-R'])
    print('-----+-----+-----')
    print(board['low-L']+'     |'+board['low-M']+'     |'+board['low-R'])

printboard(theTicTacToeBoard)

"""
The print board can handle any kind of dictionary structured data for the tic tac toe game
"""

theNewTicTacToeBoard={
    'top-L':'0', 'top-M':'0', 'top-R':'',
    'mid-L':'', 'mid-M':'X', 'mid-R':'0',
    'low-L':'', 'low-M':'', 'low-R':'X'}

printboard(theNewTicTacToeBoard)



