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


#########################################################################
#TIMER START:
#########################################################################
startTime = time.perf_counter()

#########################################################################
#GLOBAL VARS:
#########################################################################

#########################################################################
#FUNCTIONS DEF:
#########################################################################
def playerSwitcher(playerNumber):
    while(playerNumber <= 1):
        return 2
    while(playerNumber >= 2):
        return 1

#########################################################################
#MAIN STARTS HERE:
#########################################################################

tttGame = tictactoe_module.ticTacToe()
player = 1

# Main game loop:
while(True):
    tttGame.printBoard(tttGame.boardDict)

    playerInput = int(input(f"Player {player} -> Enter number [1 -> 9]: "))
    while(type(playerInput) != int):
        playerInput = int(input(f"Player {player} -> Enter number [1 -> 9]: "))

    tttGame.markBoard(playerInput, player)
    
    player = playerSwitcher(player)


endTime = time.perf_counter()
print(f"Runtime: {startTime - endTime}s")
#########################################################################
#CODE_END: nameOfProgram.py starts here.
#########################################################################