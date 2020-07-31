#!/usr/bin/env python3
"""Alta3 Research | Author: csfeeser@alta3.com"""

# imports always go at the top of your code
import requests
import random

r = requests.get('https://cat-fact.herokuapp.com/facts')


def highest_upvotes():
    upvote_list= []
    for x in r.json()["all"]:
        upvote_list.append(x.get("upvotes"))
    print("\nThe highest upvote count was:")
    print("=============================")
    print(max(upvote_list))

def random_cat_fact():
    fact_list= []
    for x in r.json()["all"]:
        fact_list.append(x.get("text"))
    print("\nEnjoy a random cat fact!")
    print("========================")
    print(random.choice(fact_list))
                             
                             
random_cat_fact()
highest_upvotes() 
