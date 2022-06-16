vehicles = {
  'dream': 'Honda 250T',
  'roadster': 'BMW R1100',
  'er5': 'Kawasaki ER5',
  'can-am': 'Bombardier Can-Am 250',
  'virago': 'Yamaha XV250',
  'tenere': 'Yamaha XT650',
  'jimmy': 'Suzuki Jimmy 1.5',
  'fiesta': 'Ford Fiesta Ghia 1.4',
}

# Deleting the Jimmy key from the dictionary
del vehicles['jimmy']

# Deleting the key using the pop method
vehicles.pop("dream", None)  # None is a default return value
vehicles.pop("ferrari", "No Ferrari in inventory")  # Passing a string as the default value


for key, value in vehicles.items():
  print(key, value, sep=", ")
  