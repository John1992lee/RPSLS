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
        print()
        pass

    def game_action(self):
        self.human_player = int(input("How many humans are participating in this game?\n 0, 1, or 2: "))
        if self.human_player == 0:
            time.sleep(1)
            print()
            print("There are 0 human participating this game. ")
            print()
            self.ai_robot_one = Artificial("AI number 1")
            self.ai_robot_two = Artificial("AI number 2")
            time.sleep(1)
            print(self.ai_robot_one.players, "vs", self.ai_robot_two.players, "Let the Game Begin! ")
            print()
            bool = True
            while bool == True:
                self.ai_robot_one.rand_choices()
                self.ai_robot_two.rand_choices()
                time.sleep(1)
                print()
                print(self.ai_robot_one.players, "has chose", self.ai_robot_one.ai_choices)
                time.sleep(1)
                print(self.ai_robot_two.players, "has chose", self.ai_robot_two.ai_choices)
                print()
                if self.ai_robot_one.ai_choices == self.ai_robot_two.ai_choices:
                    time.sleep(1)
                    print()
                    print("It's a draw! Please Play again!")
                elif self.ai_robot_one.ai_choices == "Rock":
                    self.rock(self.ai_robot_one, self.ai_robot_two)
                elif self.ai_robot_one.ai_choices == "Scissors":
                    self.scissor(self.ai_robot_one, self.ai_robot_two)
                elif self.ai_robot_one.ai_choices == "Paper":
                    self.paper(self.ai_robot_one, self.ai_robot_two)
                elif self.ai_robot_one.ai_choices == "Lizard":
                    self.lizard(self.ai_robot_one, self.ai_robot_two)
                elif self.ai_robot_one.ai_choices == "Spock":
                    self.spock(self.ai_robot_one, self.ai_robot_two)
                if self.ai_robot_one.best_of == 2 or self.ai_robot_two.best_of == 2:
                    self.display_winner(self.ai_robot_one, self.ai_robot_two)
                    bool = False
        elif self.human_player == 1:
            print()
            self.human_name = str(input("Please Enter Player One Name: "))
            self.player_one = Human(self.human_name)
            self.ai_robot_one = Artificial("AI")
            print()
            time.sleep(1)
            print(f"Choose 0 for {self.player_one.action_list[0]}")
            time.sleep(1)
            print(f"Choose 1 for {self.player_one.action_list[1]}")
            time.sleep(1)
            print(f"Choose 2 for {self.player_one.action_list[2]}")
            time.sleep(1)
            print(f"Choose 3 for {self.player_one.action_list[3]}")
            time.sleep(1)
            print(f"Choose 4 for {self.player_one.action_list[4]}")
            print()
            bool = True
            while bool:
                self.ai_robot_one.rand_choices()
                self.human_input = int(input("Please choose your option: "))
                self.human_input = self.player_one.gesture(self.human_input)
                print()
                time.sleep(1)
                print(f"{self.player_one.players} chose {self.human_input}")
                print(f"{self.ai_robot_one.players} chose {self.ai_robot_one.ai_choices}")
                time.sleep(1)
                print()
                if self.human_input == self.ai_robot_one.ai_choices:
                    time.sleep(1)
                    print()
                    print("It's a draw! Please Play again!")
                elif self.human_input == "Rock":
                    self.rock(self.player_one, self.ai_robot_one)    
                elif self.human_input == "Paper":
                    self.paper(self.player_one, self.ai_robot_one)
                elif self.human_input == "Scissors":
                    self.scissor(self.player_one, self.ai_robot_one)
                elif self.human_input == "Lizard":
                    self.lizard(self.player_one, self.ai_robot_one)
                elif self.human_input == "Spock":
                    self.spock(self.player_one, self.ai_robot_one)
                else: 
                    print("Thats wasn't one of the option! ")
                if self.player_one.best_of == 2 or self.ai_robot_one.best_of == 2:
                    self.display_winner(self.player_one, self.ai_robot_one)
                    bool = False
        elif self.human_player == 2:
            self.human_name_one = str(input("Please Enter Player One Name: "))
            self.player_one = Human(self.human_name_one)
            self.human_name_two = str(input("Please Enter Player two Name: "))
            self.player_two = Human(self.human_name_two)
            time.sleep(1)
            print()
            print(f"Choose 0 for {self.player_one.action_list[0]}")
            time.sleep(1)
            print(f"Choose 1 for {self.player_one.action_list[1]}")
            time.sleep(1)
            print(f"Choose 2 for {self.player_one.action_list[2]}")
            time.sleep(1)
            print(f"Choose 3 for {self.player_one.action_list[3]}")
            time.sleep(1)
            print(f"Choose 4 for {self.player_one.action_list[4]}")
            print()
            bool = True
            while bool:
                print()
                time.sleep(1)
                self.player_one_input = int(input(f"{self.player_one.players} Please Choose your options: "))
                self.player_one_input = self.player_one.gesture(self.player_one_input)
                print()
                time.sleep(1)
                self.player_two_input = int(input(f"{self.player_two.players} Please choose your options: "))
                self.player_two_input = self.player_two.gesture(self.player_two_input)
                print()
                time.sleep(1)
                print(self.player_one.players, "chose", self.player_one_input)
                time.sleep(1)
                print(self.player_two.players, "chose", self.player_two_input)
                time.sleep(1)
                print()
                if self.player_one_input == "Rock":
                    self.rock(self.player_one, self.player_two)
                elif self.player_one_input == "Paper":
                    self.paper(self.player_one, self.player_two)
                elif self.player_one_input == "Scissors":
                    self.scissor(self.player_one, self.player_two)
                elif self.player_one_input == "Lizard":
                    self.lizard(self.player_one, self.player_two)
                elif self.player_one_input == "Spock":
                    self.spock(self.player_one, self.player_two)
                if self.player_one.best_of == 2 or self.player_two.best_of == 2:
                    self.display_winner(self.player_one, self.player_two)
        else:
            print("Invaild Input! ")
            self.game_action()

    def rock(self, user_1, user_2):
        if user_2 == "Scissors":
            print(user_1.players, "Won!")
            user_1.best_of += 1
        elif user_2.ai_choices == "Paper":
            print(user_2.players, "Won!")
            user_2.best_of += 1
        elif user_2.ai_choices == "Spock":
            print(user_2.players, "Won!")
            user_2.best_of += 1
        else:
            print(user_1.players, "Won!")
            user_1.best_of += 1
        
    def paper(self, action_1, aciton_2):
        if action_1 == "Scissors":
            print(aciton_2, "Won!")
            action_1.best_of += 1
        elif aciton_2.ai_choices == "Rock":
            print(action_1.players, "Won!")
            action_1.best_of += 1
        elif aciton_2.ai_choices == "Lizard":
            print(aciton_2.players, "Won!")
            aciton_2.best_of += 1
        else:
            print(action_1.players, "Won!")
            action_1.best_of += 1

    def scissor(self, user_1, user_2):
        if user_2.ai_choices == "Rock":
            print(user_2.players, "Won!")
            user_2.best_of += 1
        elif user_2.ai_choices == "Paper":
            print(user_1.players, "Won!")
            user_1.best_of += 1
        elif user_2.ai_choices == "Lizard":
            print(user_1.players, "Won!")
            user_1.best_of += 1
        else:
            print(user_2.players, "Won!")
            user_2.best_of += 1

    def lizard(self, user_1, user_2):
        if user_2 == "Rock":
            print(user_2.players, "Won!")
            user_2.best_of += 1
        elif user_2.ai_choices == "Paper":
            print(user_1.players, "Won!")
            user_1.best_of += 1
        elif user_2.ai_choices == "Spock":
            print(user_1.players, "Won!")
            user_1.best_of += 1
        else:
            print(user_2.players, "Won!")
            user_2.best_of += 1

    def spock(self, user_1, user_2):
        if user_2.ai_choices == "Scissors":
            print(user_2.players, "Won!")
            user_2.best_of += 1
        elif user_2.ai_choices == "Rock":
            print(user_1.players, "Won!")
            user_1.best_of += 1
        elif user_2.ai_choices == "Lizard":
            print(user_2.players, "Won!")
            user_2.best_of += 1
        else:
            print(user_1.players, "Won!")
            user_1.best_of += 1

    def display_winner(self, player_one, player_two):        
        if player_one.best_of > player_two.best_of:
            print(player_one.players, "is the Winner!")
        elif player_one.best_of < player_two.best_of:
            print(player_two.players, "is the Winner!")
        pass