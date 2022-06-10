
from math import fabs


empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

print(even+odd)

# Replacing index 2 on in the even sequence
print(even)
even[2:] = odd
print(even)

digits = sorted("432985617")
digits_obj = list("432985617")

print(f"{digits}")       # prints a list of characters that are each strings of 1
print(f"{id(digits_obj)}: {digits_obj}")

sorted_objects = sorted(digits_obj)

print(f"{id(sorted_objects)}: {sorted_objects}")

print(sorted_objects == digits) #True because they have the same items inside
print(sorted_objects is digits) #False because they are not the same list

#COPYING LISTS
copied_list = sorted_objects.copy()
print(f"{id(copied_list)}: {copied_list}")