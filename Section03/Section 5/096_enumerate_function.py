available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "hdmi cable",
                   "dvd drive"
                   ]

#Enumerate gets a pair of values 
# - The first being the index of the item
# - The second being the item itself


# Creating a list of Valid Number Options for user to choose
valid_choices = []
for i in range(1, len(available_parts)+1):
    valid_choices.append(str(i))

#print(valid_choices)

current_choice = None    #Initialize current choice
build_list = [] # create an empty list

#Start the Loop
# Exit Condition - User Enters 0
while current_choice != '0':
    # True if user entered a valid index number
    if current_choice in valid_choices:
        # Get index value of part in sequence
        index = int(current_choice) - 1
        # Get Part from parts list sequence
        chosen_part = available_parts[index]
        # True if part already exists in the build_list
        if chosen_part in build_list:   
            # If already in the build list, Remove it
            print(f"Removing {current_choice}")
            build_list.remove(chosen_part)  # Remove part from build_list
        else:
            # If not in the build list, Add it
            print(f"Adding {current_choice}")
            build_list.append(chosen_part)  # Append part to build_list
        #print updated build list
        print(f"Your list now contains: {build_list}")
    else:
        #User Entered Incorrect Input
        print("Please add options from the list below:")
        # Reprint list
        for number, part in enumerate(available_parts):
            print(f"{number+1}: {part}")

    current_choice = input("Enter Part Number to add")

print(f"Computer build list... {build_list}")
