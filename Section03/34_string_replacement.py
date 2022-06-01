
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