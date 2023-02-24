import random
from player import Player

class Artificial(Player):

    def __init__(self, player) -> None:
        super().__init__(player)
        pass
    
    # AI random Choice 
    
    def rand_choices(self):
        self.ai_choices = self.action_list[random.randint(0, 4)]
        pass
