import random

class Game:
    def __init__(self):
        self.options = ["rock", "paper", "scissors"]

    def get_user_item(self):
        while True:
            user_item = input("Please choose rock, paper, or scissors:\n").lower()
            if user_item in self.options:
                return user_item
            else:
                print("Invalid choice! Please choose rock, paper, or scissors.")

    def get_computer_item(self):
        return random.choice(self.options)

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif (user_item == "rock" and computer_item == "scissors") or \
             (user_item == "scissors" and computer_item == "paper") or \
             (user_item == "paper" and computer_item == "rock"):
            return "win"
        else:
            return "loss"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        print(f"You selected {user_item}. The computer selected {computer_item}.")
        if result == "draw":
            print("It's a draw!")
        elif result == "win":
            print("You win!")
        else:
            print("You lose!")
        return result
