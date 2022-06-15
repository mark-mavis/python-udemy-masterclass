def factorial(num: int) -> int:
  """
  DocString of the function
  """
  if num == 1:
    return 1
  return num * factorial(num-1)

for i in range(1,36):
  print(f"{i}: {factorial(i)}")
