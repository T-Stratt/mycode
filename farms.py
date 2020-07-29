#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

message = input("What farm would you like to visit, the NE Farm, W Farm, or SE Farm ?")

if message == "NE Farm":
    print("Here at the NE Farm are the available animals:")
    for every_animal in farms [0]["agriculture"]:
        print(every_animal)
elif message == "W Farm":
    print("Here at the W Farm are the available animals:")
    for every_animal in farms [1]["agriculture"]:
        print(every_animal)
elif message == "SE Farm":
    print("Here at the SE Farm are the available animals:")
    print(farms [2]["agriculture"][0]) 
        


