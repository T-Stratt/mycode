#!/usr/bin/env python3

astro= {"message": "success", "number": 5, "people": [{"craft": "ISS", "name": "Chris Cassidy"}, {"craft": "ISS", "name": "Anatoly Ivanishin"}, {"craft": "ISS", "name": "Ivan Vagner"}, {"craft": "ISS", "name": "Doug Hurley"}, {"craft": "ISS", "name": "Bob Behnken"}]} 

for every_astro in astro["people"]:
    print(every_astro['name']) 
    print(every_astro['craft'])

message = print(f" {every_astro['name']} is on {every_astro['craft']} in space")


