
age = int(input("Please enter your age"))

#Using and operator in if statement
if age >=16 and age <= 65:
    print("You are of age to work")
else:
    print("Sorry")

#Simpler Comparison
if 16 <= age <= 65:
    print("You are of age to work")
else:
    print("Sorry")

#Using OR operator in if statement
if age <= 16 or age >= 65:
    print("You are of age to work")
else:
    print("Sorry")