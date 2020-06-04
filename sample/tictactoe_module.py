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

        self.gameVersion = 1.03

    def __str__(self):
        return f"A TicTacToe game by s1b30v. v{self.gameVersion}"
        
    def printBoard(self):
        i = 9
        while(i in self.boardDict):
            print(f"|{self.boardDict[i-2]}|{self.boardDict[i-1]}|{self.boardDict[i]}|")
            i -= 3
        
    def markBoard(self, playerNumber, playerIp):
        while(playerIp in self.allowedNumbers):
            while(playerIp in self.availableNumbers and playerNumber == 1):
                self.availableNumbers.remove(playerIp)
                self.boardDict[playerIp] = self.player1Mark
                return 1
            while(playerIp in self.availableNumbers and playerNumber == 2):
                self.availableNumbers.remove(playerIp)
                self.boardDict[playerIp] = self.player2Mark
                return 1
            return 0

            
    #//TODO: Create a row checking function.
    def checkRows(self):
        pass

    #//TODO: Code a roundcounter function.
    def roundCounter(self):
        while((self.player1Turn and self.player2Turn) == 0):
            self.roundNumber = 1
            return
        while(self.player1Turn == self.player2Turn):
            self.roundNumber += 1
            return

    #//TODO: Code a player switcher.
    def playerTurn(self, nextRoundFlag):
        