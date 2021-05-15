
blackIcons = {"Pawn" : "♙", "Rook" : "♖", "Knight" : "♘", "Bishop" : "♗", "King" : "♔", "Queen" : "♕" }
whiteIcons = {"Pawn" : "♟", "Rook" : "♜", "Knight" : "♞", "Bishop" : "♝", "King" : "♚", "Queen" : "♛" }

validCharacters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
validNumbers = ['1', '2', '3', '4', '5', '6', '7', '8']

# Validations
def validateInputByLengthAndType(value, length, passedType):
    return (len(value) == length and type(value) is passedType)

def validateInputByCharactersAndNumbers(value, validCharacters = validCharacters, validNumbers = validNumbers):
    return (value[0] in validCharacters and value[1] in validNumbers)

# Error messages
def printInputLengthAndTypeErrorMessage():
    print('Function input validation for length and type failed. Try again.')

def printInvalidCharacterOrNumberErrorMessage():
    print('Character or number input has invalid value. Try again.')

def printInvalidMovementErrorMessage(pieceName, errorIn = 'position'):
    print('Invalid movement for piece "', pieceName, '". It cant move on given ', errorIn,'.')

# Knight
def validateKnightMovement(pieceName, oldPosition, newPosition):
    if (
        (validCharacters.index(newPosition[0]) == (validCharacters.index(oldPosition[0]) + 2)) or
        (validCharacters.index(newPosition[0]) == (validCharacters.index(oldPosition[0]) - 2)) or
        (validCharacters.index(newPosition[0]) == (validCharacters.index(oldPosition[0]) + 1)) or
        (validCharacters.index(newPosition[0]) == (validCharacters.index(oldPosition[0]) - 1)) 
    ):
        if (
            (validNumbers.index(newPosition[1]) == (validNumbers.index(oldPosition[1]) + 2)) or
            (validNumbers.index(newPosition[1]) == (validNumbers.index(oldPosition[1]) - 2)) or
            (validNumbers.index(newPosition[1]) == (validNumbers.index(oldPosition[1]) + 1)) or
            (validNumbers.index(newPosition[1]) == (validNumbers.index(oldPosition[1]) - 1)) 
        ):
            return True
        else:
            printInvalidMovementErrorMessage(pieceName, 'Number')
    else:
            printInvalidMovementErrorMessage(pieceName, 'Character')

    return False

# Rook
def validateRookMovement(pieceName, oldPosition, newPosition):
    if (
            (
                newPosition[0] == oldPosition[0] and 
                newPosition[1] != oldPosition[1]
            ) or 
            (
                newPosition[0] != oldPosition[0] and 
                newPosition[1] == oldPosition[1]
            )
        ):
            return True
    else:
        printInvalidMovementErrorMessage(pieceName)
    
    return False

# Bishop
def bishopMoveCondition(oldPosition, newPosition, value, action):
    if (action == '+'):
        return (
                    (validCharacters.index(newPosition[0]) == (validCharacters.index(oldPosition[0]) + value)) and
                    (
                        (validNumbers.index(newPosition[1]) == validNumbers.index(oldPosition[1]) + value) or
                        (validNumbers.index(newPosition[1]) == validNumbers.index(oldPosition[1]) - value)
                    )
                )
    elif (action == '-'):
        return (
                    (validCharacters.index(newPosition[0]) == (validCharacters.index(oldPosition[0]) - value)) and
                    (
                        (validNumbers.index(newPosition[1]) == validNumbers.index(oldPosition[1]) + value) or
                        (validNumbers.index(newPosition[1]) == validNumbers.index(oldPosition[1]) - value)
                    )
                )

def validateBishopMovement(pieceName, oldPosition, newPosition):
    if (
        bishopMoveCondition(oldPosition, newPosition, 1, '+') or
        bishopMoveCondition(oldPosition, newPosition, 2, '+') or
        bishopMoveCondition(oldPosition, newPosition, 3, '+') or
        bishopMoveCondition(oldPosition, newPosition, 4, '+') or
        bishopMoveCondition(oldPosition, newPosition, 5, '+') or
        bishopMoveCondition(oldPosition, newPosition, 6, '+') or
        bishopMoveCondition(oldPosition, newPosition, 7, '+') or
        bishopMoveCondition(oldPosition, newPosition, 1, '-') or
        bishopMoveCondition(oldPosition, newPosition, 2, '-') or
        bishopMoveCondition(oldPosition, newPosition, 3, '-') or
        bishopMoveCondition(oldPosition, newPosition, 4, '-') or
        bishopMoveCondition(oldPosition, newPosition, 5, '-') or
        bishopMoveCondition(oldPosition, newPosition, 6, '-') or
        bishopMoveCondition(oldPosition, newPosition, 7, '-')
    ):
        return True
    else:
        printInvalidMovementErrorMessage(pieceName)

    return False

# Queen
def validateQueenMovement(pieceName, oldPosition, newPosition):
    if (
        validateBishopMovement(pieceName, oldPosition, newPosition) or
        validateRookMovement(pieceName, oldPosition, newPosition)
    ):
        return True
    else:
        printInvalidMovementErrorMessage(pieceName)

    return False

# King
def validateKingMovement(pieceName, oldPosition, newPosition):
    if (
        bishopMoveCondition(oldPosition, newPosition, 1, '+') or
        bishopMoveCondition(oldPosition, newPosition, 1, '-') or
        (
            (newPosition[0] == oldPosition[0]) and
            (
                (
                    (validNumbers.index(newPosition[1]) == validNumbers.index(oldPosition[1]) + 1) or
                    (validNumbers.index(newPosition[1]) == validNumbers.index(oldPosition[1]) - 1)
                )
            )
        ) or
        (
            (newPosition[1] == oldPosition[1]) and
            (
                (validNumbers.index(newPosition[0]) == validNumbers.index(oldPosition[0]) + 1) or
                (validNumbers.index(newPosition[0]) == validNumbers.index(oldPosition[0]) - 1)
            )
        )
    ):
        return True
    else:
        printInvalidMovementErrorMessage(pieceName)

    return False

# Pawn
def validatePawnMovement(pieceName, oldPosition, newPosition, color):
    if(
        color == 'White' and
        (oldPosition[0] == 'G')
    ):
        if(
            (validCharacters.index(newPosition[0]) == validCharacters.index(oldPosition[0]) - 1) or
            (validCharacters.index(newPosition[0]) == validCharacters.index(oldPosition[0]) - 2) or
            (validCharacters.index(newPosition[0]) == validCharacters.index(oldPosition[0]) - 6) or
            (
                (validCharacters.index(newPosition[0]) == validCharacters.index(oldPosition[0]) - 1) and
                (
                    (validCharacters.index(newPosition[1]) == validCharacters.index(oldPosition[1]) + 1) or
                    (validCharacters.index(newPosition[1]) == validCharacters.index(oldPosition[1]) - 1)
                )
            )
        ):
            return True
    elif (
        color == 'White' and
        (oldPosition[0] != 'G')
    ):
        if(
            (validCharacters.index(newPosition[0]) == validCharacters.index(oldPosition[0]) - 1) or
            (
                (validCharacters.index(newPosition[0]) == validCharacters.index(oldPosition[0]) - 1) and
                (
                    (validCharacters.index(newPosition[1]) == validCharacters.index(oldPosition[1]) + 1) or
                    (validCharacters.index(newPosition[1]) == validCharacters.index(oldPosition[1]) - 1)
                )
            )
        ):
            return True
    elif(
        color == 'Black' and
        (oldPosition[0] == 'B')
    ):
        if (
            (validCharacters.index(newPosition[0]) == validCharacters.index(oldPosition[0]) + 1) or
            (validCharacters.index(newPosition[0]) == validCharacters.index(oldPosition[0]) + 2) or
            (
                (validCharacters.index(newPosition[0]) == validCharacters.index(oldPosition[0]) + 1) and
                (
                    (validCharacters.index(newPosition[1]) == validCharacters.index(oldPosition[1]) + 1) or
                    (validCharacters.index(newPosition[1]) == validCharacters.index(oldPosition[1]) - 1)
                )
            )
        ):
            return True
    elif(
        color == 'Black' and
        (oldPosition[0] != 'B')
    ):
        if (
            (validCharacters.index(newPosition[0]) == validCharacters.index(oldPosition[0]) + 1) or
            (
                (validCharacters.index(newPosition[0]) == validCharacters.index(oldPosition[0]) + 1) and
                (
                    (validCharacters.index(newPosition[1]) == validCharacters.index(oldPosition[1]) + 1) or
                    (validCharacters.index(newPosition[1]) == validCharacters.index(oldPosition[1]) - 1)
                )
            )
        ):
            return True
    else:
        printInvalidMovementErrorMessage(pieceName)

    return False

# Action
def validatePieceMovement(pieceName, oldPosition, newPosition, color = 'White', canKill = False):
    if (newPosition != oldPosition):
        if (pieceName == 'Knight'):
            # check if position is possible for knight movement
            return validateKnightMovement(pieceName, oldPosition, newPosition)
        elif (pieceName == 'Rook'):
            # check if position is possible for rook movement
            return validateRookMovement(pieceName, oldPosition, newPosition)
        elif (pieceName == 'Bishop'):
            # check if position is possible for bishop movement
            return validateBishopMovement(pieceName, oldPosition, newPosition)
        elif (pieceName == 'Queen'):
            # check if position is possible for queen movement
            return validateQueenMovement(pieceName, oldPosition, newPosition)
        elif (pieceName == 'King'):
            # check if position is possible for king movement
            return validateKingMovement(pieceName, oldPosition, newPosition)
        elif (pieceName == 'Pawn'):
            # check if position is possible for pawn movement
            return validatePawnMovement(pieceName, oldPosition, newPosition, color)
    else:
        print('Cant move in the same place')
        return False

def moveHelper(checkMove, position, pieces, color, instance):
    if (checkMove(position)):
        for pieceName in pieces.get(color):
            piece = pieces.get(color).get(pieceName)['instance']
            if (piece == instance):
                piece.setPosition(position)

        return True
    else:
        return False

def blockCheckHelper(pieces, position):
    moveBlocked = False
    for player in pieces:
        for pieceName in pieces.get(player):
            if (
                (pieces.get(player).get(pieceName)['isAlive'] == True) and
                (pieces.get(player).get(pieceName)['instance'].getPosition() == position)
            ):
                moveBlocked = True
    return moveBlocked

def pieceKillMove(pieces, color, newPosition):
    for pieceObject in pieces.get(color):
        if (
            (pieces.get('Black').get(pieceObject)['instance'].getPosition()[0] == newPosition[0]) and 
            (pieces.get('Black').get(pieceObject)['instance'].getPosition()[1] == newPosition[1])
        ):
            pieceToDelete = pieces.get(color).get(pieceObject)
            pieceToDelete['isAlive'] = False
            return True
    return False

def pieceKillHelper(pieces, pieceName, pieceColor, newPosition):
    if (pieceColor == 'White'):
        return pieceKillMove(pieces, 'Black', newPosition)
    elif (pieceColor == 'Black'):
        return pieceKillMove(pieces, 'White', newPosition)

def validateNewPieceInput(input):
    return (
        len(input) > 0 and
        (
            (input == 'Knight') or
            (input == 'Rook') or
            (input == 'Bishop') or
            (input == 'Queen') 
        )
    )

def pawnPromotion(board, piece, newPosition):
    for pieceObject in board.pieces.get(piece.getColor()):
        if (board.pieces.get(piece.getColor()).get(pieceObject)['instance'] == piece):
            newPieceName = str(input('Enter new piece: '))
            while not validateNewPieceInput(newPieceName):
                newPieceName = str(input('Enter new piece: '))

            if (newPieceName == 'Knight'):
                oldPiece = board.pieces.get(piece.getColor()).get(pieceObject)
                newKnight = Knight(oldPiece['instance'].getColor(), board, newPosition)
                oldPiece['isAlive'] = True
                oldPiece['instance'] = newKnight

            elif (newPieceName == 'Queen'):
                oldPiece = board.pieces.get(piece.getColor()).get(pieceObject)
                newQueen = Queen(oldPiece['instance'].getColor(), board, newPosition)
                oldPiece['isAlive'] = True
                oldPiece['instance'] = newQueen

            elif (newPieceName == 'Bishop'):
                oldPiece = board.pieces.get(piece.getColor()).get(pieceObject)
                newBishop = Bishop(oldPiece['instance'].getColor(), board, newPosition)
                oldPiece['isAlive'] = True
                oldPiece['instance'] = newBishop

            elif (newPieceName == 'Rook'):
                oldPiece = board.pieces.get(piece.getColor()).get(pieceObject)
                newRook = Rook(oldPiece['instance'].getColor(), board, newPosition)
                oldPiece['isAlive'] = True
                oldPiece['instance'] = newRook

    return


class Piece:
    def __init__(self, color, board, position):
        self.__color = color
        self.__position = position;
        self.board = board;
        pass

    def checkMove(self, dest):
        return False

    def move(self, dest):
        return False
        
    def getName(self):
        return self.__class__.__name__

    def getIcon(self):
        return None

    def getColor(self):
        return self.__color

    def getPosition(self):
        return self.__position

    def setPosition(self, value):
        if (validateInputByLengthAndType(value, 2, tuple)):
            if (validateInputByCharactersAndNumbers(value)):
                self.__position = (value[0], value[1])
            else:
                printInvalidCharacterOrNumberErrorMessage();
                return
            return
        else:
            printInputLengthAndTypeErrorMessage();
                

    property(getColor)
    property(getPosition, setPosition)

class Knight(Piece):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)

    def checkMove(self, dest):
        # function input validation
        if (validateInputByLengthAndType(dest, 2, tuple)):
            if (validateInputByCharactersAndNumbers(dest)):
                if (validatePieceMovement(self.getName(), self.getPosition(), dest)):
                    # get all other pieces and check if it can kill or is blocked
                    moveBlocked = blockCheckHelper(self.board.pieces, dest)
                    if (moveBlocked):
                        if (pieceKillHelper(self.board.pieces, self.getName(), self.getColor(), dest)):
                            return True
                        else:
                            printInvalidMovementErrorMessage(self.getName())
                            return False
                    return (not moveBlocked)
                else:
                    printInvalidMovementErrorMessage(self.getName());
            else:
                printInvalidCharacterOrNumberErrorMessage();
        else:
            printInputLengthAndTypeErrorMessage();

        return False

    def getIcon(self):
        if (self.getColor() == 'White'):
            return whiteIcons.get(self.getName())
        elif (self.getColor() == 'Black'):
            return blackIcons.get(self.getName())

    def move(self, dest):
        return moveHelper(self.checkMove, dest, self.board.pieces, self.getColor(), self)
       
        
class Rook(Piece):

    def __init__(self, color, board, position):
        super().__init__(color, board, position)

    def checkMove(self, dest):
        if (validateInputByLengthAndType(dest, 2, tuple)):
            if (validateInputByCharactersAndNumbers(dest)):
                if (validatePieceMovement(self.getName(), self.getPosition(), dest)):
                    # get other pieces from board and check if any of them interupts movement
                    moveBlocked = blockCheckHelper(self.board.pieces, dest)
                    if (moveBlocked):
                        if (pieceKillHelper(self.board.pieces, self.getName(), self.getColor(), dest)):
                            return True
                        else:
                            printInvalidMovementErrorMessage(self.getName())
                            return False
                    return (not moveBlocked)
                else:
                    printInvalidMovementErrorMessage(self.getName());
            else:
                printInvalidCharacterOrNumberErrorMessage();
        else:
            printInputLengthAndTypeErrorMessage();

    def getIcon(self):
        if (self.getColor() == 'White'):
            return whiteIcons.get(self.getName())
        elif (self.getColor() == 'Black'):
            return blackIcons.get(self.getName())

    def move(self, dest):
        return moveHelper(self.checkMove, dest, self.board.pieces, self.getColor(), self)
                
class Bishop(Piece):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)

    def checkMove(self, dest):
        if (validateInputByLengthAndType(dest, 2, tuple)):
            if (validateInputByCharactersAndNumbers(dest)):
                if (validatePieceMovement(self.getName(), self.getPosition(), dest)):
                    # get other pieces from board and check if any of them interupts movement
                    moveBlocked = blockCheckHelper(self.board.pieces, dest)
                    if (moveBlocked):
                        if (pieceKillHelper(self.board.pieces, self.getName(), self.getColor(), dest)):
                            return True
                        else:
                            printInvalidMovementErrorMessage(self.getName())
                            return False
                    return (not moveBlocked)
                else:
                    printInvalidMovementErrorMessage(self.getName());
            else:
                printInvalidCharacterOrNumberErrorMessage();
        else:
            printInputLengthAndTypeErrorMessage();

    def getIcon(self):
        if (self.getColor() == 'White'):
            return whiteIcons.get(self.getName())
        elif (self.getColor() == 'Black'):
            return blackIcons.get(self.getName())

    def move(self, dest):
        return moveHelper(self.checkMove, dest, self.board.pieces, self.getColor(), self)
        
class Queen(Piece):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)

    def checkMove(self, dest):
        if (validateInputByLengthAndType(dest, 2, tuple)):
            if (validateInputByCharactersAndNumbers(dest)):
                if (validatePieceMovement(self.getName(), self.getPosition(), dest)):
                    # get other pieces from board and check if any of them interupts movement
                    moveBlocked = blockCheckHelper(self.board.pieces, dest)
                    if (moveBlocked):
                        if (pieceKillHelper(self.board.pieces, self.getName(), self.getColor(), dest)):
                            return True
                        else:
                            printInvalidMovementErrorMessage(self.getName())
                            return False
                    return (not moveBlocked)
                else:
                    printInvalidMovementErrorMessage(self.getName());
            else:
                printInvalidCharacterOrNumberErrorMessage();
        else:
            printInputLengthAndTypeErrorMessage();

    def getIcon(self):
        if (self.getColor() == 'White'):
            return whiteIcons.get(self.getName())
        elif (self.getColor() == 'Black'):
            return blackIcons.get(self.getName())

    def move(self, dest):
        return moveHelper(self.checkMove, dest, self.board.pieces, self.getColor(), self)

class King(Piece):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)

    def checkMove(self, dest):
        if (validateInputByLengthAndType(dest, 2, tuple)):
            if (validateInputByCharactersAndNumbers(dest)):
                if (validatePieceMovement(self.getName(), self.getPosition(), dest)):
                    # get other pieces from board and check if any of them interupts movement
                    moveBlocked = blockCheckHelper(self.board.pieces, dest)
                    if (moveBlocked):
                        if (pieceKillHelper(self.board.pieces, self.getName(), self.getColor(), dest)):
                            return True
                        else:
                            printInvalidMovementErrorMessage(self.getName())
                            return False
                    return (not moveBlocked)
                else:
                    printInvalidMovementErrorMessage(self.getName());
            else:
                printInvalidCharacterOrNumberErrorMessage();
        else:
            printInputLengthAndTypeErrorMessage();

    def getIcon(self):
        if (self.getColor() == 'White'):
            return whiteIcons.get(self.getName())
        elif (self.getColor() == 'Black'):
            return blackIcons.get(self.getName())

    def move(self, dest):
        return moveHelper(self.checkMove, dest, self.board.pieces, self.getColor(), self)

class Pawn(Piece):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)

    def checkMove(self, dest):
        if (validateInputByLengthAndType(dest, 2, tuple)):
            if (validateInputByCharactersAndNumbers(dest)):
                if (validatePieceMovement(self.getName(), self.getPosition(), dest, self.getColor())):
                    # get other pieces from board and check if any of them interupts movement
                    moveBlocked = blockCheckHelper(self.board.pieces, dest)
                    if (moveBlocked):
                        if (pieceKillHelper(self.board.pieces, self.getName(), self.getColor(), dest)):
                            return True
                        else:
                            printInvalidMovementErrorMessage(self.getName())
                    if (
                        (self.getColor() == 'White') and
                        (dest[0] == 'A')
                    ):
                        pawnPromotion(self.board, self, dest)
                    elif (
                        (self.getColor() == 'Black') and
                        (dest[0] == 'H')
                    ):
                        pawnPromotion(self.board, self, dest)
                            
                    return (not moveBlocked)
                else:
                    printInvalidMovementErrorMessage(self.getName());
            else:
                printInvalidCharacterOrNumberErrorMessage();
        else:
            printInputLengthAndTypeErrorMessage();

    def getIcon(self):
        if (self.getColor() == 'White'):
            return whiteIcons.get(self.getName())
        elif (self.getColor() == 'Black'):
            return blackIcons.get(self.getName())

    def move(self, dest):
        return moveHelper(self.checkMove, dest, self.board.pieces, self.getColor(), self)
        
