import random
from player import Player

class Artificial(Player):

    def __init__(self, player) -> None:
        super().__init__(player)
        pass
    
    def rand_choices(self):
        self.ai_choices = random.choice(self.action_list)
        pass
