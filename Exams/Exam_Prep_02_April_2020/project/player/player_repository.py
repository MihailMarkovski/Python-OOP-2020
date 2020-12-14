from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player: Player):
        username = player.username
        searched = [p for p in self.players if p.username == username]
        if searched:
            raise ValueError(f"Player {username} already exists!")
        self.players.append(player)
        self.count += 1

    def remove(self, player: str):
        if player == '':
            raise ValueError("Player cannot be an empty string!")
        p = [p for p in self.players if p.username == player][0]
        self.players.remove(p)
        self.count -= 1

    def find(self, username: str):
        player = [p for p in self.players if p.username == username][0]
        return player
