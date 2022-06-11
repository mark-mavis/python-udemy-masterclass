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
new_albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

for album, artist, release_year, songs in new_albums:
    for track, song_title in songs:
        print(f"{artist} - {album} - {track} - {song_title}")

print(new_albums[3])
print(new_albums[3][3])
print(new_albums[3][3][2])
print(new_albums[3][3][2][1])