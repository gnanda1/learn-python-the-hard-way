#Reading Files
#python3 ex15.py ex15_sample.txt

from sys import argv

script, filename = argv

# txt variable to open a file.
txt = open(filename)

print(f"Here's your file {filename}.")
print(txt.read())

print("Type the filename again:")
file_again = input('> ')

txt_again = open(file_again)

print(txt_again.read())

txt.close()
txt_again.close()
