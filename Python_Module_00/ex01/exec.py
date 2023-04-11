import sys

argc = len(sys.argv)
if (argc < 2):
    print("You must provide an Argument.")
    exit()

sys.argv.pop(0)
str = ' '.join(sys.argv)[::-1].swapcase()
print(str)