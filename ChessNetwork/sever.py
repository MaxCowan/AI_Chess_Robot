import socket, threading, pickle
from DataTypes.dataPlayer import Player

class server(threading.Thread):
    def __init__(self, eventQueue, statusQueue, ip="localhost", port=9001):
            threading.Thread.__init__(self)
            self.daemon = True
            self.queueStatus = statusQueue
            self.queueEvent = eventQueue
            self.port = port
            self.ip = ip

    def run(self):
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(socket.gethostname())
        serversocket.bind((self.ip, self.port))
        serversocket.listen(10)
        while 1:
            client, address = serversocket.accept()
            client.settimeout(30)
            t = threading.Thread(target=self.dealWithClient, args=(client, address))
            t.daemon = True
            t.start()

    def dealWithClient(self, client, address):
        self.size = 1024
        while 1:
            try:
                data = client.recv(self.size).decode("UTF-8")
                if data:
                    print("server says:     SERVER RECIEVED:         ", data)
                    if data == "CONNECT":
                        client.send(bytes("400", "UTF-8"))
                        self.handleRespond(client)
                    else:
                        client.send(bytes("ERROR INVALID COMMAND", "UTF-8"))
                        raise Exception("Server says:     Invalid command sent")
            except Exception as e:
                print(e)
                break

    def handleRespond(self, client):
        data = client.recv(self.size).decode("UTF-8")
        try:
            if data:
                if data == "SEND GAME":
                    client.send(bytes("400", "UTF-8"))
                    self.recieveGame(client)
                elif data == "GET STATS":
                    client.send(bytes("400", "UTF-8"))
                    self.sendStats(client)
                elif data == "PLAYER CONNECT":
                    client.send(bytes("400", "UTF-8"))
                    self.connectPlayer(client)

            else:
                raise Exception("Server says:     No response")
        except Exception as e:
            print(e)

    def recieveGame(self, client):
        data = client.recv(self.size).decode("UTF-8")
        tempGame = pickle.load(data)

    def sendStats(self, client):
        data = client.recv(self.size).decode("UTF-8")

    def connectPlayer(self, client):
        data = client.recv(4096).decode("UTF-8")
        player = Player().initJSON(data)
        self.queueEvent.put("CONNECTED PLAYER")
        self.queueEvent.put(player)
        client.send(bytes("400", "UTF-8"))

