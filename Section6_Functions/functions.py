
def multiply_first() -> None:
    print("Hello from the function")
    result = 10.5 * 4
    return result
                        # Convention to have 2 black lines in between function definition
                        #   and other code
def multiply(a: float, b: float) -> float:
    print(f"multiplying {a} x {b}")
    return a*b

def is_palindrom(string: str) -> bool:
    """Compares an alpha numeric string to see if it is a palindrom

    Args:
        string: strickly alpha-numeric string

    Returns:
        `bool`
    """
    return string.casefold() == string[::-1].casefold()

def palindrome_sentence(sentence: str) -> bool:
    """Filters out all non-alpha numeric characters from user input

    Loop that combines all alpha numeric characters from user input

    Returns:
        `string` iterator
    """
    sentence = ""
    for char in sentence:
        if char.isalnum():
            sentence += char
    return is_palindrom(sentence)   # Calling Helper function

print(multiply(12, 52))
print(palindrome_sentence("Ah. Satan sees Natasha."))
