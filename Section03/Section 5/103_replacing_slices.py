
# Replacing an item in a list
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

computer_parts[3:] = "trackball"
print(computer_parts)
