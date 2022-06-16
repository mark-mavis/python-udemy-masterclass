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

# Dictionaries preseve the insertion order
# The following items being added, add to the end of the dictionary
vehicles["roadster"] = "Chevy SS"   # Preserves key/value location in dictionary

for key, value in vehicles.items():
  print(key, value, sep=", ")
  