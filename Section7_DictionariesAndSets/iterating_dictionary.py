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

# Iterating over the keys in the dictionary
for key in vehicles:
  print(f"Key: {key} Value: {vehicles[key]}")
  
# Use enumerators when iterating over sequences
for index, value in enumerate(vehicles):
  print(f"Key Index: {index} Value: {vehicles[value]}")

# Use .items() when iterating over Dictionaries
for key, value in vehicles.items():
  print(f"Key: {key} Value: {value}")