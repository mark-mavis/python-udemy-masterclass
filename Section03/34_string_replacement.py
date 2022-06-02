
age = 24
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, and {7}"
      .format(age, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec\n"))

print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {2}, Jul: {2}, Aug: {2}, Sep: {2}, Nov: {2}, Dec: {2}".format(28, 30, 31))

print("""Jan: {2} 
Feb: {0} 
Mar: {2} 
Apr: {1} 
May: {2} 
Jun: {2} 
Jul: {2} 
Aug: {2} 
Sep: {2} 
Nov: {2} 
Dec: {2}""".format(28, 30, 31))

for i in range(1,13):
    # Setting the format width of the replacement operators
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i**2, i**3))


for i in range(1,13):
    # Setting the format alignment - <=left, ^=center, >=right
    print("No. {0:<2} squared is {1:^4} and cubed is {2:>4}".format(i, i**2, i**3))
    

print("Pi is approximately {0:12}".format(22/7))
print("Pi is approximately {0:12f}".format(22/7))
print("Pi is approximately {0:12.50f}".format(22/7))
print("Pi is approximately {0:52.50f}".format(22/7))
print("Pi is approximately {0:62.50f}".format(22/7))
print("Pi is approximately {0:72.50f}".format(22/7))


name = "Mark Mavis"
age = 38
sal = 10000.25

#Approach 1
print(name, age, sal)

#Approach 2
print("Name is: ", name)
print("Age is: ", age)
print("Salary is: ", sal)

#Approach 3 : Using % operator --> Type is implied
print("Name: %s Age: %d Salary: %f"%(name, age, sal))

#Approach 4 : Using {} --> Value is Implied
#The types do not matter in these examples
print("Name: {} Age: {} Salary: {}".format(name, age, sal))
print("Name: {} Age: {} Salary: {}".format(sal, sal, sal))  
print("Name: {} Age: {} Salary: {}".format(sal, name, age))

#Approach 5 : Using {} -->Index & Value are implied
print("Name: {0} Age: {1} Salary: {2}".format(name, age, sal))
print("Name: {0} Age: {0} Salary: {0}".format(name, age, sal))  #Can pass the variations of the variables

#Padding String Replacement 
# {:<}  Left hand align
# {:>n} Right hand align
# {:^n} Center Align
print("Name: {0:<}".format(name))
print("Name: {0:^50}".format(name)) # Pad the center alignment 50 spaces (including input string)
print("Name: {0:>20}".format(name))

#passing in digits as variables
length = 26
print("Length is {:d}.".format(length))
print("Length is {:>6d}".format(length))
print("Length is {age:^10d}".format(age=8))

