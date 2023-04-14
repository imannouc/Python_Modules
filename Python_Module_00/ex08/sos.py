import sys
morse_code = {
    'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ' ':'/'
}

if __name__ == '__main__':
    if (len(sys.argv) == 1):
        print('ERROR: arguments required.')
        exit()
    sys.argv.pop(0)
    str = ' '.join(sys.argv)
    if not all(c.isalnum() or c == ' ' for c in str):
        print('ERROR: Enter a string containing alphanumeric characters and/or space only.')
        exit()
    str = str.upper()
    s = map(lambda x : morse_code[x], str)
    print(' '.join(s))