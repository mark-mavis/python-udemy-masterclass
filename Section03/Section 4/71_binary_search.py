import random

guess = None
num_guesses = 0
max_guesses = 10
min_range = 1
max_range = 1000

answer = random.randint(min_range, max_range)

#Automated Binary Search
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
    
##Resetting 
#guess = 0
#num_guesses = 0
#max_guesses = 10
#min_range = 1
#max_range = 1000

#answer = random.randint(min_range, max_range)

##Manual Guessing Game
#while guess != answer:
    
#    #specify range for first guess and then hide the range as it updates
    
#    guess = int(input(f"Please enter a guess between {min_range} and {max_range}: "))
#    num_guesses += 1    #Increment guesses

#    if guess < answer:
#        min_range = int(guess + 1)  #Update min_range to cut off half of the possible numbers
#        print("guess higher")

#    elif guess > answer:
#        max_range = int(guess - 1)  #Update max_range to cut off top half of the possible numbers
#        print("guess lower")

#    else:
#        print(f"you found the answer! : {answer} in {num_guesses} guesses")
#        break


    #Resetting 
comp_guess = 0
num_guesses = 0
min_range = 1
max_range = 1000000000

#Computer Playing Guessing Game by itself
while comp_guess != answer:
    comp_guess = random.randint(min_range, max_range)
    num_guesses += 1    #Increment guesses
    print(f"Computer Guessing: {comp_guess}")

    if comp_guess < answer:
        min_range = comp_guess + 1  #Update min_range to cut off half of the possible numbers
        print("guess higher")

    elif comp_guess > answer:
        max_range = comp_guess - 1  #Update max_range to cut off top half of the possible numbers
        print("guess lower")

    else:
        print(f"Computer found the answer! : {answer} in {num_guesses} guesses")
        break
    

comp_guess = 0
num_guesses = 0
min_range = 1
max_range = 1000000000

#Computer Playing Guessing Game by itself
while min_range != max_range:
    comp_guess = random.randint(min_range, max_range)
    num_guesses += 1    #Increment guesses
    print(f"Computer Guessing: {comp_guess}")

    if comp_guess < answer:
        min_range = comp_guess + 1  #Update min_range to cut off half of the possible numbers
        print("guess higher")

    elif comp_guess > answer:
        max_range = comp_guess - 1  #Update max_range to cut off top half of the possible numbers
        print("guess lower")

    else:
        print(f"Computer found the answer! : {answer} in {num_guesses} guesses")
        break
else:
    print("You have to get the right answer now because there are no options left")
    print(f"It took {num_guesses}")
