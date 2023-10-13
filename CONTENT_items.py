from imports import *

#########################
## CUSTOM BATTLE ITEMS ##
#########################

class StrawberryShakeItem(BattleItem):
  def __init__(self, quantity = 1):
    self.name = "Strawberry Shake"
    self.nameColor = "PI"
    self.rarity = 1
    self.type = 0
    self.desc = '''\
The Strawberry is the main source of calories
for all diehard Celeste fans.

This became unhealthy for Pilliam after a while,
so he made some Strawberry Milkshakes.

Then he realized that they were even unhealthier,
so he sold them to Maya for a profit.


Heals for |R|40 health|--| when consumed in battles.
'''

    self.quantity = quantity

  def use(self, player, target):
    self.quantity -= 1
    printC("\nYou chug the |PI|Strawberry Shake|B|.")
    remindsYouOf = random.choice(["wavedashing", "wallbouncing", "hyperdashing", "hyper-bunnyhopping", "chained ultras", "cassooted fupers", "leniency frames", "double block boosts", "Kevin Blocks", "superdashing", "mid-air supers", "neutral jumping", "dream smuggles"])
    printC("It makes you think of |PI|{}|B| and gives you a burst of energy.".format(remindsYouOf))
    printC("You heal for |PI|40 |B|health.")
    player.heal(40)

class TectonicSnacksItem(BattleItem):
  def __init__(self, quantity = 1):
    self.name = "Tectonic Snacks"
    self.nameColor = "BR"
    self.rarity = 1
    self.type = 0
    self.desc = '''\
The wrapping says to simulate plate boundaries:
- Convergent Collides
- Divergent Divides
- Transform Sliiiiides

But everyone eats them immediately, so who cares.


Can be used in battles to either:
- Heal for |R|25 Health|--| OR
- Deal |R|30 Damage|DG| (Not Affected By Boosts)'''

    self.quantity = quantity

  def use(self, player, target):
    self.quantity -= 1
    printC("\nYou unwrap the |BR|Tectonic Snacks|B|.")
    choice = dropdownMenu("What boundary will you simulate?", ["|PI|Convergent Boundary (Heal 25 Health)", "|R|Divergent boundary (Deal 30 Damage)"])
    if choice == 1:
      printC("You use the |BR|Tectonic Snacks|B| to simulate a |PI|Convergent Boundary|B|.")
      printC("Upon eating the delicious mixture, you heal for |PI|25|B| health.")
      player.heal(25)
    if choice == 2:
      printC("You use the |BR|Tectonic Snacks|B| to summon a |R|Divergent Boundary|B| on {}.".format(target.getName()))
      printC("{} is split by the |R|Divergent Boundary|B| (literally), taking 30 damage!".format(target.getName()))
      target.takeDamage(30)

class PopcornItem(BattleItem):
  def __init__(self, quantity = 1):
    self.name = "InstaPop Popcorn"
    self.nameColor = "Y"
    self.rarity = 2
    self.type = 0
    self.desc = '''\
Fresh out of the oven. These preheated kernels pop
into fresh popcorn as soon as they impact an object.


Can be used in battles to deal anywhere
from |R|20 |B|to |R|50|B| damage.
'''

    self.quantity = quantity

  def use(self, player, target):
    self.quantity -= 1
    printC("\nYou quickly unwrap the |Y|InstaPop Popcorn|B| and aim at your opponent.")
    res = getZone(timedHitbar(1.25, [8, 4, 2, 4, 8]), [8, 4, 2, 4, 8])
    damage = 0
    if res == REDZONE:
      damage = 20
    elif res == YELLOWZONE:
      damage = 35
    elif res == GREENZONE:
      damage = 50

    printC("You throw the popcorn at {}, whereupon it instantly explodes.".format(target.getName()))
    printC("{} takes {} damage from the explosion!".format(target.getName(), damage))
    target.takeDamage(damage)


class SmoresItem(BattleItem):
  def __init__(self, quantity = 1):
    self.name = "Smores"
    self.nameColor = "W"
    self.rarity = 2
    self.type = 0
    self.desc = '''\
Cooked through a long and arduous process over
a tiny microwave burner.


Can be used in battles to increase your boost
by |Y|50%|B|, capped at |Y|75%|B|.'''

    self.quantity = quantity

  def use(self, player, target):
    self.quantity -= 1
    printC("\nYou quickly devour the Smores.")
    printC("They're really sweet... you feel a sudden burst of energy.")
    printC("Your boost increases by |Y|50%|B|.")

    player.castBoost(0.5, 1.75)



class CokeSodaItem(BattleItem):
  def __init__(self, quantity = 1):
    self.name = "Coke"
    self.nameColor = "R"
    self.rarity = 1
    self.type = 0
    self.desc = '''\
A classic soda.

Consuming it in battles heals |PI|10|B| health and
gives you a |Y|10%|B| boost (capped at |Y|50%|B|).'''

    self.quantity = quantity

  def use(self, player, target):
    self.quantity -= 1
    printC("\nYou open the |BR|Coke |B|and take a huge swig of it.")
    printC("The sweetness heals you for |PI|10|B| health!")
    printC("The carbonation boosts you by |Y|10%|B|!")

    player.castBoost(0.1, 1.5)
    player.heal(10)



class OrangeFantaSodaItem(BattleItem):
  def __init__(self, quantity = 1):
    self.name = "Orange Fanta"
    self.nameColor = "O"
    self.rarity = 1
    self.type = 0
    self.desc = '''\
It has a nice tangy taste to it.

Consuming it in battles will convert your |Y|boost|B|
into |PI|health|B|, setting your boost back to |Y|0%|B|
and healing you for |PI|1|B| health per |Y|1%|B| boost.

This item will have no effect if your boost is zero or
negative.'''

    self.quantity = quantity

  def use(self, player, target):
    if player.boost <= 1:
      printC("\nYou don't think drinking the |O|Orange Fanta|B| would do anything, so you save it for later.")
      printC("|DG|*(Use this item with a positive boost to maximize its potential!)*")
    else:
      self.quantity -= 1
      printC("\nYou open the |O|Orange Fanta|B| and gulp it all down.")
      printC("You suddenly feel a burst of tangy sweetness!")
      healingAmount = int(100 * (player.boost - 1.00) * 2)
      player.boost = 1
      player.heal(healingAmount)
      printC("Your boost was converted into |PI|{}|B| health.".format(healingAmount))
      


class PineappleFantaSodaItem(BattleItem):
  def __init__(self, quantity = 1):
    self.name = "Pineapple Fanta"
    self.nameColor = "Y"
    self.rarity = 1
    self.type = 0
    self.desc = '''\
You might disagree on pineapple belonging on pizza,
but everyone can agree that Pineapple Fanta is great.
(Maybe.)

Consuming it in battles will increase your boost by
|Y|20%|B|, capping at |Y|50%|B|.

|DG|*Also, pineapple on pizza is the best. Period.*'''

    self.quantity = quantity

  def use(self, player, target):
    self.quantity -= 1
    printC("\nYou open the |Y|Pineapple Fanta|B| and gulp it all down.")
    printC("The sourness & sweetness of the drink empowers you!")
    printC("Your boost was increased by |Y|20%|B|.")

    player.castBoost(0.2, 1.5)


class SpriteSodaItem(BattleItem):
  def __init__(self, quantity = 1):
    self.name = "Sprite"
    self.nameColor = "G"
    self.rarity = 1
    self.type = 0
    self.desc = '''\
A sprinkling lemon-lime drink.

Consuming it in battles will increase your shield by
|G|20%|B|, capping at |G|40%|B|.'''

    self.quantity = quantity

  def use(self, player, target):
    self.quantity -= 1
    printC("\nYou open the |G|Sprite|B| and take a big swig of it.")
    printC("The unique taste makes you feel more protected!")
    printC("Your shield increases by |G|20%|B|.")

    player.castShield(0.2, 1.4)


class IcedTeaSodaItem(BattleItem):
  def __init__(self, quantity = 1):
    self.name = "Iced Tea"
    self.nameColor = "BR"
    self.rarity = 1
    self.type = 0
    self.desc = '''\
A new take on a classic historical drink.
Boston Iced Tea Party, anyone?

Consuming it in battles will heal you for
|PI|25|B| health.'''

    self.quantity = quantity

  def use(self, player, target):
    self.quantity -= 1
    printC("\nYou open the |BR|Iced Tea|B| and take a sip.")
    printC("The sweetness casts a repairing effect on your body!")
    printC("You heal for |PI|25|B| health.")

    player.heal(25)



class LifeformAnalyzerItem(BattleItem):
  def __init__(self, quantity = 1):
    self.name = "Lifeform Analyzer"
    self.nameColor = "BR"
    self.rarity = 2
    self.type = 0
    self.desc = '''\
It appears to be a jumbled mixture of telescopes,
stethscopes, gyroscopes, and various other scopes...

Using this item in battles will allow you to see
various statistics about your opponent.

|R|Special: |B|This item can be used infinitely many times
in battles. It will still consume a turn, however.
'''

    self.quantity = quantity

  def use(self, player, target):
    if target.name.lower() in ["gummy", "effie", "dobby", "gimli", "mr. adams"]:
      printC("\n============== LIFEFORM ANALYZER STATISTICS ==============\n", "BR")
      printC("|{}|{}|--|, Max Health |R|{}".format(target.nameColor, target.name, target.maxHealth), "BR")
      printC("This is a special Frog Boss enemy! It uses custom attacks.", "BR")
      printC("\n============================================================", "BR")
    else:
      printC("\n============== LIFEFORM ANALYZER STATISTICS ==============\n", "BR")
      printC("|{}|{}|--|, Max Health |R|{}".format(target.nameColor, target.name, target.maxHealth), "BR")
      printC("Uses Wand: |{}|{}".format(target.selectedWand.nameColor, target.selectedWand.name), "BR")
      print()
      printC("Can Cast the Following Spells:", "BR")
      for s in target.arsenal:
        printC(s.getName())
      printC("\n============================================================", "BR")
    


############################
## CUSTOM OVERWORLD ITEMS ##
############################

class ChobaniYogurtItem(Item):
  def __init__(self, quantity = 1):
    self.name = "Chobani Yogurt"
    self.nameColor = "Y"
    self.rarity = 0
    self.type = 1
    self.desc = '''\
Limited edition mango-flavored.

It looks tasty, but the packaging is too tightly
duct-taped to be opened in a battle.'''
    self.battleUsable = False
    
    self.quantity = quantity

class PaperclipItem(Item):
  def __init__(self, quantity = 1):
    self.name = "Paperclip"
    self.nameColor = "DG"
    self.rarity = 0
    self.type = 1
    self.desc = '''\
Could be useful for lockipicking doors... 

... if you stretch it far enough.
    '''
    self.battleUsable = False
    
    self.quantity = quantity

class HalfRippedPosterItem(Item):
  def __init__(self, quantity = 1):
    self.name = "Half-Ripped Poster"
    self.nameColor = "B"
    self.rarity = 0
    self.type = 1
    self.desc = '''\
Was a poster for an attack helicopter but
your idiocy ruined it. 

It was a cool poster. TwT
    '''
    self.battleUsable = False
    
    self.quantity = quantity

class MasterKeysItem(Item):
  def __init__(self, quantity = 1):
    self.name = "Master Keys"
    self.nameColor = "DG"
    self.rarity = 0
    self.type = 1
    self.desc = '''\
You... stole (rightfully) these keys from Ms. Palank.

Hopefully, you put them to good use.
    '''
    self.battleUsable = False
    
    self.quantity = quantity

class SSLFormsItem(Item):
  def __init__(self, quantity = 1):
    self.name = "Brooke's SSL Forms"
    self.nameColor = "B"
    self.rarity = 0
    self.type = 1
    self.desc = '''\
Brooke was volunteering at a Pokemon center...

She received an SSL hour for every Pokemon plush 
she bought...

She received 151 SSL hours.
    '''
    self.battleUsable = False
    
    self.quantity = quantity

class ShreddedSSLFormsItem(Item):
  def __init__(self, quantity = 1):
    self.name = "Brooke's Shredded SSL Forms"
    self.nameColor = "B"
    self.rarity = 0
    self.type = 1
    self.desc = '''\
Brooke was volunteering at a Pokemon center...

She received an SSL hour for every Pokemon plush 
she bought...

...

The text ends there before being cut off.
    '''
    self.battleUsable = False
    
    self.quantity = quantity

class SpeedcubeLubeItem(Item):
  def __init__(self, quantity = 1):
    self.name = "Speedcube Lubricant"
    self.nameColor = "DG"
    self.rarity = 0
    self.type = 1
    self.desc = '''\
Specialized lubricant. 50% of cubers say that
it improved their PBs by up to 1.37 seconds.
Make sure to apply to Rubix Cube joints at least
once every month for maximal benefits.

It's probably general-purpose, too...'''
    self.battleUsable = False
    self.quantity = quantity


class TeachersPassItem(Item):
  def __init__(self, quantity = 1):
    self.name = "Teacher's Pass"
    self.nameColor = "W"
    self.rarity = 2
    self.type = 1
    self.desc = '''\
The pass used to let teachers enter the school early,
while the rest of us with early busses have to sit
outside like peasants.'''
    self.battleUsable = False
    
    self.quantity = quantity



class GymKeysItem(Item):
  def __init__(self, quantity = 1):
    self.name = "Gym Keys"
    self.nameColor = "W"
    self.rarity = 2
    self.type = 1 
    self.desc = '''\
These keys can unlock the school gym...
not sure why Ms. Gleich gave it to you so effortlessly.

Guess she has a lot of trust in you, huh?
    '''
    self.battleUsable = False
    
    self.quantity = quantity


class TableTennisPaddleItem(Item):
  def __init__(self, quantity = 1): # the player keeps the paddle for the table tennis tournmanet
    self.name = "Ping Pong Paddle" # check discord
    self.nameColor = "BR"
    self.rarity = 2
    self.type = 1
    self.desc = '''\
As you wield this racket, you feel the power of Jerry Wong's
table tennis expertise caress through your vains.'''
    self.battleUsable = False

    self.quantity = quantity



class StolenFurryBookItem(Item):
  def __init__(self, quantity = 1):
    self.name = "Stolen Furry Book"
    self.nameColor = "BR"
    self.rarity = 3
    self.type = 1
    self.desc = '''\
The long-awaited and critically-acclaimed sequel to
Cryptography w/ Furries!

Last Checked Out by: Shrem Masala
Due By: 03/14/2021
'''

    self.battleUsable = False

    self.quantity = quantity


# Succulents 

    
class OrangeEcherviaSucculentItem(Item):
  def __init__(self, quantity = 1):
    self.name = "Orange Echervia Succulent"
    self.nameColor = "O"
    self.rarity = 1
    self.type = 1
    self.desc = '''\
This succulent was used as a decoration
in Jessika's Gemstone Gallery.
    '''
    self.battleUsable = False
    
    self.quantity = quantity

class AloeVeraSucculentItem(Item):
  def __init__(self, quantity = 1):
    self.name = "Aloe Vera Succulent"
    self.nameColor = "G"
    self.rarity = 1
    self.type = 1
    self.desc = '''\
This succulent was used by Ms. Presley
for a demonstration on transpiration.
    '''
    self.battleUsable = False
    
    self.quantity = quantity

class LavenderEcherviaSucculentItem(Item):
  def __init__(self, quantity = 1):
    self.name = "Lavender Echervia Succulent"
    self.nameColor = "PU"
    self.rarity = 1
    self.type = 1
    self.desc = '''\
This succulent was used by Akash for
his tonal shading assignment in IED.
    '''
    self.battleUsable = False
    
    self.quantity = quantity

class MoonCactusSucculentItem(Item):
  def __init__(self, quantity = 1):
    self.name = "Moon Cactus Succulent"
    self.nameColor = "R"
    self.rarity = 1
    self.type = 1
    self.desc = '''\
This succulent was used by a group of
7th graders for their hydroponics project. 
    '''
    self.battleUsable = False
    
    self.quantity = quantity

class BallCactusSucculentItem(Item):
  def __init__(self, quantity = 1):
    self.name = "Ball Cactus Succulent"
    self.nameColor = "G"
    self.rarity = 1
    self.type = 1
    self.desc = '''\
This succulent has seen the inside of a duck.
    '''
    self.battleUsable = False
    
    self.quantity = quantity

class RedEcherviaSucculentItem(Item):
  def __init__(self, quantity = 1):
    self.name = "Red Echervia Succulent"
    self.nameColor = "R"
    self.rarity = 1
    self.type = 1
    self.desc = '''\
This succulent cost Edem ten grand,
along with his dignity. 
    '''
    self.battleUsable = False
    
    self.quantity = quantity

class BurrosTailSucculentItem(Item):
  def __init__(self, quantity = 1):
    self.name = "Burro's Tail Succulent"
    self.nameColor = "G"
    self.rarity = 1
    self.type = 1
    self.desc = '''\
This succulent was priced at 9,999 tickets in
Shriram's Shady Sales.
    '''
    self.battleUsable = False
    
    self.quantity = quantity

class WhiteHaworthiaSucculentItem(Item):
  def __init__(self, quantity = 1):
    self.name = "White Haworthia Succulent"
    self.nameColor = "W"
    self.rarity = 1
    self.type = 1
    self.desc = '''\
This succulent was busy scoring hoops
in basketball.
    '''
    self.battleUsable = False
    
    self.quantity = quantity

class StrawberrySempervivumSucculentItem(Item):
  def __init__(self, quantity = 1):
    self.name = "Strawberry Semp. Succulent"
    self.nameColor = "PI"
    self.rarity = 1
    self.type = 1
    self.desc = '''\
This succulent is Pilliam's favorite. 
    '''
    self.battleUsable = False
    
    self.quantity = quantity


#########################
## CUSTOM COLLECTIBLES ##
#########################

class MagicalParchmentItem(Item):
  def __init(self, quantity = 1):
    self.name = "Magical Parchment"
    self.nameColor = "BR"
    self.rarity = 3
    self.type = 2
    self.desc = '''\
It's a faded scroll of parchment.
There's some barely legible writing on the paper...

|BG|
5 * PLAYER_NAME
ADD 24 * NUMBER_SPELLS
SUBTRACT 5 * NUMBER_WANDS
IF NEGATIVE, ELBOUD THE RESULT

|B|...
'''

class AncientScrollItem(Item):
  def __init__(self, quantity = 1):
    self.name = "⎎ Scroll of Uplifting"
    self.nameColor = "BR"
    self.rarity = 6
    self.type = 2
    self.desc = '''\
"We work to uplift each other at all times."

The scroll is worn and faded, the power
long gone from the passage of time...


But maybe the real scroll was the friends we
made along the way.

*Thanks for everything. ❤*'''

    self.battleUsable = False

    self.quantity = quantity



class RedCrayonItem(Item):
  def __init__(self, quantity = 1):
    self.name = "✎  Red Crayon"
    self.nameColor = "R"
    self.rarity = 1
    self.type = 2
    self.desc = '''\
Bold & brazen, it makes you stand out from the crowd.

Bring this to the art classroom to change the
color of your name!'''
    self.battleUsable = False

    self.quantity = quantity

class OrangeCrayonItem(Item):
  def __init__(self, quantity = 1):
    self.name = "✎  Orange Crayon"
    self.nameColor = "O"
    self.rarity = 1
    self.type = 2
    self.desc = '''\
Orange makes you feel quirky and unique.
Almost like a grapefruit.

Bring this to the art classroom to change the
color of your name!'''
    self.battleUsable = False

    self.quantity = quantity

class YellowCrayonItem(Item):
  def __init__(self, quantity = 1):
    self.name = "✎  Yellow Crayon"
    self.nameColor = "Y"
    self.rarity = 1
    self.type = 2
    self.desc = '''\
The goldness makes you feel richer, even though
you're actually poorer after buying this.

Bring this to the art classroom to change the
color of your name!'''
    self.battleUsable = False

    self.quantity = quantity

class GreenCrayonItem(Item):
  def __init__(self, quantity = 1):
    self.name = "✎  Green Crayon"
    self.nameColor = "G"
    self.rarity = 1
    self.type = 2
    self.desc = '''\
It fills you with the spirit of nature.
(Pilliam would probably hate it.)

Bring this to the art classroom to change the
color of your name!'''
    self.battleUsable = False

    self.quantity = quantity
    
class BlueCrayonItem(Item):
  def __init__(self, quantity = 1):
    self.name = "✎  Blue Crayon"
    self.nameColor = "B"
    self.rarity = 0
    self.type = 2
    self.desc = '''\
Simple, yet refined.

Bring it to the art classroom to change the color
of your name!'''
    self.battleUsable = False

    self.quantity = quantity

class PurpleCrayonItem(Item):
  def __init__(self, quantity = 1):
    self.name = "✎  Purple Crayon"
    self.nameColor = "PU"
    self.rarity = 1
    self.type = 2
    self.desc = '''\
This color makes you feel like thriving coral...
before being bleached.

Bring this to the art classroom to change the
color of your name!'''
    self.battleUsable = False

    self.quantity = quantity


class BrownCrayonItem(Item):
  def __init__(self, quantity = 1):
    self.name = "✎  Brown Crayon"
    self.nameColor = "BR"
    self.rarity = 2
    self.type = 2
    self.desc = '''\
As if the crayon wasn't brown enough,
it's also covered with dust and dirt.

Honestly, it makes the crayon such 
a rich chocolate color.'''

    self.battleUsable = False
    self.quantity = quantity


    self.battleUsable = False
    self.quantity = quantity


#######################
## COMMUNITY SCROLLS ##
#######################


class ScrollOfSupportItem(Item):
  def __init__(self, quantity = 1):
    self.name = "⎎ Scroll of Support"
    self.nameColor = "BR"
    self.rarity = 2
    self.type = 3
    self.desc = '''\
"We support one another in order to cultivate
the genius within others as well as within
ourselves."

The scroll glows with power.
Buying this scroll will immediately boost your
|R|max health|B| by |R|20 HP|B| in battles.'''
    self.battleUsable = False

    self.quantity = 1


class ScrollOfDiversityItem(Item):
  def __init__(self, quantity = 1):
    self.name = "⎎ Scroll of Diversity"
    self.nameColor = "BR"
    self.rarity = 2
    self.type = 3
    self.desc = '''\
"We embrace, nurture, and learn from diverse
perspectives, experiences, and identities."

The scroll glows with power.
Buying this scroll will immediately boost your
|R|max health|B| by |R|30 HP|B| in battles.'''
    self.battleUsable = False

    self.quantity = 1


class ScrollOfPresenceItem(Item):
  def __init__(self, quantity = 1):
    self.name = "⎎ Scroll of Presence"
    self.nameColor = "BR"
    self.rarity = 3
    self.type = 3
    self.desc = '''\
"We show up for ourselves and others and give
the best we have each day."

The scroll glows with power.
Buying this scroll will immediately boost your
|R|max health|B| by |R|50 HP|B| in battles.'''
    self.battleUsable = False

    self.quantity = 1


class ScrollOfCompassionItem(Item):
  def __init__(self, quantity = 1):
    self.name = "⎎ Scroll of Compassion"
    self.nameColor = "BR"
    self.rarity = 3
    self.type = 3
    self.desc = '''\
"We listen, reflect, and respond with compassion
and empathy."

The scroll glows with power.
Buying this scroll will immediately boost your
|R|max health|B| by |R|50 HP|B| in battles.'''
    self.battleUsable = False

    self.quantity = 1

class ScrollOfOwnershipItem(Item):
  def __init__(self, quantity = 1):
    self.name = "⎎ Scroll of Ownership"
    self.nameColor = "BR"
    self.rarity = 4
    self.type = 3
    self.desc = '''\
"We take ownership of our community by using
all spaces respectfully and responsibly."

The scroll glows with power.
Buying this scroll will immediately boost your
|R|max health|B| by |R|50 HP|B| in battles.'''
    self.battleUsable = False

    self.quantity = 1


class ScrollOfWellbeingItem(Item):
  def __init__(self, quantity = 1):
    self.name = "⎎ Scroll of Wellbeing"
    self.nameColor = "BR"
    self.rarity = 4
    self.type = 3
    self.desc = '''\
"We prioritize the social, emotional, and
physical wellbeing of ourselves and others."

The scroll glows with power.
Buying this scroll will immediately boost your
|R|max health|B| by |R|100 HP|B| in battles.'''
    self.battleUsable = False

    self.quantity = 1


class ScrollOfEqualityItem(Item):
  def __init__(self, quantity = 1):
    self.name = "⎎ Scroll of Equality"
    self.nameColor = "BR"
    self.rarity = 5
    self.type = 3
    self.desc = '''\
"We work to be anti-bias and antiracist."

The scroll glows with power.
Buying this scroll will immediately boost your
|R|max health|B| by |R|100 HP|B| in battles.'''
    self.battleUsable = False

    self.quantity = 1
