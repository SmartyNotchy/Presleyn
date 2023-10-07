from imports import *

##################
## GENERIC WAND ##
##################

class Wand:
  objectType = "Wand"
  
  def __init__(self):
    self.name = "Generic Wand"
    self.nameColor = "W"

    self.startDesc = "How did you even get this?"
    self.passiveDesc = "How did you even get this?"
    
    self.lore = "How did you even get this?"

  def getName(self):
    return "|" + self.nameColor + "|" + self.name + "|--|"

  def printDesc(self, offset, clearLine = False):
    endStr = ""
    if clearLine:
      endStr = "\x1b[K"
    offsetStr = "\x1b[{}C".format(offset)
    printC(offsetStr + self.getName() + endStr)
    printC(offsetStr + "|G|On Battle Start: " + self.startDesc + endStr)
    printC(offsetStr + "|Y|Passive Ability: " + self.passiveDesc + endStr)
    printC(offsetStr + "*" + self.lore + "*" + endStr)

  def printShopDesc(self, offset):
    offsetStr = "\x1b[{}C".format(offset)
    printC(offsetStr + self.getName())
    printC(offsetStr + "|W|Wand")
    print()
    printC(offsetStr + "|G|On Battle Start: " + self.startDesc)
    printC(offsetStr + "|Y|Passive Ability: " + self.passiveDesc)
    printC(offsetStr + "*" + self.lore + "*")

  def onBattleStart(self, caster, enemy):
    pass
    
  def cast(self, spell, caster, enemy):
    pass


