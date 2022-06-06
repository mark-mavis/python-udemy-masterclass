import random

num_guesses = 0
max_guesses = 10
min_range = 1
max_range = 1000

answer = random.randint(min_range, max_range)

while num_guesses <= max_guesses:
    
    guess = int(min_range + (max_range - min_range)/2)
    print(f"guessing: {guess}")

    num_guesses += 1    #Increment guesses

    if guess < answer:
        min_range = int(guess + 1)  #Update min_range to cut off half of the possible numbers
        print("guess higher")

    elif guess > answer:
        max_range = int(guess - 1)  #Update max_range to cut off top half of the possible numbers
        print("guess lower")
    else:
        print(f"you found the answer! : {answer} in {num_guesses} guesses")
        break
    


