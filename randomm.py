import random
while True:
    user_action = input("enter a choice (rock, paper ,scissors)")
    possible_actions = ["rock","paper","scissors"]
    computer_action = random.choice(possible_actions)
    print(f"/n you chose"{user_action},"computer chose" {computer_action}/n)
    if user_action == computer_action:
        print(f"both players selected{user_action}")
        play_again = input("play again? (y/n)")
        if play_again != "y":
            break