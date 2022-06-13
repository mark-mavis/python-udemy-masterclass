
# Screen Width = 80 and text = " " is setting a default value if no 
#   argument is included in the function call
def banner_text(text: str = " ", screen_width: int = 80) -> None:
    """ Print a string centred, with ** either side.
  
    :param text: The string to print.
        An asterisk (*) will result in a row of asterisks.
        The default will print a blank line, with a ** border at
        the left and right edges.
    :param screen_width: The overall width to print within
        (including the 4 spaces for the ** either side).
    :raises ValueError: if the supplied string is too long to fit.
    """
    
    text_length = len(text)

    if text_length > screen_width:
        print("The Text is too long!")
        # raise ValueError(f"String '{text}, is longer then Screewidth {screen_width}")
    
    if text == "*":
        print("*" * screen_width)
    else:
        centered_text = text.center(screen_width-4)
        output_text = f"**{centered_text}**"
        print(output_text)

width = 60

banner_text("*", width)
banner_text("Always look on the bright side of life...", width)
banner_text("If life seems jolly rotten,", width)
banner_text("There's something you've forgotten!", width)
banner_text("And that's to laugh and smile and dance and sing,", width)
banner_text()
banner_text("When you're feeling in the dumps,")
banner_text("Don't be silly chumps,")
banner_text("Just purse your lips and whistle - that's the thing!")
banner_text("And... always look on the bright side of life...")
banner_text("*", width)

banner_text("jalkjfaslkjfoiajo joiwfhjowijef aoiwef aijfoawiej fawj  waejf iojf aiwojf wjfajfwjef aoijf jioaej  ij  weji gjojag ajrejgiagj r jakslj f", width)

# This function is not using the return value. None is returned
result = banner_text("Nothing is returned", 20)
print(result)
print(banner_text.__doc__)