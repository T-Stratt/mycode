from cheatdice import *
swapper = Cheat_Swapper()
loaded_dice = Cheat_Loaded_Dice()
Mulligan_Cheater = Cheat_Mulligan()
Extra_Die_Roller = Cheat_Extra_Die()
swapper_score = 0
loaded_dice_score = 0
Mulligan_Cheater_score = 0
Extra_Die_Roller_score = 0
number_of_games = 100000
game_number = 0
print("Simulation running")
print("==================")
while game_number < number_of_games:
  swapper.roll()
  loaded_dice.roll()
  Mulligan_Cheater.roll()
  Extra_Die_Roller.roll()

  swapper.cheat()
  loaded_dice.cheat()
  Mulligan_Cheater.cheat()
  Extra_Die_Roller.cheat()
   #Remove # before print statements to see simulation running
   #Simulation takes approximately one hour to run with print
   #statements or ten seconds with print statements
   #commented out

 #print("Cheater 1 rolled" + str(swapper.get_dice()))
 #print("Cheater 2 rolled" + str(loaded_dice.get_dice()))
  if sum(swapper.get_dice()) == sum(loaded_dice.get_dice()):
 #print("Draw!")
    pass
  elif sum(swapper.get_dice()) > sum(loaded_dice.get_dice()):
 #print("Dice swapper wins!")
   swapper_score+= 1
  elif sum(swapper.get_dice()) == sum(Mulligan_Cheater.get_dice()):
 #print("Draw!")
    pass
  elif sum(swapper.get_dice()) > sum(Mulligan_Cheater.get_dice()):
   swapper_score+= 1
  elif sum(swapper.get_dice()) == sum(Extra_Die_Roller.get_dice()):
 #print("Draw!")
    pass
  elif sum(swapper.get_dice()) > sum(Extra_Die_Roller.get_dice()):
   swapper_score+= 1 
  else:
 #print("Loaded dice wins!")
    loaded_dice_score += 1
    Mulligan_Cheater_score += 1
    Extra_Die_Roller_score += 1
  game_number += 1
print("Simulation complete")
print("-------------------")
print("Final scores")
print("------------")
print("Swapper won: " + str(swapper_score))
print("Loaded dice won: " + str(loaded_dice_score))
print("Mulligan_Cheater won: " + str(Mulligan_Cheater_score))
print("Extra_Die_Roller won: " + str(Extra_Die_Roller_score))
if swapper_score == loaded_dice_score:
  print("Game was drawn")
elif swapper_score > loaded_dice_score:
  print("Swapper won most games")
elif swapper_score > Mulligan_Cheater_score:
  print("Swapper won most games")
elif swapper_score > Extra_Die_Roller_score:
  print("Swapper won most games")
else:
  print("Loaded dice won most games")
  print("Mulligan_Cheater won most games")
  print("Extra_Die_Roller won most games")

