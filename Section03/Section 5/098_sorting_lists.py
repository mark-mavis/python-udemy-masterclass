
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# sequence.extend(iterable) takes all items of the iterable and addes them to the even iterable

even.extend(odd)    #Adds odd list to end of even list
print(even)

# Sort the iterable in Ascending order
even.sort(reverse=False)
print(even)

# Sort the iterable in Descending order
even.sort(reverse=True)
print(even)

# Sort the iterable in Ascending order
even.reverse()
print(even)