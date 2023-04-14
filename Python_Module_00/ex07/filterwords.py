import sys , string

if __name__ == '__main__':
    err = 1
    if (len(sys.argv) == 3 and (isinstance(sys.argv[1],str)) and (sys.argv[2].isdigit())):
        err = 0
    if err:
        print("ERROR")
        exit()

    S = sys.argv[1]
    N = int(sys.argv[2])
    S = S.translate(S.maketrans('','',string.punctuation))
    S = S.split()
    tmp = [ word for word in S if (len(word) > N)]
    print(tmp)