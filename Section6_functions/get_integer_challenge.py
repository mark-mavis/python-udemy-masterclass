def get_integer():
    """Get an integer from Standart Input (stdin).
    
    The function will continue looping, and prompting the user,
    until a valid `int` is entered.
    
    Param prompt: The String that the user will see, when they're
        prompted to enter the value.
        
    Returns: `int`
    """
    while True:
        temp = input("Please Enter and Integer Value")
        if temp.isdigit():
            return int(temp)
        print("You entered an invalid number")

get_integer()
get_integer()

print("*" * 80)
print(get_integer.__doc__)  # Printing out the documentation of the function
print("*" * 80)
help(get_integer)
print("*" * 80)