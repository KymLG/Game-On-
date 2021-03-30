print("You are in a dark room in an mysterious castle")
import time
time.sleep(1.5)
print("In front of you there are four doors. You must choose one.")
playerChoice = input("Choose 1, 2, 3, or 4...")
if playerChoice == "1":
  print("You find a room full of treasure. You're rich!")
  print ("GAME OVER, YOU WIN!")
elif playerChoice == "2":
  print("The door opens and an angry ogre hits you with his club.")
  time.sleep(1)
  print("GAME OVER, YOU LOSE!")
elif playerChoice =="3":
  print("You go into the room and find a sleeping dragon")
  time.sleep(1.5)
  print("1) Try to steal some of the dragons sacred gold.")
  print("2) Try to sneak around the dragon to exit.")
  dragonChoice = input("Type 1 or 2...")
  if dragonChoice == "1":
    time.sleep(1)
    print("The dragon wakes up and eats you. You are delicious")
    print("GAME OVER, YOU LOSE!")
  if dragonChoice == "2":
    print("You sneak around the dragon and escape the castle, blinking in the golden sunshine.")
    print("GAME OVER, YOU WIN!")
elif playerChoice =="4":
   print(" A wizard appears and casts a spell over you, you turn into a T-Rex and go on a hunt for meat!")
   time.sleep(2)
   print("Game over, let the meat hunt begin!")
else:
  print("Sorry, you didn't enter 1, 2, 3 or 4!")
  print("Run the game to have another go.")