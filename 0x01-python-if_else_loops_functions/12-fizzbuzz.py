#!/usr/bin/python3
# Write a function that prints from 1 to 100 separated by a space.
# For multiples of three print Fizz instead and for multiples of five print Buzz.
# For numbers which are multiples of both three and five print FizzBuzz.

def fizzbuzz():
    for digits in range(1, 101):
        if digits % 3 == 0 and digits % 5 == 0:
            print("FizzBuzz ", end="")
        elif digits % 3 == 0:
            print("Fizz ", end="")
        elif digits % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(digits), end="")
