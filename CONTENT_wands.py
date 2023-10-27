from imports import *

class FeldsparWand(Wand):
  def __init__(self):
    self.name = "Feldspar Wand"
    self.nameColor = "BR"

    self.startDesc = "|DG|None"
    self.passiveDesc = "|DG|None"
    
    self.lore = "Simple, yet the basis of all spell-casting. Officially Goran-Approved!"

  def cast(self, spell, caster, enemy):
    res = None
    if caster.isPlayer:
      res = timedHitbar(spell.castingSpeed, spell.castingZones)
    else:
      res = random.randint(0, sum(spell.castingZones))

    printCastMessage("|B|You cast %s with your |BR|Feldspar Wand|B|!" % spell.getName(),\
                     "|B|{} casts %s with their |BR|Feldspar Wand|B|!" % spell.getName(), caster, enemy)

    res = getZone(res, spell.castingZones)
    spell.cast([res, caster.boost], caster, enemy)

  def exactCast(self, spell, caster, enemy, zone):
    printCastMessage("|B|You cast %s with your |BR|Feldspar Wand|B|!" % spell.getName(),\
                     "|B|{} casts %s with their |BR|Feldspar Wand|B|!" % spell.getName(), caster, enemy)

    spell.cast([zone, caster.boost], caster, enemy)


class SapphireWand(Wand):
  def __init__(self):
    self.name = "Sapphire Wand"
    self.nameColor = "DB"

    self.startDesc = "|DG|None"
    self.passiveDesc = "|DB|Slows all spell hitbars by 25%"
    
    self.lore = "It always feels cold to the touch..."

  def cast(self, spell, caster, enemy):
    res = None
    if caster.isPlayer:
      res = timedHitbar(spell.castingSpeed * 0.75, spell.castingZones)
    else:
      res = random.randint(0, sum(spell.castingZones))

    printCastMessage("|B|You cast %s with your |DB|Sapphire Wand|B|!" % spell.getName(),\
                     "|B|{} casts %s with their |DB|Sapphire Wand|B|!" % spell.getName(), caster, enemy)

    res = getZone(res, spell.castingZones)
    spell.cast([res, caster.boost], caster, enemy)

  def exactCast(self, spell, caster, enemy, zone):
    printCastMessage("|B|You cast %s with your |DB|Sapphire Wand|B|!" % spell.getName(),\
                     "|B|{} casts %s with their |DB|Sapphire Wand|B|!" % spell.getName(), caster, enemy)

    spell.cast([zone, caster.boost], caster, enemy)



class RubyWand(Wand):
  def __init__(self):
    self.name = "Ruby Wand"
    self.nameColor = "R"

    self.startDesc = "|DG|None"
    self.passiveDesc = "|R|Heals for 5 health every spell cast"
    
    self.lore = "Just holding it makes you feel more healthy than before"

  def cast(self, spell, caster, enemy):
    res = None
    if caster.isPlayer:
      res = timedHitbar(spell.castingSpeed, spell.castingZones)
    else:
      res = random.randint(0, sum(spell.castingZones))

    printCastMessage("|B|You cast %s with your |R|Ruby Wand|B|!" % spell.getName(),\
                     "|B|{} casts %s with their |R|Ruby Wand|B|!" % spell.getName(), caster, enemy)

    res = getZone(res, spell.castingZones)
    spell.cast([res, caster.boost], caster, enemy)

    caster.heal(5)
    printCastMessage("|B|The |R|Ruby Wand|B| gives you a healing aura for |R|5|B| health!",\
                    "|B|The |R|Ruby Wand|B| gives {} a healing aura for |R|5|B| health!",\
                     caster, enemy)

  def exactCast(self, spell, caster, enemy, zone):
    printCastMessage("|B|You cast %s with your |R|Ruby Wand|B|!" % spell.getName(),\
                     "|B|{} casts %s with their |R|Ruby Wand|B|!" % spell.getName(), caster, enemy)

    spell.cast([zone, caster.boost], caster, enemy)

    caster.heal(5)
    printCastMessage("|B|The |R|Ruby Wand|B| gives you a healing aura for |R|5|B| health!",\
                    "|B|The |R|Ruby Wand|B| gives {} a healing aura for |R|5|B| health!",\
                     caster, enemy)


class AmethystWand(Wand):
  def __init__(self):
    self.name = "Amethyst Wand"
    self.nameColor = "PU"
    
    self.startDesc = "|DG|None"
    self.passiveDesc = "|Y|Boosts for 10% per spell cast (80% Cap)"
    
    self.lore = "Found growing in an underground geode"

  def cast(self, spell, caster, enemy):
    res = None
    if caster.isPlayer:
      res = timedHitbar(spell.castingSpeed, spell.castingZones)
    else:
      res = random.randint(0, sum(spell.castingZones))

    printCastMessage("|B|You cast %s with your |PU|Amethyst Wand|B|!" % spell.getName(),\
                     "|B|{} casts %s with their |PU|Amethyst Wand|B|!" % spell.getName(), caster, enemy)

    res = getZone(res, spell.castingZones)
    spell.cast([res, caster.boost], caster, enemy)

    caster.castBoost(0.1, 1.8)
    printCastMessage("|B|The |PU|Amethyst Wand|B| gives you an energizing aura, boosting you for |Y|10%|B|!",\
                    "|B|The |PU|Amethyst Wand|B| gives {} an energizing aura, boosting them for |Y|10%|B|!",\
                     caster, enemy)

  def exactCast(self, spell, caster, enemy, zone):
    printCastMessage("|B|You cast %s with your |PU|Amethyst Wand|B|!" % spell.getName(),\
                     "|B|{} casts %s with their |PU|Amethyst Wand|B|!" % spell.getName(), caster, enemy)

    spell.cast([zone, caster.boost], caster, enemy)
    caster.castBoost(0.1, 1.8)
    
    printCastMessage("|B|The |PU|Amethyst Wand|B| gives you an energizing aura, boosting you for |Y|10%|B|!",\
                    "|B|The |PU|Amethyst Wand|B| gives {} an energizing aura, boosting them for |Y|10%|B|!",\
                     caster, enemy)



class OpalWand(Wand):
  def __init__(self):
    self.name = "Opal Wand"
    self.nameColor = "LB"

    self.startDesc = "|DG|None"
    self.passiveDesc = "|LB|Upon cast, negative boosts/shields will reset to 0%."

    self.lore = "It's so pure, it feels wrong to handle it without gloves..."
  
  def cast(self, spell, caster, enemy):
    res = None
    if caster.isPlayer:
      res = timedHitbar(spell.castingSpeed, spell.castingZones)
    else:
      res = random.randint(0, sum(spell.castingZones))

    if caster.boost < 1:
      caster.boost = 1
    if caster.shield > 1:
      caster.shield = 1
    
    printCastMessage("|B|The |LB|Opal Wand|B| washes away your negative boosts & shields!",\
                     "|B|The |LB|Opal Wand|B| washes away {}'s negative boosts & shields!", caster, enemy)
    
    printCastMessage("|B|You cast %s with your |LB|Opal Wand|B|!" % spell.getName(),\
                     "|B|{} casts %s with their |LB|Opal Wand|B|!" % spell.getName(), caster, enemy)

    res = getZone(res, spell.castingZones)
    spell.cast([res, caster.boost], caster, enemy)

  def exactCast(self, spell, caster, enemy, zone):
    if caster.boost < 1:
      caster.boost = 1
    if caster.shield > 1:
      caster.shield = 1
    
    printCastMessage("|B|The |LB|Opal Wand|B| washes away your negative boosts & shields!",\
                     "|B|The |LB|Opal Wand|B| washes away {}'s negative boosts & shields!", caster, enemy)
    
    printCastMessage("|B|You cast %s with your |LB|Opal Wand|B|!" % spell.getName(),\
                     "|B|{} casts %s with their |LB|Opal Wand|B|!" % spell.getName(), caster, enemy)

    spell.cast([zone, caster.boost], caster, enemy)


class EmeraldWand(Wand):
  def __init__(self):
    self.name = "Emerald Wand"
    self.nameColor = "LG"
    
    self.startDesc = "|DG|None"
    self.passiveDesc = "|LG|Defends for 5% per spell cast (50% Cap)"
    
    self.lore = "Straight out of the Emerald City"

  def cast(self, spell, caster, enemy):
    res = None
    if caster.isPlayer:
      res = timedHitbar(spell.castingSpeed, spell.castingZones)
    else:
      res = random.randint(0, sum(spell.castingZones))

    printCastMessage("|B|You cast %s with your |LG|Emerald Wand|B|!" % spell.getName(),\
                     "|B|{} casts %s with their |LG|Emerald Wand|B|!" % spell.getName(), caster, enemy)

    res = getZone(res, spell.castingZones)
    spell.cast([res, caster.boost], caster, enemy)

    caster.castShield(0.05, 1.5)
    printCastMessage("|B|The |LG|Emerald Wand|B| gives you a defensive aura, defending for |G|5%|B|!",\
                    "|B|The |LG|Emerald Wand|B| gives {} a defensive aura, defending for |G|5%|B|!",\
                     caster, enemy)

  def exactCast(self, spell, caster, enemy, zone):
    printCastMessage("|B|You cast %s with your |LG|Emerald Wand|B|!" % spell.getName(),\
                     "|B|{} casts %s with their |LG|Emerald Wand|B|!" % spell.getName(), caster, enemy)

    spell.cast([zone, caster.boost], caster, enemy)
    caster.castShield(0.05, 1.5)
    
    printCastMessage("|B|The |LG|Emerald Wand|B| gives you a defensive aura, defending for |G|5%|B|!",\
                    "|B|The |LG|Emerald Wand|B| gives {} a defensive aura, defending for |G|5%|B|!",\
                     caster, enemy)


class BloodstoneWand(Wand):
  def __init__(self):
    self.name = 'Bloodstone Wand'
    self.nameColor = 'R'
    self.desc = "Heals 50% of all damage dealt"
    self.lore = ""

    
class DiamondWand(Wand):
  def __init__(self):
    self.name = 'Diamond Wand'
    self.nameColor = 'W'
    self.desc = 'Triples all damage'
    self.lore = 'Crafted with pure 24 karat diamonds'

    
class GoldWand(Wand):
  def __init__(self):
    self.name = 'Gold Wand'
    self.nameColor = 'Y'
    self.desc = 'Shiny! 10% chance for a double turn.'
    self.lore = 'Like the Prismite Wand but... somehow more tangible'

    