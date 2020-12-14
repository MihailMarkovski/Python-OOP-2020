# from Defining_Classes.guild_system_07E.project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player.guild != 'Unaffiliated' and player.guild != self.name:
            return f"Player {player.name} is in another guild."
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        players = [p for p in self.players if p.name == player_name]
        if not players:
            return f"Player {player_name} is not in the guild."
        for player in players:
            self.players.remove(player)
            player.guild = 'Unaffiliated'
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result = f'Guild: {self.name}\n'
        for p in self.players:
            result += p.player_info()
        return result

# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())
