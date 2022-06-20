# Calculate the cube of all numbers from 1 to a given number
# Write a program to rint the cube of all numbers from 1 to a given number
from re import I

n = int(input("Value: "))
for i in range(1, n+1):
    # logic for finding cube of number
    cub = i * i * i
    print("Current Number is: ", i, "and the cube is", cub)
