import random
import matplotlib.pyplot as plt
import numpy as np

shopping_list = ["milk", "bread", "jelly", "ketchup", "mustard", "hotdogs"]

# If the break statement is executed, the following else statement is ignored

for i in range(0, 6):
    if shopping_list[i] == "tuna":
        print("Invalid Recipe")
        break
else:
    print("Recipe list is valid")

comp_guess = 0
num_guesses = 0
min_range = 1
max_range = 1000000000

answer = random.randint(min_range, max_range)
comp_guess = random.randint(min_range, max_range)
range_list = []
x = []

#Computer Playing Guessing Game by itself
while min_range != max_range:
    
    num_guesses += 1    #Increment guesses
    print(f"Computer Guessing: {comp_guess}")

    if comp_guess < answer:
        min_range = comp_guess + 1  #Update min_range to cut off half of the possible numbers
        print(f"guess higher --> min_val: {min_range} max_val: {max_range} range: {max_range-min_range}")
        x += [num_guesses]
        range_list.append([num_guesses, (max_range - min_range), comp_guess])

    elif comp_guess > answer:
        max_range = comp_guess - 1  #Update max_range to cut off top half of the possible numbers
        print(f"guess lower --> min_val: {min_range} max_val: {max_range} range: {max_range-min_range}")
        x += [num_guesses]
        range_list.append([num_guesses, (max_range - min_range), comp_guess]) 
    else:
        print(f"Computer found the answer! : {answer} in {num_guesses} guesses")
        ax = plt.axes(projection='3d')
        #ax.scatter3D()
        break
    comp_guess = random.randint(min_range, max_range)
else:
    print("You have to get the right answer now because there are no options left")
    print(f"It took {num_guesses}")


