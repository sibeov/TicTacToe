#AUTHOR: Sindre Bergsvik Øvstegård
#YEAR: 2020

#########################################################################
#COMMENTS: nameOfProgram.py starts here.
#########################################################################

#########################################################################
#CODE_START:
#########################################################################

#########################################################################
#IMPORTS:
#########################################################################
from sample import tictactoe_module
import time
import pdb
import re

#########################################################################
#TIMER START:
#########################################################################
startTime = time.perf_counter()

#########################################################################
#GLOBAL VARS:
#########################################################################
tttGame = tictactoe_module.ticTacToe()
tttBoard = tttGame.boardDict

playerNum = 1
result = (0, 0)
playerInput = "Gibberish"


#########################################################################
#FUNCTIONS DEF: Some helper functions.
#########################################################################
def playerSwitcher(playerNumber):
    while(playerNumber <= 1):
        return 2
    while(playerNumber >= 2):
        return 1

#########################################################################
#MAIN STARTS HERE:
#########################################################################

# Main game loop:
while(True):

    # Print board part.
    tttGame.printBoard(tttBoard)

    # Player input part.
    playerInput = int(input(f"Player{playerNum} input number [1-9] -> "))
    while(playerInput not in tttGame.availableNumbers):
        playerInput = int(input(f"Player{playerNum} input number [1-9] -> "))

    # Mark board and remove marked tile.
    tttGame.markBoard(playerInput, playerNum)
    tttGame.removeUnavailableTile(playerInput)

    # Check board for three in row.
    # BUG: Does not detect winner. Scope issue?
    while(result == (0, 0)):
        result = tttGame.checkColumns(tttBoard)
        result = tttGame.checkRows(tttBoard)
        result = tttGame.checkDiagonals(tttBoard)
        break

    # Print winner and exit game:
    while(result != (0, 0)):
        while(result[1] == 'X'):
            print(f"Player 1 is the winner!")
        while(result[1] == 'O'):
            print(f"Player 2 is the winner!")

    playerNum = playerSwitcher(playerNum)

endTime = time.perf_counter()
print(f"Runtime: {startTime - endTime}s")
#########################################################################
#CODE_END: nameOfProgram.py starts here.
#########################################################################