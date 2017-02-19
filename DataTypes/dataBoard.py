

class Board():
    def __init__(self):
        self.board = {
            "a8":"B_Rook", "b8":"B_Knight", "c8":"B_Bishop", "d8":"B_King", "e8":"B_Queen", "f8":"B_Bishop", "g8":"B_Knight", "h8":"B_Rook",
            "a7":"B_Pawn", "b7":"B_Pawn", "c7":"B_Pawn", "d7":"B_Pawn", "e7":"B_Pawn", "f7":"B_Pawn", "g7":"B_Pawn", "h7":"B_Pawn",
            "a6":"", "b6":"", "c6":"", "d6":"", "e6":"", "f6":"", "g6":"", "h6":"",
            "a5":"", "b5":"", "c5":"", "d5":"", "e5":"", "f5":"", "g5":"", "h5":"",
            "a4":"", "b4":"", "c4":"", "d4":"", "e4":"", "f4":"", "g4":"", "h4":"",
            "a3":"", "b3":"", "c3":"", "d3":"", "e3":"", "f3":"", "g3":"", "h3":"",
            "a2": "W_Pawn", "b2": "W_Pawn", "c2": "W_Pawn", "d2": "W_Pawn", "e2": "W_Pawn", "f2": "W_Pawn", "g2": "W_Pawn", "h2": "W_Pawn",
            "a1": "W_Rook", "b1": "W_Knight", "c1": "W_Bishop", "d1": "W_King", "e1": "W_Queen", "f1": "W_Bishop",
            "g1": "W_Knight", "h1": "W_Rook"
        }
        self.moves = []

    def move(self, stringMove, special=""):
        moveStart = stringMove[0:2].lower()
        moveEnd = stringMove[2:4].lower()
        print(moveStart, moveEnd)
        if self.board[moveEnd] != "":
            pieceAttack = self.board[moveStart][2:]
            if pieceAttack == "Knight":
                tempMove = "N"+moveStart+"x"+moveEnd
            elif pieceAttack == "Rook":
                tempMove = "R"+moveStart+"x"+moveEnd
            elif pieceAttack == "Bishop":
                tempMove = "Bx"+moveEnd
            elif pieceAttack == "Queen":
                tempMove = "Q"+moveStart+"x"+moveEnd
            elif pieceAttack == "King":
                tempMove = "Kx"+moveEnd
            elif pieceAttack == "Pawn":
                tempMove = moveStart[0:1]+"x"+moveEnd
            if special == "check":
                tempMove += "+"
            self.moves.append(tempMove)
        else:
            startChar = self.board[moveStart][2]
            if startChar == "P":
                tempMove = moveEnd
            else:
                tempMove = startChar+moveStart+moveEnd
            self.moves.append(tempMove)
        self.board[moveEnd] = self.board[moveStart]
        self.board[moveStart] = ""

    def displayBoard(self):
        print("{a8:8} {a7:8} {a6:8} {a5:8} {a4:8} {a3:8} {a2:8} {a1:8}".format(**self.board))
        print("{b8:8} {b7:8} {b6:8} {b5:8} {b4:8} {b3:8} {b2:8} {b1:8}".format(**self.board))
        print("{c8:8} {c7:8} {c6:8} {c5:8} {c4:8} {c3:8} {c2:8} {c1:8}".format(**self.board))
        print("{d8:8} {d7:8} {d6:8} {d5:8} {d4:8} {d3:8} {d2:8} {d1:8}".format(**self.board))
        print("{e8:8} {e7:8} {e6:8} {e5:8} {e4:8} {e3:8} {e2:8} {e1:8}".format(**self.board))
        print("{f8:8} {f7:8} {f6:8} {f5:8} {f4:8} {f3:8} {f2:8} {f1:8}".format(**self.board))
        print("{g8:8} {g7:8} {g6:8} {g5:8} {g4:8} {g3:8} {g2:8} {g1:8}".format(**self.board))
        print("{h8:8} {h7:8} {h6:8} {h5:8} {h4:8} {h3:8} {h2:8} {h1:8}".format(**self.board))

    def getChessMoves(self):
        return self.moves


# b = Board()
# b.move("c2c3")
# b.displayBoard()
# b.move("g8h6")
# b.displayBoard()
# b.move("d2d3")
# b.displayBoard()
# b.move("g7g6")
# b.displayBoard()
# b.move("c3c4")
# b.displayBoard()
# b.move("f8g7")
# b.displayBoard()
# b.move("d3d4")
# b.displayBoard()
# b.move("h8g8")
# b.displayBoard()
#
# print(b.getChessMoves())
