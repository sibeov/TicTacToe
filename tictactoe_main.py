'''
####################################################################################
Author: Sindre Bergsvik Øvstegård
Year: 2020

FileName:           tictactoe_main.py
Dependencies:       ./module/tictactoe_module.py
Design Software:    Microsoft Visual Studio Vode Insiders - v1-48.0-Insider

Python CODE IS PROVIDED 'AS IS.' Sindre Bergsvik Øvstegård DISCLAIMS ANY
WARRANTY OF ANY KIND, WHETHER EXPRESS OR IMPLIED, INCLUDING BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE, OR NON-INFRINGEMENT. IN NO EVENT SHALL Sindre Bergsvik Øvstegård
BE LIABLE FOR ANY INCIDENTAL, SPECIAL, INDIRECT OR CONSEQUENTIAL
DAMAGES, LOST PROFITS OR LOST DATA, HARM TO YOUR EQUIPMENT, COST OF
PROCUREMENT OF SUBSTITUTE GOODS, TECHNOLOGY OR SERVICES, ANY CLAIMS
BY THIRD PARTIES (INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF),
ANY CLAIMS FOR INDEMNITY OR CONTRIBUTION, OR OTHER SIMILAR COSTS.

Comments:
The goal of this project was to become more familiar with classes and interfacing.
Also I tried to use while loops as the main "logic checker". As a personal
challange.

Version History
Version 1.0 - 03.08.2020 - Sindre Bergsvik Øvstegård
  Initial Public Release.
  Known bugs:
    - Drawlogic not implemented.
    - PlayerX wins when there is a draw.
#####################################################################################
'''

#####################################################################################
# CODE_START: tictactoe_main.py
#####################################################################################

#####################################################################################
# IMPORTS:
#####################################################################################
from sample import tictactoe_module
import pdb
import re

#####################################################################################
# GLOBAL VARS:
#####################################################################################
tttGame = tictactoe_module.ticTacToe()
tttBoard = tttGame.boardDict

playerNum = 1
result = (0, 0)
playerInput = "Gibberish"


#####################################################################################
# FUNCTIONS DEF: Some helper functions.
#####################################################################################
def playerSwitcher(playerNumber):
    while(playerNumber <= 1):
        return 2
    while(playerNumber >= 2):
        return 1

#####################################################################################
# MAIN STARTS HERE:
#####################################################################################


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
    while(result == (0, 0)):
        result = tttGame.checkColumns(tttBoard)
        if(result != (0, 0)):
            break
        result = tttGame.checkRows(tttBoard)
        if(result != (0, 0)):
            break
        result = tttGame.checkDiagonals(tttBoard)
        if(result != (0, 0)):
            break
        break

    # Print winner and exit game:
    while(result != (0, 0)):
        while(result[1] == 'X'):
            tttGame.printBoard(tttBoard)
            print(f"Player 1 is the winner!")
            exit()
        while(result[1] == 'O'):
            tttGame.printBoard(tttBoard)
            print(f"Player 2 is the winner!")
            exit()
        break

    # TODO: Fix draw logic.
    if(not tttGame.availableNumbers):
        print("Draw!")
        exit()

    playerNum = playerSwitcher(playerNum)

#####################################################################################
# CODE_END: tictactoe_main.py starts here.
#####################################################################################
