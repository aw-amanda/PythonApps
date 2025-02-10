# Simple random number/option/card generator code in python
import random

# number
low = 1
high = 100

number = random.randint(low, high)      # prints a random number between 1 and 100

number2 = random.random()   # returns a random floating point number between 0 and 1

# option
options = ("Rock", "Paper", "Scissors")
option = random.choice(options)
print(option)

# card
cards = ["2," "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q", "A"]

random.shuffle(cards)
print(cards)