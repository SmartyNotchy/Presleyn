from imports import *

def defaultLockedDoorInteraction(player):
  printC("\nUnfortunately, the door's locked.\n\nYou should come back later...", "B", end="")
  input()
  player.classroom = None
  
  if player.act == 1:
    if player.hasItem(MasterKeysItem):
      dial("Peter", "Katherine, don't you dare use the master keys to open this door.")
      dial("Katherine", "I wasn't going to. -_-")
    elif player.questProgressIsAtLeast(IronicCriminalPursuitQuest, 5):
      dial("Peter", "Katherine, don't you dare think about lockpicking the door.")
      dial("Katherine", "I wasn't going to. -_-")      
  else:
    pass
    
class Classroom:
  def __init__(self):
    self.name = ""
    self.locked = []
    
  def getName(self, act):
    if act in self.locked:
      return "|DG|" + self.name + " (Locked)"
    return self.name
    
    
  def run(self, player):
    defaultLockedDoorInteraction(player)

class ClassroomTemplate(Classroom):
  def __init__(self):
    self.name = "Generic Classroom"
    # If the classroom needs any specific attributes, add them here
    # DO NOT MODIFY the arguments of the __init__ method

  def run(self, player):
    pass
    
    # vvv DIALOG OPTIONS vvv

    # This can be literally anything, as long as it only depends/is affected by the player state.

    # Dialog options can change based on:
    # - Player has certain wand (or not)
    # - Player has certain spell (or not)
    # - Player has certain item (or not)
    # - Player has started certain quest (or not)
    # - Player has completed certain quest (or not)
    # - Player is at (least) certain stage in certain quest (or not)
    # to name a few.

    # Dialog options can also change the player state themselves, such as:
    # - Starting a spell battle
    # - Giving the player an item/spell/wand
    # - Giving the player a quest
    # - Manually advancing quest progress
    # - Manually completing a quest
    # to name a few.

    # For more information, look at the methods in MAP_player or ask me IRL/on the discord group chat.
    # - SmartyNotchy
    # ok - akash

