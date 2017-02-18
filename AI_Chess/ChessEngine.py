import os
import chess.uci
import chess
from chess import Move
import platform


class ChessEngine:
    print(platform.system())
    moveList = ""
    script_dir = os.path.dirname(__file__)
    if platform.system() == "Windows":
        rel_path = "stockfish_8_x64.exe"
    elif platform.system() == "Darwin":
        rel_path = "stockfish"
    else:
        print("WTF are you using?")
    abs_file_path = os.path.join(script_dir, rel_path)
    defaultFEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    currentFEN = ""
    engine = chess.uci.popen_engine(abs_file_path)

    def __init__(self):
        self.engine.uci()

        self.engine.ucinewgame()

        self.position = chess.Board(self.defaultFEN)

        self.engine.position(self.position)


    def best_move_from_FEN(self):


        self.position = chess.Board(self.get_current_FEN())
        self.engine.position(self.position)
        print(self.position.fen())
        moveString = str(self.engine.go(movetime=3000))
        print(moveString)
        self.position.push(Move.from_uci(moveString[33:-33]))
        print(self.position)

    def get_current_FEN(self):
        return self.position.fen()

    def make_human_move(self, uci_move):
        self.position.push(Move.from_uci(uci_move))



