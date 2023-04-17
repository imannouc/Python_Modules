import sys

if (len(sys.argv) != 2):
    print("You must provide ONE integer as an argument.")
    exit()

try:
    num = int(sys.argv[1])
except (ValueError,AssertionError):
    print('AssertionError: argument is not an integer')
    exit()

if (num == 0):
    print("I'm Zero.")
elif (num % 2 == 0):
    print("I'm Even.")
else:
    print("I'm Odd.")