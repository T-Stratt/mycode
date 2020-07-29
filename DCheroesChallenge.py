#!/usr/bin/env python3

hero= {"flash":{"speed": "fastest", "intelligence": "lowest", "strength": "lowest"}, "batman":{"speed": "slowest", "intelligence": "highest", "strength": "money"}, "superman":{"speed": "fast", "intelligence": "average", "strength": "strongest"}}

answer= " "

while answer != "q":
  try:
    char_name= input("Which character do you want to know about? (Flash, Batman, Superman) ")

    char_stat= input("What statistic do you want to know about? (strength, speed, or intelligence) ")

    print(f"{char_name.capitalize()}'s {char_stat} is: {hero[char_name][char_stat].capitalize()}")
  except:
    print("You provided incorrect input.")

  answer= input("Press ENTER to choose another hero, or press Q to quit!")
