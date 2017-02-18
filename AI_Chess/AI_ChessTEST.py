from AI_Chess.WebInterface import WebInterface
from AI_Chess.ChessEngine import ChessEngine

keepPlaying = True

myBrowser = WebInterface()
myEngine = ChessEngine()

while keepPlaying:
    move = input("What is your move?:")
    myEngine.make_human_move(move)
    myBrowser.pushToLichess(myEngine.get_current_FEN())
    myEngine.best_move_from_FEN()
    myBrowser.pushToLichess(myEngine.get_current_FEN())