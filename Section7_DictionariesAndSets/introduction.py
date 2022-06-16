
# Dictionaries and Sets are NOT sequences so they can not be indexed into
# We use a KEY to get individual values from the dictionary. Referred to as a 
# mapping. Python dictionary is equivalent to a java HashMap
#   - Dictionaries store KEY/VALUE pairs

# A set is an unordered collection of things. There is no way to retrieve a specific item from a set.

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

my_car = vehicles['can-am'] # Providing a key, then the dictionary returns the value
                            # associated with the key
print(my_car)

key = vehicles.get("er5") # The key has to match exactly! Case matters
print(key)


# Indexing is faster when you know the key exists
# Get method is safer when you don't know if the key exists