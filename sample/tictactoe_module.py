import unittest


class ticTacToe:

    def __init__(self, boardDict=None):

        self.boardDict = {
            9: ' ',
            8: ' ',
            7: ' ',
            6: ' ',
            5: ' ',
            4: ' ',
            3: ' ',
            2: ' ',
            1: ' ',
        } if boardDict == None else boardDict

        self.allowedNumbers = (9, 8, 7, 6, 5, 4, 3, 2, 1)
        self.availableNumbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]

        self.player1Mark = 'X'
        self.player2Mark = 'O'

        self.gameVersion = 1.2

    def __str__(self):
        return f"A TicTacToe game by s1b30v. v{self.gameVersion}"

    def printBoard(self, tttBoard):
        i = 9
        while(i in tttBoard):
            print(f"|{tttBoard[i-2]}|{tttBoard[i-1]}|{tttBoard[i]}|")
            i -= 3

    def printRoundNumber(self):
        print(f"Round: {self.roundNumber}")

    def markBoard(self, playerIp, player):
        while(playerIp in self.allowedNumbers):
            while(player == 1):
                self.boardDict[playerIp] = 'X'
                return 1
            while(player == 2):
                self.boardDict[playerIp] = 'O'
                return 1
        return 0

    def removeUnavailableTile(self, playerIp):
        while(playerIp in self.availableNumbers):
            self.availableNumbers.remove(playerIp)
            return 1
        return 0

    # PENDING: Check function Columns.
    def checkColumns(self, tttBoard):
        i = 9
        while(i > 6 and i < 10):
            while(tttBoard[i] == tttBoard[i-3] == tttBoard[i-6]):
                if(tttBoard[i] == ' '):
                    break
                return (1, tttBoard[i])
            i -= 1
        return (0, 0)

    # PENDING: Check function Rows.
    def checkRows(self, tttBoard):
        i = 9
        while(i > 2 and i < 10):
            while(tttBoard[i] == tttBoard[i-1] == tttBoard[i-2]):
                if(tttBoard[i] == ' '):
                    break
                return (1, tttBoard[i])
            i -= 3
        return (0, 0)

    # PENDING: Check function diagonals.
    def checkDiagonals(self, tttBoard):
        while(tttBoard[1] == tttBoard[5] == tttBoard[9]):
            if(tttBoard[5] == ' '):
                break
            return (1, tttBoard[5])
        while(tttBoard[3] == tttBoard[5] == tttBoard[7]):
            if(tttBoard[5] == ' '):
                break
            return (1, tttBoard[5])
        return (0, 0)
