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
                self.compare(self.ai_robot_one, self.ai_robot_two)
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
                time.sleep(1)
                print(f"{self.ai_robot_one.players} chose {self.ai_robot_one.ai_choices}")
                time.sleep(1)
                print()
                self.human_comparsion(self.human_input, self.ai_robot_one, self.player_one)
                if self.player_one.best_of == 2 or self.ai_robot_one.best_of == 2:
                    self.display_winner(self.player_one, self.ai_robot_one)
                    bool = False
        elif self.human_player == 2:
            print()
            self.human_name_one = str(input("Please Enter Player One Name: "))
            self.player_one = Human(self.human_name_one)
            print()
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
            while bool == True:
                print()
                time.sleep(1)
                self.player_one_input = int(input(f"{self.player_one.players}, Please Choose your options: "))
                self.player_one_input = self.player_one.gesture(self.player_one_input)
                print()
                time.sleep(1)
                self.player_two_input = int(input(f"{self.player_two.players}, Please choose your options: "))
                self.player_two_input = self.player_two.gesture(self.player_two_input)
                print()
                if self.player_one_input == self.player_two_input:
                    time.sleep(1)
                    print(f"{self.player_one.players} chose {self.player_one_input}")
                    time.sleep(1)
                    print(f"{self.player_two.players} chose {self.player_two_input}")
                    time.sleep(1)
                    print()
                    print("It's a Tie! Please choose again!")
                elif self.player_one_input == "Rock":
                    time.sleep(1)
                    print(f"{self.player_one.players} chose {self.player_one_input}")
                    time.sleep(1)
                    print(f"{self.player_two.players} chose {self.player_two_input}")
                    time.sleep(1)
                    print()
                    if self.player_two_input == "Paper" or self.player_two_input == "Spock":
                        print(self.player_two.players, "Won!")
                        self.player_two.best_of += 1
                    elif self.player_two_input == "Scissors" or self.player_two_input == "Lizard":
                        print(self.player_one.players, "Won!")
                        self.player_one.best_of += 1
                elif self.player_one_input == "Paper":
                    time.sleep(1)
                    print(f"{self.player_one.players} chose {self.player_one_input}")
                    time.sleep(1)
                    print(f"{self.player_two.players} chose {self.player_two_input}")
                    time.sleep(1)
                    print()
                    if self.player_two_input == "Scissors" or self.player_two_input == "Lizard":
                        print(self.player_two.players, "Won!")
                        self.player_two.best_of += 1
                    elif self.player_two_input == "Rock" or self.player_two_input == "Spock":
                        print(self.player_one.players, "Won!")
                        self.player_one.best_of += 1
                elif self.player_one_input == "Scissors":
                    time.sleep(1)
                    print(f"{self.player_one.players} chose {self.player_one_input}")
                    time.sleep(1)
                    print(f"{self.player_two.players} chose {self.player_two_input}")
                    time.sleep(1)
                    print()
                    if self.player_two_input == "Paper" or self.player_two_input == "Lizard":
                        print(self.player_one.players, "Won!")
                        self.player_one.best_of += 1
                    elif self.player_two_input == "Rock" or self.player_two_input == "Spock":
                        print(self.player_two.players, "Won!")
                        self.player_two.best_of += 1
                elif self.player_one_input == "Lizard":
                    time.sleep(1)
                    print(f"{self.player_one.players} chose {self.player_one_input}")
                    time.sleep(1)
                    print(f"{self.player_two.players} chose {self.player_two_input}")
                    time.sleep(1)
                    print()
                    if self.player_two_input == "Paper" or self.player_two_input == "Spock":
                        print(self.player_one.players, "Won!")
                        self.player_one.best_of += 1
                    elif self.player_two_input == "Rock" or self.player_two_input == "Scissors":
                        print(self.player_two.players, "Won!")
                        self.player_two.best_of += 1
                elif self.player_one_input == "Spock":
                    time.sleep(1)
                    print(f"{self.player_one.players} chose {self.player_one_input}")
                    time.sleep(1)
                    print(f"{self.player_two.players} chose {self.player_two_input}")
                    time.sleep(1)
                    print()
                    if self.player_two_input == "Scissors" or self.player_two_input == "Rock":
                        print(self.player_one.players, "Won!")
                        self.player_one.best_of += 1
                    elif self.player_two_input == "Lizard" or self.player_two_input == "Paper":
                        print(self.player_two.players, "Won!")
                        self.player_two.best_of += 1
                else: 
                    print(f"Invaild! {self.player_one.players}, please choose another gesture! ")

                if self.player_two_input == "Rock":
                    if self.player_one_input == "Paper" or self.player_one_input == "Spock":
                        print()
                    elif self.player_one_input == "Scissors" or self.player_one_input == "Lizard":
                        print()
                elif self.player_two_input == "Paper":
                    if self.player_one_input == "Scissors" or self.player_one_input == "Lizard":
                        print()
                    elif self.player_one_input == "Rock" or self.player_one_input == "Spock":
                        print()
                elif self.player_two_input == "Scissors":
                    if self.player_one_input == "Paper" or self.player_one_input == "Lizard":
                        print()
                    elif self.player_one_input == "Rock" or self.player_one_input == "Spock":
                        print()
                elif self.player_two_input == "Lizard":
                    if self.player_one_input == "Paper" or self.player_one_input == "Spock":
                        print()
                    elif self.player_one_input == "Rock" or self.player_one_input == "Scissors":
                        print()
                elif self.player_two_input == "Spock":
                    if self.player_one_input == "Scissors" or self.player_one_input == "Rock":
                        print()
                    elif self.player_one_input == "Lizard" or self.player_one_input == "Paper":
                        print()
                else: 
                    print(f"Error! {self.player_two.players}, Please choose other options! ")
                if self.player_one.best_of == 2 or self.player_two.best_of == 2:
                    self.display_winner(self.player_one, self.player_two)
                    bool = False
        else:
            print("Invaild Input! ")
            self.game_action()

    def compare(self, user_1, user_2):
        if user_1.ai_choices == user_2.ai_choices:
            print()
            print("It's a Tie! Please choose again!")
        elif user_1.ai_choices == "Rock":
            if user_2.ai_choices == "Paper" or user_2.ai_choices == "Spock":
                print(user_2.players, "Won!")
                user_2.best_of += 1
            else:
                print(user_1.players, "Won!")
                user_1.best_of += 1
        elif user_1.ai_choices == "Paper":
            if user_2.ai_choices == "Scissors" or user_2.ai_choices == "Lizard":
                print(user_2.players, "Won!")
                user_2.best_of += 1
            else:
                print(user_1.players, "Won!")
                user_1.best_of += 1
        elif user_1.ai_choices == "Scissors":
            if user_2.ai_choices == "Paper" or user_2.ai_choices == "Lizard":
                print(user_1.players, "Won!")
                user_1.best_of += 1
            else:
                print(user_2.players, "Won!")
                user_2.best_of += 1
        elif user_1.ai_choices == "Lizard":
            if user_2.ai_choices == "Paper" or user_2.ai_choices == "Spock":
                print(user_1.players, "Won!")
                user_1.best_of += 1
            else:
                print(user_2.players, "Won!")
                user_2.best_of += 1
        elif user_1.ai_choices == "Spock":
            if user_2.ai_choices == "Scissors" or user_2.ai_choices == "Rock":
                print(user_1.players, "Won!")
                user_1.best_of += 1
            else:
                print(user_2.players, "Won!")
                user_2.best_of += 1
        else:
            print("Please choose a different gesture! ")
    
    def human_comparsion(self, user_1, user_2, user_3):
        if user_1 == user_2.ai_choices:
            print()
            print("It's a Tie! Please choose again!")
        elif user_1 == "Rock":
            if user_2.ai_choices == "Paper" or user_2.ai_choices == "Spock":
                print(user_2.players, "Won!")
                user_2.best_of += 1
            else:
                print(user_3.players, "Won!")
                user_3.best_of += 1
        elif user_1 == "Paper":
            if user_2.ai_choices == "Scissors" or user_2.ai_choices == "Lizard":
                print(user_2.players, "Won!")
                user_2.best_of += 1
            else:
                print(user_1.players, "Won!")
                user_3.best_of += 1
        elif user_1 == "Scissors":
            if user_2.ai_choices == "Paper" or user_2.ai_choices == "Lizard":
                print(user_3.players, "Won!")
                user_3.best_of += 1
            else:
                print(user_2.players, "Won!")
                user_2.best_of += 1
        elif user_1 == "Lizard":
            if user_2.ai_choices == "Paper" or user_2.ai_choices == "Spock":
                print(user_3.players, "Won!")
                user_3.best_of += 1
            else:
                print(user_2.players, "Won!")
                user_2.best_of += 1
        elif user_1 == "Spock":
            if user_2.ai_choices == "Scissors" or user_2.ai_choices == "Rock":
                print(user_3.players, "Won!")
                user_3.best_of += 1
            else:
                print(user_2.players, "Won!")
                user_2.best_of += 1
        else:
            print("Please choose a different gesture! ")


    def display_winner(self, player_one, player_two):        
        if player_one.best_of > player_two.best_of:
            print(player_one.players, "is the Winner!")
        elif player_one.best_of < player_two.best_of:
            print(player_two.players, "is the Winner!")
        pass