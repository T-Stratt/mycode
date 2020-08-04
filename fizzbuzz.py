#!/usr/bin/env python3

Fizz = 0
Buzz = 0
FizzBuzz = 0
num = 0

for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz", end= "\n ") 
        FizzBuzz += 1

    elif x % 3 == 0:
        print("Fizz" , end= "\n ")
        Fizz += 1

    elif x % 5 == 0:
        print("Buzz", end= "\n ")
        Buzz += 1

    else:
        print(x, end= "\n ") 
        num += 1

print("\n")
print("Fizz=" , Fizz)
print("Buzz=" , Buzz)
print("FizzBuzz=" , FizzBuzz)
print("Integers=" , num) 
