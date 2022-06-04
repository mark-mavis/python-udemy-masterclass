
import random

highest = 20
answer = random.randint(1, highest)
guess = None
num_guess = 0

while guess != answer:
    guess = int(input(f"Please guess a number between 1 and {highest}"))
    if guess == 0:
        print("quiting game")
        break
    num_guess += 1
    if guess < answer:
        print("Guess Higher")
    elif guess > answer:
        print("Guess Lower")  
    else:
        print(f"You got it after {num_guess} guesses!")
        break

