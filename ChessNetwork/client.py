import socket, threading, pickle

class client():
    def __init__(self, ip="localhost", port=9001, bytesize=1024):
        self.ip = ip
        self.size = bytesize
        self.port = port

    def connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((self.ip, self.port))

        s.send(bytes("CONNECT", "UTF-8"))
        data = s.recv(self.size).decode("UTF-8")
        if not data == "400":
            raise Exception("Client says:     Failed to receive proper response from server")
        return s

    def connectToGame(self, player):
        s = self.connect()
        s.send(bytes("PLAYER CONNECT", "UTF-8"))
        data = s.recv(self.size).decode("UTF-8")
        if not data == "400":
            print("Client says:     Error connecting")
        s.send(player.getJSON())
        data = s.recv(self.size).decode("UTF-8")
        if data == "400":
            return True
        else:
            return False
