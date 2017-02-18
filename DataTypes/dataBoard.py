

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

    def move(self, stringMove):
        moveStart = stringMove[0:2].lower()
        moveEnd = stringMove[2:4].lower()
        print(moveStart, moveEnd)
        if self.board[moveEnd] != "":
            pass
        self.board[moveEnd] = self.board[moveStart]


b = Board()
b.move("D1H5")