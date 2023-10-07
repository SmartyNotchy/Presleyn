from imports import *

class BattlePlayer:
  def __init__(self):
    self.name = "Unnamed Player" 
    self.nameColor = "B"
    self.isPlayer = True
    self.isTutorial = False
    
    self.health = 100
    self.maxHealth = 100
    self.boost = 1 # 1 = 1x mult, 1.5 = 1.5x mult, etc.
    self.shield = 1 # 1 = 100% damage taken, 0.5 = 50% damage taken, etc.

    self.selectedWand = None # currently selected wand (should be singular)
    self.arsenal = [] # currently selected spells (up to 4)
    self.items = [] # all BATTLE items in inventory

  def getName(self):
    return "|{}|{} (You)".format(self.nameColor, self.name)

  def update(self):
    self.health = clamp(self.health, 0, self.maxHealth)
    return self.health != 0

  def attack(self, target):
    choice = None
    if self.isTutorial:
      choice = dropdownMenu("What will you do?", ["Cast Spell"], highlight_choice=False)
    else:
      choice = dropdownMenu("What will you do?", ["Cast Spell", "Use Item"], highlight_choice=False)
    if choice == 1:
      if self.isTutorial:
        choice = dropdownMenu("Choose a spell to cast:", list(spell.getMenuName() for spell in self.arsenal))
      else:
        choice = dropdownMenu("Choose a spell to cast:", list(spell.getMenuName() for spell in self.arsenal) + ["|DG|Cancel"])
        
      if choice == 5:
        return False
      self.selectedWand.cast(self.arsenal[choice-1], self, target)
      return True
    elif choice == 2:
      if len(self.items) == 0:
        printC("You do not have any items to use!", "R")
        return False
      choice = dropdownMenu("Choose an item to use:", list(item.getMenuName() for item in self.items) + ["|DG|Cancel"])
      if choice == len(self.items) + 1:
        return False
      item_chosen = self.items[choice-1]
      item_chosen.use(self, target)
      if item_chosen.quantity == 0:
        self.items.remove(item_chosen)
      return True

  def heal(self, amount):
    self.health += int(amount)
    return int(amount)
    
  def takeDamage(self, amount):
    newAmount = int(amount * (2 - self.shield))
    self.health -= newAmount
    return newAmount

  def castShield(self, shieldAmount, cap):
    if (self.shield < cap and cap < 1) or (self.shield > cap and cap > 1):
      return
      
    self.shield += shieldAmount
    if shieldAmount < 0:
      self.shield = max(self.shield, cap)
    else:
      self.shield = min(self.shield, cap)

  def castBoost(self, boostAmount, cap):
    if (self.boost < cap and cap < 1) or (self.boost > cap and cap > 1):
      return
      
    self.boost += boostAmount
    if boostAmount < 0:
      self.boost = max(self.boost, cap)
    else:
      self.boost = min(self.boost, cap)

  def receiveEffect(self, effect, duration = None):
    if duration != None:
      effect.duration = duration
      
    for playerEffect in self.effects:
      if effect.icon == playerEffect.icon:
        playerEffect.duration = effect.duration
        return

    self.effects.append(effect)


























# haha gottem L