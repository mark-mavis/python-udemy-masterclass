def fibonacci(n: int) -> int:
  """Returns the `n`th Fibonacci number, for positive `n`
  """
  if 0 <= n <= 1:
    return n
  
  fib1, fib2 = 1, 0
  result = None
  for i in range(n-1):
    result = fib2 + fib1
    fib2 = fib1
    fib1 = result
  return result
 
    
for i in range(36):
  print(f"{i}: {fibonacci(i)}")
  
fibonacci(100)
