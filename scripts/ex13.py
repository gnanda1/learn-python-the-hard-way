#Parameters, Unpacking, Variables
"""
Run the program like this (and you must pass three command line arguments):
$ python3.6 ex13.py first 2nd 3rd
$ python3.6 ex13.py stuff things that
$ python3.6 ex13.py apple orange grapefruit
"""

from sys import argv
# read the WYSS section for how to run this

#Unpack variables
script, first, second, thrid = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your thrid variable is:", thrid)
