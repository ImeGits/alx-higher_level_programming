#!/usr/bin/python3
#Write a program that will assign a random signed number to the variable number each time it is executed.
import random
number = random.randint(-10000, 10000)
figure = abs(number) % 10
if number < 0:
    figure = -figure
print(f"Last digit of {number:d} is {figure:d} and is ", end="")
if figure > 5:
    print("greater than 5")
elif figure == 0:
    print("0")
else:
    print("less than 6 and not 0")
