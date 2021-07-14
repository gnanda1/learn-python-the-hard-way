# Functions and Files.
from sys import argv

script, input_file = argv

# function to print the whole file.
def print_all(f):
    print(f.read())

# 0: sets the reference point at the beginning of the file
# seek() function is used to change the position of the File Handle to a given specific position.
def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print(line_count, f.readline())

# Priting the whole file.
current_file = open(input_file)
print("First, let's print the whole file:\n")
print_all(current_file)

print("Now let's rewind, like a tape.")
rewind(current_file)

# Printing each line.

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_file.close()
