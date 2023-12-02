#!/usr/bin/python3
# Write a program that prints numbers from 0 to 99.
# Numbers must be separated by ,, followed by a space.
# Numbers should be printed in ascending order, with two digits.
# The last number should be followed by a new line.
for i in range(100):
    if i == 99:
        print("{}".format(i))
    else:
        print("{:02}".format(i), end=", ")
