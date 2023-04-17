import sys

if (len(sys.argv) != 2):
    print("You must provide ONE integer as an argument.")
    exit()

try:
    assert sys.argv[1].isnumeric()
except AssertionError:
    print('AssertionError: argument is not an integer')
    exit()

if (int(sys.argv[1]) == 0):
    print("I'm Zero.")
elif (int(sys.argv[1]) % 2 == 0):
    print("I'm Even.")
else:
    print("I'm Odd.")