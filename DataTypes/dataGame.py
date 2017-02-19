from DataTypes import Board
from ChessNetwork import server
from ChessNetwork import client
import queue

class Game():
    def __init__(self):
        self.arrayMovesChessNotation = []
        self.arrayMovesNonChess = []
        self.board = Board()
        self.player = ""
        self.queueEvent = queue.Queue()
        self.queueInfo = queue.Queue()
        self.connected = False
        self.opponent = ""
        # TODO: Add vision object

    def addMove(self, moveString):
        self.board.move()

    def startServer(self):
        self.s = server(self.queueEvent, self.queueInfo)
        self.s.start()
        self.handleServer()

    def handleServer(self):
        try:
            # print("Size before pull:", self.queueServer.qsize())
            msg = self.queueEvent.get_nowait()
            # print("Size after pull:", self.queueServer.qsize())
            if msg == "CONNECTED PLAYER":
                msg = self.queueEvent.get()
                self.opponent = msg
                self.connected = True
        except queue.Empty:
            pass

    def connectToServer(self, player):
        self.client = client()
        self.connected = client.connectToGame(player)
