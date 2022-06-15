def fizz_buzz(num: int) -> str:
  """
  Function that returns game fizz buzz
  """
  fizz_val = "fizz"
  buzz_val = "buzz"
  
  if i%3 == 0 and i%5 == 0:
    return fizz_val + " " + buzz_val
  
  if i%3 == 0 or i%5 == 0:
    if i%3 == 0:
      return "fizz"      
    else:
      return "buzz" 
  else:
    return str(i)


def game(guess: str, val: int) -> str:
  if i%3 != 0 and i%5 != 0:
    return int(guess) == val
  
  if i%3 == 0 and i%5 ==0:
    return guess == "fizz buzz"
    
  if i%3 == 0 or i%5 == 0:
    if i%3 == 0:
      return guess == "fizz"
    else:
      return guess == "buzz"

print("Welcome to Fizz Buzz the Game")
print("Enter Values and see how far you can get")


for i in range(1,101):
  guess = input(f"{i}: ")
  if game(guess, i):
    print("Correct")
  else:
    print("You failed!!")
    break    