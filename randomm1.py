import random
playing = True
number =str(random.randint(10,20))
print("Iwill generate a number from 0 to 9 and you have to guess the number one digit at a time")
print("the game ends when you get 1 hero")
while playing:
    guess = input("give me your best guess!")
    if number== guess:
        print("YOU WIN")
        print("THE NUMBER WAS,NUMBER")
        break
    else:
        print("your guess isnt quite write/n")


