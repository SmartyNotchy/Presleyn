from imports import *

###################
## GENERIC SPELL ##
###################

class Spell:
  objectType = "Spell"
  
  def __init__(self):
    self.name = "Generic Spell"
    self.type = "Attack"
    self.nameColor = "W" 

    self.castingZones = [5,4,3,4,5] 
    self.castingSpeed = 1  

    self.desc = "How Did We Get Here?"
    self.lore = "Generic Lore"
    self.hint = "You can't get this haha"

  def getName(self):
    return "|" + self.nameColor + "|" + self.name + "|--|"

  def getMenuName(self):
    return COLOR_KEY[self.nameColor] + "{} ({})".format(self.name, self.type)

  def getDisabledMenuName(self):
    return COLOR_KEY["DG"] + "{} ({})".format(self.name, self.type)

  def printDesc(self, offset, clearLine = False):
    endStr = ""
    if clearLine:
      endStr = "\x1b[K"
    offsetStr = "\x1b[{}C".format(offset)
    printC(offsetStr + self.getMenuName() + endStr)
    printC(offsetStr + "Cast Zones: [|R|{}|Y|{}|G|{}|Y|{}|R|{}|B|]".format(
      *map(lambda x : "=" * x, (self.castingZones[0], self.castingZones[1], self.castingZones[2],
      self.castingZones[3], self.castingZones[4]))) + endStr, "B")
    printC(offsetStr + self.desc + endStr, "B")
    printC(offsetStr + "*" + self.lore + "*" + endStr, "DG")

  def printShopDesc(self, offset):
    offsetStr = "\x1b[{}C".format(offset)
    printC(offsetStr + self.getName())
    printC(offsetStr + "|W|" + self.type + " Spell")
    print()    
    printC(offsetStr + "Cast Zones: [|R|{}|Y|{}|G|{}|Y|{}|R|{}|B|]".format(
      *map(lambda x : "=" * x, (self.castingZones[0], self.castingZones[1], self.castingZones[2],
      self.castingZones[3], self.castingZones[4]))), "B")
    printC(offsetStr + self.desc, "B")
    printC(offsetStr + "*" + self.lore + "*", "DG")
    
  def cast(self, damageMultiplier, caster, target):
    pass
      

#######################
#### SPELL HELPERS ####
#######################


def notEffective():
  printC("It's not very effective...", "R")

def superEffective():
  printC("It's super effective!", "G")

def printCastMessage(casterIsPlayer, casterIsEnemy, caster, target):
  if caster.isPlayer:
    printC(casterIsPlayer.format(target.getName()), "B")
  else:
    printC(casterIsEnemy.format(caster.getName()), "B")


