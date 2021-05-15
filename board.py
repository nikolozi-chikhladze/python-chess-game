from pieces import *

class Board:

    def __init__(self):
        self.placePieces()

    def placePieces(self):
        self.pieces = {
            'White': {
                'pawn1': {
                    'isAlive': True,
                    'instance': Pawn('White', self, ('G', '1'))
                },
                'pawn2': {
                    'isAlive': True,
                    'instance': Pawn('White', self, ('G', '2'))
                },
                'pawn3': {
                    'isAlive': True,
                    'instance': Pawn('White', self, ('G', '3'))
                },
                'pawn4': {
                    'isAlive': True,
                    'instance': Pawn('White', self, ('G', '4'))
                },
                'pawn5': {
                    'isAlive': True,
                    'instance': Pawn('White', self, ('G', '5'))
                },
                'pawn6': {
                    'isAlive': True,
                    'instance': Pawn('White', self, ('G', '6'))
                },
                'pawn7': {
                    'isAlive': True,
                    'instance': Pawn('White', self, ('G', '7'))
                },
                'pawn8': {
                    'isAlive': True,
                    'instance': Pawn('White', self, ('G', '8'))
                },
                'rook1': {
                    'isAlive': True,
                    'instance': Rook('White', self, ('H', '1'))
                },
                'rook2': {
                    'isAlive': True,
                    'instance': Rook('White', self, ('H', '8'))
                },
                'knight1': {
                    'isAlive': True,
                    'instance': Knight('White', self, ('H', '2'))
                },
                'knight2': {
                    'isAlive': True,
                    'instance': Knight('White', self, ('H', '7'))
                },
                'bishop1': {
                    'isAlive': True,
                    'instance': Bishop('White', self, ('H', '3'))
                },
                'bishop2': {
                    'isAlive': True,
                    'instance': Bishop('White', self, ('H', '6'))
                },
                'queen': {
                    'isAlive': True,
                    'instance': Queen('White', self, ('H', '4'))
                },
                'king': {
                    'isAlive': True,
                    'instance': King('White', self, ('H', '5'))
                }
            },
            'Black': {
                'pawn1': {
                    'isAlive': False,
                    'instance': Pawn('Black', self, ('B', '1'))
                },
                'pawn2': {
                    'isAlive': False,
                    'instance': Pawn('Black', self, ('B', '2'))
                },
                'pawn3': {
                    'isAlive': True,
                    'instance': Pawn('Black', self, ('B', '3'))
                },
                'pawn4': {
                    'isAlive': True,
                    'instance': Pawn('Black', self, ('B', '4'))
                },
                'pawn5': {
                    'isAlive': True,
                    'instance': Pawn('Black', self, ('B', '5'))
                },
                'pawn6': {
                    'isAlive': True,
                    'instance': Pawn('Black', self, ('B', '6'))
                },
                'pawn7': {
                    'isAlive': True,
                    'instance': Pawn('Black', self, ('B', '7'))
                },
                'pawn8': {
                    'isAlive': True,
                    'instance': Pawn('Black', self, ('B', '8'))
                },
                'rook1': {
                    'isAlive': False,
                    'instance': Rook('Black', self, ('A', '1'))
                },
                'rook2': {
                    'isAlive': True,
                    'instance': Rook('Black', self, ('A', '8'))
                },
                'knight1': {
                    'isAlive': True,
                    'instance': Knight('Black', self, ('A', '2'))
                },
                'knight2': {
                    'isAlive': True,
                    'instance': Knight('Black', self, ('A', '7'))
                },
                'bishop1': {
                    'isAlive': True,
                    'instance': Bishop('Black', self, ('A', '3'))
                },
                'bishop2': {
                    'isAlive': True,
                    'instance': Bishop('Black', self, ('A', '6'))
                },
                'queen': {
                    'isAlive': True,
                    'instance': Queen('Black', self, ('A', '4'))
                },
                'king': {
                    'isAlive': True,
                    'instance': King('Black', self, ('A', '5'))
                }
            }
        }

    def setPiece(self, position, piece):
        for player in self.pieces:
            for pieceName in self.pieces.get(player):
                object = self.pieces.get(player).get(pieceName)
                if (object['instance'].getPosition() == position):
                    object['instance'] = piece

    def getPiece(self, position):
        result = None
        for player in self.pieces:
            for pieceName in self.pieces.get(player):
                object = self.pieces.get(player).get(pieceName)
                if (object['isAlive'] and object['instance'].getPosition() == position):
                    result = object['instance']

        return result


    def makeMove(self, startPosition, endPosition, player):
        # print('player: ', player)
        # print('pieces: ', self.pieces.get(player))
        pieces = self.pieces.get(player)
        # print('pieces: ', pieces)
        for pieceName in pieces:
            piece = pieces.get(pieceName)['instance']
            # print('piece position: ', piece.getPosition())
            # print('start position: ', startPosition)
            if (piece.getPosition() == startPosition):
                # print('Found piece: ', piece)
                return piece.move(endPosition)
        return False

    def displayBoard(self):
        columnCounter = 0
        rowCounter = 0
        stringToPrint = ''
        while rowCounter < (len(validNumbers) + 1):
            while columnCounter < (len(validCharacters) + 1):
                if (rowCounter == 0 and columnCounter == 0):
                    stringToPrint += '   '
            
                if (rowCounter == 0 and columnCounter != len(validNumbers)):
                    stringToPrint += '(' + validNumbers[columnCounter] + ')'
                elif (rowCounter != 0 and columnCounter == 0):
                    stringToPrint += '(' + validCharacters[rowCounter - 1] + ')'
                elif (
                    (rowCounter > 0 and rowCounter <= len(validNumbers)) or
                    (columnCounter > 0 and columnCounter < len(validCharacters))
                ):
                    found = False
                    for color in self.pieces:
                        for pieceName in self.pieces.get(color):
                            piece = self.pieces.get(color).get(pieceName)
                            if (
                                (validCharacters.index(piece['instance'].getPosition()[0]) == rowCounter - 1) and
                                (validNumbers.index(piece['instance'].getPosition()[1]) == columnCounter - 1) and
                                (piece['isAlive'] == True)
                            ):
                                found = True
                                stringToPrint += '[' + piece['instance'].getIcon() + ']'
                    if (not found):
                        stringToPrint += '[ ]'
                    
                columnCounter += 1
            rowCounter += 1
            columnCounter = 0
            print(stringToPrint)
            stringToPrint = ''
        return
            