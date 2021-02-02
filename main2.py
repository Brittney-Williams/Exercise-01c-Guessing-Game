#!/usr/bin/env python3
import sys, random
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"



number = random.randrange(1,11)
count = 0
guess = -1
while guess != number:
    count = count + 1
    guess = input("Guess a number from 1 to 10 ")
    try:
     guess = int(guess)
     if guess != number:
        print("Not quite! Try and guess again")
    except:
        print("Try and answer a number buddy.")
print("Great work! You recieve a gold star! You got the number of tries in " + str(count) + " tries. ")