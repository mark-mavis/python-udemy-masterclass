
str_values = input("Please enter three numbers:")

values = []

for val in str_values.split(","):
    values.append(int(val))

print(values[0] + values[1] - values[2])