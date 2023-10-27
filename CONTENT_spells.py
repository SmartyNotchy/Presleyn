from imports import *


class TemplateSpell(Spell):  # class <Spellname>Spell(Spell):

  def __init__(self):
    self.name = "Aadhavan Spell"  # Basic spell name
    self.type = "Attack"  # Spell type
    self.nameColor = "G"  # Self-explanatory, check TERMCOL_KEY in the reference comment above
    self.castingZones = [6, 4, 2, 4, 6]  # R/Y/G/Y/R zones
    self.castingSpeed = 2 # 2 = 2x faster, 0.5 = 2x slower 
    self.desc = "This spell does something"  # Description of what the spell does (functionally)
    self.lore = "Generic Lore"  # Flavor text for the spell, which can be literally anything.

  def cast(self, damageMultiplier, caster, target):
    pass  # Don't worry about this, I'll implement it based on spell.desc


####################
## QUICKER CODING ##
####################

def quickDamageSpell(damageMultiplier, caster, target, messages, damage):
  if damageMultiplier[0] == REDZONE:
    printCastMessage(messages[0], messages[1], caster, target)
    notEffective()
    
  elif damageMultiplier[0] == YELLOWZONE:
    res = target.takeDamage(damage[1] * damageMultiplier[1])
    printCastMessage(messages[2] % res, messages[3] % res, caster, target)
    
  elif damageMultiplier[0] == GREENZONE:
    res = target.takeDamage(damage[0] * damageMultiplier[1])
    printCastMessage(messages[4] % res, messages[5] % res, caster, target)
    superEffective()

def quickBoostSpell(damageMultiplier, caster, target, messages, boosts, cap):
  if damageMultiplier[0] == REDZONE:
    printCastMessage(messages[0], messages[1], caster, target)
    notEffective()
    
  elif damageMultiplier[0] == YELLOWZONE:
    caster.castBoost(boosts[1], 1 + cap)
    printCastMessage(messages[2], messages[3], caster, target)
    
  elif damageMultiplier[0] == GREENZONE:
    caster.castBoost(boosts[0], 1 + cap)
    printCastMessage(messages[4], messages[5], caster, target)
    superEffective()

def quickShieldSpell(damageMultiplier, caster, target, messages, shields, cap):
  if damageMultiplier[0] == REDZONE:
    printCastMessage(messages[0], messages[1], caster, target)
    notEffective()
    
  elif damageMultiplier[0] == YELLOWZONE:
    caster.castShield(shields[1], 1 + cap)
    printCastMessage(messages[2], messages[3], caster, target)
    
  elif damageMultiplier[0] == GREENZONE:
    caster.castShield(shields[0], 1 + cap)
    printCastMessage(messages[4], messages[5], caster, target)
    superEffective()

def quickHealthSpell(damageMultiplier, caster, target, messages, Health):
  if damageMultiplier[0] == REDZONE:
    printCastMessage(messages[0], messages[1], caster, target)
    notEffective()
    
  elif damageMultiplier[0] == YELLOWZONE:
    res = caster.heal(Health[1] * damageMultiplier[1])
    printCastMessage(messages[2] % res, messages[3] % res, caster, target)
    
  elif damageMultiplier[0] == GREENZONE:
    res = caster.heal(Health[0] * damageMultiplier[1])
    printCastMessage(messages[4] % res, messages[5] % res, caster, target)
    superEffective()


def quickWeakenSpell(damageMultiplier, caster, target, messages, weakening):
  if damageMultiplier[0] == REDZONE:
    printCastMessage(messages[0], messages[1], caster, target)
    notEffective()
    
  elif damageMultiplier[0] == YELLOWZONE:
    target.castBoost(-1 * weakening[1], 1 - weakening[0])
    printCastMessage(messages[2], messages[3], caster, target)
    
  elif damageMultiplier[0] == GREENZONE:
    target.castBoost(-1 * weakening[0], 1 - weakening[0])
    printCastMessage(messages[4], messages[5], caster, target)
    superEffective()


def quickNullifySpell(damageMultiplier, caster, target, messages, nullification):
  if damageMultiplier[0] == REDZONE:
    printCastMessage(messages[0], messages[1], caster, target)
    notEffective()
    
  elif damageMultiplier[0] == YELLOWZONE:
    target.castShield(-1 * nullification[1], 1 - nullification[0])
    printCastMessage(messages[2], messages[3], caster, target)
    
  elif damageMultiplier[0] == GREENZONE:
    target.castShield(-1 * nullification[0], 1 - nullification[0])
    printCastMessage(messages[4], messages[5], caster, target)
    superEffective()

###########################
## SPELL IMPLEMENTATIONS ##
###########################
    
class AadhavanSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Nebula Noose"
    self.type = "Attack"
    self.nameColor = "R"
    self.castingZones = [4, 2, 4, 2, 4]
    self.castingSpeed = 1.25
    self.desc = "Deals |G|52|W|/|Y|26|W|/|R|0|--| damage."
    self.lore = "Loves Valorant and Astronomy, a killer combo"

  def cast(self, damageMultiplier, caster, target):
    quickDamageSpell(damageMultiplier, caster, target, \
                    [
                      "But you break your telescope trying to look at Neptune!",
                      "But {} breaks their telescope trying to look at Neptune!",
                      "You can envision Makemake, dealing |R|%d|--| damage!",
                      "{} can envision Makemake, dealing |R|%d|--| damage!",
                      "You can see the Helix Nebula with a perfect view, empowering you to deal |R|%d|--| damage!",
                      "{} can see the Helix Nebula with a perfect view, empowering them to deal |R|%d|--| damage!"
                    ], [52, 26, 0])


class AaryaSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Veto Violence"
    self.type = "Attack"
    self.nameColor = "R"
    self.castingZones = [1, 2, 3, 2, 8]  # R/Y/G/Y/R
    self.castingSpeed = 1.75
    self.desc = "Deals |G|75|W|/|Y|38|W|/|R|0|--| damage."
    self.lore = "The democratic power makes her go crazy"
    

  def cast(self, damageMultiplier, caster, target):
    quickDamageSpell(damageMultiplier, caster, target, \
                    [
                      "You veto {}'s law, but two-thirds of both the Senate and the House vote against you!",
                      "{} vetoes your law, but two-thirds of the Senate and the House vote against them!",
                      "You successfully veto {}'s law, dealing |R|%d|--| damage!",
                      "{} successfully vetoes your law, dealing |R|%d|--| damage!",
                      "You veto {}'s law, and everyone agrees with you, dealing |R|%d|--| damage!",
                      "{} vetoes your law, and everyone agrees with them, dealing |R|%d|--| damage!"
                    ], [75, 38, 0])
      
class AkashSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Grapefruit Grapple"
    self.type = "Defense"
    self.nameColor = "G"
    self.castingZones = [3, 3, 3, 3, 3]
    self.castingSpeed = 1.0
    self.desc = "Defends for |G|15%|W|/|Y|8%|W|/|R|0%|--|. Caps at |G|25%|--|."
    self.lore = "Loves grapefruits and sitting in a corner"
    

  def cast(self, damageMultiplier, caster, target):
    quickShieldSpell(damageMultiplier, caster, target, \
                    [
                      "You eat your grapefruits, but they were rotten...",
                      "{} eats their grapefruits, but they were rotten... ",
                      "You eat your grapefruits, defending yourself for |G|8%|--|!",
                      "{} eats their grapefruits, defending them for |G|8%|--|!",
                      "You eat all of your grapefruits and are completely nourished, defending you for |G|15%|--|!",
                      "{} eats all of their grapefruits and are completely nourished, defending them for |G|15%|--|!"
                    ], [0.15, 0.08, 0], 0.25)
      
class AkshajSpell(Spell):  
  def __init__(self):
    # Unfinished
    self.name = "One-Inch Punch"
    self.type = "|R|Attack|B|-|BR|Weaken|B|"
    self.nameColor = "B"
    self.castingZones = [5, 3, 2, 3, 5]  # R/Y/G/Y/R
    self.castingSpeed = 1
    self.desc = "TBD"
    self.lore = "That's as far as his arms go."
    

  def cast(self, damageMultiplier, caster, target):
    pass

class AnkushSpell(Spell): 
  def __init__(self):
    # Unfinished
    self.name = "Auditory Agony"
    self.type = "Weaken"
    self.nameColor = "BR"
    self.castingZones = [2, 5, 2, 5, 2]
    self.castingSpeed = 2.0
    self.desc = "Weakens the enemy's boost by |G|40%|W|/|Y|20%|W|/|R|0%|--|."
    self.lore = "His abysmal violin skills will make you die."
    

  def cast(self, damageMultiplier, caster, target):
    quickWeakenSpell(damageMultiplier, caster, target, \
                    [
                      "You play your violin, but everyone loves the sound of it...",
                      "{} plays their violin, but everyone hates the sound of it and tells them to stop...", 
                      "You play your violin and the audience gives a mixed reaction. You weaken {} by |BR|20%|--|!",
                      "{} plays their violin and the audience gives a mixed reaction. They weaken you by |BR|20%|--|!", 
                      "You play the violin, and it turns {}'s into mush! You weaken {} by |BR|40%|--|!",
                      "{} plays the violin, and it turns your brain into mush! They weaken you by |BR\40%|--|! "
                    ], [0.40, 0.20, 0])
      
      
class AnnaSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Cacao Combinatorics"
    self.type = "Health"
    self.nameColor = "PI"
    self.castingZones = [4, 2, 5, 2, 4]
    self.castingSpeed = 1.75
    self.desc = "Heal for |G|54|W|/|Y|27|W|/|R|0|--| health."
    self.lore = "An aboslute sweat at anything math, and loves to stalk"
    

  def cast(self, damageMultiplier, caster, target):
    quickHealthSpell(damageMultiplier, caster, target, \
                    [
                      "You eat some chocolate, but you can't find all of the pieces...",
                      "{} eats some chocolate, but they couldn't find all of the pieces...",
                      "You eat some chocolate and add the pieces up, healing you for |PI|27|--| health!",
                      "{} eats some chocolate and adds the pieces up, healing them for |PI|27|--| health!",
                      "You eat all of your chocolate and add the pieces up perfectly, healing you for |PI|54|--| health!",
                      "{} eats all of their chocolate and adds the pieces up perfectly, healing them for |PI54|--|health!"
                    ], [54, 27, 0])

class AriamSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Valor of Pursuit"
    self.type = "Boost"
    self.nameColor = "Y"
    self.castingZones = [8, 3, 3, 3, 5]
    self.castingSpeed = 1.0
    self.desc = "Boosts spells by |G|20%|W|/|Y|12%|W|/|R|0%|--|. Caps at |G|40%|--|."
    self.lore = 'Loves online multiplayer shooter games'
    

  def cast(self, damageMultiplier, caster, target):
    quickBoostSpell(damageMultiplier, caster, target, \
                    [
                      "You tried to boost yourself, but you're in {}'s line of sight!",
                      "{} tried to boost themselves, but they're in your line of sight!",
                      "You partially boost yourself by |Y|12%|--|! ",
                      "{} partially boosting themselves by |Y|12%|--|!", 
                      "You boost yourself to the max, energizing yourself & boosting by |Y|20%|--|!",
                      "{} boosts themselves to the max, energizing them & bossting by |Y|20%|--|!"
                    ], [0.20, 0.12, 0], 0.4)

class ArjunSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Spirit Of Ducks"
    self.type = "Boost"
    self.nameColor = "Y"
    self.castingZones = [3, 4, 4, 4, 3]
    self.castingSpeed = 1.0
    self.desc = "Boosts spells by |G|18%|W|/|Y|16%|W|/|R|0%|--|. Caps at |G|36%|--|."
    self.lore = "Duck Master, you will suffer if you harm them"
    
    
  def cast(self, damageMultiplier, caster, target):
    quickBoostSpell(damageMultiplier, caster, target, \
                    [#what are you doing i can do that later work on something else take a break then editing to be slightly shorter + consistency also removing the helper comments procrastinating on effie + don't know what to do for effie it fine
                      "You try to use your ducks to empower yourself, but you fail...",
                      "{} tries to use their ducks to empower themselves, but they fail...", 
                      "Your ducks quack repeatedly, boosting you by |Y|16%|--|!",
                      "{}'s ducks quack repeatedly, boosting them by |Y|16%|--|!",
                      "The ducks quack to their limit, boosting you by |Y|18%|--|!",
                      "The ducks quack to their limit, boosting them by |Y|18%|--|!"
                    ], [0.18, 0.16, 0], 0.36)

class BenedicteSpell(Spell):
  def __init__(self):
    # Unfinished take a break
    self.name = "Sugar Rush"
    self.type = "Health"
    self.nameColor = "PI"
    self.castingZones = [2, 4, 3, 4, 2]
    self.castingSpeed = 1.25
    self.desc = "Heal for |G|38|W|/|Y|12|W|/|R|0|--| health."
    self.lore = "Has candy everywhere, at all times"
    

  def cast(self, damageMultiplier, caster, target):
    quickHealthSpell(damageMultiplier, caster, target, \
                    [
                      "But, unfortunately, the sugar did not hype you up.",
                      "But, unfortunately, the sugar did not hype {} up.",
                      "The sugar only partially hyped you up, healing you for |PI|%d|--| health!",
                      "The sugar only partially hyped {} up, healing them for |PI|%d|--| health!",
                      "The sugar fully hyped you up, and you feel energized, healing you for |PI|%d|--| health!",
                      "They sugar fully hyped {} up, and they feel energized, healing you for |PI|%d|--| health!"
                    ], [38, 12, 0])
    
class BrandonTSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Broken Humor"
    self.type = "Nullify"
    self.nameColor = "DG"
    self.castingZones = [7, 0, 6, 0, 7]
    self.castingSpeed = 1.5
    self.desc = "Nullifies the enemy's shield by |G|20%|W|/|R|0%|--|."
    self.lore = "Lost at Brawl Stars"
    
    
  def cast(self, damageMultiplier, caster, target):
    quickNullifySpell(damageMultiplier, caster, target, \
                    [
                      "You make a joke, but no one laughs...",
                      "{} makes a joke, but no one laughs...", 
                      "no mid, if you see this ignore it",
                      "no mid, if you see this ignore it", 
                      "You make a joke and everyone laughs, nullifying {}'s shield by |DG|20%|--|!",
                      "{} makes a joke and everyone laughs, nullifying your shield by |DG|20%|--|!"
                    ], [0.20, 0, 0])

class BrandonVSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Rain of Beanies"
    self.type = "Boost"
    self.nameColor = "Y"
    self.castingZones = [3, 3, 3, 3, 3]
    self.castingSpeed = 1.5
    self.desc = "Boosts spells by |G|38%|W|/|Y|19%|W|/|R|0%|--|. Caps at |G|60%|--|."
    self.lore = "Don't get too close, he'll smack you"
    
    
  def cast(self, damageMultiplier, caster, target):
    quickBoostSpell(damageMultiplier, caster, target, \
                    [
                      "You try to smack {} with your hat, but you miss...", # You failed to boost yourself.
                      "{} tries to smack you with their hat, but they miss...", # {} fails to boost themselves.
                      "You smack {} with your hat, boosting yourself by |Y|19%|--|!", # You successfully boost yourself by 12%
                      "{} smacks you with their hat, boosting them by |Y|19%|--|!", # {}'s boost themselves by 12%
                      "You land a perfect whack on {} with your hat, boosting yourself by |Y|38%|--|!", # Your boost is strong, boosting by 20%
                      "{} lands a perfect whack on you with their hat, boosting them by |Y|38%|--|!" # {}'s boost is strong, boosting by 20%
                      # For these messages, put the percentages in the messages. DO NOT USE %d
                    ], [0.38, 0.19, 0], 0.6) # [Green Boost, Yellow Boost, 0]

class BrookeSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Artisan Magic"
    self.type = "Boost"
    self.nameColor = "Y"
    self.castingZones = [1, 1, 4, 1, 1]
    self.castingSpeed = 1.75
    self.desc = "Boosts spells by |G|43%|W|/|Y|22%|W|/|R|0%|--|. Caps at |G|70%|--|."
    self.lore = "Artiste at Work - Keep Out"
    

  def cast(self, damageMultiplier, caster, target):
    quickBoostSpell(damageMultiplier, caster, target, \
                    [
                      "You create a piece of art, but not that many people like it...",
                      "{} creates a piece of art, but not that many people like it...",
                      "You present a piece of art you made, and it gains some traction, boosting yourself by |Y|22%|--|!",
                      "{} presents a piece of art they made, and it gains some traction, boosting them by |Y|22%|--|!",
                      "You show off your art porfolio and become world-famous, boosting yourself by |Y|43%|--|!", 
                      "{} shows off their art porfolio and become world-famous, boosting them by |Y|43%|--|!"
                    ], [0.43, 0.22, 0], 0.7)


class BryceSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Know-it-All's Knack"
    self.type = "Weaken"
    self.nameColor = "BR"
    self.castingZones = [5, 4, 2, 4, 5]
    self.castingSpeed = 1.75
    self.desc = "Weakens the enemy's boost by |G|32%|W|/|Y|20%|W|/|R|0%|--|."
    self.lore = "Brown Nosing"
    

  def cast(self, damageMultiplier, caster, target):
    quickWeakenSpell(damageMultiplier, caster, target, \
                    [
                      "You ask the teacher if there's homework, but you get bullied to oblivion...",
                      "{} asks the teacher if there's homework, but they get bullied to oblivion...", 
                      "You get a 32/32 on your science CER, weakening {} by |BR|20%|--|!",
                      "{} gets a 32/32 on their science CER, weakening you by |BR|20%|--|!", 
                      "You beat the teacher in an argument about the class they teach!, weakening {} by |BR|32%|--|!",
                      "{} beats the teacher in an argument about the class they teach, weakening you by |BR|32%|--|!"
                    ], [0.32, 0.20, 0])

class CalebSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Paradoxical Pyramix"
    self.type = "|BR|Weaken|--|-|G|Defense|--|"
    self.nameColor = 'B'
    self.castingZones = [5,3,2,3,5]
    self.castingSpeed = 1.5
    self.desc = "Boosts your spells by 30%."
    self.lore = '"This is a monkey free zone" - Caleb'
    

  def cast(self, damageMultiplier, caster, target):
    pass

class ChaseSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Screech of Terror"
    self.type = "Weaken"
    self.nameColor = "BR"
    self.castingZones = [1, 3, 3, 3, 1]
    self.castingSpeed = 1.5
    self.desc = "Weakens the enemy's boost by |G|27%|W|/|Y|20%|W|/|R|0%|--|."
    self.lore = "Even the banshees are scared of him"
    
  def cast(self, damageMultiplier, caster, target):
    quickWeakenSpell(damageMultiplier, caster, target, \
                    [
                      "You screech your lungs out, but it is not powerful enough...",
                      "{} screeches their lungs out, but it is not powerful enough...", 
                      "You screech as loud as you can, and you get some nasty looks from others, weakening {} by |BR|20%|--|!",
                      "{} screeches as loud as they can, and they get some nastly looks from others, weakening you by |BR|20%|--|!", 
                      "You screech to your fullest, and it instantly ruptures the eardrums of everyone in a 10-mile radius, weakening {} by |BR|27%|--|!",
                      "{} screeches to their fullest, and it instantly ruptures the eardrums of everyone in a 10-mile radius, weakening you by |BR|27%|--|!"
                    ], [0.27, 0.20, 0])

class ChrisSpell(Spell):
  def __init__(self):
    self.name = "Glue Gun's Fury"
    self.type = "Attack"
    self.nameColor = "R"
    self.castingZones = [4, 4, 5, 4, 4]
    self.castingSpeed = 1
    self.desc = "Deals |G|24|W|/|Y|12|W|/|R|0|--| damage."
    self.lore = "Will ask you to play chess with him"
    
  def cast(self, damageMultiplier, caster, target):
    quickDamageSpell(damageMultiplier, caster, target, \
                    [ # btw how's strawberry jam music awesome really motivating k ?
                      # traditionally i put a "but" before redzone hits but its not required, what's your opinion on it
                      # so like "But you burn yourself..." idk if it's a good idea or not, your choice
                      # Yyour choice, just saying (sorry caps lock) actually you know what just speedrun the general idea of each cast method
                      # and i/akash will standardize it for consistency (grammar-wise) k
                      "But you burn yourself with a hot glue gun!",
                      "But {} burns themselves with a hot glue gun!",
                      "A little bit of hot glue sticks on to {}, dealing |R|%d|--| damage!", #might work better idk
                      "A little bit of hot glue sticks on to you, dealing |R|%d|--| damage!", # just letting you know you can do this
                      "You fire the glue gun perfectly at {}, dealing |R|%d|--| damage!",
                      "{} fires the glue gun perfectly at you, dealing |R|%d|--| damage!"
                    ], [24, 12, 0])

class DanielSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Chromebook Repulsion"
    self.type = "Weaken"
    self.nameColor = 'BR'
    self.castingZones = [10, 1, 3, 1, 10]
    self.castingSpeed = 1.5
    self.desc = "Weakens the enemy's boost by |G|30%|W|/|Y|15%|W|/|R|0%|--|."
    self.lore = "GUI? Never heard of it."
    
    pass

  def cast(self, damageMultiplier, caster, target):
    quickWeakenSpell(damageMultiplier, caster, target, \
                    [
                      "You throw some Chromebook keyboard keys at {}, but it barely does anything...",
                      "{} throws some Chromebook keyboard keys at you, but it barely does anything...", 
                      "You throw a Chromebook stylus at {}, and it makes some decent scratches, weakening {} by |BR|15%|--|!",
                      "{} throws a Chromebook stylus at you, and it makes some decent scratches, weakening you by |BR|15%|--|!", 
                      "You throw an entire Chromebook at {}, and it brings them to the floor, weakening {} by |BR|30%|--|!",
                      "{} throws an entire Chromebook at you, and it brings you to the floor, weakening you by |BR|30%|--|!"
                    ], [0.30, 0.15, 0])

class DashaSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Solo Rhapsody"
    self.type = "Boost"
    self.nameColor = 'Y'
    self.castingZones = [4, 1, 3, 1, 9]
    self.castingSpeed = 1.25
    self.desc = "Boosts spells by |G|33%|W|/|Y|17%|W|/|R|0%|--|. Caps at |G|50%|--|."
    self.lore = "Loves to talk about her musical passions, a lot"
    
  def cast(self, damageMultiplier, caster, target):
    quickBoostSpell(damageMultiplier, caster, target, \
                    [
                      "You jammed out, but it didn't help...",
                      "{} jammed out, but it didn't help...", 
                      "You jammed out, boosting yourself by |Y|17%|--|", 
                      "{} jammed out, boosting themselves by |Y|17%|--|!",
                      "You jammed out, improving your mental state & boosting yourself by |Y|33%|--|!", 
                      "{} jammed out, improving their mental state & boosting them by |Y|33%|--|!"
                    ], [0.33, 0.17, 0], 0.5) 

class DonSpell(Spell):
  def __init__(self):
    self.name = "Shadow Slice"
    self.type = "Attack"
    self.nameColor = "R"
    self.castingZones = [5, 2, 4, 2, 5]
    self.castingSpeed = 1.5
    self.desc = "Deals |G|64|W|/|Y|32|W|/|R|0|--| damage."
    self.lore = "..."
    

  def cast(self, damageMultiplier, caster, target):
    quickDamageSpell(damageMultiplier, caster, target, \
                    [
                      "You lurk in the shadows, but get exposed!",
                      "{} lurks in the shadows, but they get exposed!",
                      "You successfully lurk in the shadows, dealing |R|%d|--| damage!",
                      "{} successfully lurks in the shadows, dealing |R|%d|--| damage!",
                      "You master the art of stealth and get to {}, dealing |R|%d|--| damage!",
                      "{} masters the art of stealth and gets to you, dealing |R|%d|--| damage!"
                    ], [64, 32, 0])


class EdemSpell(Spell):
  def __init__(self):
    self.name = "Sweetness"
    self.type = "Health"
    self.nameColor = "PI"
    self.castingZones = [5, 4, 3, 4, 5]
    self.castingSpeed = 1.5
    self.desc = "Heal for |G|50|W|/|Y|15|W|/|R|0|--| health."
    self.lore = "The sweetest guy on the planet, until he's the worst"
    

  def cast(self, damageMultiplier, caster, target):
    quickHealthSpell(damageMultiplier, caster, target, \
                    [
                      "You try to be sweet, but it doesn't really work...",
                      "{} tries to be sweet, but it doesn't really work...",
                      "You are pretty sweet, healing you for |PI|%d|--| health!",
                      "{} is pretty sweet, healing them for |PI|%d|--| health!",
                      "You are so sweet that you become every teacher's favorite, healing you for |PI|%d|--| health!",
                      "{} is so sweet that they become every teacher's favorite, healing them for |PI|%d|--| health!" 
                    ], [50, 15, 0])

class EllaSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Derisive Dash"
    self.type = "Defense"
    self.nameColor = "G"
    self.castingZones = [2, 2, 2, 2, 2]
    self.castingSpeed = 2.0
    self.desc = "Defends for |G|30%|W|/|Y|21%|W|/|R|0%|--|. Caps at |G|55%|--|."
    self.lore = "Will take everything very seriously, a comedy show is not the place to be"
    

  def cast(self, damageMultiplier, caster, target):
    quickShieldSpell(damageMultiplier, caster, target, \
                    [
                      "But, you are not serious enough and therefore are taken as a joke...",
                      "But, {} is not serious enough and therefore is taken as a joke...",
                      "You are a bit serious, and it makes other people take you seriously as well! You defend yourself by |G|21%|--|!",
                      "{} is a bit serious, and it makes other people take them seriously as well! You defend yourself by |G|21%|--|!",
                      "You are so serious to others, that they leave you alone! You defend yourself by |G|30%|--|!",
                      "{} is so serious to others, that they leave them alone! They defend themselves by |G|30%|--|!"
                    ], [0.30, 0.21, 0], 0.55)
      
class EllieSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Botanical Bash"
    self.type = "Health"
    self.nameColor = "PI"
    self.castingZones = [4, 3, 2, 3, 4]
    self.castingSpeed = 2.0
    self.desc = "Heal for |G|65|W|/|Y|25|W|/|R|0|--| health."
    self.lore = "Will spend 43 hours staring at grass and flowers"
    
    
  def cast(self, damageMultiplier, caster, target):
    quickHealthSpell(damageMultiplier, caster, target, \
                    [
                      "But all of your flowers wilt...",
                      "But all of {}'s flowers wilt...",
                      "Your garden looks lovely, healing you for |PI%d|--| health!",
                      "{}'s garden looks lovely, healing them for |PI%d|--| health!",
                      "Your garden looks fantastic, and all your flowers are flourishing, healing you for |PI%d|--| health!",
                      "{}'s garden looks fantastic, and all their flowers are flourishing, healing them for |PI%d|--| health!"
                    ], [65, 25, 0])

class GabrielleSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Writer's Prose"
    self.type = "Boost"
    self.nameColor = "Y"
    self.castingZones = [4, 2, 5, 2, 4]
    self.castingSpeed = 1.75
    self.desc = "Boosts spells by |G|18%|W|/|Y|14%|W|/|R|0%|--|. Caps at |G|84%|--|."
    self.lore = "Fanfics will be the end of you..."
        
  def cast(self, damageMultiplier, caster, target):
    quickBoostSpell(damageMultiplier, caster, target, \
                    [
                      "But, you hit a writer's block...",
                      "But, {} hits a writer's block...",
                      "You ekes out a piece of literature, boosting yourself by |Y|14%|--|!",
                      "{} ekes out a piece of literature, boosting them by |Y|14%|--|!",
                      "You create an incredible, life-moving piece of literature, boosting yourself by |Y|18%|--|!",
                      "{} creates an incredible, life-moving piece of literature, boosting them by |Y|18%|--|! "
                    ], [0.18, 0.14, 0], 0.84)

class GloriaSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Protective Pages"
    self.type = "Defense"
    self.nameColor = "G"
    self.castingZones = [6, 3, 4, 3, 6]  # R/Y/G/Y/R
    self.castingSpeed = 1.75
    self.desc = "Gives you a shield for 3 turns that'll block 50% of the damage coming towards you."
    self.lore = "X"
    

  def cast(self, damageMultiplier, caster, target):
    pass

class GoranSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Rivalry Repellent"
    self.type = "Defense"
    self.nameColor = "G"
    self.castingZones = [5, 2, 4, 2, 5]
    self.castingSpeed = 1.0
    self.desc = "Defends for |G|10%|W|/|Y|6%|W|/|R|0%|--|. Caps at |G|30%|--|."
    self.lore = "Loves to watch people building stuff and talk with people"

  def cast(self, damageMultiplier, caster, target):
    quickShieldSpell(damageMultiplier, caster, target, \
                    [
                      "But, you cannot find anyone to argue with...",
                      "But, {} cannot find anyone to argue with...",
                      "You find someone to argue with, defending you for |G|6%|--|!",
                      "{} finds someone to argue with, defending them for |G|6%|--|!",
                      "You successfully win an argument against {}, defending you for |G|10%|--|!",
                      "{} successfully wins an argument against you, defending them for |G|10%|--|!"
                    ], [0.10, 0.06, 0], 0.30)



class HenrySpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Gym Jamboree"
    self.type = "Boost"
    self.nameColor = "Y"
    self.castingZones = [2, 2, 7, 2, 2]
    self.castingSpeed = 1.25
    self.desc = "Boosts spells by |G|12%|W|/|Y|10%|W|/|R|0%|--|. Caps at |G|64%|--|."
    self.lore = "Jim is all he does, Jim is all he is"

  def cast(self, damageMultiplier, caster, target):
    quickBoostSpell(damageMultiplier, caster, target, \
                    [
                      "But, you could not hit your PB...", # You failed to boost yourself.
                      "But, {} could not hit their PB...", # {} fails to boost themselves.
                      "You hit your PB, boosting yourself by |Y|10%|--|!", # You successfully boost yourself by 12%
                      "{} hits their PB, boosting themselves by |Y|10%|--|!", # {}'s boost themselves by 12%
                      "You break your PB by a massive margin, boosting you by |Y|12%|--|!", # Your boost is strong, boosting by 20%
                      "{} breaks their PB by a massive margin, boosting them by |Y|12%|--|!" # {}'s boost is strong, boosting by 20%
                      # For these messages, put the percentages in the messages. DO NOT USE %d
                    ], [0.12, 0.10, 0], 0.64) # [Green Boost, Yellow Boost, 0]

class JaniyahSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "DELETED"
    self.type = "DELETED"
    self.nameColor = "PI"
    self.castingZones = [5,3,2,3,5]
    self.castingSpeed = 1.25
    self.desc = "DELETED"
    self.lore = "DELETED"
    
  def cast(self, damageMultiplier, caster, target):
    pass

class JashleeSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Uno Reverse"
    self.type = "Weaken"
    self.nameColor = "DG"
    self.castingZones = [7, 5, 2, 5, 7]
    self.castingSpeed = 1.5
    self.desc = "Nullifies the enemy's shield by |G|30%|W|/|Y|15%|W|/|R|0%|--|."
    self.lore = "Loves playing card games, wants to be a professional Uno player"

  
  def cast(self, damageMultiplier, caster, target):
    quickNullifySpell(damageMultiplier, caster, target, \
                    [
                      "But, you have to draw 4...",
                      "But, {} has to draw 4...", 
                      "You put down an Uno Reverse, but they reverse back, only nullifying {}'s shield by |BR|15%|--|!",
                      "{} puts down an Uno Reverse, but you reverse back, only nullifying your shield by |BR|15%|--|!", 
                      "You put down an Uno Reverse and save yourself from a +4, nullifying {}'s shield by |BR|30%|--|!",
                      "{} puts down an Uno Reverse and saves themselves from a +4, weakening your shield by |BR|30%|--|!"
                    ], [0.30, 0.15, 0])

class JessikaSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Glistening Glory"
    self.type = "Defense"
    self.nameColor = "G"
    self.castingZones = [0, 0, 9, 0, 0]
    self.castingSpeed = 1.75
    self.desc = "Defends for |G|20%|--|. Caps at |G|45%|--|."
    self.lore = "Will brag about anything and everything"

  
  def cast(self, damageMultiplier, caster, target):
    quickShieldSpell(damageMultiplier, caster, target, \
                    [
                      "no bad",
                      "no bad",
                      "no mid",
                      "no mid",
                      "You brag about something very important to you, defending you for |G|20%|--|!",
                      "{} brags about something very important to them, defending them for |G|20%|--|!"
                    ], [0.20, 0, 0], 0.45)


class JustinSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Half-Note Healing"
    self.type = "Health"
    self.nameColor = "PI"
    self.castingZones = [7, 5, 3, 3, 4]
    self.castingSpeed = 1.0
    self.desc = "Heal for |G|20|W|/|Y|5|W|/|R|0|--| health."
    self.lore = "Will talk about musical passions as well, mainly with Dasha"
    
    
  def cast(self, damageMultiplier, caster, target):
    quickHealthSpell(damageMultiplier, caster, target, \
                    [
                      "But you hit the wrong notes on your guitar...",
                      "But {} hits the wrong notes on their guitar...",
                      "You play your guitar, healing you for |PI|%d|--| health!",
                      "{} plays their guitar, healing them for |PI|%d|--| health!",
                      "You play your guitar and impress onlookers, healing you for |PI|%d|--| health!",
                      "{} plays their guitar and impresses onlookers, healing them for |PI|%d|--| health!"
                    ], [20, 5, 0])


    
class KatherineSpell(Spell):
  def __init__(self):
    self.name = "Possessing Perfection"
    self.type = "Attack"
    self.nameColor = "R"
    self.castingZones = [9, 0, 1, 0, 9]
    self.castingSpeed = 3.0
    self.desc = "Deals |G|120|W|/|R|0|--| damage."
    self.lore = "Perfection is a critical part of life" 
    
  def cast(self, damageMultiplier, caster, target):
    quickDamageSpell(damageMultiplier, caster, target, \
                    [
                      "But you get a 9.75/10 on an assignment!",
                      "But {} gets a 9.75/10 on an assignment!",
                      "Mid Player %d (If you're reading this something really bad happened)",
                      "Mid Enemy %d (If you're reading this something really bad happened)",
                      "All of your grades are a perfect 100, empowering you to summon a powerful beam dealing |R|%d|--| damage!",
                      "All of {}'s grades are a perfect 100, empowering then to summon a powerful beam dealing |R|%d|--| damage!"
                    ], [120, 0, 0])

class KedusSpell(Spell): 
  def __init__(self):
    self.name = "Tiny Tempest"
    self.type = "Defense"
    self.nameColor = "G"
    self.castingZones = [9, 2, 3, 4, 3]
    self.castingSpeed = 1.25
    self.desc = "Defends for |G|25%|W|/|Y|6%|W|/|R|0%|--|. Caps at |G|32%|--|."
    self.lore = "You can see the top of his head!"
    
    
  def cast(self, damageMultiplier, caster, target):
    quickShieldSpell(damageMultiplier, caster, target, \
                    [
                      "But, you are too small to protect yourself from any real damage...",
                      "But, {} is too small to protect themselves from any real damage...",
                      "You can protect yourself pretty well, defending yourself by |G|6%|--|!",
                      "{} can protect themselves pretty well, defending them by |G|6%|--|!",
                      "You attack from underneath, rendering them defenseless and defending yourself by |G|25%|--|!",
                      "{} attacks from underneath, rendering you defenseless and defending them by |G|25%|--|!"
                    ], [0.25, 0.06, 0], 0.32)

class KhangSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Confidential Phishing"
    self.type = "Weaken"
    self.nameColor = "BR"
    self.castingZones = [2, 3, 3, 3, 2]
    self.castingSpeed = 2.0
    self.desc = "Weakens the enemy's boost by |G|37%|W|/|Y|25%|W|/|R|0%|--|."
    self.lore = "TBD"
    

  def cast(self, damageMultiplier, caster, target):
    quickWeakenSpell(damageMultiplier, caster, target, \
                    [
                      "But, you get exposed trying to phish someone...",
                      "But, {} gets exposed trying to phish someone...", 
                      "You successfully phish someone, but you don't get that big of a reward, weakening {} by |BR|25%|--|!",
                      "{} successfully phishes someone, but they don't get that big of a reward, weakening you by |BR|25%|--|!", 
                      "You easily phish someone, and you get a massive payout, weakening {} by |BR|37%|--|!",
                      "{} easily phishes someone, and they get a massive payout, weakening you by |BR!37%|--|!"
                    ], [0.37, 0.25, 0])

class KrishanSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Geographical Extortion"
    self.type = "Attack"
    self.nameColor = "R"
    self.castingZones = [5,3,2,3,5]
    self.castingSpeed = 1
    self.desc = "Absorbs 1/14 of you opponents health"
    self.lore = "Hates OCD people so absorbs a oddly specific fraction of health."
    
  
  def cast(self, damageMultiplier, caster, target):
    pass

'''
class LeeSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Misleen"
    self.type = "Boost"
    self.nameColor = "Y"
    self.castingZones = [5,3,2,3,5]
    self.castingSpeed = 1.1
    self.desc = "Boosts your spells for the next 3 turns by 65%. Cannot be stacked."
    self.lore = "TBD"
    

  def cast(self, damageMultiplier, caster, target):
    pass
'''

class LillianSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Alibi of Mastery"
    self.type = "|R|Attack|B| + |PI|Health|B|"
    self.nameColor = "B"
    self.castingZones = [5, 5, 2, 3, 3]  # R/Y/G/Y/R
    self.castingSpeed = 1.5
    self.desc = "Deals |G|36|W|/|Y|20|W|/|R|0|--| damage & Heals for |G|30|W|/|Y|10|W|/|R|0|--| health"
    self.lore = "TBD" 
    
    
  def cast(self, damageMultiplier, caster, target):
    if damageMultiplier[0] == REDZONE:
      printCastMessage("But you don't have a good alibi...", "But {} doesn't have a good alibi...", caster, target)
      notEffective()
      
    elif damageMultiplier[0] == YELLOWZONE:
      res1 = target.takeDamage(20 * damageMultiplier[1])
      res2 = caster.heal(10 * damageMultiplier[1])
      printCastMessage("You have a plausible excuse, dealing |R|%d|--| damage and healing yourself for |PI|%d|--| health!" % (res1, res2), "{} has a plausible excuse, dealing |R|%d|--| damage and healing them for |PI|%d|--| health!" % (res1, res2), caster, target)
      
    elif damageMultiplier[0] == GREENZONE:
      res1 = target.takeDamage(36 * damageMultiplier[1])
      res2 = caster.heal(30 * damageMultiplier[1])
      printCastMessage("You craft an incredible alibi, dealing |R|%d|--| damage and healing yourself for |PI|%d|--| health!" % (res1, res2), "{} crafts an incredible alibi, dealing |R|%d|--| damage and healing for by |PI|%d|--| health!" % (res1, res2), caster, target)
      superEffective()
  
class LukeSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Low-Profile Intellect"
    self.type = "Boost"
    self.nameColor = "Y"
    self.castingZones = [0, 4, 6, 4, 0]
    self.castingSpeed = 1.5
    self.desc = "Boosts spells by |G|20%|W|/|Y|12%|W|/|R|0%|--|. Caps at |G|70%|--|."
    self.lore = "TBD"
    
    
  def cast(self, damageMultiplier, caster, target):
    quickBoostSpell(damageMultiplier, caster, target, \
                    [
                      "no failure, he's goated", # You failed to boost yourself.
                      "no failure, he's goated", # {} fails to boost themselves.
                      "Your intellect is barely enough, boosting you by |Y|12%|--|!", # You successfully boost yourself by 12%
                      "{}'s intellect is barely enough, boosting them by |Y|12%|--|!'", # {}'s boost themselves by 12%
                      "Your intellect puts everyone to shame, boosting you by |Y|20%|--|!", # Your boost is strong, boosting by 20%
                      "{}'s intellect puts everyone to shame, boosting them by |Y|20%|--|!'" # {}'s boost is strong, boosting by 20%
                      # For these messages, put the percentages in the messages. DO NOT USE %d
                    ], [0.20, 0.12, 0], 0.7) # [Green Boost, Yellow Boost, 0]

class MayaSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Concentric Chaos"
    self.type = "|R|Attack|B| + |Y|Boost|B|"
    self.nameColor = "B"
    self.castingZones = [3, 5, 2, 5, 3]  # R/Y/G/Y/R
    self.castingSpeed = 2.5
    self.desc = "Deals 60/17 damage/ boosts 25%/15%"
    self.lore = "TBD"
    
  def cast(self, damageMultiplier, caster, target):
    pass

class NathanSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Peanut Barrage"
    self.type = "Health"
    self.nameColor = "PI"
    self.castingZones = [6, 3, 5, 3, 6]
    self.castingSpeed = 1.5
    self.desc = "Heal for |G|40|W|/|Y|22|W|/|R|0|--| health."
    self.lore = "TBD"
    

  def cast(self, damageMultiplier, caster, target):
    quickHealthSpell(damageMultiplier, caster, target, \
                    [
                      "But, your nuts were not strong enough to threaten {}...",
                      "But, {}'s nuts were not strong enough to threaten you...",
                      "Your nuts had some good substance in them, healing you for |PI|%d|--| health!",
                      "{}'s nuts had some good substance in them, healing them for |PI|%d|--| health!",
                      "Your nuts were the best snack in the land, healing you for |PI|%d|--| health!",
                      "{}'s nuts were the best snack in the land, healing them for |PI|%d|--| health! "
                    ], [40, 22, 0])

class OmkarSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Extrusion of Thoughts"
    self.type = "Attack"
    self.nameColor = "R"
    self.castingZones = [3, 3, 6, 3, 3]
    self.castingSpeed = 0.8
    self.desc = "Deals |G|18|W|/|Y|16|W|/|R|0|--| damage."
    self.lore = "Spends 20 hours a day doing CAD, the other 4 mowing his lawn"

  def cast(self, damageMultiplier, caster, target):
    quickDamageSpell(damageMultiplier, caster, target, \
                    [
                      "But you get constraint errors, making you have to redo your sketch!",
                      "But {0} gets constraint errors, making them have to redo their sketch!",
                      "Your assembly parts are overlapping a tiny bit, but it still deals |R|%d|--| damage!",
                      "{}'s assembly parts are overlapping a tiny bit, but it still deals |R|%d|--| damage!",
                      "Your dimensioning is spot on, dealing |R|%d|--| damage!",
                      "{}'s dimensioning is spot on, dealing |R|%d|--| damage!"
                    ], [18, 16, 0])

class PercySpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Rainbow Radioactivity"
    self.type = "Attack"
    self.nameColor = "R"
    self.castingZones = [1, 3, 2, 3, 1]
    self.castingSpeed = 1.5
    self.desc = "Deals |G|56|W|/|Y|44|W|/|R|0|--| damage."
    self.lore = "TBD"

  def cast(self, damageMultiplier, caster, target):
    quickDamageSpell(damageMultiplier, caster, target, \
                    [
                      "But your rainbow turns black and white!",
                      "But {}'s rainbow turns black and white!",
                      "Your rainbow works, but it is missing red! It still deals |R|%d|--| damage.",
                      "{}'s rainbow works, but it is missing red! It still deals |R|%d|--| damage.",
                      "Your rainbow works, and you even find a pot of gold at the end, dealing |R|%d|--| damage!",
                      "{}'s rainbow works, and they even find a pot of gold at the end, dealing |R|%d|--| damage!"
                    ], [56, 44, 0])

class PeterSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Vector Vanquish"
    self.type = "Attack + Defense"
    self.nameColor = "B"
    self.castingZones = [5,3,2,3,5]
    self.castingSpeed = 1.25
    self.desc = "Boosts spells by 20%, unless your opponent is Valeria then its does nothing."
    self.lore = "TBD"
    

  def cast(self, damageMultiplier, caster, target):
    pass

class PilliamSpell(Spell):
  def __init__(self):
    self.name = "Berry Overflow"
    self.type = "Health"
    self.nameColor = "PI"
    self.castingZones = [4, 3, 4, 3, 4]
    self.castingSpeed = 1.0
    self.desc = "Heal for |G|15|W|/|Y|10|W|/|R|0|--| health."
    self.lore = "Eats strawberries and codes the whole day"

  def cast(self, damageMultiplier, caster, target):
    quickHealthSpell(damageMultiplier, caster, target, \
                    [
                      "But you can't find any strawberries to collect!",
                      "But {} can't find any strawberries to collect!",
                      "You successfully claim a juicy strawberry, healing you for |PI|%d|--| health!",
                      "{} successfully claims a juicy strawberry, healing them for |PI|%d|--| health!",
                      "Your strawberry basket is overflowing, healing you for |PI|%d|--| health!",
                      "{}'s strawberry basket is overflowing, healing them for |PI|%d|--| health!"
                    ], [15, 10, 0])



class PoorviSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Literature Lash"
    self.type = "Attack"
    self.nameColor = "R"
    self.castingZones = [7, 5, 2, 5, 7]
    self.castingSpeed = 2.0
    self.desc = "Deals |G|86|W|/|Y|55|W|/|R|0|--| damage."
    self.lore = "TBD"
    
  def cast(self, damageMultiplier, caster, target):
    quickDamageSpell(damageMultiplier, caster, target, \
                    [ # i think i'll go to bed for today, do you need anything other spell.cast() templates
                      # boost is same as attack, except write out the percentages (i.e 12%) instead of a %d
                      # shield is same as boost (except, you knwo, its a shield instead of a boost)
                      # heals use the same format as attacks
                      # nullifies & weakens use the same format as boosts & shields i think
                      #tyvm, gn
                      # gn (why is akash not active lol) anyways gn gn
                      "You throw your book at {}, but you completely miss...",
                      "{} throws their book at you, but they completely miss...",
                      "You throw your book at {}, grazing their face and dealing |R|%d|--| damage!",
                      "{} throws their book at you, grazing your face and dealing |R|%d|--| damage!",
                      "You throw your book at {}, knocking the wind out of them and dealing |R|%d|--| damage!",
                      "{} throws their book at you, knocking the wind out of you and dealing |R|%d|--| damage!"
                    ], [86, 55, 0])


'''
class PresleySpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Presleyn"
    self.type = "Effect"
    self.nameColor = "P"
    self.castingZones = [5, 3, 1, 3, 5]
    self.castingSpeed = 1.75
    self.desc = "Gives your opponent an evaporation effect that'll gradually depletes damage from your opponent. 1/16th max HP on the first turn, 1/12th max HP on the second, and 1/8th max HP on the third."
    self.lore = "A Benevolent Dictatorship"
    
  def cast(self, damageMultiplier, caster, target):
    pass
'''

class PrestonSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Blufin Sweep"
    self.type = "Attack"
    self.nameColor = "R"
    self.castingZones = [5, 3, 5, 3, 5]
    self.castingSpeed = 1
    self.desc = "Deals |G|20|W|/|Y|13|W|/|R|0|--| damage."
    self.lore = "Will ask you to dab him up, it is mandatory"

  def cast(self, damageMultiplier, caster, target):
    quickDamageSpell(damageMultiplier, caster, target, \
                    [
                      # k
                      "But your reality company loses a lot of money!", 
                      "But {}'s reality company loses a lot of money!",
                      "Your reality company makes a net gain, dealing |R|%d|--| damage!",
                      "{}'s reality company makes a net gain, dealing |R|%d|--| damage!",
                      "Your reality company makes a boatload of earnings, dealing |R|%d|--| damage!",
                      "{}'s reality company makes a boatload of earnings, dealing |R|%d|--| damage!"
                    ], [20, 13, 0])

class RachelSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "BTS Purple Magic"
    self.type = "Attack"
    self.nameColor = "R"
    self.castingZones = [3, 4, 3, 4, 3]
    self.castingSpeed = 1.75
    self.desc = "Deal 73-77 damage."
    
  def cast(self, damageMultiplier, caster, target):
    pass

 
class RoselynSpell(Spell):

  def __init__(self):
    # Unfinished
    self.name = "Nepalese Necromancy"
    self.type = "Attack"
    self.nameColor = "R"
    self.castingZones = [2, 5, 4, 5, 2]
    self.castingSpeed = 1.75
    self.desc = "Deals |G|68|W|/|Y|45|W|/|R|0|--| damage."
    self.lore = "TBD"

  def cast(self, damageMultiplier, caster, target):
    quickDamageSpell(damageMultiplier, caster, target, \
                    [
                      "But the Nepalese Government catches you instead of {}!",
                      "But the Nepalese Government catches them instead of you!",
                      "The Nepalese Government runs after {} and deals |R|%d|--| damage!",
                      "The Nepalese Government runs after you and deals |R|%d|--| damage! ",
                      "The Nepalese Government successfully traps {}, dealing |R|%d|--| damage!",
                      "The Nepalese Government successfully traps you, dealing |R|%d|--| damage!"
                    ], [68, 45, 0])
    
class RyanSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Debugging Purge"
    self.type = "Attack"
    self.nameColor = "R"
    self.castingZones = [8, 4, 4, 4, 3]
    self.castingSpeed = 1.25
    self.desc = "Deals |G|46|W|/|Y|34|W|/|R|0|--| damage."
    self.lore = "Spends 90% of class playing random computer games"
    
  def cast(self, damageMultiplier, caster, target):
    quickDamageSpell(damageMultiplier, caster, target, \
                    [
                      "But you are unable to debug your program!",
                      "But {} is unable to debug their program!",
                      "You debug your program, but can't fix a logic error! It still deals |R|%d|--| damage.",
                      "{} debugs their program, but can't fix a logic error! They still deal |R|%d|--| damage.",
                      "You completely debugged your program, empowering you to deal |R|%d|--| damage!",
                      "{} completely debugged their program, empowering them to deal |R|%d|--| damage!"
                    ], [46, 34, 0])

class SayfSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Military Scamming"
    self.type = "Weaken"
    self.nameColor = "BR"
    self.castingZones = [6, 2, 2, 2, 6]
    self.castingSpeed = 1.25
    self.desc = "Weakens the enemy's boost by |G|25%|W|/|R|0%|--|."
    self.lore = "Likes to listen to K-Pop and K-Dramas, it's his personality"
    
  def cast(self, damageMultiplier, caster, target):
    quickWeakenSpell(damageMultiplier, caster, target, \
                    [
                      "But, your scamming platform gets corrupted and crashes...",
                      "but, {}'s scamming platform gets corrupted and crashes...", 
                      "this message crashed into a building",
                      "this message crashed into a building", 
                      "You scam all the grandmas in the world effortlessly, weakening {} by |BR|25%|--|!",
                      "{} scams all the grandmas in the world effortlessly, weakening you by |BR|25%|--|!"
                    ], [0.25, 0, 0])

class SergiSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Wig Frenzy"
    self.type = "Defense"
    self.nameColor = "G"
    self.castingZones = [8, 3, 2, 3, 8]
    self.castingSpeed = 1.5
    self.desc = "Defends for |G|24%|W|/|Y|12%|W|/|R|0%|--|. Caps at |G|37%|--|."
    self.lore = "TBD"
    
  def cast(self, damageMultiplier, caster, target):
    quickShieldSpell(damageMultiplier, caster, target, \
                    [
                      "But, your wig falls off...",
                      "But, {}'s wig falls off...",
                      "You get your wig, but it's of poor quality, only defending you for |G|12%|--|!",
                      "{} gets their wig, but it's of poor quality, only defending themselves for |G|12%|--|!",
                      "You get your wig, and it's of great quality, defending yourself for |G|24%|--|!",
                      "{} gets their wig, and it's of great quality, defending themselves for |G|24%|--|!"
                    ], [0.24, 0.12, 0], 0.37)

class ShameerSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Deafening Music"
    self.type = "Weaken + Health"
    self.nameColor = "DG"
    self.castingZones = [5, 5, 2, 5, 5]
    self.castingSpeed = 1.25
    self.desc = "TBD"

  def cast(self, damageMultiplier, caster, target):
    pass

class SherrySpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Ace of Isometry"
    self.type = "Defense"
    self.nameColor = "G"
    self.castingZones = [5, 5, 2, 5, 5]
    self.castingSpeed = 1.75
    self.desc = "Defends for |G|27%|W|/|Y|18%|W|/|R|0%|--|. Caps at |G|50%|--|."
    self.lore = "TBD"
    
  def cast(self, damageMultiplier, caster, target):
    quickShieldSpell(damageMultiplier, caster, target, \
                    [
                      "Ineffective Player",
                      "Ineffective Enemy",
                      "Mid Player",
                      "Mid Enemy",
                      "Effective Player",
                      "Effective Enemy"
                    ], [0.27, 0.18, 0], 0.50)


class ShriramSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Unseasoned Masala"
    self.type = "\"Health\""
    self.nameColor = "PI"
    self.castingZones = [9, 0, 0, 0, 0]
    self.castingSpeed = 1
    self.desc = "Heals |R|-15|B| health."
    self.lore = "Will brag about test scores and having the worst grades"

  def cast(self, damageMultiplier, caster, target):
    caster.health -= 15
    if caster.isPlayer:
      printC("The masala is somehow unseasoned, making you take |R|15|B| damage!", "B")
    else:
      printC("The masala is somehow unseasoned, making {}|B| take |R|15|B| damage!".format(caster.getName()), "B")
    


class SofyaSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Vitality Blessing"
    self.type = "Health"
    self.nameColor = "PI"
    self.castingZones = [5, 4, 2, 4, 9]
    self.castingSpeed = 1.75
    self.desc = "Heal for |G|58|W|/|Y|20|W|/|R|0|--| health."
    self.lore = "TBD"
    
  def cast(self, damageMultiplier, caster, target):
    quickHealthSpell(damageMultiplier, caster, target, \
                    [
                      "But, you don't have enough power yet...",
                      "But, {} doesn't have enough power yet...",
                      "You are able to strengthen yourself, healing yourself for |PI|%d|--|!",
                      "{} is able to strengthen themselves, healing themselves for |PI|%d|--|!",
                      "You are able to fully self-vitalize, healing yourself for |PI|%d|--|! ",
                      "{} is able to fully self-vitalize, healing themselves for |PI|%d|--|!"
                    ], [58, 20, 0])

    
class SriSpell(Spell):
  def __init__(self):
    self.name = "Snow Savagery"
    self.type = "Weaken"
    self.nameColor = "BR"
    self.castingZones = [3, 3, 3, 3, 3]
    self.castingSpeed = 1.75
    self.desc = "Weakens the enemy's boost by |G|35%|W|/|Y|5%|W|/|R|0%|--|."
    self.lore = "Resident Class Clown"

  def cast(self, damageMultiplier, caster, target):
    quickWeakenSpell(damageMultiplier, caster, target, \
                    [
                      "But, it never snowed...",
                      "But, it never snowed...", 
                      "It snowed in your backyard, but only an inch, weakening {} by |BR|5%|--|!",
                      "It snowed in {}'s backyard, but only an inch, weakening you by |BR|5%|--|!", 
                      "It was a full on blizzard in your city, weakening {} by |BR|35%|--|!",
                      "It was a full on blizzard in {}'s city, weakening you by |BR|35%|--|!"
                    ], [0.35, 0.05, 0])

class TerenceSpell(Spell):
  def __init__(self):
    self.name = "Innocent Deception"
    self.type = "Defense"
    self.nameColor = "G"
    self.castingZones = [5, 1, 5, 1, 5]
    self.castingSpeed = 1.5
    self.desc = "Defends for |G|18%|W|/|Y|15%|W|/|R|0%|--|. Caps at |G|42%|--|."
    self.lore = "TBD"
  
  def cast(self, damageMultiplier, caster, target):
    quickShieldSpell(damageMultiplier, caster, target, \
                    [
                      "But, {} doesn't fall for your tricks...",
                      "But, you don't fall for {}'s tricks...'",
                      "You can keep up the charade, but you're a bit suspicious, only defending yourself for |G|15%|--|!",
                      "{} can keep up the charade, but they're a bit suspicious, only defending themselves for |G|15%|--|!",
                      "You are a master at work, fooling everyone and defending yourself for |G|18%|--|!",
                      "{} is a master at work, fooling everyone and defending themselves for |G|18%|--|!"
                    ], [0.18, 0.15, 0], 0.42)

class TylerSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Masked Secrecy"
    self.type = "Defense"
    self.nameColor = "G"
    self.castingZones = [3, 4, 3, 2, 9]
    self.castingSpeed = 1.25
    self.desc = "Defends for |G|12%|W|/|Y|12%|W|/|R|0%|--|. Caps at |G|35%|--|."
    self.lore = "You'll never see what hides behind that hood..."
    
  def cast(self, damageMultiplier, caster, target):
    quickShieldSpell(damageMultiplier, caster, target, \
                    [
                      "But, someone takes your hood off...",
                      "But, someone takes {}'s hood off...",
                      "You remain masked, but insecure, defending yourself for |G|12%|--|!",
                      "{} remains masked, but insecure, defending themelves for |G|12%|--|!",
                      "You remain masked and sane, defending yourself for |G|12%|--|!",
                      "{} remains masked and sane, defending themselves for |G|12%|--|!"
                    ], [0.12, 0.12, 0], 0.35)




class ValeriaSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Deceitful Wiles"
    self.type = "Boost"
    self.nameColor = "Y"
    self.castingZones = [5, 4, 2, 4, 5]
    self.castingSpeed = 2.0
    self.desc = "Boosts spells by |G|48%|W|/|Y|22%|W|/|R|0%|--|. Caps at |G|80%|--|."
    self.lore = "TBD"

  def cast(self, damageMultiplier, caster, target):
    quickBoostSpell(damageMultiplier, caster, target, \
                    [
                      "Ineffective Player", # You failed to boost yourself.
                      "Ineffective Enemy", # {} fails to boost themselves.
                      "Mid Player", # You successfully boost yourself by 12%
                      "Mid Enemy", # {}'s boost themselves by 12%
                      "Effective Player", # Your boost is strong, boosting by 20%
                      "Effective Enemy" # {}'s boost is strong, boosting by 20%
                      # For these messages, put the percentages in the messages. DO NOT USE %d
                    ], [0.48, 0.22, 0], 0.8) # [Green Boost, Yellow Boost, 0]
    

class WilliamSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Surly Suprise"
    self.type = "Weaken"
    self.nameColor = "BR"
    self.castingZones = [4, 3, 3, 3, 4]
    self.castingSpeed = 1.25
    self.desc = "Weakens the enemy's boost by |G|20%|W|/|Y|10%|W|/|R|0%|--|."
    self.lore = "Likes to hang out with the East Asians, I wonder why..."

  def cast(self, damageMultiplier, caster, target):
    quickWeakenSpell(damageMultiplier, caster, target, \
                    [
                      "But, you aren't angry enough to startle {}...",
                      "But, {} isn't angry enough to startle you...", 
                      "You get angry, but only enough to mildly confuse {}, weakening {} by |BR|10%|--|!",
                      "{} gets angry, but only enough to mildly confuse you, weakening you by |BR|10%|--|!", 
                      "You get extremely angry, scaring {} and weakening them by |BR|20%|--|!",
                      "{} extremely angry, scaring you and weakening you by |BR|20%|--|!"
                    ], [0.20, 0.10, 0])
    
class YuliaSpell(Spell):
  def __init__(self):
    # Unfinished
    self.name = "Tardy Trepidation"
    self.type = "Weaken"
    self.nameColor = "BR"
    self.castingZones = [3, 0, 6, 0, 3]
    self.castingSpeed = 1.25
    self.desc = "Weakens the enemy's boost by |G|17%|W|/|Y|15%|--|."
    self.lore = "Late to class, and then leaves 5 minutes later"
    
  def cast(self, damageMultiplier, caster, target):
    quickWeakenSpell(damageMultiplier, caster, target, \
                    [
                      "she is never early",
                      "she is never early", 
                      "You get to class on time, weakening {} by |BR|15%|--|!",
                      "{} gets to class on time, weakening you by |BR|15%|--|!", 
                      "You get to class 5 minutes late, greatly upsetting the teacher and weakening {} by |BR|17%|--|!",
                      "{} gets to class 5 minutes late, greatly upsetting the teacher and weakening you by |BR|17%|--|!"
                    ], [0.17, 0.15, 0])



class DebugSpell(Spell):
  def __init__(self):
    self.name = "Apotheosis"
    self.type = "Debug"
    self.nameColor = "DB"
    self.castingZones = [0, 0, 10, 0, 0]
    self.castingSpeed = 2
    self.desc = "Deals |G|1000000|--| damage."
    self.lore = "Skill -100, Clout +1000"
    
  def cast(self, damageMultiplier, caster, target):
    quickDamageSpell(damageMultiplier, caster, target, \
                    [
                      "a","b","c","d",
                      "You absolutely annihilate your opponent, dealing |R|%d|--| damage!",
                      "{} wields too much power, dealing |R|%d|--| damage and eliminating you!"
                    ], [1000000, 0, 0])

