class ticTacToe:
    
    def __init__(self, boardDict = None):
        # self.boardDict = {
        #     9:'9',
        #     8:'8',
        #     7:'7',
        #     6:'6',
        #     5:'5',
        #     4:'4',
        #     3:'3',
        #     2:'2',
        #     1:'1',
        # } if boardDict == None else boardDict

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

        self.gameVersion = 1.03

    def __str__(self):
        return f"A TicTacToe game by s1b30v. v{self.gameVersion}"
        
    def printBoard(self, tttBoard):
        i = 9
        while(i in tttBoard):
            print(f"|{tttBoard[i-2]}|{tttBoard[i-1]}|{tttBoard[i]}|")
            i -= 3
        
    # IN PROGRESS: markBoard function. Marking the board from input.
    def markBoard(self, playerIp, playerMark):
        while(playerIp in self.allowedNumbers):
            self.boardDict[playerIp] = playerMark
            return

    def removeUnavailableTile(self, playerIp, availableNumbers):
        availableNumbers.remove(playerIp)
        return
            
    # TODO: Create columns checking function.
    def checkColumns(self, tttBoard):
        return

    # TODO: Create rows checking function.
    def checkRows(self, tttBoard):
        return

    # TODO: Verify function. Errorcheck and test. checkDiagonals.
    def checkDiagonals(self, tttBoard):
        return

    #//IN PROGRESS: Code a roundcounter function.
    def roundCounter(self):
        while((self.player1Turn and self.player2Turn) == 0):
            self.roundNumber = 1
            return
        while(self.player1Turn == self.player2Turn):
            self.roundNumber += 1
            return

    #//TODO: Code a player switcher.
    def playerTurn(self, nextRoundFlag):
        return