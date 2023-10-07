from imports import *

###########
## ITEMS ##
###########

TYPES = {
  0: "Battle Item",
  1: "Overworld Item",
  2: "Collectible",
  3: "Community Scroll"
}

class Item:
  objectType = "Item"
  
  def __init__(self, quantity = 1):
    self.name = "Generic Item"
    self.nameColor = "W"
    self.rarity = 0
    self.type = 1
    self.desc = '''\
This is the Generic Item.
If you're reading this, either I messed up big time
or Omkar thought this would be a funny joke.

(It's not.)'''
    self.battleUsable = False
    
    self.quantity = quantity

  def getName(self):
    return "|" + self.nameColor + "|" + self.name
    
  def getInventoryName(self):
    if self.quantity == 1:
      return self.getName()
    return "|" + self.nameColor + "|" + self.name + " x{}".format(self.quantity)
  
  def printDesc(self, offset):
    startStr = "\x1b[{}C".format(offset)
    printC(startStr + "|{}".format(self.nameColor) + "|" + self.name)
    printC(startStr + RARITIES[self.rarity] + " " + TYPES[self.type])

    print()
    for line in self.desc.split("\n"):
      printC(startStr + line, "B")

  def printShopDesc(self, offset):
    self.printDesc(offset)


##################
## BATTLE ITEMS ##
##################
    
class BattleItem(Item):
  def __init__(self, quantity = 1):
    self.name = "Generic Battle Item"
    self.nameColor = "W"
    self.rarity = 0
    self.type = 0
    self.desc = '''\
This is the Generic Battle Item.
If you're reading this, either I messed up big time
or Omkar thought this would be a funny joke.

(It's not.)'''
    self.battleUsable = True
    
    self.quantity = quantity

  def getMenuName(self):
    return "|" + self.nameColor + "|" + self.name + " ({} left)".format(self.quantity)
    
  def use(self, player, target):
    # This takes a BattlePlayer Object, NOT a MapPlayer!
    pass
