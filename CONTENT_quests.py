from imports import *

class IronicCriminalPursuitQuest(Quest): # Don't change this
  def __init__(self, stage, pinned):
    self.name = "Ironic Criminal Pursuit" # <-- the name (You can change this)

    self.priority = 3
    # 3 = Red (Main Questline)
    # 2 = Yellow (High Priority)
    # 1 = Blue (Medium Priority)
    # 0 = Gray (Low Priority) 


    self.subtasks = [
      "Familiarize yourself with spell battles",       # 0
      "Talk to Katherine in Room 236A",                # 1
      "Become friends with Katherine",                 # 2
      "Meet Katherine at Room 128",                    # 3
      "Lockpick Ms. Presley's Door",                   # 4
      "Meet the Froggy Girls in Ms. Ramasamy's",       # 5
      "Find the RCMS Master Keys",                     # 6
      "Unlock Ms. Ramasamy's Door",                    # 7
      "Deal with the \"surprise\""                     # 8
    ]

    # v Don't change this v
    self.stage = stage
    self.pinned = pinned 

class OverdueSSLFormsQuest(Quest): # Don't change this
  def __init__(self, stage, pinned):
    self.name = "Overdue SSL Forms" # <-- the name (You can change this)

    self.priority = 1
    # 3 = Red (Main Questline)
    # 2 = Yellow (High Priority)
    # 1 = Blue (Medium Priority)
    # 0 = Gray (Low Priority) 


    self.subtasks = [
      "Turn in Brooke's forms to Ms. Palank", # 0
      "Give Brooke the shredded SSL forms",   # 1
    ]

    # v Don't change this v
    self.stage = stage
    self.pinned = pinned



class SucculentQuest(Quest):
  def __init__(self, stage, pinned):
    self.name = "Succulent Stash" # <-- the name (You can change this)

    self.priority = 3
    # 3 = Red (Main Questline)
    # 2 = Yellow (High Priority)
    # 1 = Blue (Medium Priority)
    # 0 = Gray (Low Priority) 


    self.subtasks = [
      "Talk to Ellie in the Greenhouse",
      "Complete Ellie's Succulent Shelf"
    ]

    # v Don't change this v
    self.stage = stage
    self.pinned = pinned

class GrammarCheckerQuest(Quest): # Don't change this
  def __init__(self, stage, pinned):
    self.name = "Grammar Checker" # <-- the name (You can change this)

    self.priority = 2
    # 3 = Red (Main Questline)
    # 2 = Yellow (High Priority)
    # 1 = Blue (Medium Priority)
    # 0 = Gray (Low Priority) 


    self.subtasks = [
      "Convince Pilliam to aid Ms. Palank", # 0
      "Talk to Ms. Palank",   # 1
    ]

    # v Don't change this v
    self.stage = stage
    self.pinned = pinned

class TableTennisQuest(Quest): # Don't change this
  def __init__(self, stage, pinned):
    self.name = "Table Tennis Champion" # <-- the name (You can change this)

    self.priority = 2
    # 3 = Red (Main Questline)
    # 2 = Yellow (High Priority)
    # 1 = Blue (Medium Priority)
    # 0 = Gray (Low Priority) 


    self.subtasks = [
      "Collect the Table Tennis Paddle", # 0
      "Return Ms. Gleich the Gym Keys",   # 1
      "Participate in the Table Tennis Tournament",   # 2
    ]

    # v Don't change this v
    self.stage = stage
    self.pinned = pinned

