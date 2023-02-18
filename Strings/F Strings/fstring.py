import math
from this import d
from tkinter import Variable

Greeting = "Hello "
name = "Mark Mavis"
age = 24

print(Greeting + name)  #Printing concatenated two strings
print(age)              #Printing the age string
print(type(age))        #Printing the Type of the age variable
print(type(Greeting))   #Printing the Type of the greeting variable

#========= F STRING ===============
age_in_words = "2 years"
print(name + f" is {age_in_words} old")

#========= OPTIONS ================
# < - Forces left alightment of expression inside curly brace {} - Default for strings
# > - Forces right alignment of expression inside curly brace {} 
# ^ - Forces center alignment of expression inside curly brace {}
# | - Delineate the spacing
# : - The number after the semi-colon with cause the field to be that number of characters wide

# print(f"|-->{variable = }<--|")       Output = |--> variable = value <--|

#========== DATA TYPES =============
# s - String format - this is the default type for strings
# d - Decimal Integer
# n - Number. This is the same as d except that it uses the current
#       locale setting to insert the appropriate number separator characters
# E - Exponent Notation. Prints the number in scientific notation
# f - Fixed-point notation. Display number as fixed point number
# % - Percentage. Multiplys numberby 100 and displays in fixed format
#       followed by a percentage sign

value = 3.14159;
variable = math.pi

print(f"Using Numeric {variable = }") # Using Numberic variable = 3.141592653589793
print(f"|{variable:25}|")      # DEFAULT
print(f"|{variable:<25}|")
print(f"|{variable:>25}|")
print(f"|{variable:^25}|")
print(f"|{variable:^25}|\n")

# ALIGNMENT
print("ALIGHNMENT")
variable = "Python 3.9"
print(f"Using String {variable = }")
print(f"f\"|{variable:25}|\"")       # DEFAULT
print(f"f\"|{variable:<25}|\"")
print(f"f\"|{variable:>25}|\"")
print(f"f\"|{variable:^25}|\"")
print(f"f\"|{variable:^25}|\"\n")

# FILL ALIGHNMENT

variable = math.pi
print(f"Using string {variable = }")    #Using String variable = 3.141592653589793
print("FILL ALIGNMENT var:=<25")
print(f"|{variable:=<25}|")             #|3.141592653589793========|
print("FILL ALIGNMENT var:=>25")
print(f"|{variable:=>25}|")             #|========3.141592653589793|
print("FILL ALIGNMENT var:=^25")
print(f"|{variable:=^25}|")             #|====3.141592653589793====|
                                        
print()

variable = "Python 3.9"                 
print(f"Using String {variable = }")    #Using String variable = 'Python 3.9'
print(f"|{variable:=<25}|")             #|Python 3.9===============|             
print(f"|{variable:=>25}|")             #|===============Python 3.9|
print(f"|{variable:=^25}|")             #|=======Python 3.9========|



variable = 10
print(f"|Decimal Formatting: {variable:d}")
print(f"|Decimal 20 spaces Formatting: {variable:20d}|")


variable = 4
print(f"Percentage: {variable:%}")
variable = 3252564634
print(f"Exponential Form: {variable:e}")
variable = 153235423.5233
print(f"{variable:+,.2f}")  # added sign (+) and added commas (,) with two decimal places (.2f) ---->    +153,235,423.52

variable = math.pi
print(f"|{variable:025}|")              #|000000003.141592653589793|
print(f"|{variable:<025}|")             #|3.14159265358979300000000|
print(f"|{variable:>025}|")             #|000000003.141592653589793|
print(f"|{variable:^025}|")             #|00003.1415926535897930000|

print(f"|{variable:=<025}|")        #|3.141592653589793========|
print(f"|{variable:=>025}|")        #|========3.141592653589793|
print(f"|{variable:=^025}|")        #|====3.141592653589793====|

print(f"|{variable:<025f}|")


print(f"|Printing with zeros as spaces {variable:09.5f}|")
print(f"|No Formatting: {variable:>010}|")

print("{:.2f}".format(value))      # Output 3.14
print("{:<10.3f}".format(value))   # Display a float with 3 decimal places and left-align it in a field of width 10
print("{:>110.5f}".format(value))  # Display a float with 5 decimal places and right-align it in a field of width 10, padding with zeroes
#0003.14159

