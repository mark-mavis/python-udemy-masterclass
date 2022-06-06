
numbers = [1, 15, 55, 40, 43, 29]

# When the number sequence contains a number divisible by 8, the for loop hits the if statement
#   and breaks and prevents the else statement from running

for number in numbers:
    if number % 8 == 0:
        print("Numbers are unacceptable")
        break
else:
    print("The for loop executed with out hitting a break statement")