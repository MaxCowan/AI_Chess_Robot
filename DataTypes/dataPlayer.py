import json

class Player():
    def __init__(self, name=""):
        self.name = name
        self.games = []
        self.stats = ""
        self.auth = ""

    def getName(self):
        return self.name

    def getGames(self):
        return self.games

    def getAuth(self):
        return self.auth

    def initJSON(self, jsonString):
        temp = json.loads(jsonString)
        self.games = temp["games"]
        self.name = temp["name"]
        self.stats = temp["stats"]
        self.auth = temp["auth"]

    def getJSON(self):
        temp = {}
        temp["name"] = self.name
        temp["stats"] = self.stats
        temp["games"] = self.games
        temp["auth"] = self.auth
        return json.dumps(temp)
