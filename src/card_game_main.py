class Game:
    def __init__(self):
        self.players = []
        self.playing = False

    def get_player(self, player):
        self.players.append(player)