import time
from ai import Artificial
from human import Human


class Game:
    def __init__(self) -> None:
        self.human = Human
        self.ai = Artificial
        pass

    def run_game(self):
        self.display_rules()
        self.game_action()
        self.display_winner()
        pass

    def display_rules(self):
        print("Welcome to the complex Rock, Paper, Scissor, Lizard, Spock Game!")
        print()
        print("This game will be best out of 3. ")
        print()
        time.sleep(1)
        print("Rock crushes Scissors.")
        time.sleep(1)
        print("Scissors cuts Paper.")
        time.sleep(1)
        print("Paper covers Rock.")
        time.sleep(1)
        print("Rock crushes Lizard.")
        time.sleep(1)
        print("Lizard poisons Spock.")
        time.sleep(1)
        print("Spock smashes Scissors.")
        time.sleep(1)
        print("Scissors decapitates Lizard.")
        time.sleep(1)
        print("Lizard eats Paper.")
        time.sleep(1)
        print("Paper disproves Spock.")
        time.sleep(1)
        print("Spock vaporizes Rock.")
        pass

    def game_action(self):
        best_of = 0
        self.human_player = int(input("How many humans are participating in this game?\n 0, 1, or 2: "))
        while best_of < 3:
            if self.human_player == 0:
                ai_robot_one = Artificial("AI number 1")
                ai_robot_two = Artificial("AI number 2")
                time.sleep(1)
                print("There are 0 human participating in this game. ")
                time.sleep(1)
                print(ai_robot_one.players, "vs", ai_robot_two.players, "! Let the battle Begin! ")
                time.sleep(1)
                print(ai_robot_one.players, "has chose", ai_robot_one.rand_choices())
                time.sleep(1)
                print(ai_robot_two.players, "has chose", ai_robot_two.ai_choices)
                if ai_robot_one.rand_choices == ai_robot_two.rand_choices:
                    time.sleep(1)
                    print("It's a draw! Please chose again!")
                elif ai_robot_one.rand_choices == "Rock":
                    if ai_robot_two.rand_choices == "Scissors":
                        print("Rock crushes Scissors!")
                        ai_robot_one.best_of += 1
                    elif ai_robot_two.rand_choices == "Paper":
                        print("Paper covers Rock!")
                        ai_robot_two.best_of += 1
                    elif ai_robot_two.rand_choices == "Spock":
                        print("Spock vaporizes Rock!")
                        ai_robot_two.best_of += 1
                    else:
                        print("Rock crushes Lizard")
                        ai_robot_one.best_of += 1
                elif ai_robot_one.rand_choices == "Scissors":
                    if ai_robot_two.rand_choices == "Rock":
                        print("Rock crushes Scissors!")
                        ai_robot_two.best_of += 1
                    elif ai_robot_two.rand_choices == "Paper":
                        print("Scissors cuts Paper!")
                        ai_robot_one.best_of += 1
                    elif ai_robot_two.rand_choices == "Lizard":
                        print("Rock crushes Lizard!")
                        ai_robot_one.best_of += 1
                    else:
                        print("Spock smashes Scissors!")
                        ai_robot_two.best_of += 1
                elif ai_robot_one.rand_choices == "Paper":
                    if ai_robot_two.rand_choices == "Rock":
                        print("Paper covers Rock!")
                        ai_robot_one.best_of += 1
                    elif ai_robot_two.rand_choices == "Scissors":
                        print("Scissors cuts Paper!")
                        ai_robot_two.best_of += 1
                    elif ai_robot_two.rand_choices == "Lizard":
                        print("Lizard eats Paper!")
                        ai_robot_two.best_of += 1
                    else:
                        print("Paper disapprove Spock!")
                        ai_robot_one.best_of += 1
                elif ai_robot_one.rand_choices == "Lizard":
                    if ai_robot_two.rand_choices == "Rock":
                        print("Rock crushes Lizard!")
                        ai_robot_two.best_of += 1
                    elif ai_robot_two.rand_choices == "Paper":
                        print("Lizard eats Paper!")
                        ai_robot_one.best_of += 1
                    elif ai_robot_two.rand_choices == "Spock":
                        print("Lizard posion Spock!")
                        ai_robot_one.best_of += 1
                    else:
                        print("Scissors decapitates Lizard!")
                        ai_robot_two.best_of += 1
                elif ai_robot_one.rand_choices == "Spock":
                    if ai_robot_two.rand_choices == "Rock":
                        print("Spock vaporize Rock!")
                        ai_robot_one.best_of += 1
                    elif ai_robot_two.rand_choices == "Paper":
                        print("Paper disapprove Spock!")
                        ai_robot_two.best_of += 1
                    elif ai_robot_two.rand_choices == "lizard":
                        print("Lizard posion Spock!")
                        ai_robot_one.best_of += 1
                    else:
                        print("Spock smashes Scissors!")
                        ai_robot_one.best_of += 1
                elif ai_robot_one.best_of == 2 or ai_robot_two.best_of == 2:
                    False
            elif self.human_player == 1:
                human_name = str(input("Please Enter Player One Name: "))
                player_one = Human(human_name)
                ai_robot_one = Artificial()
            elif self.human_player == 2:
                human_name_one = str(input("Please Enter Player One Name: "))
                player_one = Human(human_name_one)
                human_name_two = str(input("Please Enter Player two Name: "))
                player_two = Human(human_name_two)
        
        pass

    def display_winner(self):
        pass