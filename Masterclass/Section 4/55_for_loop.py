# The set of values comes from a sequence, or some other iterable object.
# Sequences are iterable objects (anything that can be iterated over)
# If you can use an object with a for loop, then it is iterable

#ITERABLE TYPES
#   - string
#   - range


parrot = "Norwegian Blue"

# Boolean operator
if "orw" in parrot:
    print("Found")
# "character" is recieving the character from the parrot sequence
# the character variable name will be bound to each items in the sequence and then be 
#   printed out beleow
for character in parrot:
    print(character)    #Printing the character passed back by the parrot sequence


number = "9,223;372:036 854,775;806"
string_val = "Hello Mark, it is good to see you. And Casey too!"
separators = ""
numeric_chars = ""
capital_letters = ""
sum = 0

for char in number:
    if not char.isnumeric():
        separators += char
print(separators)

for number_chars in number:
    if number_chars.isnumeric():
        numeric_chars += number_chars
        sum += int(number_chars)

print(numeric_chars)
print("Sum: {0}".format(sum))

for char in string_val:
    if char.isupper():
        capital_letters  += char
print(capital_letters)





# values = "".join(char if char not in separators else " " for char in number).split()
# print([int(val) for val in values])