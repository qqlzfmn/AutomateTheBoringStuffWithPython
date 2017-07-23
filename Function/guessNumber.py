#This is a guess the number game.
import random
def guess():
    count = 1
    randNum = random.randint(1, 20)
    print('I am thinking of a number between 1 and 20.')
    while count < 7:
        guessNum = input('Take a guess.')
        if guessNum > randNum:
            print('Your guess is too high.')
        elif guessNum < randNum:
            print('Your guess is too low.')
        else:
            break
        count = count + 1
    if guessNum == randNum:
        print('Good Job! You guessed my number in ' + str(count) + ' guesses!')
    else:
        print('Nope. The number I was thinking of was ' + str(randNum) + ' .')
    return
guess()
exit()