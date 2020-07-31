#!/usr/bin/env python3
import random

num= int(input("How many Shakespearean insults would you like?"))

insult_list = open("/home/student/mycode/myinsults.txt", "r")

insult = insult_list.readlines()

def insult_list(num):
     print("You are a", end="")
     for x in range(num):
        print(random.choice(insult))

insult_list(num)
