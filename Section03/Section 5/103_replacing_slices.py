
# Replacing an item in a list
import re


s = ["a", "f", "c", "d"]
s[1] = "b"

# Replacing a slice with the contents of an iterable
t = ["Hello", "World"]
s = ["And", "I", "Say"]

print(s)
print(t)
s[2:] = t
print(s)

# Deleting a slice
print(f"Deleting {s[2:]}")
del s[2:]
print(s)


computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"]


computer_parts[3:] = "trackball"    # Enters "trackball" chars as individual iteams
                                    # The "trackball" string is an iterable and views them
                                    #   as individual items that are strings of length 1
print(computer_parts)
del computer_parts[3:]
print(computer_parts)
computer_parts[3:] = ["trackball"]
print(computer_parts)

min_val = 100
max_val = 200
stop = None

data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360, 400, 600, 750, 1000]

# Enumerating the list forward
for index, val in enumerate(data):
    # print(f"index: {index} Val: {val}")
    if val >= min_val:
        stop = index
        break
if stop != None:
    del data[:stop]

print(data)     # Print List

# Enumerating the list in reverse
for index, val in enumerate(reversed(data)):
    # print(f"index: {index} Val: {val}")
    if val <= max_val:
        stop = index
        break
if stop != None:
    del data[-stop:]

print(data)     # Print List