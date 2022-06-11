panagram = "The quick brown fox jumps over the lazy dog"
print(panagram)
print(panagram.split(" "))

numbers = "9,223,523,526,745,232,645,844"
split_numbers = numbers.split(",")
print(split_numbers)


joined_values = " ".join(split_numbers)
print(joined_values)

print(joined_values.split())

numeric_list = []
for index, val in enumerate(numbers.split(",")):
	print(f"Index: {index} Val: {val}")
	numeric_list.append(int(val))
	
print(numeric_list)
