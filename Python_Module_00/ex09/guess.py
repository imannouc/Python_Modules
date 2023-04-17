import sys,random

if __name__ == '__main__':
    number = random.randint(1, 99)
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!")
    trials = 0
    while (1):
        print("What's your guess between 1 and 99?")
        guess = input(">> ")
        if (guess == 'exit'):
            print("Goodbye!")
            exit()
        try:
            assert guess.isnumeric()
        except AssertionError:
            print("That's not a number.")
            trials += 1
            continue
        if (int(guess) > number):
            print("Too high !")
            trials += 1
        elif (int(guess) < number):
            print("Too low !")
            trials += 1
        else:
            trials += 1
            if (int(guess) == 42):
                print('The answer to the ultimate question of life, the universe and everything is 42.')
            if (trials == 1):
                print("Congratulations! You got it on your first try!")
                trials = 0
                continue
            print("Congratulations, you've got it!")
            print(f"You won in {trials} attempts")
            trials = 0