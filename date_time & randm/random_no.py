# Generates a number from 1 through 10 inclusive
import random

guesses_left = 3
# Start your game!

count = 0
while count<guesses_left:
    guess = int(input("Your GUess:"))
    random_number = random.randrange(10)
    if guess == random_number:
        print("You Win")
        break
        guesses_left -= 1
    else:
        print ("You Lose")