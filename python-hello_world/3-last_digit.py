#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    last_digit = -1 * (abs(number) % 10)
else:
    last_digit = number % 10

num = ""

if last_digit > 5:
    num = "greater than 5"
elif last_digit < 6 and last_digit != 0:
    num = "less than 6 and not 0"
else:
    num = "0"

print("Last digit of {:d} is {:d} and is {}".format(number, last_digit, num)) 
