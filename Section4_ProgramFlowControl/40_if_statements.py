name = input("Please enter your name: ")
#
#
age = int(input("How old are you, {0}?".format(name)))
#
if age >= 18:
    print("You are old enough to vote!")
else:
    print("Please come back in {} years".format(18-age))