#Tuple is a mathematical name from an ordered set of data

#Tuples are immutable which means they can not be changed

#Advantages of tuples, they can always be unpacked successfully because tuples cant be changed, you always know how many items there are to unpack

#Deciding What to Use....
# - Depends on whether or not you want to add new items.
#	You can't append to a tuple because tuples are immutable


data = 1, 2, 3
x, y, z = data
print(x)	# prints 1
print(y)	# prints 2
print(z)	# prints 3

for tuple_val in enumerate("abcdefgh"):
	print("Tuple: {0}".format(tuple_val))

table = ("Coffee Table", 200, 100, 75, 34.50)
name, width, length, height, weight = table		# "Unpacking" the tuple
print(f"Area of {name}: {(width*length)/12}sq. ft.")

albums = [
	("Welcome to my Nightmare", "Alice Cooper", 1975),
	("Bad Company", "Bad Company", 1974),
	("Nightflight", "Budgie", 1981),
	("More Mayhem", "Emilda May", 2011),
	("Ride the Lightning", "Metallica", 1984)
	]

# Unpacking Tuples

for album in albums:
	title, artist, release_year = album
	print(f"Artist: {artist} Album Title: {title} Release Year: {release_year}")

for title, artist, release_year in albums:
	print(f"Artist: {artist} Album Title: {title} Release Year: {release_year}")

# Nested Tuples
