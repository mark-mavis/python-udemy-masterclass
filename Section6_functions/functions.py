
from audioop import reverse


def multiply():
    print("Hello from the function")
    result = 10.5 * 4
    return result

    # Convention to have 2 black lines in between function definition
    #   and other code

def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a*b

def is_palindrom(string):
    return string.casefold() == string[::-1].casefold()

def palindrome_sentence(sentence):
    sentence = ""
    for char in sentence:
        if char.isalnum():
            sentence += char
    return is_palindrom(sentence)   # Calling Helper function




print(multiply(12, 52))
print(palindrome_sentence("Ah. Satan sees Natasha."))
