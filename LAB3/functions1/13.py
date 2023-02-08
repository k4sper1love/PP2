import random
def GuessTheNumber(name, cnt = 0):
    global randnum
    numb = int(input('Take a guess.\n'))
    if randnum == numb:
        cnt += 1
        return print("\nGood job, {}! You guessed my number in {} guesses!".format(name, cnt))
    elif randnum > numb:
        print("\nYour guess is too low.")
        cnt += 1
        GuessTheNumber(name, cnt)
    elif randnum < numb:
        print("\nYour guess is too high.")
        cnt += 1
        GuessTheNumber(name, cnt)
    
name = input("Hello! What is your name?\n")
print("\nWell, {}, I am thinking of a number between 1 and 20.".format(name))
randnum = random.randint(1,21)
GuessTheNumber(name)

    