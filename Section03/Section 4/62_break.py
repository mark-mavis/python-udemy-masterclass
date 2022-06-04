
shopping_list = ["Milk", "Pasta", "Eggs", "Spam", "Bread", "Rice"]

# Both for loops do the same thing, exclude spam
for item in shopping_list:
    if item == "Spam":
        break           # Causes the current execusion to stop
                        # Loop ends
    print("Buy " + item)

#item_to_find = "Africa"
item_to_find = "Pasta"
found_at = None

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break

if found_at is not None:
    print(f"{item_to_find} was found at index {index}" )
else:
    print(f"{item_to_find} Not found")

#Cleaner way of writing the previous code

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)
print(f"Item found at {found_at}")