#!/usr/bin/env python3

# Fuctions to define the methods of arithmetic 
def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

# While loop executes to allow to try again.
while True:
    welcome = print("Welcome, What would you like to learn today?")
    message = input("Do you want to Add, Subtract, Divide, or Multiply?")

# The raise ValueError will occur when message condition is not met.
    try:
        if message not in ["add", "subtract", "multiply", "divide"]:
            raise ValueError
# Doing float allows for the use of decimals, without would create False conditon.
        x = float(input("Choose a number:"))  
        y = float(input("Choose another number:")) 
# Terminates the loop after conditions have been met.
        break
    except:
        print("You're dumb,try again.")
# If,Elif statements are executed and print out respective answers.
if message.lower() == "add":
    print('The answer is ' + str(add(x,y)))

elif message.lower() == "subtract":
    print('The answer is ' + str(subtract(x,y)))

elif message.lower() == "multiply":
    print('The answer is ' + str(multiply(x,y)))

elif message.lower() == "divide":
    print('The answer is ' + str(divide(x,y)))
