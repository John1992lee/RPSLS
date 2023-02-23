

class Player:
    def __init__(self, player) -> None:
        self.players = player
        self.best_of = 0
        pass

    def choices(self):
        self.action_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        pass