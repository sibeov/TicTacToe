class ticTacToe:
    
    def __init__(self, boardDict = None):

        self.boardDict = {
            9:' ',
            8:' ',
            7:' ',
            6:' ',
            5:' ',
            4:' ',
            3:' ',
            2:' ',
            1:' ',
        } if boardDict == None else boardDict
        
        self.allowedNumbers = (9,8,7,6,5,4,3,2,1)
        self.availableNumbers = [9,8,7,6,5,4,3,2,1]

        self.player1Mark = 'X'
        self.player2Mark = 'O'

        self.player1Turn = 0
        self.player2Turn = 0
        self.roundNumber = 1

        self.gameVersion = 1.04

    def __str__(self):
        return f"A TicTacToe game by s1b30v. v{self.gameVersion}"
        
    def printBoard(self, tttBoard):
        i = 9
        while(i in tttBoard):
            print(f"|{tttBoard[i-2]}|{tttBoard[i-1]}|{tttBoard[i]}|")
            i -= 3
    
    # PENDING: Check function.
    def printRoundNumber(self):
        print(f"Round: {self.roundNumber}")
        
    # IN PROGRESS: markBoard function. Marking the board from input.
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
    
    # PENDING: Checker functions.
    # PENDING: Check function Columns.
    def checkColumns(self, tttBoard):
        i = 9
        while(i in self.allowedNumbers):
            while(tttBoard[i-6] == tttBoard[i-3] == tttBoard[i]):
                return 1
            i -= 1
        return 0

    # PENDING: Check function Rows.
    def checkRows(self, tttBoard):
        i = 9
        while(i in self.allowedNumbers):
            while(tttBoard[i-2] == tttBoard[i-1] == tttBoard[i]):
                return 1
            i -= 1
        return 0

    # PENDING: Check function diagonals.
    def checkDiagonals(self, tttBoard):
        i = 1
        while(i in self.allowedNumbers):
            while(tttBoard[i] == tttBoard[5] == tttBoard[i+6]):
                return 1
            i += 3
        return 0