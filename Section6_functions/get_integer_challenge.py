def get_integer():
    """
        Prompts the user to enter a integer value and returns the strings
        as an integer.
    """
    while True:
        temp = input("Please Enter and Integer Value")
        if temp.isdigit():
            return int(temp)
        print("You entered an invalid number")

get_integer()
get_integer()