__author__ = 'casey'

import random

def main():

    #varibles
    randNumber = random.randint(0,9)
    guessedNumber = 0

    while True:
        #pick a number
        print("I've picked a number.")
        guessedNumber = int(input("Guess what it is: "))


        if guessedNumber == randNumber:
            print(guessedNumber)
            print("That's correct! How did you know??")
            break

        elif guessedNumber < randNumber:
            print(guessedNumber)
            print("Too low. Try again")

        elif guessedNumber > randNumber:
            print(guessedNumber)
            print("Too high. Try again")

main()