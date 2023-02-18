
#Sequence Types allow you to "slice" them

# 
# INDEX VS SLICE
#   index ---> parrot[10];
#   slice ---> parrot[0:6]  

parrot = "Norwegian Blue"

# print(sequence[start:stop])

print(parrot[0:6])  # Norweg (inclusive start position - exclusiveend position)
print(parrot[-14:-8])

print(parrot[0:9])  # Norwegian
print(parrot[ :9])  # Norwegian Same as previous statement

print(parrot[10:])
print(parrot[:])    #prints from start to finish

print(parrot[-4:-2])    # Bl
print(parrot[-4:12])    # Bl

# Slicing with Steps
# print(sequence[start:stop:step])

print(parrot[0:6:2])
print(parrot[0:6:3])

number = "9,224,523,654,294,694,603"
seperators = number[1::4]
print(number[1::4]);

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])
