from AI_Chess.WebInterface import WebInterface
from AI_Chess.ChessEngine import ChessEngine
from AI_Chess.Vision import Vision

keepPlaying = True

myBrowser = WebInterface()
myEngine = ChessEngine()
myCV = Vision()
while keepPlaying:

    input("Press enter to capture")
    string = myCV.calculateMove()
    print("CHESS HERE " + string)
    myEngine.make_human_move(string)
    myBrowser.pushToLichess(myEngine.get_current_FEN())
    myEngine.best_move_from_FEN()
    myBrowser.pushToLichess(myEngine.get_current_FEN())
    input("press enter to update with computer move")
    myCV.calculateMove()