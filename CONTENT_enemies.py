from imports import *

class GoranTutorialEnemy(BattleEnemy):
  def __init__(self):
    self.name = "Goran"
    self.nameColor = "R"
    self.isPlayer = False

    self.health = 100
    self.maxHealth = 100
    
    self.boost = 1
    self.shield = 1


class BattleStudent(BattleEnemy):
  def __init__(self, name, nameColor, maxHealth, wand, arsenal):
    self.name = name 
    self.nameColor = nameColor
    self.isPlayer = False

    self.health = maxHealth
    self.maxHealth = maxHealth

    self.selectedWand = wand
    self.arsenal = arsenal
    
    self.boost = 1
    self.shield = 1

  def onBattleStart(self):
    msgs = ["A wild {} approaches!", "{} prepares themselves for a spell battle!"]
    printC(random.choice(msgs).format("|{}|{}".format(self.nameColor, self.name)), "B")



###################################
## CUSTOM STUDENT BATTLE ENEMIES ##
###################################


class SofyaBattleStudent(BattleEnemy):
  def __init__(self):
    # Standard
    self.name = "Sofya"
    self.nameColor = "Y"
    self.isPlayer = False

    self.health = 100
    self.maxHealth = 100

    self.selectedWand = FeldsparWand()
    self.arsenal = [SofyaSpell(), ChrisSpell(), PrestonSpell(), OmkarSpell()]
    
    self.boost = 1
    self.shield = 1

    # Special
    self.healCooldown = 0

  def attack(self, target):
    if self.health <= 30:
      if self.healCooldown == 0:
        self.healCooldown = 2
        self.selectedWand.exactCast(self.arsenal[0], self, target, randomZone(0.3, 0.6, 0.1))
        return
      else:
        self.healCooldown -= 1

    self.selectedWand.exactCast(random.choice(self.arsenal[1:]), self, target, randomZone(0.6, 0.3, 0.1))



class LillianBattleStudent(BattleEnemy):
  def __init__(self):
    # Standard
    self.name = "Lillian"
    self.nameColor = "Y"
    self.isPlayer = False

    self.health = 100
    self.maxHealth = 100

    self.selectedWand = FeldsparWand()
    self.arsenal = [LillianSpell(), ArjunSpell(), ChrisSpell(), PrestonSpell()]
    
    self.boost = 1
    self.shield = 1

    # Special
    self.superCooldown = 0
    self.boostCooldown = 1
    
    

  def attack(self, target):
    if self.health <= 30:
      if self.superCooldown == 0:
        self.superCooldown = 4
        self.selectedWand.exactCast(self.arsenal[0], self, target, randomZone(0.3, 0.6, 0.1))
        return
      else:
        self.superCooldown -= 1

    self.boostCooldown -= 1
    if self.boost < 1.3 and self.boostCooldown <= 0:
      self.selectedWand.exactCast(self.arsenal[1], self, target, randomZone(0.1, 0.4, 0.5))
      self.boostCooldown = 5
    else:
      self.selectedWand.exactCast(random.choice(self.arsenal[2:]), self, target, randomZone(0.4, 0.4, 0.2))




class AkshajBattleStudent(BattleEnemy):
  def __init__(self):
    # Standard
    self.name = "Akshaj"
    self.nameColor = "LB"
    self.isPlayer = False

    self.health = 100
    self.maxHealth = 100

    self.selectedWand = FeldsparWand()
    self.arsenal = [AkshajSpell(), AkashSpell()]
    
    self.boost = 1
    self.shield = 1

    # Special
    self.attackOn = 0
    
  def attack(self, target):
    self.selectedWand.exactCast(self.arsenal[self.attackOn], self, target, randomZone(0.3, 0.5, 0.2))
    if self.attackOn == 0:
      self.attackOn = 2
    self.attackOn -= 1


class SayfBattleStudent(BattleEnemy):
  def __init__(self):
    # Standard
    self.name = "Sayf"
    self.nameColor = "LB"
    self.isPlayer = False

    self.health = 120
    self.maxHealth = 120

    self.selectedWand = FeldsparWand()
    self.arsenal = [SayfSpell(), OmkarSpell()]
    
    self.boost = 1
    self.shield = 1

    # Special
    self.attackOn = 1
    self.sayfCooldown = 3
    
  def attack(self, target):
    self.selectedWand.exactCast(self.arsenal[self.attackOn], self, target, randomZone(0.6, 0.0, 0.4))
    if self.attackOn == 1:
      self.sayfCooldown -= 1
      if self.sayfCooldown == 0:
        self.attackOn = 0
    else:
      self.sayfCooldown = 3
      self.attackOn = 1



class ChrisBattleStudent(BattleEnemy):
  def __init__(self):
    # Standard
    self.name = "Chris"
    self.nameColor = "Y"
    self.isPlayer = False

    self.health = 100
    self.maxHealth = 100

    self.selectedWand = FeldsparWand()
    self.arsenal = [ChrisSpell()]
    
    self.boost = 1
    self.shield = 1

    
  def attack(self, target):
    self.selectedWand.exactCast(self.arsenal[0], self, target, randomZone(0.1, 0.3, 0.6))



class AadhavanBattleStudent(BattleEnemy):
  def __init__(self):
    # Standard
    self.name = "Aadhavan"
    self.nameColor = "LG"
    self.isPlayer = False

    self.health = 100
    self.maxHealth = 100

    self.selectedWand = FeldsparWand()
    self.arsenal = [AadhavanSpell(), ChrisSpell()]
    
    self.boost = 1
    self.shield = 1

    # Special
    self.superCooldown = 2

    
  def attack(self, target):
    self.superCooldown -= 1
    if self.superCooldown == 0:
      self.selectedWand.exactCast(self.arsenal[0], self, target, randomZone(0.1, 0.1, 0.8))
      self.superCooldown = 4
    else:
      self.selectedWand.exactCast(self.arsenal[1], self, target, randomZone(0.3, 0.6, 0.1))


class AriamBattleStudent(BattleEnemy):
  def __init__(self):
    # Standard
    self.name = "Ariam"
    self.nameColor = "R"
    self.isPlayer = False

    self.health = 100
    self.maxHealth = 100

    self.selectedWand = FeldsparWand()
    self.arsenal = [AriamSpell(), PrestonSpell()]
    
    self.boost = 1
    self.shield = 1

    
  def attack(self, target):
    if self.boost < 1.35:
      self.selectedWand.exactCast(self.arsenal[0], self, target, randomZone(0.05, 0.05, 0.9))
    else:
      self.selectedWand.exactCast(self.arsenal[1], self, target, randomZone(0.3, 0.6, 0.1))


class TylerBattleStudent(BattleEnemy):
  def __init__(self):
    # Standard
    self.name = "Tyler"
    self.nameColor = "R"
    self.isPlayer = False

    self.health = 100
    self.maxHealth = 100

    self.selectedWand = FeldsparWand()
    self.arsenal = [TylerSpell(), PrestonSpell()]
    
    self.boost = 1
    self.shield = 1

    
  def attack(self, target):
    if self.shield < 1.35:
      self.selectedWand.exactCast(self.arsenal[0], self, target, randomZone(0.05, 0.05, 0.9))
    else:
      self.selectedWand.exactCast(self.arsenal[1], self, target, randomZone(0.3, 0.6, 0.1))


class GummyBattleFrog(BattleEnemy):
  def __init__(self):
    # Standard
    self.name = "Gummy"
    self.nameColor = "G"
    self.isPlayer = False

    self.health = 250
    self.maxHealth = 250

    self.selectedWand = FeldsparWand()
    
    self.boost = 1
    self.shield = 1

    # Special
    self.failureCooldown = 2
    
  def attack(self, target):
    self.failureCooldown -= 1
    if self.failureCooldown <= 0 and random.randint(0, 3) <= (-1 * self.failureCooldown):
      printC("|G|Gummy |B|takes a break from paging through her dictionary, and does nothing!\n")
      self.failureCooldown = 2
    else:
      printC("|G|Gummy |B|pages through the dictionary until she finds the word she's looking for...\n")
      if target.boost > 1.35:
        printC("|G|Gummy: |BR|Weaken: |B|to reduce in intensity or effectiveness.")
        printC("|G|Gummy: |B|Say goodbye to your |Y|boost|B|!\n")
        printC("|B|Your boost was decreased by |Y|15%|B|.")
        target.castBoost(-0.15, 0.99)
      elif target.shield > 1.35:
        printC("|G|Gummy: |DG|Vulnerable: |B|open to attack or damage.")
        printC("|G|Gummy: |B|What |G|shield|B| did you have again?\n")
        printC("|B|Your shield was decreased by |G|15%|B|.")
        target.castShield(-0.15, 0.99)
      elif random.randint(1, 3) == 1 and self.health <= 200:
        printC("|G|Gummy: |PI|Vitalize: |B|to endow with life, or vitality.")
        printC("|G|Gummy: |B|You'll never be able to defeat me!\n")
        printC("|G|Gummy|B| heals for |PI|10|B| health.")
        self.health += 10
      else:
        printC("|G|Gummy: |R|Damage: |B|loss or harm resulting from injury to person, property, or reputation.")
        printC("|G|Gummy: |B|Words are the most powerful weapon!\n")
        res = target.takeDamage(20)
        printC("|G|Gummy|B| deals |R|{}|B| damage to you, somehow.".format(res))





class AkashBattleStudent(BattleEnemy):
  def __init__(self):
    # Standard
    self.name = "Akash"
    self.nameColor = "R"
    self.isPlayer = False

    self.health = 250
    self.maxHealth = 250

    self.selectedWand = FeldsparWand()
    self.arsenal = [AkashSpell(), RyanSpell()]
    
    self.boost = 1
    self.shield = 1

    
  def attack(self, target):
    if self.shield < 1.2:
      self.selectedWand.exactCast(self.arsenal[0], self, target, randomZone(0.01, 0.01, 0.98))
    else:
      self.selectedWand.exactCast(self.arsenal[1], self, target, randomZone(0.2, 0.5, 0.3))




class JessikaBattleStudent(BattleEnemy):
  def __init__(self):
    # Standard
    self.name = "Jessika"
    self.nameColor = "PU"
    self.isPlayer = False

    self.health = 250
    self.maxHealth = 250

    self.selectedWand = RubyWand()
    self.arsenal = [JessikaSpell(), AadhavanSpell()]
    
    self.boost = 1
    self.shield = 1

    
  def attack(self, target):
    if self.shield < 1.42:
      self.selectedWand.exactCast(self.arsenal[0], self, target, randomZone(0, 0, 1))
    else:
      self.selectedWand.exactCast(self.arsenal[1], self, target, randomZone(0.4, 0.3, 0.3))






class BryceBattleStudent(BattleEnemy):
  def __init__(self):
    # Standard
    self.name = "Bryce"
    self.nameColor = "PU"
    self.isPlayer = False

    self.health = 250
    self.maxHealth = 250

    self.selectedWand = SapphireWand()
    self.arsenal = [BryceSpell(), RyanSpell()]
    
    self.boost = 1
    self.shield = 1

    # Special
    self.superCooldown = 0

    
  def attack(self, target):
    if self.superCooldown <= 0:
      self.selectedWand.exactCast(self.arsenal[0], self, target, randomZone(0, 0, 1))
      self.superCooldown = 4
    else:
      self.superCooldown -= 1
      self.selectedWand.exactCast(self.arsenal[1], self, target, randomZone(0.2, 0.5, 0.3))



class SriBattleStudent(BattleEnemy):
  def __init__(self):
    # Standard
    self.name = "Sri"
    self.nameColor = "Y"
    self.isPlayer = False

    self.health = 250
    self.maxHealth = 250

    self.selectedWand = SapphireWand()
    self.arsenal = [SriSpell(), AadhavanSpell()]
    
    self.boost = 1
    self.shield = 1

    # Special
    self.superCooldown = 0
    
  def attack(self, target):
    if self.superCooldown == 0:
      self.selectedWand.exactCast(self.arsenal[0], self, target, randomZone(0, 0, 1))
      self.superCooldown = 4
    else:
      self.superCooldown -= 1
      self.selectedWand.exactCast(self.arsenal[1], self, target, randomZone(0.05, 0.95, 0))



class WilliamBattleStudent(BattleEnemy):
  def __init__(self):
    # Standard
    self.name = "William"
    self.nameColor = "LB"
    self.isPlayer = False

    self.health = 250
    self.maxHealth = 250

    self.selectedWand = FeldsparWand()
    self.arsenal = [WilliamSpell(), DonSpell()]
    
    self.boost = 1
    self.shield = 1

    # Special
    self.superCooldown = 0
    
  def attack(self, target):
    if self.superCooldown == 0:
      self.selectedWand.exactCast(self.arsenal[0], self, target, randomZone(0, 0, 1))
      self.superCooldown = 3
    else:
      self.superCooldown -= 1
      self.selectedWand.exactCast(self.arsenal[1], self, target, randomZone(0.3, 0.6, 0.1))



class GloriaBattleStudent(BattleEnemy):
  def __init__(self):
    # Standard
    self.name = "Gloria"
    self.nameColor = "O"
    self.isPlayer = False

    self.health = 250
    self.maxHealth = 250

    self.selectedWand = RubyWand()
    self.arsenal = [WilliamSpell(), DonSpell()]
    
    self.boost = 1
    self.shield = 1

    # Special
    self.superCooldown = 0
    
  def attack(self, target):
    if self.superCooldown == 0:
      self.selectedWand.exactCast(self.arsenal[0], self, target, randomZone(0, 0, 1))
      self.superCooldown = 3
    else:
      self.superCooldown -= 1
      self.selectedWand.exactCast(self.arsenal[1], self, target, randomZone(0.3, 0.6, 0.1))



class BenedicteBattleStudent(BattleEnemy):
  def __init__(self):
    # Standard
    self.name = "Benedicte"
    self.nameColor = "PU"
    self.isPlayer = False

    self.health = 250
    self.maxHealth = 250

    self.selectedWand = RubyWand()
    self.arsenal = [BenedicteSpell(), OmkarSpell()]
    
    self.boost = 1
    self.shield = 1

    # Special
    self.superCooldown = 0
    
  def attack(self, target):
    if self.superCooldown == 0:
      self.selectedWand.exactCast(self.arsenal[0], self, target, randomZone(0, 0, 1))
      self.superCooldown = 1
    else:
      self.superCooldown -= 1
      self.selectedWand.exactCast(self.arsenal[1], self, target, randomZone(0.5, 0.5, 0))




class YuliaBattleStudent(BattleEnemy):
  def __init__(self):
    # Standard
    self.name = "Yulia"
    self.nameColor = "BR"
    self.isPlayer = False

    self.health = 250
    self.maxHealth = 250

    self.selectedWand = FeldsparWand()
    self.arsenal = [YuliaSpell(), BenedicteSpell(), RyanSpell()]
    
    self.boost = 1
    self.shield = 1

    # Special
    self.superCooldown = 0
    
  def attack(self, target):
    if self.superCooldown == 0:
      self.selectedWand.exactCast(random.choice(self.arsenal[:2]), self, target, randomZone(0, 0, 1))
      self.superCooldown = 1
    else:
      self.superCooldown -= 1
      self.selectedWand.exactCast(self.arsenal[2], self, target, randomZone(0.5, 0.5, 0))




class JustinBattleStudent(BattleEnemy):
  def __init__(self):
    # Standard
    self.name = "Justin"
    self.nameColor = "PU"
    self.isPlayer = False

    self.health = 250
    self.maxHealth = 250

    self.selectedWand = RubyWand()
    self.arsenal = [JustinSpell(), PrestonSpell()]
    
    self.boost = 1
    self.shield = 1

    # Special
    self.superCooldown = 0
    
  def attack(self, target):
    if self.superCooldown == 0:
      self.selectedWand.exactCast(self.arsenal[0], self, target, randomZone(0, 0, 1))
      self.superCooldown = 2
    else:
      self.superCooldown -= 1
      self.selectedWand.exactCast(self.arsenal[1], self, target, randomZone(0.5, 0.5, 0))



class BrookeBattleStudent(BattleEnemy):
  def __init__(self):
    # Standard
    self.name = "Brooke"
    self.nameColor = "LB"
    self.isPlayer = False

    self.health = 250
    self.maxHealth = 250

    self.selectedWand = SapphireWand()
    self.arsenal = [BrookeSpell(), ChrisSpell()]
    
    self.boost = 1
    self.shield = 1

    
  def attack(self, target):
    if self.boost < 1.5:
      self.selectedWand.exactCast(self.arsenal[0], self, target, randomZone(0, 0, 1))
    else:
      self.selectedWand.exactCast(self.arsenal[1], self, target, randomZone(0, 0, 1))




class EffieBattleFrog(BattleEnemy):
  def __init__(self):
    # Standard
    self.name = "Effie"
    self.nameColor = "G"
    self.isPlayer = False

    self.health = 500
    self.maxHealth = 500

    self.selectedWand = FeldsparWand()
    self.arsenal = [OmkarSpell()]
    
    self.boost = 1
    self.shield = 1.5

    # Special
    self.shieldBar = 0
    self.parryBar = 0
    
    self.lastHealth = 500

    self.daggerCooldown = 3
  
  def attack(self, target):
    if self.lastHealth > self.health:
      res = self.lastHealth - self.health
      self.parryBar += res
      
      if self.shield > 1:
        printC("|G|Effie|B|'s shield is weakend from the blow, decreasing by |G|2%|B|!", "B")
        self.shield -= 0.02
        if self.shield < 1:
          self.shield = 1
        self.shieldBar += res

      if random.randint(1, 150) < self.parryBar:
        if res > 20:
          printC("|G|Effie|B| parries your attack, reflecting the attack back to you and ignoring your shield!")
          printC("You take |R|{}|B| damage!".format(res), "B")
          self.health = self.lastHealth
          target.health -= res
          self.parryBar = 0
          self.lastHealth = self.health
          return
          
    if random.randint(1, 150) < self.shieldBar and self.shield < 1.75:
      self.shieldBar = 0
      self.shield += 0.1
      printC("|G|Effie|B| repairs their shield with froggy magic, increasing their shield by |G|10%|B|!") # katherine has all the plot armor
    else:
      if self.daggerCooldown < 0 and random.randint(1, 2) == 1:
        res = int(target.health / 4)
        printC("|G|Effie|B| throws a poison dagger at you, dealing |R|{}|B| damage!".format(res))
        target.health -= res
        self.daggerCooldown = 3
      else:
        res = random.randint(20, 40)
        printC("|G|Effie|B| strikes you with a medieval sword, dealing |R|{}|B| damage!".format(res))
        target.takeDamage(res)
        self.daggerCooldown -= 1

    self.lastHealth = self.health
