
#Pangram is a statment that has every letter of the alphabet
#FUNCTIONS CREATE NEW ARRAY AND DO NOT CHANGE ORIGINAL ARRAY
pangram = "The quick brown fox jumps over the lazy dog"
sorted_pangram = sorted(pangram)    #creates and returns a new sorted string
sorted_pangram_ignore_capital = sorted(pangram, key=str.casefold)   #str.casefold tells the sorted function to ignore uppercase chars

print(f"{id(pangram)}: {sorted_pangram}")  
print(f"{id(sorted_pangram)}: {sorted_pangram}")
print(f"{id(sorted_pangram_ignore_capital)}: {sorted_pangram_ignore_capital}")

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)    #creates and returns a new sorted array of numbers
print(f"{id(numbers)}: {numbers}")
print(f"{id(sorted_numbers)}: {sorted_numbers}")


#METHODS CHANGE THE ITERATOR ITSELF
numbers2 = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
numbers2.sort()


names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "michael"
         ]

names.sort(key=str.casefold)
print(names)





