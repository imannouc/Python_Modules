import sys

if __name__ == '__main__':
    ac = len(sys.argv)
    if (ac < 3):
        print('Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3')
        exit()
    elif (ac > 3):
        print('AssertionError: too many arguments')
        exit()
    elif (ac == 3 and not(sys.argv[1].isnumeric() and sys.argv[2].isnumeric())):
        print('AssertionError: only integers')
        exit()
    # print(type(sys.argv[1]).__name__)
    A = int(sys.argv[1])
    B = int(sys.argv[2])
    print('Sum:', A + B)
    print('Difference:', A - B)
    print('Product:', A * B)
    print('Quotient:', A / B if B != 0 else 'ERROR (division by zero)')
    print('Remainder:', A % B if B != 0 else 'ERROR (modulo by zero)')
