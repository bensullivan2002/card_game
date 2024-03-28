class Game:
    def __init__(self):
        self.players = []
        self.playing = False

    def add_player(self, player):
        self.players.append(player)
