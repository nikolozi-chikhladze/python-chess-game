from board import Board
from pieces import *

class Chess:
    def __init__(self):
        self.__board = Board()
        self.__currentPlayer = 'White'
        pass

    def swapPlayers(self):
        if (self.__currentPlayer == 'White'):
            self.__currentPlayer = 'Black'
        elif (self.__currentPlayer == 'Black'):
            self.__currentPlayer = 'White'
    
    def isStringValidMove(self, moveStr):
        if (len(moveStr) == 5):
            startPosition = moveStr[0] + moveStr[1]
            endPosition = moveStr[3] + moveStr[4]
            return (startPosition, endPosition)
        else:
            printInvalidCharacterOrNumberErrorMessage()
            return None

    def play(self):
        while True:
            self.__board.displayBoard()
            print('Now is ' + self.__currentPlayer + ' player turn')
            userInput = str(input('Enter position of piece you want to move and a new position. Example: (H1 H2) '))
            if (userInput != 'EXIT'):
                result = self.isStringValidMove(userInput)
                if (
                    (result != None) and
                    validateInputByCharactersAndNumbers(result[0]) and
                    validateInputByCharactersAndNumbers(result[1])
                ):
                    result = self.__board.makeMove((result[0][0], result[0][1]), (result[1][0], result[1][1]), self.__currentPlayer)
                    if (result == True):
                        self.swapPlayers()
            else:
                print('Game over.')
                break

        pass

if __name__ == "__main__":
    game = Chess()
    game.play() 
