
for i in range(10):
    print(f"i is now {i}")

i = 0
while i < 10:
    print(f"i is now {i}")
    i += 1

available_exits = ["North", "East", "South", "West"]
chosen_exit = ""

while chosen_exit not in available_exits:
    chosen_exit = input("Please enter directions")
    if chosen_exit.casefold() == "quit":
        print("Game Over")
        break