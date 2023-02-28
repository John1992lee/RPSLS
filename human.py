from player import Player



class Human(Player):
    def __init__(self, player) -> None:
        super().__init__(player)
        pass

    # Change players gesture to strings
    def gesture(self, number): 
        if number == 0:
            return "Rock"
        elif number == 1:
            return "Paper"
        elif number == 2:
            return "Scissors"
        elif number == 3:
            return "Lizard"
        elif number == 4:
            return "Spock"
        else: 
            return "Invaild Input!"