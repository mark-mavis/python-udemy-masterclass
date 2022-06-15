# Mode
# - r - read - open file
# - w - write - open file for writing. Creates new file if it does not exists or truncates the file it if exists.
# - a - append - opens file for appending to the end of the file without truncating. creates new file if it does not exist.
# - x - exclusive creation - opens file for exclusive creation. If file exists, operation fails.
# - + - updating (reading and writing)

# Can also open as TEXT MODE (default) and BINARY MODE
# - t - text mode
# - b - binary mode

# TEXT MODE
#   Gets strings when reading the file
# BINARY MODE
#   Gets bytes when readig the file (meant for dealing with non-text files like images or executable files)


file = open("textfile.txt", mode='r', encoding='utf-8')
