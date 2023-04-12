import string, sys

def text_analyzer(str=None):
    '''This function counts the number of upper characters, lower characters, punctuation and spaces in a given text.'''
    if (str == None):
        str = input('What is the text to analyze?\n')
    try:
        assert type(str).__name__ == 'str'
    except AssertionError:
        print('AssertionError: argument is not a string')
        return
    print("The text contains",len(str),"character(s):")
    lowerCount, upperCount, punctCount, spaceCount = 0,0,0,0
    for c in str:
        if (c in string.punctuation):
            punctCount += 1
        elif (c.isspace()):
            spaceCount += 1
        elif (c.islower()):
            lowerCount += 1
        elif (c.isupper()):
            upperCount += 1
    print("-",upperCount,"upper letter(s)")
    print("-",lowerCount,"lower letter(s)")
    print("-",punctCount,"punctuation mark(s)")
    print("-",spaceCount,"space(s)")

if __name__ == '__main__':
    try:
        assert len(sys.argv) == 2
    except AssertionError:
        print('AssertionError: You MUST provide one argument (only).')
        exit()
    text_analyzer(sys.argv[1])

# def main():
#     text_analyzer("Python 2.0, released 2000, introduced features like List comprehensions and a garbage collection system capable of collecting reference cycles.")
#     text_analyzer("Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace.")
#     text_analyzer()
# main()
