name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))

if (age >= 18 and age <= 99):
    print("You are able to vote")
elif age > 100:
    print("You are too old to vote because you are dead")
else:
    print("You are not old enough. Come bask in {} years".format(18-age))


print("test")  #Comment

