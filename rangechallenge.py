#!/usr/bin/env python3

# Part 1

for x in range(10):
    print(x, end= " ")

print("Round One Complete \n") 

# Part 2

for x in range(4,32,2):
    print(x, end= "\n")

print("Round Two Complete \n")

# Part 3

num= int(input("How many bottles do ya want?"))

for x in range(num,0,-1):
    print(f"{x} bottles of beer on the wall, {x} bottles beer on the wall, Take one down pass it around {x} bottles of beer on the wall")

print("Round Three Complete \n") 
