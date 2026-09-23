#!/usr/bin/env python3

print("Enter a number")
num = int(input())

i = 0
while i < 10:
    print(str(i) + " x " + str(num) + " = " + str(i * num))
    i += 1
    