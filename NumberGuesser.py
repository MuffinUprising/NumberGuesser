__author__ = 'casey'

import random

def main():

    #varibles
    high_number = 0
    low_number = 0
    guessedNumber = 0

    #pick a number
    print("Choose a range of numbers to guess from")
    low_number = int(input("First, choose the lowest number in range: "))
    high_number = int(input("Second, choose the highest number in range: "))
    print("I've picked a number.")

    randNumber = random.randint(low_number, high_number)


    while True:

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