# Names, Variables, Code, Functions
# this one is like your scripts with argv

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this.
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument.
def print_one(arg1):
    print(f"arg1: {arprint_two_againg1}")

# this just takes no arguments.
def print_none():
    print("I got nothin'.")

print_two("Bruce", "Wayne")
print_two_again("Bruce", "Wayne")
print("Python!")
print_none()
