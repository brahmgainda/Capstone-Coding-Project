# Course: CS 30
# Period: 1
# Date created: 20/10/24
# Date last modified: 20/10/26
# Name: Brahm Gainda
# Description: Capstone Coding Project

# Imports
import time as t
import random as r
from tabulate import tabulate

# Lists and dicts
knowledge = []
items = []
map_updates = []

# Prompts (User Input)
supplies = "Supplies Room or Showers "

courtyard_sneak = "\nNow that you've done that \
Will you sneak out to the courtyard \
to plan youre escape more in depth?(yes/no)"

security_guard = "\nYou are stopped by a security guard! \
Will you attack or run away?"

library_sneak = "\nOk well, You need the prisons blueprints to escape  \
Well you sneak to the library to get them? \
(yes/no)"

wake_up = "\nTonight is your escape \
you have 8 hours left \
Would you like to sneak to the library to get \
the crucial blueprints or act like a normal \
prisoner (sneak/act) ?"

escape_1 = "4 hrs have passed, the delivery truck \
has just arrived! Will you run to it (yes/no)"

# Prints Map Of The Prison
def print_map():
    """Function for printing grid map of Prison"""
    map = [['Guards Tower', 'Library', 'Guards Tower'],
           ['Supply Room', 'Your Cell', 'Showers'],
           ['Guards Tower', 'Courtyard', 'Guards Tower' ]]
    print(tabulate(map, tablefmt="grid"))


# creating a class for the rooms in the map
class Map:
    """Class for different rooms and their relevance"""
    def __init__(self, room, relevance):
        self.room = room
        self.relevance = relevance

    def __str__(self):
        desc = (f"the {self.room} is the room where "
                f"{self.relevance}")
        return desc

# Defining the different rooms
library = Map("Library", "you can find books\
to help you escape")
your_cell = Map("Your Cell", "you are meant to\
be most times")
supply_room = Map("Supply Room", "is where you can find items\
to help you escape")
courtyard = Map("Courtyard", "is where you go to\
scop out the surrounding areas")

# Intro Messages Explaining The Game
print("enter 'quit' at any time to quit ")
print("enter 'map' to see the map")
print("\nYour a prisoner who is failsely sentensced to life in prione")
print("You decided your going to escape the prison")
print("In exaclty 24 hours a delivery truck is going to come deliver food to the priosn")
print("That is your ticket out of here")
print("You need to start to prepare for the escape")


# Fixed Game Info That Is Used Throughout The Code
hours_left = 24

# Functions Used Throughout The Game
# Main Function
def escape(hours_left):
    "Returns The # of turns the user has left in the game"
    while hours_left > 0:
        message = """
Would you like to search for supplies? (say yes)
> \
""".format(hours_left)
# Prompt That Asks The User Their Desired Path
        x = input(message)
# map
        if x.lower() == "map":
                print_map()
                break
# Supplies path, One Path The User Could Use
# If the user wishs to look for supplies
        if x.lower() == "yes":
          print_map()
          print("Where will you go to find supplies")
          choice = input(supplies)
# If the user wants to go to the supplies room
          if choice.lower() == "supplies room":
                    hours_left -= 4
                    items.append("sharp object")
                    print(f"\nYou found a sharp object, \
this will help you escape ")
                    print("you have " + str(hours_left) + " hours left")
                    input(courtyard_sneak)
# the user encounters a guard
          if courtyard_sneak.lower() == "yes":
            choice1 = input(security_guard)
# The user attacks the guard (GAME OVER)
            if choice1.lower() == "attack":
              hours_left -= 2
              if "sharp object" in items:
                print("You killed the guard with your \
sharp obeject! You were caught on the security cams \
You failed to escape. GAME OVER")
                exit()
                break
              if  "soap" in items:
                    print(f"\nYou could not do anything with just your soap, \
you were caught. GAME OVER ")
# The user runs away from the guard
            choice1 = input(security_guard)
            if choice1.lower() == "run away":
              if "sharp object" in items:
                print("You succesfuly ran away to your cell")
                input(wake_up)
  # wake up the next morning
  # User waits until delivery truck arrives
            if wake_up.lower() == "act":
                      print("\nYou decided to act non suspicious until the truck comes")
                      print("Your almost out, dont let the nerves get to you!")
                      input(escape_1)
  # the user is able to escape using blueprint
                      if escape_1.lower() == "yes":
                          if "blueprints" in knowledge:
                            print("\nYou used your blueprints to navigate your way to the delivery truck \
                            You snuck into the truck and escaped prison! \
                  GOOD JOB YOU WON THE GAME!")
                            break
  # User does not have blueprints, cannot escape
                          if  "blueprints" not in knowledge:
                            print(f"\nYou did not have the blueprints so \
                            you could not navigate your way to the truck. \
                            It left without you, your stuck in prison.\
                            GAME OVER")
                            exit()
                            break
  # User does not want to escape
                      if escape_1.lower() == "no":
                        print("you did not go to the truck in time \
                It left you behind and now your stuck in prison \
                GAME OVER")
                        exit()
                        break


            break
            if  "soap" in items:
                    print(f"\nYou succesfuly ran away to your cell")
                    input(wake_up)
        # wake up 
            if wake_up.lower() == "act":
        # User waits until delivery truck arrives
                      print("\nYou decided to act non suspicious until the truck comes")
                      print("Your almost out, dont let the nerves get to you!")
                      input(escape_1)
                      if escape_1.lower() == "yes":
        # the user is able to escape using blueprint
                          if "blueprints" in knowledge:
                            print("\nYou used your blueprints to navigate your way to the delivery truck \
                            You snuck into the truck and escaped prison! \
                  GOOD JOB YOU WON THE GAME!")
                            break
        # user does not have blueprint, cannot escape
                          if  "blueprints" not in knowledge:
                            print(f"\nYou did not have the blueprints so \
                            you could not navigate your way to the truck. \
                            It left without you, your stuck in prison.\
                            GAME OVER")
                            exit()
                            break
        # user does not want to escape
                      if escape_1.lower() == "no":
                        print("you did not go to the truck in time \
                It left you behind and now your stuck in prison \
                GAME OVER")
                        exit()
                        break
# If they dont want to sneak to courtyard
          if courtyard_sneak.lower() == "no":
            input(library_sneak)
# If they want to sneak to Library
          if library_sneak.lower() == "yes":
            knowledge.append("blueprints")
# Would you like to go to courtyard  
            input(courtyard_sneak)
          if courtyard_sneak.lower() == "yes":
# You are stopped by a guard
            choice1 = input(security_guard)
            if choice1.lower() == "run away":
              if "sharp object" in items:
                print("You succesfuly ran away to your cell")
                input(wake_up)
  # wake up
            if wake_up.lower() == "act":
                      print("\nYou decided to act non suspicious until the truck comes")
                      print("Your almost out, dont let the nerves get to you!")
                      input(escape_1)
  # user wants to escape
                      if escape_1.lower() == "yes":
  # user is able to escape using blueprint
                          if "blueprints" in knowledge:
                            print("\nYou used your blueprints to navigate your way to the delivery truck \
                            You snuck into the truck and escaped prison! \
                  GOOD JOB YOU WON THE GAME!")
                            break
  # user is not able to escape, does not have blueprint
                          if  "blueprints" not in knowledge:
                            print(f"\nYou did not have the blueprints so \
                            you could not navigate your way to the truck. \
                            It left without you, your stuck in prison.\
                            GAME OVER")
                            exit()
                            break
 # user does not want to escape
                      if escape_1.lower() == "no":
                        print("you did not go to the truck in time \
                It left you behind and now your stuck in prison \
                GAME OVER")
                        exit()
                        break


            break
            if  "soap" in items:
                    print(f"\nYou succesfuly ran away to your cell")
                    input(wake_up)
        # wake up 
        # user wants to wait till truck comes
            if wake_up.lower() == "act":
                      print("\nYou decided to act non suspicious until the truck comes")
                      print("Your almost out, dont let the nerves get to you!")
                      input(escape_1)
        # user is able to escape using blueprint
                      if escape_1.lower() == "yes":
                          if "blueprints" in knowledge:
                            print("\nYou used your blueprints to navigate your way to the delivery truck \
                            You snuck into the truck and escaped prison! \
                  GOOD JOB YOU WON THE GAME!")
                            break
        # user does not have blueprint, cannt escape
                          if  "blueprints" not in knowledge:
                            print(f"\nYou did not have the blueprints so \
                            you could not navigate your way to the truck. \
                            It left without you, your stuck in prison.\
                            GAME OVER")
                            exit()
                            break
        # user does not want to escape
                      if escape_1.lower() == "no":
                        print("you did not go to the truck in time \
                It left you behind and now your stuck in prison \
                GAME OVER")
                        exit()
                        break


            break
        # user wants to attack guard
            if choice1.lower() == "attack":
              hours_left -= 2
              if "sharp object" in items:
                print("You killed the guard with your \
                sharp obeject! You were caught on the security cams \
                You failed to escape. GAME OVER")
                exit()
                break
              if  "soap" in items:
                    print(f"\nYou could not do anything with just your soap, \
you were caught. GAME OVER ")
                    exit()
                    break
              break
# If they dont want to go to library
          if library_sneak.lower() == "no":
            hours_left -= 8
            print("Ok, well its time to sleep")
            print("You need to be in bed for countdown.")
            print("tomorrow night is your escape. Rest well!")
            input(wake_up)
      # wake up
        if wake_up.lower() == "act":
          print("\nYou decided to act non suspicious until the truck comes")
          print("Your almost out, dont let the nerves get to you!")
          input (escape_1)
      # user has blueprints, is able to escape
          if escape_1.lower() == "yes":
              if "blueprints" in knowledge:
                print("\nYou used your blueprints to navigate your way to the delivery truck \
                You snuck into the truck and escaped prison! \
                GOOD JOB YOU WON THE GAME!")
                break
      # user does not have blueprints, cannot escape
              if  "blueprints" not in knowledge:
                    print(f"\nYou did not have the blueprints so \
                    you could not navigate your way to the truck. \
                    It left without you, your stuck in prison.\
                    GAME OVER")
              exit()
              break
     # user does not want to escape
          if escape_1.lower() == "no":
            print("you did not go to the truck in time \
            It left you behind and now your stuck in prison \
            GAME OVER")
            exit()
            break

         
# If they want to go to showers
          if choice.lower() == "showers":
                    hours_left -= 4
                    items.append("soap")
                    print(f"\nYou found a soap bar \
this will not help your escape ")
                    print("you have " + str(hours_left) + " hours left")
                    input(courtyard_sneak)
# You are stopped by a guard       
        y = input(courtyard_sneak)
        if y.lower() == "yes":
          choice1 = input(security_guard)
# user runs away from guard
          if choice1.lower() == "run away":
              if "sharp object" in items:
                print("\nYou succesfuly ran away to your cell")
                input(wake_up)
            # wake up prompt
                if wake_up.lower() == "act":
                      print("\nYou decided to act non suspicious until the truck comes")
                      print("Your almost out, dont let the nerves get to you!")
                      input(escape_1)
            # user has blueprints, can escape
                      if escape_1.lower() == "yes":
                          if "blueprints" in knowledge:
                            print("\nYou used your blueprints to navigate your way to the delivery truck \
                            You snuck into the truck and escaped prison! \
                  GOOD JOB YOU WON THE GAME!")
                            break
            # user does not have blueprints, cannot escape
                          if  "blueprints" not in knowledge:
                            print(f"\nYou did not have the blueprints so \
                            you could not navigate your way to the truck. \
                            It left without you, your stuck in prison.\
                            GAME OVER")
                            exit()
                            break
            # user does not want to escape
                      if escape_1.lower() == "no":
                        print("you did not go to the truck in time \
                It left you behind and now your stuck in prison \
                GAME OVER")
                        exit()
                        break
              # if you only have soap
              if  "soap" in items:
                    print(f"\nYou succesfuly ran away to your cell")
                    input(wake_up)
            # wake up the next morning
                    if wake_up.lower() == "act":
                      print("\nYou decided to act non suspicious until the truck comes")
                      print("Your almost out, dont let the nerves get to you!")
                      input(escape_1)
            # user has blueprints, can escape
                      if escape_1.lower() == "yes":
                          if "blueprints" in knowledge:
                            print("\nYou used your blueprints to navigate your way to the delivery truck \
                            You snuck into the truck and escaped prison! \
                  GOOD JOB YOU WON THE GAME!")
                            break
            # user doesn't have blueprints, cant escape
                          if  "blueprints" not in knowledge:
                            print(f"\nYou did not have the blueprints so \
                            you could not navigate your way to the truck. \
                            It left without you, your stuck in prison.\
                            GAME OVER")
                            exit()
                            break
            # user doesnt want to escape
                      if escape_1.lower() == "no":
                        print("you did not go to the truck in time \
                It left you behind and now your stuck in prison \
                GAME OVER")
                        exit()
                        break
            # user wants to attack guard (GAME OVER)
          if choice1.lower() == "attack":
            hours_left -= 2
            if "sharp object" in items:
                print("You killed the guard with your \
                sharp obeject! You were caught on the security cams \
                You failed to escape. GAME OVER")
                exit()
                break
            if  "soap" in items:
                    print(f"\nYou could not do anything with just your soap, \
you were caught. GAME OVER ")
          exit()
          break
        # If they dont want to sneak to courtyard
        if y.lower() == "no":
          z = input(library_sneak)
       # If they want to sneak to library
          if z.lower() == "yes":
            hours_left -= 4
            knowledge.append("blueprints")
            print("\n You got the blueprints you need to escape!")
            input(wake_up)
# Wake up
          if wake_up.lower() == "act":
            print("\nYou decided to act non suspicious until the truck comes")
            print("Your almost out, dont let the nerves get to you!")
            q = input(escape_1)
            if q.lower() == "yes":
              if "blueprints" in knowledge:
# user has blueprints, can escape
                print("\nYou used your blueprints to navigate your way to the delivery truck \
                You snuck into the truck and escaped prison! \
                GOOD JOB YOU WON THE GAME!")
                input(wake_up)
                break
# user doesnt have blueprints, cannot escape
              if  "blueprints" not in knowledge:
                    print(f"\nYou did not have the blueprints so \
                    you could not navigate your way to the truck. \
                    It left without you, your stuck in prison.\
                    GAME OVER")
              exit()
              break
# user dosnt want to escape
            if q.lower() == "no":
              print("you did not go to the truck in time \
              It left you behind and now your stuck in prison \
              GAME OVER")
              exit()
              break
        
        
# If they dont want to sneak to library
          if z.lower() == "no":
            print("\n Ok well, you need to go back to your cell for headcount")
            print("tomorrow is your escape. good luck!")
            input(wake_up)
# Wake up
        if wake_up.lower() == "act":
              print("\nYou decided to act non suspicious until the truck comes")
              print("Your almost out, dont let the nerves get to you!")
              input(escape_1)
# user has blueprints, can escape
              if escape_1.lower() == "yes":
                if "blueprints" in knowledge:
                  print("\nYou used your blueprints to navigate your way to the delivery truck \
                You snuck into the truck and escaped prison! \
                GOOD JOB YOU WON THE GAME!")
                  exit()
                  break
# user doesnt have blueprints cannot escape
              if  "blueprints" not in knowledge:
                    print(f"\nYou did not have the blueprints so \
                    you could not navigate your way to the truck. \
                    It left without you, your stuck in prison.\
                    GAME OVER")
              exit()
        break
# user doesnt want to escape
        if escape_1.lower() == "no":
            print("you did not go to the truck in time \
            It left you behind and now your stuck in prison \
            GAME OVER")
            exit()
            break

# You are stopped by a guard
            input(courtyard_sneak)
# You are stopped by a guard       
        if courtyard_sneak.lower() == "yes":
          choice1 = input(security_guard)
          if choice1.lower() == "run away":
              if "sharp object" in items:
                print("\nYou succesfuly ran away to your cell")
                input(wake_up)
            # wake up
                if wake_up.lower() == "act":
                      print("\nYou decided to act non suspicious until the truck comes")
                      print("Your almost out, dont let the nerves get to you!")
                      input(escape_1)
                      if escape_1.lower() == "yes":
            # user has blueprints, can escape
                          if "blueprints" in knowledge:
                            print("\nYou used your blueprints to navigate your way to the delivery truck \
                            You snuck into the truck and escaped prison! \
                  GOOD JOB YOU WON THE GAME!")
                            break
            # user does not have blueprints, cannot escape
                          if  "blueprints" not in knowledge:
                            print(f"\nYou did not have the blueprints so \
                            you could not navigate your way to the truck. \
                            It left without you, your stuck in prison.\
                            GAME OVER")
                            exit()
                            break
            # user does not want to escape
                      if escape_1.lower() == "no":
                        print("you did not go to the truck in time \
                It left you behind and now your stuck in prison \
                GAME OVER")
                        exit()
                        break
              # if you only have soap
              if  "soap" in items:
                    print(f"\nYou succesfuly ran away to your cell")
                    input(wake_up)
            # wake up
                    if wake_up.lower() == "act":
                      print("\nYou decided to act non suspicious until the truck comes")
                      print("Your almost out, dont let the nerves get to you!")
                      input(escape_1)
                      if escape_1.lower() == "yes":
            # user has blueprint, can escape
                          if "blueprints" in knowledge:
                            print("\nYou used your blueprints to navigate your way to the delivery truck \
                            You snuck into the truck and escaped prison! \
                  GOOD JOB YOU WON THE GAME!")
                            break
            # user doesnt have blueprint, cant escape
                          if  "blueprints" not in knowledge:
                            print(f"\nYou did not have the blueprints so \
                            you could not navigate your way to the truck. \
                            It left without you, your stuck in prison.\
                            GAME OVER")
                            exit()
                            break
            # if user does not want to escape
                      if escape_1.lower() == "no":
                        print("you did not go to the truck in time \
                It left you behind and now your stuck in prison \
                GAME OVER")
                        exit()
                        break
            # if user wants to attack guard
          if choice1.lower() == "attack":
            hours_left -= 2
            if "sharp object" in items:
                print("You killed the guard with your \
sharp obeject! You were caught on the security cams \
You failed to escape. GAME OVER")
                exit()
                break
            if  "soap" in items:
                    print(f"\nYou could not do anything with just your soap, \
you were caught. GAME OVER ")
          exit()
          break
  
# escape (wake up)
          input(wake_up)
# Wake up
        if wake_up.lower() == "act":
          print("\nYou decided to act non suspicious until the truck comes")
          print("Your almost out, dont let the nerves get to you!")
          q = input(escape_1)
          if q.lower() == "yes":
# user has blueprints, can escape
              if "blueprints" in knowledge:
                print("\nYou used your blueprints to navigate your way to the delivery truck \
                You snuck into the truck and escaped prison! \
                GOOD JOB YOU WON THE GAME!")
                input(wake_up)
                break
# user doesnt have blueprints, cannot escape
              if  "blueprints" not in knowledge:
                    print(f"\nYou did not have the blueprints so \
                    you could not navigate your way to the truck. \
                    It left without you, your stuck in prison.\
                    GAME OVER")
              exit()
              break
# if user doesnt want to escape
          if q.lower() == "no":
            print("you did not go to the truck in time \
            It left you behind and now your stuck in prison \
            GAME OVER")
            exit()
            break
        break

# Quit, Incase The User Wants To Stop The Program
        if x.lower() == "quit":
          hours_left = 0
          exit()

# Incase The User Inputs An Unknown Input
        else:
          print("\nYou did not pick one of the available options")
          print("try again")
          continue

escape(hours_left)