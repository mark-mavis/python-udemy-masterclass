
from nesting_exercise import albums

# Add your code below this comment.
print(albums[1][3][5][1])
print(albums[2][2])
print(albums[3][3][3][0])

for album_title, artist, release_year, songs in albums:
    for song in songs:
        if song[1] == "Keeping a Rendezvous":
            print(song)

while True:
    for index, album in enumerate(albums):
        title, artist, year, songs = album
        print(index, title, artist, year, songs)
    break

while True:
    for index, (title, artist, year, songs) in enumerate(albums):
        print(index, title, artist, year, songs)
    break