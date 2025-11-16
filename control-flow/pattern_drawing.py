#!/usr/bin/env python3

size = int(input("Enter the size of the pattern: "))

row = 0

while row < size:
    for star in range(size):
        print("*", end="")
    print()
    row += 1
