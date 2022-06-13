def get_integer():
    """
        prompts user to enter a string integer value
    Returns:
        integer value
    """    
    while True:
        temp = input("Please Enter and Integer Value")
        if temp.isdigit():
            return int(temp)
        print("You entered an invalid number")

get_integer()
get_integer()