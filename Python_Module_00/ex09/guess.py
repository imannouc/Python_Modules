import sys,random

if __name__ == '__main__':
    number = random.randint(1,99)
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
            num = int(guess)
        except ValueError:
            print("That's not a number.")
            trials += 1
            continue
        if (num < 1 or num > 99):
            print('A number must be between 1 and 99')
            trials += 1
            continue
        if (num > number):
            print("Too high !")
            trials += 1
        elif (num < number):
            print("Too low !")
            trials += 1
        else:
            trials += 1
            if (num == 42):
                print('The answer to the ultimate question of life, the universe and everything is 42.')
            if (trials == 1):
                print("Congratulations! You got it on your first try!")
                trials = 0
                break
            print("Congratulations, you've got it!")
            print(f"You won in {trials} attempts")
            break