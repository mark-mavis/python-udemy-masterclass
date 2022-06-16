

numbers = (1, 2, 3, 4, 5) # numbers = Tuple
print(numbers)
print(*numbers) # * unpacked the numbers, and fed them to the print function


print(numbers, sep=";") # sep=";" does nothing because there is only one value or iterator
print(*numbers, sep=";")
print(1, 2, 3, 4, 5, sep=";")

def test_star(*args):   # *args specifies that args is an unpacked tuple
  print(args)           # print the tuple
  for x in args:        # print the unpacked values
    print(x)



test_star(0, 1, 2, 3, 4, 5)