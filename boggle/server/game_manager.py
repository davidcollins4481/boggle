class GameManager:
    def __init__(self):
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def get_game_by_id(self, identifier):
        game = [game for game in self.games if game.id == identifier]
        if len(game) > 1:
            raise Exception("Games with the same id cannot exist")

        return game

    def get_active_games(self):
        return [g for g in self.games if g.in_progress()]

    def get_completed_games(self):
        return [g for g in self.games if not g.in_progress()]

    def add_player_to_game(self, player, game):
        game.add_player(player)
        return game
