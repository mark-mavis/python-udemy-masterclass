
#Sequence Types allow you to "slice" them

parrot = "Norwegian Blue"

print(parrot[0:6])  # Norweg (inclusive start position - exclusive end position)
print(parrot[0:9])  # Norwegian
print(parrot[ :9])  # Norwegian Same as previous statement

# 
# INDEX VS SLICE
#   index ---> parrot[10];
#   slice ---> parrot[0:6]  

print(parrot[10:])
print(parrot[:])    #prints from start to finish

      
print(parrot[-4:-2])    # Bl
