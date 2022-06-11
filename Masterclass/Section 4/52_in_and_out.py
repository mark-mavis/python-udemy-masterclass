
parrot = "Norwegian Blue"

letter = input("Enter a character: ")


#Using the "in" operator
if letter in parrot:
    print("{0} is in {1}".format(letter, parrot))
else:
    print("{0} is not in {1}".format(letter, parrot))

#Using the "not in" operator
if letter not in parrot.casefold(): #converts all characters to lower case
    print("{0} is not in {1}".format(letter, parrot))
else:
    print("{0} is in {1}".format(letter, parrot))
