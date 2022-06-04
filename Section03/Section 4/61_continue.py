
#list

shopping_list = ["Milk", "Pasta", "Eggs", "Spam", "Bread", "Rice"]

# Both for loops do the same thing, exclude spam
for item in shopping_list:
    if item == "Spam":
        continue        # Causes the rest of the code in the block to be skipped
                        # Continue to the next iteration of the for loop
    print("Buy " + item)

for item in shopping_list:
    if item != "Spam":
        print(item)




for index in range(1,5):
    print("Buy: " + shopping_list[index])

if "Spam" in shopping_list:
    print("Found Spam")