#!/usr/bin/env python3


                            #Part One
def main():

    x= float(input("How would you rank your day today on a scale of 1-10?"))
    if x == 10:
        print("Attaboy! Stay positive!")
    elif x >= 8:
        print("Sounds lovely! Keep on truckin'!")
    elif x >= 6:
        print("Chin up, buttercup!")                    
    elif x >= 4:            
        print("I recommend some hot chocolate and a hug, maybe...")               
    elif x >= 2:
        print("Dude, are you ok?")                   
    else:
        print("Geez!!! You might as well just go back to bed!")

main() 


                            #Part Two

#Creates input outside of the function, to be placed within the function.

adj1 = input("Choose an adjective: ")
adj2 = input("Choose another adjective: ")

def python_props(x, y):
    print(f"Python is {x} and {y}!")

python_props(adj1, adj2)



                            #Part Three

#Will create random capitalization and lower case of words

from random import choice

sentence = input("What would you like to change? ") 
print(''.join(choice((str.upper, str.lower))(c) for c in sentence))
