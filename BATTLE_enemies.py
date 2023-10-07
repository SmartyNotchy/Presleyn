from imports import *

#########################
## GENERIC ENEMY CLASS ##
#########################

class BattleEnemy:
  def __init__(self):
    self.name = "Generic Enemy"
    self.nameColor = "W"
    self.isPlayer = False

    self.health = 100
    self.maxHealth = 100
    self.selectedWand = None # Wand that the enemy will use (should be singular)
    self.arsenal = [] # Spells that the enemy will use (no limit)
    
    self.boost = 1
    self.shield = 1
  
  def getName(self):
    return "|" + self.nameColor + "|" + self.name + "|--|"
    
  def update(self):
    self.health = clamp(self.health, 0, self.maxHealth)
    return self.health != 0


  def onBattleStart(self):
    msgs = ["A wild {}|B| approaches!", "{}|B| prepares themselves for a spell battle!"]
    printC(random.choice(msgs).format("|{}|{}".format(self.nameColor, self.name)), "B")


  def attack(self, target):
    self.selectedWand.cast(random.choice(self.arsenal), self, target)

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
      
    for enemyEffect in self.effects:
      if effect.icon == enemyEffect.icon:
        enemyEffect.duration = effect.duration
        return

    self.effects.append(effect)