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

#########################################################################
#GLOBAL VARS:
#########################################################################

#########################################################################
#FUNCTIONS DEF:
#########################################################################

#########################################################################
#MAIN STARTS HERE:
#########################################################################
startTime = time.perf_counter()

tttGame = tictactoe_module.ticTacToe()
playerNumber = 

while(True):
    tttGame.printBoard()
    tttGame.markBoard(input(f"Player {} -> Enter number: "), playerNumber)

endTime = time.perf_counter()
print(f"Runtime: {startTime - endTime}s")
#########################################################################
#CODE_END: nameOfProgram.py starts here.
#########################################################################