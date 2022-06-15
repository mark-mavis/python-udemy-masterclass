def fizz_buzz(num: int) ->str:
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
        
for i in range(1,101):
   print(fizz_buzz(i)) 