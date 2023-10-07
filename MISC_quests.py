from imports import *

############
## QUESTS ##
############


class Quest:
  
  def __init__(self, stage, pinned):
    self.name = "Goran's Quest"
    
    self.priority = 3
    # 3 = Red (Main Questline)
    # 2 = Yellow (High Priority)
    # 1 = Blue (Medium Priority)
    # 0 = Gray (Low Priority)

    # self.acts = [0,1,2,3,4,5,6]
    # 0 = Prologue/Tutorial/Whatever
    # 1-6 = Acts I-VI

    self.desc = "Help Goran Do Something"
    self.subtasks = [
      "Talk to Goran",
      "Get Item",
      "Talk again with Goran"
    ]

    self.stage = stage
    self.pinned = pinned

  def getName(self):
    return "|" + ("R", "Y", "LB", "DG")[3 - self.priority] + "| " + self.name + ("|R| 🝯" if self.pinned else "")

  def printDesc(self, offset):
    startStr = "\x1b[{}C".format(offset)
    printC(startStr + "|{}".format(("R", "Y", "LB", "DG")[3 - self.priority]) + "|" + self.name)
    print(startStr + "━" * 50)
    
    #prioEndStr = (", |G|Pinned" if self.pinned else "")
    if self.priority == 3:
      printC(startStr + "|R|Main Questline")
    elif self.priority == 2:
      printC(startStr + "|Y|High Priority Quest")
    elif self.priority == 1:
      printC(startStr + "|LB|Medium Priority Quest")
    else:
      printC(startStr + "|DG|Low Priority Quest")
    #printC(startStr + "|DG|*" + self.desc + "*")
    print()
    for i in range(len(self.subtasks)):
      if i == self.stage:
        printC(startStr + "|Y|! |W|" + self.subtasks[i])
        break
      else:
        printC(startStr + "|G|√ |B|" + self.subtasks[i])

  def toggleQuestPin(self):
    self.pinned = not self.pinned
    

  def isComplete(self):
    return self.stage >= len(self.subtasks)
