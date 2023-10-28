##### SHERRY WANG, ANNA ZHOU, AND BROOKE YIN STOP LOOKING AT THE CODE, THANK YOU VERY MUCH ####

from imports import *
    
class AlwaysLockedClassroom(Classroom):
  def __init__(self):
    self.name = "THIS SHOULD NOT BE USED AS A WAYPOINT"
    self.locked = [1,2,3,4,5,6]
    
class PrologueEntranceClassroom(Classroom):
  def __init__(self):
    self.name = "School Entrance"
    self.locked = []
    
  def run(self, player):
    dialNoSpeaker("You try to open the door, but it's locked.")
    dialNoSpeaker("It looks pretty fragile, though... You could probably break it open if you tried.")

    while True:
      printC("\nPress [ENTER] when the |W|arrow|B| is in the |LG|green zone!", "B")
      res = getZone(timedHitbar(1, [7, 4, 2, 4, 7]), [7, 4, 2, 4, 7])
      if res == 2:
        dialNoSpeaker("You manage to twist the handle just enough to unlock the door with a pop.")
        dialNoSpeaker("You hesitantly walk into the school...")
        break
      elif res == 0 or res == 4:
        dialNoSpeaker("You try to break open the door handle with your fist.")
        dialNoSpeaker("Nothing happens...")
        dialNoSpeaker("You feel like you should try again.")
        deleteLines(14)
      else:
        dialNoSpeaker("The door handle wobbles a bit when you try to twist it loose.")
        dialNoSpeaker("You feel like you should try it again.")
        deleteLines(12)
      flush_input()

    
    dialNoSpeaker("Suddenly, you run face to face into someone.")
    dial("Goran", "Agh!")
    dial("Goran", "Oh... Hi?")
    dial("Goran", "How did you get in here? It's ten minutes past opening time.")
    dial("Goran", "Wait, where's that draft coming from? Did the door lock break again?")
    dialNoSpeaker("You nod your head.")
    dial("Goran", "Dang it, that's the third time this week.")
    dial("Goran", "I've told Ms. Presley to fix it but she hasn't gotten around to it.")

    if db["COMPLETED_TUTORIAL_BEFORE"]:
      dial("Goran", "Anyways, are you new here? You look kind of familiar...")
      choice = dropdownMenu(None, ["|G|I'm new", "|R|I've been here before (Skip Tutorial)"])
      if choice == 1:
        pass
      elif choice == 2:
        dial("Goran", "Okay! Well, I guess that means you know how |LB|spell battles|B| work.")
        dial("Goran", "Here, I guess you already know how to use these starter wands & spells, so might as well take them.")

        dialNoSpeaker("You receive a {} from Goran!".format(FeldsparWand().getName()))
        dialNoSpeaker("You receive the spell {} from Goran!".format(OmkarSpell().getName()))
        dialNoSpeaker("You receive the spell {} from Goran!".format(ArjunSpell().getName()))
        dialNoSpeaker("You receive the spell {} from Goran!".format(AkashSpell().getName()))
        dialNoSpeaker("You receive the spell {} from Goran!".format(PilliamSpell().getName()))
        
        player.classroom = None
        player.loc = ["MAIN_ENTRANCE", "ENTRANCE_HALLWAY_8"]
        player.act = 1
    
        player.wands = [FeldsparWand()]
        player.selectedWand = FeldsparWand()
        player.spells = [OmkarSpell(), ArjunSpell(), AkashSpell(), PilliamSpell()]
        player.arsenal = [OmkarSpell(), ArjunSpell(), AkashSpell(), PilliamSpell()]

        dial("Goran", "See you around!")
        
        player.startQuest(IronicCriminalPursuitQuest)
        player.incrementQuestProgress(IronicCriminalPursuitQuest)
        
        player.sendEmail(WelcomeToClementeEmail)

        return
            
    else: 
      dial("Goran", "Anyways, are you new here? I don't think I've seen you around.")
      
    dial("Goran", "Well, welcome to RCMS! It's pretty nice here.")
    dial("Goran", "One thing you need to know, though...")
    dial("Goran", "Conflicts happen pretty often around here, so students resolve them with friendly |LB|spell battles|B|!")
    dial("Goran", "Spell battles are like normal fights, but they use magic, are completely fair, and nobody gets physically hurt.")
    dial("Goran", "~~I mean, there's still the emotional aspect of it, but that's unavoidable...~~")
    dial("Goran", "Anyways, I doubt you know how to cast spells, so I'll teach you them! They're pretty easy to get the hang of.")
    
    battlePlayer = BattlePlayer()
    battlePlayer.name = player.name
    battlePlayer.nameColor = player.nameColor
    battlePlayer.selectedWand = FeldsparWand()
    battlePlayer.arsenal = [OmkarSpell()]
    battlePlayer.isTutorial = True
    
    enemy = GoranTutorialEnemy()

    clear()
    printBattleHeader(battlePlayer, enemy)

    dial("Goran", "In a nutshell, battles work by taking turns casting spells at each other.")
    dial("Goran", "To cast spells, you channel the essence of them through wands.")
    dial("Goran", "Wands can modify your spells to make them stronger, but let's start with a simple one for now.")
    
    dialNoSpeaker("You receive a {} from Goran!".format(FeldsparWand().getName()))

    dial("Goran", "The main way of dealing damage is through |R|Attack Spells|--|.")
    dial("Goran", "Here's one to get you started with.")
    
    dialNoSpeaker("You receive the spell {} from Goran!".format(OmkarSpell().getName()))

    dial("Goran", "Anyways, I think you're itching to try out spells... Let's give it a go!")
    
    while enemy.health == 100:
      clear()
      printBattleHeader(battlePlayer, enemy)

      printC("\n|R|Goran|B|: Select the attack spell I gave you, and try casting it!")

      battlePlayer.attack(enemy)
      battlePlayer.update()

      flush_input()
      enter()

    clear()
    printBattleHeader(battlePlayer, enemy)

    dial("Goran", "Great job!")

    dial("Goran", "|R|Attack Spells|B| are the primary spell used to defeat opponents, but sometimes you need to make them more potent in a pinch.")
    dial("Goran", "That's where |Y|Boost Spells|B| come in! They give you a spell boost that's permanent unless it gets removed by an enemy.")

    battlePlayer.arsenal.append(ArjunSpell())
    dialNoSpeaker("You receive the spell {} from Goran!".format(ArjunSpell().getName()))
    
    dial("Goran", "Try using a |Y|Boost Spell|B| to increase the damage your attack deals!")

    attackedWithBoost = False
    usedTooManyAttacks = False
    
    while not attackedWithBoost:
      clear()

      if enemy.health < 50:
        enemy.health = 100
        usedTooManyAttacks = True
        
      printBattleHeader(battlePlayer, enemy)

      if usedTooManyAttacks:
        # this shouldn't happen unless the player pulls an omar balenciaga
        usedTooManyAttacks = False
        printC("\n|R|Goran|B|: Looks like you're enjoying |R|Attack Spells|B|! Why not practice using |Y|Boosts|B|, though?") 
        printC("\n*Goran heals back up to full health.*", "DG")
      else:
        printC("\n|R|Goran|B|: Try using a |Y|Boost Spell|B| to increase the damage your attack deals!")
      
      lastHealth = enemy.health
      battlePlayer.attack(enemy)
      battlePlayer.update()
      newHealth = enemy.health

      if newHealth < lastHealth and battlePlayer.boost != 1:
        attackedWithBoost = True

      flush_input()
      enter()

    clear()
    enemy.update()
    printBattleHeader(battlePlayer, enemy)
    
    dial("Goran", "Nice!")
    dial("Goran", "Of course, in a real battle, I'd be casting spells back, too!")
    dial("Goran", "So, you can use |G|Defense|--| and |PI|Healing|--| spells to defend yourself.")
    dial("Goran", "Both of these spell types do what they say; |G|Defense|--| spells give you a damage reduction shield, and |PI|Healing|--| spells heal you for an amount of health!")

    spell = AkashSpell()
    battlePlayer.arsenal.append(spell)
    dialNoSpeaker("You receive the spell {} from Goran!".format(spell.getName()))
    
    spell = PilliamSpell()
    battlePlayer.arsenal.append(spell)
    dialNoSpeaker("You receive the spell {} from Goran!".format(spell.getName()))

    dial("Goran", "Now, I'll deal |R|30|B| damage per turn to you; try using |G|Defense|B| and |PI|Healing|B| spells to survive for four turns.")

    wonChallenge = False
    while not wonChallenge:
      wonChallenge = True
      for i in range(5):
        clear()
        printBattleHeader(battlePlayer, enemy)

        if battlePlayer.health <= 0:
          dial("Goran", "Oof, hopefully that didn't hurt too much.")
          dial("Goran", "Try using your |G|Defense|B| and |PI|Healing|B| spells more tactically this time!")
          dialNoSpeaker("|DG|*Goran heals you and himself back to full health.*")
          enemy.health = 100
          battlePlayer.health = 100
          wonChallenge = False
          break
        elif enemy.health <= 0:
          dial("Goran", "Ow...")
          dial("Goran", "You're really something, huh? Well, congrats I guess.")
          dial("Goran", "I *am* kind of supposed to be teaching you *|G|Defense|B| and |PI|Healing|B| spells*, though, so...")
          dial("Goran", "Let's try this again.")
          dialNoSpeaker("|DG|*Goran heals you and himself back to full health.*")
          enemy.health = 100
          battlePlayer.health = 100
          wonChallenge = False
          break

        if i == 4:
          break
  
        printC("\n|R|Goran|B|: Cast |G|Defense|B| and |PI|Healing|B| spells to try to survive my attacks!")
  
        battlePlayer.attack(enemy)
        battlePlayer.update()

        damage = battlePlayer.takeDamage(30)

        if enemy.update():
          dialNoSpeaker("Goran casts a mysterious spell, dealing |R|{}|B| damage to you!".format(damage))

        battlePlayer.update()
        enemy.update()
        
        enter()

    clear()
    printBattleHeader(battlePlayer, enemy)

    dial("Goran", "Great job!")
    dial("Goran", "I think you're all set to win any spell battles you get yourself into.")
    dial("Goran", "RCMS isn't just about fighting, though. Friendship here is really valuable.")
    dial("Goran", "It's worth making a few friends, especially since you're new.")
    dial("Goran", "You have a |W|Chromebook|B|, right? The school should have given one to you.")
    dial("Goran", "I've added a |W|Quest|B| to your Online |W|Todo-List|B|. You should check on it every so often to see what you have to do.")
    dial("Goran", "Anyways, good luck out there, and see you around!")

    player.classroom = None
    player.loc = ["MAIN_ENTRANCE", "ENTRANCE_HALLWAY_8"]
    player.act = 1

    player.wands = [FeldsparWand()]
    player.selectedWand = FeldsparWand()
    player.spells = [OmkarSpell(), ArjunSpell(), AkashSpell(), PilliamSpell()]
    player.arsenal = player.spells.copy()

    player.startQuest(IronicCriminalPursuitQuest)
    player.incrementQuestProgress(IronicCriminalPursuitQuest)
    
    player.sendEmail(WelcomeToClementeEmail)

    db["COMPLETED_TUTORIAL_BEFORE"] = True
    
    return




class SchoolExitClassroom(Classroom):
  def __init__(self):
    self.name = "The School Exit"
    self.locked = []

  def run(self, player):
    if player.timeBetween(420, 510):
      dialNoSpeaker("It's dismissal time. Your bus leaves at 4:30 PM.") 
      dialNoSpeaker("Leave school for the day?")
      choice = dropdownMenu(None, ["|G|Leave School", "|R|Stay Back"])
      if choice == 1:
        if player.questProgressIsAtLeast(IronicCriminalPursuitQuest, 5) and player.act == 1:
          dial("Katherine", "Oh right, you need to catch your bus.")
          dial("Katherine", "Me and Peter are going to stay back for a while, we both have extracurriculars till 6.")
          dial("Peter", "Volleyball only lasts till five-")
          dial("Katherine", "See you tomorrow!")
        dialNoSpeaker("You leave the school and hop on Bus 2992.")
        dialNoSpeaker("The bus pulls away from the school, and you make yourself comfortable for the long ride home...")

        player.inSchool = False
        player.classroom = None
      elif choice == 2:
        dialNoSpeaker("You decide to stay behind for a bit.")
        player.classroom = None
        pass
    else:
      dial("Ms. Palank", "Hey, where do you think you're going?")

      choice = dropdownMenu(None, ["|Y|I'm skipping school!", "|R|I'm committing crimes!", "|B|Sorry, I'll go back to class."])

      if choice == 1:
        dial("Ms. Palank", "Get back in here, honesty isn't going to persuade me that easily.")
      elif choice == 2:
        dial("Ms. Palank", "You're doing what? If you're committing crimes then you should go to jail.")
        dial("Ms. Palank", "And you kids think that school is like jail, right?")
        dial("Ms. Palank", "Get back inside.")
      elif choice == 3:
        dial("Ms. Palank", "Good, go back to class.")

      player.classroom = None

class OutsideMainEntranceClassroom(Classroom):
  def __init__(self):
    self.name = "School Entrance"
    self.locked = []

  def run(self, player):
    if player.hasItem(TeachersPassItem):
      if player.act == 3:
        if player.hasFlag("Entrance_Int1_KatherineEngineeringMoment") == False:
          dialNoSpeaker("There seems to be a gathering of mortals near the entrance of the school.")
          dial("Brooke","I can't believe it. He didn't even get to finish his AoPS midterms!")
          dial("Gloria","Truly a sad day for us mortals. :(")
          dial("Katherine","Hey guys! Sorry I'm late, what's all the commotion about?")
          dialNoSpeaker("Katherine approaches the gathering.")
          dial("Lillian","Haven't you heard? Peter was tragically killed!")
          dial("Katherine","WHAT?!?!")
          dial("Jessika","Shocking, I know.")
          dial("Katherine","D- did his plot armor run out? What happened?")
          dial("Gloria","According to Ms. Presley...")
          dial("Gloria","At the end of school yesterday, as Peter was boarding bus 4996, he found himself approached by a remarkably confident Valeria.")
          dial("Gloria","Valeria taunted Peter by discretely snaching his unfinished AoPS homework straight from the confines of his backpack.")
          dial("Gloria","Peter, upon realizing that his homework was nowhere on him, collapsed to the ground, dead.")
          dial("Katherine","...")
          dial("Katherine","He died from lack of... homework?")
          dial("Sherry","To be fair, the same would probably happen to you.")
          dial("Katherine","...")
          dial("Katherine","Hang on-")
          dialNoSpeaker("Katherine turns to you.")
          dial("Katherine","{}, you remember what Poorvi showed us yesterday, right? The P.L.A.N.T?".format(player.name))
          dial("Lillian","The... what?")
          dial("Katherine","The Perceptive Life-Awakening Nexus of Transpiration!")
          dialNoSpeaker("Katherine pulls out an Engineering Notebook from her backpack and flips to an arbitrary page.")
          dial("Lillian","... you're in engineering?")
          dial("Katherine","Wha- of course not! This is Ellie's, she let me borrow her notebook!")
          dial("Katherine","On the bus ride home yesterday, I was intrigued about the revival machine Poorvi created.")
          dial("Gloria","Revival machine?")
          dial("Katherine","Yup! After much thought and deliberation I managed to reverse engineer the core concept!")
          dial("Katherine","Here's my prototype!")
          dialNoSpeaker("Katherine flips over her Engineering Notebook, revealing to everyone a well-drawn sketch of the P.L.A.N.T.")
          dial("Anna","... you.... even... added tonal shading.")
          dial("Sherry","Katherine... this is perfect.")
          dial("Katherine","I'm always perfect. ^-^")
          dial("Katherine","Additionally, *(Katherine flips over to the next page)* I also added a bill of materials!")
          dial("Lillian","So you're saying, if we collect all those parts then we can revive Peter?")
          dial("Katherine","Pretty much!")
          dialNoSpeaker("The mortals crowd around the door, discussing extensivly on a way to recreate the P.L.A.N.T device using Katherine's engineering prowess.")
          dial("Katherine","Knew that would come in handy!")
          dialNoSpeaker("...")
          dialNoSpeaker("You try to include youself in the discussion.")
          dial("Katherine","Everyone understand?")
          dial("Anna","May you recap?")
          dial("Katherine","Sure!")
          dial("Katherine","Jashlee and Anna will collect all the Arduino circuitry in the Engineering Classroom.")
          dial("Jashlee","Not engineering. TwT")
          dial("Katherine","Jessika will scour an Aloe Vera Succulent, since from my knowledge, Poorvi stole the only one from Ellie.")
          dial("Katherine","Lillian will try and hunt down a waterproof adhesive to glue the circuitry to the base of the Aloe Vera.")
          dial("Katherine","Brooke will try to find a ruler and dial caliper to ensure the device contains precise measurements.")
          dial("Katherine","(After all, anything beneath or above the exact measurement will not be tolerated!)")
          dial("Katherine","Sherry will-")
          dial("Sherry","Hang on Katherine...")
          dial("Katherine","What is it?")
          dial("Sherry","I may or may not have a Table Tennis Tournament to attend to...")
          dial("Katherine","But... Sherry... don't you want to see your friend again?")
          dial("Sherry","I mean... it is Peter after all...")
          dial("Sherry","He's not even that good at volleyball!")
          dial("Sherry","I won't miss him that much.")
          dial("Katherine","._.")
          dial("Sherry","...")
          dial("Sherry","I guess I could construct a rabbit joint using the wooden trophy I get as a prize for winning.")
          dial("Katherine","...") 
          dial("Katherine","Well that works...")
          dial("Katherine","...")
          dial("Katherine","Where was I?")
          dial("Katherine","Oh right.")
          dial("Katherine","And lastly, {} and I will monitor everyone's progress!".format(player.name))
          dial("Anna","Sounds good!")
          dial("Gloria","Uh... what about me?")
          dial("Katherine","Uh, you can stay in Room 113 and start constructing/testing the device to ensure in meets the engineering requirements!")
          dial("Gloria","Sounds good! :)")
          dialNoSpeaker("You use the Teacher's Pass to unlock the door, letting all the mortals in as they rush to collect their respective materials.") 
          dial("Katherine","You ready, {}? Peter's counting on us!".format(player.name)) 
          dialNoSpeaker("You nod your head.")
          dial("Katherine","We got this! ^-^") 
          player.addFlag("Entrance_Int1_KatherineEngineeringMoment")
          player.addFlag("Entrance_Int1_KatherineCreatesAPlan")
          player.loc = ["MAIN_ENTRANCE", "ENTRANCE_HALLWAY_8"]
          player.classroom = None
        else:  
          dialNoSpeaker("You use the Teacher's Pass to unlock the door and enter the school.")
          player.loc = ["MAIN_ENTRANCE", "ENTRANCE_HALLWAY_8"]
          player.classroom = None      
      else:
        dialNoSpeaker("You use the Teacher's Pass to unlock the door and enter the school.")
        player.loc = ["MAIN_ENTRANCE", "ENTRANCE_HALLWAY_8"]
        player.classroom = None
    else:
      dialNoSpeaker("The door's locked.")
      dialNoSpeaker("Looks like Ms. Presley fixed the lock on the door to be less breakable.")
      dialNoSpeaker("You'll have to find another way in...")
      player.incrementTime(-2)
      player.classroom = None
    
class MainOfficeClassroom(Classroom):
  def __init__(self):
    self.name = "The Main Office"
    self.locked = [1, 2, 3]
    
class CafeteriaClassroom(Classroom):
  def __init__(self):
    self.name = "The Cafeteria"
    self.locked = [1]

  def run(self, player):
    clear()
    printBoxedText("The Cafeteria")
    print() 

    printC("You enter the Cafeteria... the floor is a bit... dirty.")
    print()
    printC("You can spot Edem eating his lunch peacefully, Brandon V with comically large sodas, and Caleb speedcubing.")
    choice = dropdownMenu("What do you do?",["Talk to Edem.","Ask Brandon V about the sodas.","Watch Caleb speedcube.","Leave the classroom."])
    if choice == 1:
      if player.hasFlag("Cafe_Int1_EdemGenshinImpact") == False:
        dial("Edem","Oh hey!")
        dial("Edem","Wanna hear a funny story?")
        choice = dropdownMenu(None,["Of course!","\"Nah I'm good.\" - Valeria"])
        if choice == 1:
          dial("Edem","Recently, someone sent me a voice recording claiming to be my Great Nigerian Uncle.")
          dial("Edem","He offered me a Nintendo Switch and Breath of The Wild: Tears of The Kingdom.")
          dial("Edem","Since my parents sold my old Nintendo, I was eager to send him my social security number and email.")
          dial("Edem","...")
          dial("Edem","I ended up receiving a Genshin Impact: Collector's Edition Box...")
          dial("Edem","...")
          dial("Edem","It also came with this red flower...")
          dialNoSpeaker("Edem pulls out a red succulent.")
          dial("Edem","I was gonna give it to Goran but... I guess you can have it.")

          player.giveItem(RedEcherviaSucculentItem)
          printFlair("You receive a Red Echervia Succulent!")
          
          dial("Edem","...                                ")
          dial("Edem","I hate Genshin Impact.")
          dial("Rachel","WHAT!")
          dialNoSpeaker("Rachel approaches the two of you.")
          dial("Rachel","Did I just hear the most |R|APPALLING|B|, most |G|HORRIFIC|B|, most |Y|DREADFUL|B|-")
          dial("Edem","Yes you did.") # gameshow done, you need to implement the claiming gorilla glue interaction tho
          dial("Rachel","...")
          dial("Rachel","You have dissapointed me today Edem...")
          dial("Rachel","I will have to consult my fellow SGA affiliate, Sofya Ro, to discuss this matter in private.")
          dial("Edem","...")
          dial("Edem","... Sofya?")
          dial("Rachel","Sofya Ro has an elementary, middle, and high school named after her in Georgia.")
          dial("Rachel","What about you?")
          dial("Edem","...                      ")
          dial("Edem","There's a business university in Spain named after me...")
          dial("Edem","...")
          dial("Edem","... it also sucks.")
          dial("Rachel","Precisely.")
          player.addFlag("Cafe_Int1_EdemGenshinImpact")
        elif choice == 2:
          dial("Edem","That's fine...")
      else:
        dial("Edem","I don't like Genshin Impact.")
        dial("Rachel","...")
    elif choice == 2:
      if player.hasFlag("Cafe_Int2_BrandonVSodaAbundance") == False:
        dialNoSpeaker("You approach Brandon V and ask him about the abundance of sodas in his backpack.")
        dial("Brandon V","These?")
        dialNoSpeaker("Brandon V pulls out a multitude of cans, each with a unique flavor.")
        dialNoSpeaker("You nod your head in agreeance.")
        dial("Brandon V","I'm selling each for a dollar a piece.")
        dial("Brandon V","Don't worry, I accept tickets as well.")
        player.addFlag("Cafe_Int2_BrandonVSodaAbundance")
      dial("Brandon V","Wanna buy some?")
      choice = dropdownMenu(None,["Sure!","Nah, I'm good."])
      if choice == 1:
        runShop([(CokeSodaItem,50,False),(OrangeFantaSodaItem,75,False),(PineappleFantaSodaItem,50,False),\
                 (SpriteSodaItem,50,False),(IcedTeaSodaItem,50,False)], "Brandon's Beverage Bargains", "B", player)
    elif choice == 3:
      if player.hasFlag("Cafe_Int3_CalebSpeedcubing") == False:
        dialNoSpeaker("You watch Caleb ferociously twist and turn the cube of multiple colors before abruptly plopping down a solved cube.")
        dial("Caleb","Yes! A 4.16s solve is my new personal best!")
        dialNoSpeaker("Caleb notices you.")
        dial("Caleb","Who are you?")
        dial("Caleb","Hang on, let me test how unintelligent you are.")
        dial("Caleb","What is the Law of Cosines?")
        choice = dropdownMenu(None,["a^2=b^2+c^2-2bc(cosA)","I have no idea, ask Pilliam Wark."])
        if choice == 1:
          dial("Caleb","Oh, guess you aren't academically challenged at all.")
          dial("Caleb","I hereby grant you a permit to watch me speedcube.")
          dial("Caleb","Your welcome.")
          dialNoSpeaker("Caleb starts speedcubing again and gets a pathetic 5.89s solve.")
          dial("Caleb","Darn.")
          dialNoSpeaker("Caleb turns back to you.")
          dial("Caleb","Do you Speedcube?")
          dial("Caleb","Granted, you probably perform way worse than me.")
          dial("Caleb","...")
          dial("Caleb","Want cube lubricant? I have plenty hoarded up from TheCubicle.com.")

          player.giveItem(SpeedcubeLubeItem)
          printFlair("You Receive Speedcube Lubricant from Caleb.")
          
          dial("Caleb","Be sure to apply that lubricant to your cube at least once a month to ensure hasty solves.")
          dial("Caleb","No need to thank me, I've gotten acustomed to my own generosity.")
          player.addFlag("Cafe_Int3_CalebSpeedcubing")
        elif choice == 2:
          dial("Caleb","Imagine having to rely on other people's intelligence.")
          dial("Caleb","Couldn't be me.")
      else:
        dial("Caleb","Practice enough and you may even get better times than me.")
        dial("Caleb","Although, that's statistically unlikely.")
      
    elif choice == 4:
      player.classroom = None
      return
    

class NursesOfficeClassroom(Classroom):
  def __init__(self):
    self.name = "The Nurse's Office"
    self.locked = []

  def run(self, player):
    clear()
    printBoxedText("The Nurse's Office")
    
    if player.justPerished:
      player.justPerished = False
      dialNoSpeaker("You suddenly find yourself in the nurse's office...")
      if player.act == 1 and player.questProgressIsAtLeast(IronicCriminalPursuitQuest, 5):
        dial("Katherine", "You alright? That last spell must have hurt a lot.")
        dial("Nurse", "Don’t worry, they’re all stitched back together...")
        dial("Nurse", "By the way, |LB|Katherine|B|, thanks for the tip of tickets. Don't usually get those around here.")
        dial("Peter", "But all you did was use an ice pack on them...")
        dial("Nurse", "*(Ignoring Peter)* Good luck out there!")
      else:
        dial("Nurse", "You alright? That last spell must have hurt a lot.")
        dial("Nurse", "Don’t worry, you’re all stitched back together.")
        dial("Nurse", "I would take some tickets as a price, but you were kind of unconscious, and that would be stealing, so...")
        dial("Nurse", "Consider leaving a tip, would ya?")
      player.classroom = None
    else:
      printC("You're in the nurse’s office, hoping for any ailments to subdue your vitamin D deficiency.")
      printC("\n|R|Nurse|B|: Well, what are you in for today?")

      choice = dropdownMenu("What will you do?", ["Request Healing", "Ask a question", "Leave the classroom"])
      if choice == 3:
        player.classroom = None
        return
      elif choice == 2:
        dial("Nurse", "Fine, but make it quick.")
        choice = dropdownMenu("Ask a question...", ["I thought spell battles didn't injure you...", "How many spell battles have I lost?", "Actually, never mind."])
        if choice == 1:
          dial("Nurse", "Yep, that's right.")
          dial("Nurse", "Actually, that's a good question. Why *are* you in here for spell injuries?")
          dial("Nurse", "Let me check your medical info.")
          dialNoSpeaker("The Nurse returns to their desk and checks something on their computer.")
          dial("Nurse", "Oh, of course, of course.")
          dial("Nurse", "It appears you have a rare medical condition that leads to |W|increased sensitivity to magic|B|.")
          dial("Nurse", "This makes it so that you can cast spells more accurately than other students, but spell damage will hit you harder.")
          dial("Nurse", "... what do you mean, \"why is magic still allowed in this school?\"")
          dial("Nurse", "I mean it's not like we can just \"cancel\" spells...")
          dialNoSpeaker("|DG|The Nurse not-so-discreetly tears a poster labelled \"2019 Magnet 8th Grade Boston Trip\" off the wall.")
          dial("Nurse", "... spells were the *main selling point* of this school, after all, and we're not going to just cancel it.")
          if player.act == 1 and player.questProgressIsAtLeast(IronicCriminalPursuitQuest, 5):
            dial("Katherine", "...")
            dial("Peter", "...")
          dialNoSpeaker("You give the Nurse a dirty look.")
          dial("Nurse", "What?")
        elif choice == 2:
          dial("Nurse", "Hm? Let me check the records.")
          dialNoSpeaker("The Nurse returns to their desk and checks something on their computer.")
          dial("Nurse", "Looks like you've been here for critical spell-related injuries |W|{}|B| times...".format(player.deaths))
          if player.deaths == 0:
            dial("Nurse", "Wow, props to you for being safe out there.")
          elif player.deaths < 4:
            dial("Nurse", "Don't worry, it happens to the best of us from time to time.")
          elif player.deaths < 20:
            dial("Nurse", "Maybe be a bit more careful out there...")
          elif player.deaths < 1000:
            dial("Nurse", "Ouch, that's gotta hurt. Do you want a lollipop?")
            dial("Nurse", "Oh wait, I ran out of them...")
          else:
            dial("Nurse", "Okay, that's just impressive at this point.")
            dial("Nurse", "Are you sure you don't need to visit a doctor?")
        elif choice == 3:
          dial("Nurse", "...")
          dial("Nurse", "Quit wasting my time.")
        enter()
        return
      elif choice == 1:
        if player.health == player.getMaxHealth():
          dial("Nurse", "What? You're perfectly fine.")
          dial("Nurse", "Trust me, don't try to fake an injury to get out of school. It won't work.")
        else:
          toHeal = player.getMaxHealth() - player.health
          price = toHeal // 5 + 20
          if player.hasFlag("Nurses_PerishDebtUnpaid"):
            price += 50
          if not player.hasFlag("Nurses_TicketPricing"):
            player.addFlag("Nurses_TicketPricing")
            dial("Nurse", "Alright, I can heal you for |R|{}|B| health.".format(toHeal))
            dial("Nurse", "I usually do it for free...")
            dial("Nurse", "But I've seen y'all use these \"tickets\" for purchasing stuff around here.")
            dial("Nurse", "Maybe if I start charging them for healing, people will stop coming in here so often.")
            dial("Nurse", "Plus, I could probably get myself a couple of coffees for free.")
            dial("Nurse", "I'll do it for, say, |W|{}|B| tickets, whadd'ya think?".format(price))
          else:
            dial("Nurse", "For |W|{}|B| tickets, I can heal you for |R|{}|B| health.".format(price, toHeal))
          choice = dropdownMenu("You have |W|{}|B| tickets. Pay |W|{}|B| of them for healing?".format(player.tickets, price), ["|G|Okay", "|R|No way"])
          if choice == 1:
            if player.takeTickets(price):
              player.health = player.getMaxHealth()
              dialNoSpeaker("You paid the Nurse |W|{}|B| tickets.".format(price))
              dialNoSpeaker("In return, the Nurse applies an ice pack to your head.")
              dial("Nurse", "Alright, you're good to go.")
              if player.act == 1 and player.questProgressIsAtLeast(IronicCriminalPursuitQuest, 5):
                dial("Peter", "But all you did was use an ice pack on them...")
              dial("Nurse", "~~Glory to the American Healthcare System-~~ I mean, come again soon!")
              if player.hasFlag("Nurses_PerishDebtUnpaid"):
                player.removeFlag("Nurses_PerishDebtUnpaid")
                dialNoSpeaker("|DG|*The 50 ticket tax on healing has been removed.*")
            else:
              dial("Nurse", "Wow, you're poor.")
              dial("Nurse", "That kind of sucks.")
              dial("Nurse", "Come back with more tickets!")
          else:
            dial("Nurse", "Suit yourself.")
        enter()
        return

      
class Room251Classroom(Classroom):
  def __init__(self):
    self.name = "Room 251"
    self.locked = [1, 2, 3, 4, 5]

class Room252Classroom(Classroom):
  def __init__(self):
    self.name = "Room 252"
    self.locked = [1, 2, 3, 4, 5]

class Room248Classroom(Classroom):
  def __init__(self):
    self.name = "Room 248" 
    self.locked = [1, 2, 3, 4, 5]

class Room241Classroom(Classroom):
  def __init__(self):
    self.name = "Room 241 - Goran's Spellshop"
    self.locked = []

  def run(self, player):
    # Clear the map
    clear()

    # Boxed text for room name
    printBoxedText("Room 241 - Goran's Spellshop")
    print() 

    printC("You enter Goran's spellshop, it's a bit murky...")

    
    if not player.hasFlag("241_Int1_BeenToGoranSpellshop"):
      dial("Goran","Greetings {}!".format(player.getName()))
      dial("Goran","If you ever need any new spells to upgrade your arsenal, here's the place to stop by!")
      player.addFlag("241_Int1_BeenToGoranSpellshop")
      return

    shops = [
      ["Buy Act I Spells", 1, [ChrisSpell, PrestonSpell, AriamSpell, GoranSpell, JustinSpell]],
      ["Buy Act II Spells", 2, [AadhavanSpell, RyanSpell, DashaSpell, HenrySpell, KedusSpell, TylerSpell, BenedicteSpell]],
      ["Buy Act III Spells", 3, [DonSpell, PercySpell, BrandonVSpell, LukeSpell, SergiSpell, TerenceSpell, EdemSpell, NathanSpell]],
      ["Buy Act IV Spells", 4, [AaryaSpell, RoselynSpell, BrookeSpell, GabrielleSpell, JessikaSpell, SherrySpell, AnnaSpell, SofyaSpell]],
      ["Buy Act V Spells", 5, [PoorviSpell, KatherineSpell, ValeriaSpell, EllaSpell, EllieSpell]]
    ]

    actions = []
    for shop in shops:
      if shop[1] <= player.act:
        actions.append(shop[0])
    actions.append("Leave the shop")

    choice = dropdownMenu("What will you do?", actions)
    
    if choice == len(actions):
      player.classroom = None
      return

    shopToConvert = shops[choice-1][2]
    spellshopConverted = []
    price = [100, 200, 300, 400, 500][choice-1]
    
    for spell in shopToConvert:
      spellshopConverted.append([spell, price, True])
      
    runShop(spellshopConverted, "Goran's Spellshop", "B", player)

class Room242Classroom(Classroom):
  def __init__(self):
    self.name = "Room 242 - Rock Band"
    self.locked = [1, 2, 3, 4, 5]

class Room246Classroom(Classroom):
  def __init__(self):
    self.name = "Room 246 - Mr. Rea, Band & Orchestra"
    self.locked = [1, 2, 3, 4, 5]

class BuildingServicesClassroom(Classroom):
  def __init__(self):
    self.name = "Building Services Closet"
    self.locked = [1, 2, 3, 4, 5]

class Room235Classroom(Classroom):
  def __init__(self):
    self.name = "Room 235 - Ms. Lee, Engineering"
    self.locked = []

  def run(self, player):

    if player.act == 1:
      if player.questProgressIsAtLeast(IronicCriminalPursuitQuest, 5) and player.hasFlag("235_Int1_KatherinePeterStayBehind") == False:
        dial("Peter","... may we stay behind?")
        dial("Katherine","Yeah, I don’t want to be plagued with eternal OnShape torture. Sorry.")
        player.addFlag("235_Int1_KatherinePeterStayBehind")
        clear()
      clear()
      printBoxedText("Room 235 - Ms. Lee's Engineering Classroom")
      print() 
      printC("You're in the Engineering Classroom, as you enter, a wave of fear and anxiety washes over you.")
      player.sendEmail(IEDOverdoseEmail)
  
      if player.hasFlag("235_Int1_MsLeeIntroduction") == False:
        dialNoSpeaker("Ms. Lee greets you as you enter the classroom.")
        dial("Ms. Lee","Hello! Are you here for engineering?")
        choice = dropdownMenu(None,["Yes, I am.","Nah, I'm good."])
        if choice == 1:
          dial("Ms. Lee","That’s wonderful! I’m your substitute teacher!") 
          dialNoSpeaker("Ms. Lee looks around the classroom.")
          dial("Ms. Lee","In seems that you and Chris are the only two students present today.")
          dial("Jashlee","...")
          dial("Jashlee","Ms. Lee?")
          dial("Ms. Lee","My mistake, I couldn’t see you all the way down there.")
          dial("Jashlee",".-.")
          dial("Ms. Lee","So that’s three people. Where's everyone else?")
          dial("Jashlee","I do recall seeing some students in the media center, not sure about everyone else.")
          dial("Ms. Lee","*(Sigh)* It’s alright, a class with fewer people is always more fun.")
          player.addFlag("235_Int1_MsLeeIntroduction")
          return
        elif choice == 2:
          dial("Ms. Lee","So you’re telling me that you came all the way over here just to leave?")
          dial("Ms. Lee","Oh well.")
          dialNoSpeaker("You leave the classroom.")
          if player.questProgressIsAtLeast(IronicCriminalPursuitQuest, 5): 
            dial("Peter","You’re back already? What was even the point of going in there?")
          player.classroom = None
          return
          
      choice = dropdownMenu("What do you do?",["Talk to Jashlee.","Talk to Chris.","Drink from the water fountain.","Leave the classroom."])    
      if choice == 1:
        if player.hasFlag("235_Int1_JashleeCardTrick") == False:
          dial("Jashlee","Hello, I’m just practicing a card trick that Peter showed off to me.")
          dial("Jashlee","It’s supposed to make the card change suits, but Peter's lack of skill led to him stabbing his own eye with the wrong card.")
          dial("Jashlee","I’ve decided to practice this trick to show to my friends that I am capable of many things, despite my small stature.")
          dialNoSpeaker("Jashlee holds up some cards face up.")
          dial("Jashlee","Here, pick a card from this deck.")
          while True:  
            choice = dropdownMenu(None,["The Two of Spades.","The Three of Diamonds.","The Eight of Clubs.","The Queen of Hearts."])
            if choice == 2:
              dial("Jashlee","Alright, you should remember your card’s suit and number.")
              dial("Jashlee","Got it?")
              dial("Jashlee","Now hand me back the card.")
              dialNoSpeaker("You hand Jashlee back the card.")
              dial("Jashlee","Okay, now check your pocket.")
              dialNoSpeaker("You slowly reach into your pocket and pull out a card...")
              dialNoSpeaker("... it's the Two of Hearts.")
              dial("Jashlee","...")
              dial("Jashlee","Chris... you put the wrong card in their pocket.")
              dial("Chris","Sorry man, I wasn't paying attention.")
              dial("Jashlee","*(Sigh)* At least I’m a better magician than Peter.")
              player.addFlag("235_Int1_JashleeCardTrick")
              break
            else:
              dial("Jashlee","My trick doesn't work with that card, choose another one.")
        else:
          dialNoSpeaker("Jashlee seems to still be practicing her card trick...")
      elif choice == 2:
        if player.hasFlag("235_Int2_ChrisMonkeyKart8Deluxe") == False:
          dial("Chris","Hey man! What’s up?")
          dial("Chris","I’m just playing some Monkey Kart 8 Deluxe on my phone. Want to watch?")
          choice = dropdownMenu(None,["Sure, sounds interesting!","Nah, I'm good."])
          if choice == 1:
            dial("Chris","Okay man.")
            dial("Chris","If you’re wondering, I found this game on some sketchy Chinese website.")
            dial("Chris","Don’t worry, I’ve done this many times and my phone still hasn’t been compromised.")
            dial("Chris","Anyways, in this game, you get to play as a monkey trying to collect all the bananas on the map.")
            dial("Chris","I’m playing as this monkey called Joe, he’s super strong and has five million power in Rise of Kingdoms.")
            dial("Chris","His ability is Banana Barrage, which consumes five of your collected bananas but stuns every other monkey within a fifty-block radius of Joe for 10 seconds, with a 30-second cooldown. It’s really helpful for claiming large banana groves because the five-banana stun cost lets you collect the groves of 20 bananas without any competition...")
            dialNoSpeaker("As Chris continues to blabber about Monkey Kart 8 Deluxe, you slowly daze out of the conversation.")
            dial("Chris","Hello? Have you been paying attention?")
            dial("Chris","Answer this question: Say I’m a Power Level 9 Joe trying to get a grove of exactly 33 ripe bananas and 2.4 rotten bananas, but there are three Power Level 2 Steves, each twice as far away from the banana trees. If both monkeys have the same average velocity, but activate the Better Together buff once there are 1.8 rotten bananas on said banana tree within the super charging radius, at what point do they both intercept each other in respect to the banana tree?")
            choice = dropdownMenu(None,["Near Vitamin B6 Town.","Near the Haunted Boo-nana Mansion.","Near Yellow Mello Caverns.","Near Makemake"])
            if choice == 4:
              dial("Chris","Make-Make? Where’s that? Well anyway, that’s wrong!")
            else:
              dial("Chris","That’s wrong!")
            dial("Chris","Seriously man, I gave you the secret to winning every Monkey Kart 8 Deluxe game and even a Raid Shadow Monkeys promo code, and yet you don’t pay attention.")
            dial("Chris","Take this!")
            
            if not runBattle(player, ChrisBattleStudent()):
              return
            
            dial("Chris","Aw man.")

            player.giveTickets(50)
            printFlair("You earned 50 tickets from the battle!")
            
            player.addFlag("235_Int2_ChrisMonkeyKart8Deluxe")
          elif choice == 2:
            dial("Chris","It’s okay man, you can always watch me play Super Monkey Bros next time.")
        else:
          dialNoSpeaker("Chris is still playing Monkey Kart 8 Deluxe. -_-")
          dialNoSpeaker("*(Seriously? What is the appeal of that game?)*")
      elif choice == 3:
        if player.hasFlag("235_Int3_DrinkFromFountain") == False:
          dialNoSpeaker("You approach the disgusting water fountain...")
          dial("Ms. Lee","I wouldn't recommend drinking from there... the taste was a bit nauseating.")
          dial("Jashlee","You drank from there?")
          dial("Ms. Lee","Being in the presenence of this classroom makes me quench my thirst.")
          dial("Jashlee","Yikes.")
          choice = dropdownMenu("Do you drink from the fountain?",["Yes, I love water!","Nah, I'd rather be dehydrated."])
          if choice == 1:
            dialNoSpeaker("You drink from the water fountain, the taste is a bit tangy but other than that, completely harmless.")
            dial("Jashlee","...")
            dial("Jashlee","Maybe we're just overreacting.")
            dial("Ms. Lee","It seems so.")
            player.addFlag("235_Int3_DrinkFromFountain")
        else:
          dialNoSpeaker("You drink from the water fountain, the taste is a bit tangy but other than that, completely harmless.")
      elif choice == 4:
        dial("Ms. Lee","See you again!")
        if player.questProgressIsAtLeast(IronicCriminalPursuitQuest, 5) and player.hasFlag("235_Int4_KatherinePeterMafia") == False:
          dialNoSpeaker("You leave the classroom.")
          dial("Katherine","Huh? Oh hey, you’re back!")
          dial("Katherine","Peter and I have been playing Mafia in your absence, turns out, it doesn’t work that well with two people.")
          dial("Peter","Tell me about it.")
          player.addFlag("235_Int4_KatherinePeterMafia")
        player.classroom = None
        return
        
    elif player.act == 2:
      clear()
  
      printBoxedText("Room 235 - Ms. Lee's Engineering Classroom")
      print() 
      
      # Classroom Description
      printC("You're in the Engineering classroom, Ms. Lee seems to be substituting.")
      print()  
      printC("Adrenaline surges through your body as you stare at the numerous posters on the wall.")
      print()
      printC("Ms. Lee is hosting a lesson on tonal shading, your favorite subject.")
      interaction = None
      if not player.hasFlag("235_Int1_LeeTonalShadingAssignment"): 
        interaction = "Engage in the lesson."
      else: 
        interaction = "Pester the IED students."

      choice = dropdownMenu("What do you do?",[interaction,"Commit Katherine on the class.","Leave the classroom."])
      if choice == 1:
        if not player.hasFlag("235_Int1_LeeTonalShadingAssignment"):
          dialNoSpeaker("You decide to engage in the tonal shading lesson.") 
          dial("Ms. Lee","There are multiple different tonal shading methods!")
          dial("Ms. Lee","The most common include hatching, cross-hatching, stippling, scribbling, and circling.")
          dial("Chris","Aren't those just fancy names for techniques that result in the same end product?")
          dial("Ms. Lee","Well- uh- I didn't get enough clarification in the sub plans.")
          dial("Ms. Lee","I'm sure studying all of them will be crucial for the end of year, final exam.")
          dial("Akash","Uh- sure.") 
          dial("Ms. Lee","Just do your assignment. -_-")
          dial("Chris","And that is?")
          dial("Ms. Lee","Each of you must chose an object in this room and sketch it using a tonal shading technique.")
          dial("Ms. Lee","The sub plans explicity mentioned that all students MUST use the best front view of that object.")
          dial("Ms. Lee","Whatever that means.")
          dial("Akash","Great. -_-")
          dial("Ms. Lee","If you need any assistance you may ask me!") 
          dial("Ms. Lee","But just remember that I'm a math teacher, not a \"read-directly-from-the-nearpod\" teacher.")
          player.addFlag("235_Int1_LeeTonalShadingAssignment")
        else:
          choice = dropdownMenu("Who do you pester?",["Chris","Akash"])
          if choice == 1:
            dialNoSpeaker("You ask Chris what object he's drawing.")
            dial("Chris","I'm drawing Nathan!")
            dial("Chris","I might have to use multiple pencils to make it visually accurate.")
          elif choice == 2:
            if not player.hasFlag("235_Int1_AkashBattleSucculent"):
              dialNoSpeaker("You ask Akash what object he's drawing.")
              dial("Akash","Oh- uh-")
              dial("Akash","Shoot, my crippling social anxiety is preventing me from speaking normally without stuttering.")
              dial("Akash","Uh- I'm just drawing- uh- a lavender succulent.")
              dial("Akash","Because- I- uh- have a fascination with the color lavender.")
              dial("Akash","Does that make sense? I hope so.")
              dialNoSpeaker("You ask Akash if could have the succulent.") # you don't have to personally attack yourself THAT much   
              dial("Akash","But- but I need it for the- the- tonal shading- uh- assignment.") 
              dialNoSpeaker("You pester him once more.")
              dial("Akash","Well I- I- I-")
              dial("Akash","I kinda need it.")
              dial("Akash","Why- why- why don't you...")
              dial("Akash","Uh- what's the right word- I'm so bad at vocabulary.")
              dial("Akash","Uhh- I guess we can- uh- battle?")
              dial("Akash","Just to uh- settle these matter in a very- uh- non-civilized way.")
              dial("Akash","I hope.")

              if not runBattle(player, AkashBattleStudent()):
                return
                
              dial("Akash","I guess I can- uh- use- a- compass?")
              dial("Akash","That might work.")
              player.giveItem(LavenderEcherviaSucculentItem)
              printFlair("You Receive a Lavender Echervia Succulent!")
              player.addFlag("235_Int1_AkashBattleSucculent")
            else:
              dial("Akash","Not gonna lie, this compass is way easier to draw than that succulent.")
              dial("Akash","Thank you for opening my eyes to laziness.")
            
            
      elif choice == 2:
        dial("???","No.")
        dial("???","As your moral compass, I request that you don't consider such heinous acts of violence.")
      elif choice == 3:
        player.classroom = None
        return

    elif player.act == 3:

      dialNoSpeaker("Before you enter the classroom, you can spot Jashlee and Anna nervously standing by the door.")
      dial("Katherine","Hey you two! How's it-")
      dial("Jashlee","Shush, be quiet Katherine.")
      dial("Katherine","Huh, what is it?")
      dial("Jashlee","You don't want them to hear you, do you?")
      dial("Katherine","Wait, what's going on?")
      dial("Anna","*(Sigh)* Today's the end of course, final exam, and the two of us haven't studied at all!")
      dial("Katherine","Oh, that's unfortunate. Can't be that bad, can it?")
      dial("Jashlee","Of course it's bad! Pilliam Wark's been studying for it since last year and even he's stressed out.")
      dial("Katherine","Yikes.")
      dial("Katherine","...")
      dial("Katherine","But- but how else will we get those Arduino parts?")
      dial("Anna","Jashlee and I were considering wearing disguises but we haven't come across any!")
      dial("Jashlee","At this point we're considering putting paper bags on our heads!")
      dial("Jashlee","...")
      dial("Jashlee","Actually, that's a good idea.")
      dial("Anna","Jaaaassshhhlleeee, you should've thought of that earlier!")
      dial("Jashlee","I'm sorry, I was too concentrated staying alert of the oncoming-")
      dial("Jashlee","Ooh, what's this, a registration form for a Hindi club?")
      dial("Anna","*(Sigh)*")
      dialNoSpeaker("Anna turns to you.")
      dial("Anna","I don't think Jashlee's short term attention span will be of much help, may you two perhaps look for some paper bags large enough to conceal our faces?")
      dial("Katherine","Oh, sure thing!")
      dial("Anna","Thanks! :)")
      
      
      clear()
  
      printBoxedText("Room 235 - Ms. Lee's Engineering Classroom")
      print() 

class Room236AClassroom(Classroom):
  def __init__(self):
    self.name = "Room 236A - Ms. Ramasamy, Computer Science"
    self.locked = []

  def run(self, player):
    if player.act == 1:
      clear()
  
      printBoxedText("Room 236A - Ms. Ramasamy's Computer Lab")
      print() 
      
      # Classroom Description
      printC("You're in Ms. Ramasamy's room, the 8th grade computer lab.")
  
      interactions = []
      if player.questProgressIsAt(IronicCriminalPursuitQuest, 1):
        print()
        printC("You can see Katherine having an argument with Ms. Ramasamy in the corner of the room.")
        interactions = ["Eavesdrop on the argument"]
      elif player.questProgressIsAt(IronicCriminalPursuitQuest, 2):
        print()
        printC("Katherine's still in the room.")
        interactions = ["Talk with Ms. Ramasamy", "Talk with Katherine"]
      elif player.getQuestProgress(IronicCriminalPursuitQuest) in [3, 4]:
        print()
        interactions = ["Talk with Ms. Ramasamy"]
      elif player.questProgressIsAt(IronicCriminalPursuitQuest, 5):
        print()
        printC("Before you open the door, you can hear voices coming from inside...")
        interactions = ["Open the door"]
      elif player.getQuestProgress(IronicCriminalPursuitQuest) in [6, 7]:
        print()
        printC("Poorvi, Ella, and Ellie’s voices can be heard from the other side of the door, along with another, unfamiliar voice.")
        interactions = ["Unlock the door"]
      elif player.questProgressIsAt(IronicCriminalPursuitQuest, 8): 
        print()
        printC("There's a \"surprise\" waiting in the classroom...")
        interactions = ["Investigate the \"surprise\""]
  
      choice = dropdownMenu("What will you do?", interactions + ["Leave the classroom"])
      if choice == len(interactions) + 1:
        player.classroom = None
        return
        
      if player.questProgressIsAt(IronicCriminalPursuitQuest, 1): # Interaction I
        dial("Ms. Ramasamy","I’m sorry Katherine, I can’t allow you to retake the quiz since it won’t be fair to anyone else.")
        dial("Katherine","But- but why? I can’t be seen with a grade below a hundred, it’ll ruin my three-year streak!")
        dial("Ms. Ramasamy","A 24/25 isn’t going to kill you, besides, you should be focusing more on getting As, not getting hundred percents.")
        dial("Katherine","I beg to differ, all I messed up on was input validation!")
        dial("Ms. Ramasamy","All input validation is going to tell you is that, even without a hundred, you’re going to be just fine.")
        dial("Katherine","But... perfectionism?")
        dial("Ms. Ramasamy","You’re not perfect, you messed up on input validation.")
        dial("Katherine","._.")
        dial("Ms. Ramasamy","And that’s alright, no one’s going to judge you.")
        dial("Rachel","Except for me!")
        dialNoSpeaker("Rachel and Sofya barge their way into the classroom.")
        dial("Ms. Ramasamy","...")
        dial("Ms. Ramasamy","Are you two here to ask about your grades as well?")
        dial("Rachel","What? Of course not! Our grades are perfect!")
        dial("Rachel","Me and Sofya were having a wonderful day when we heard the most appalling words coming from your room! ")
        dial("Ms. Ramasamy","...")
        dial("Ms. Ramasamy","Input validation?")
        dial("Rachel","No! It seems that Katherine here got a 24/25")
        dial("Sofya","A 24/25? That's still an A, great job Katherine-")
        dial("Rachel","NO! She's supposed to get a perfect score!")
        dial("Sofya","I mean...")
        dial("Sofya","... it's still a pretty good grade!")
        dial("Katherine","Thanks!")
        dial("Rachel","But.. isn't she part of the Media Center Crew? Everything she does is supposed to be perfect!")
        dial("Sofya","But-")
        dial("Rachel","She hasn't even submitted her payments yet for the school dance! They're overdue by two months!")
        dial("Katherine","I mean, all you're spending them on is licensing rights for BTS songs.")
        dial("Rachel","Of course!")
        dial("Rachel","BTS is my lord and savior, I want to support them!")
        dial("Katherine","BTS isn't even that good!")
        dialNoSpeaker("A sudden gasp echoes through the classroom.")
        dial("Rachel","...")
        dial("Katherine","I'd rather listen to Scheming Weasel by Kevin MacLeod.")
        dial("Sofya","Uhh... maybe that wasn't the best choice of words, given who you're talking to.")
        dial("Rachel","...")
        dial("Rachel","According to amendment eight of the RCMS constitution...")
        dial("Rachel","“excessive distaste of the K-pop group BTS and no plea to reconcile the matter with any SGA affiliate must warrant a spell battle as a cruel and unusual punishment.”")
        dial("Rachel","You're going to die Katherine.")
        dial("Katherine","Ok man.")
        dial("Katherine","I still need to finish my ITF project but sure!")
        dial("Katherine","I\'d be happy to lend my perishability to ensure a greater school enviornment.")
        dial("Rachel","...")
        dial("Katherine","Or shall I say...")
        dial("Katherine","...your little dictatorship.")
        dial("Rachel","...")
        dial("Rachel","I don't like you.")
        dial("Rachel","Sofya, please take care of her.")
        dial("Sofya","Uhh.. no.")
        dial("Sofya","Katherine's my friend and I'd rather not-")
        dial("Rachel","Just KILL her!")
        dial("Katherine","._.")
        dial("Katherine","That escalated quickly...")
        dial("Sofya","Why do I have to fight for you? Can't you do it?")
        dial("Rachel","I'd rather watch.")
        dial("Katherine","...")
        dial("Katherine","Well, in that case...")
        dialNoSpeaker("Katherine turns to you.")
        dial("Katherine","Hey, I don't think we've met before but let's say we're friends.")
        dial("Katherine","I'd appreciate it if you'd fight on my behalf.")
        dropdownMenu(None,["Sure!","Of course, I'm not Valeria."])
        dial("Katherine","Yay!")
        dial("Sofya","...")
        dial("Sofya","I guess this is easier to handle.")
        if not runBattle(player, SofyaBattleStudent()):
          return
        
        dial("Sofya","...")
        dial("Rachel","...")
        dial("Rachel","Sofya...")
        dial("Sofya","*(Sigh)*")
        dial("Sofya","This is why you don't make others fight for you. -_-")
        dial("Rachel","...")
        dial("Sofya","Next time, please be more considerate.")
        dial("Rachel","...")
        dial("Rachel","... fine.")
        dialNoSpeaker("Sofya and Rachel exit the classroom.")
        dial("Katherine","Are they gone?")
        dial("Katherine","At least I can go back to-")
        dial("Ms. Ramasamy","No Katherine. You’ve caused enough mischief today.")
        dial("Ms. Ramasamy", "In fact, the mere thought of letting you retake the test has completely escaped my mind.")
        dial("Katherine","TwT")
        dialNoSpeaker("Katherine turns to you.")
        dial("Katherine","Can you believe this? I’m not allowed to retake the test. :(")
        dial("Ms. Ramasamy","Katherine... I can still hear you...")
        dial("Katherine","Sorry...")
        player.incrementQuestProgress(IronicCriminalPursuitQuest)
        player.sendEmail(NursesOfficeEmail)
      elif player.questProgressIsAt(IronicCriminalPursuitQuest, 2): # Interaction #2 
        if choice == 1:
          dial("Ms. Ramasamy", "Katherine probably isn't going to leave any time soon, is she?")
          dial("Ms. Ramasamy", "Maybe you could find something to distract her from her quiz grade.")
          dial("Ms. Ramasamy", "I've heard she really likes |Y|Chobani Yogurt|B|...")
          dial("Ms. Ramasamy", "Try finding who's selling some.")
        elif choice == 2:
          dial("Katherine", "Ms. Ramasamy still isn't letting me retake the quiz.")
          dial("Katherine", "Guess I'm staying here until she does.")
          if player.hasItem(ChobaniYogurtItem):
            dial("Katherine", "Hang on. That bright orange cap in your pocket, is that what I think it is?")
            dial("Katherine", "Is that the limited edition mango flavored |Y|Chobani yogurt|B|? I love Chobani!")
            dial("Katherine", "Maya gave me one of those before, I’m her only customer after all. It was delicious.")
            dial("Katherine", "I’ll gladly take it off your hands for you. What do you say?")
  
            choice = dropdownMenu(None, ["|G|Sure, have it!", "|Y|What do I get it return?"])
  
            if choice == 2:
              dial("Katherine", "I'll be eternally grateful.")
              dialNoSpeaker("You reluctantly hand over the Chobani Yogurt.")
            else:
              dialNoSpeaker("You hand the Chobani Yogurt over to Katherine.")
  
            player.removeItem(ChobaniYogurtItem)
    
            dial("Katherine", "You’ve made an excellent decision. I will cherish this drink for the rest of my life... about two hours.")
            dial("Ms. Ramasamy", "Alright, I think it’s time for you two to leave. Don’t you have places to be?")
            dial("Katherine", "Will do!")
            dial("Katherine", "I’ll be heading to Ms. Presley’s room, she’ll definitely convince Ms. Ramasamy to bump up my grade.")
            dial("Ms. Ramasamy", "What-")
            dial("Katherine", "See you soon!")
    
            player.incrementQuestProgress(IronicCriminalPursuitQuest)
      elif player.getQuestProgress(IronicCriminalPursuitQuest) in [3, 4]:
        dial("Ms. Ramasamy","Thank goodness, the woman is gone.")
        dial("Ms. Ramasamy","I’ve told Katherine many times that she shouldn’t be striving for perfectionism but she never listens.")
        dial("Ms. Ramasamy","She thinks getting anything below a perfect score will “cut her life expectancy in half”.")
        dial("Ms. Ramasamy","Now that I think about it, maybe she isn’t wrong.")
        player.sendEmail(AssignmentGradedEmail)
      elif player.questProgressIsAt(IronicCriminalPursuitQuest, 5):
        dialNoSpeaker("Unfortunately, the door's locked.")
        dial("Katherine","... what? I could’ve sworn it was open before.")
        dialNoSpeaker("All of sudden, loud knocks can be heard from the other side of the door.")
        dial("Poorvi","*(From behind the door)* KATHERINE!?!?!")
        dialNoSpeaker("Katherine falls to the ground, startled.")
        dial("Katherine","Ow.")
        dial("Poorvi","Oh my literature, thank the OnShape gods you came.")
        dial("Katherine","What- what happened?")
        dial("Ella","What happened? Can’t you tell? We got locked in!")
        dial("Peter","...how?")
        dial("Poorvi","So... we told Ellie to steal a desktop from Ms. Ramasamy’s, right?")
        dial("Katherine","...")
        dial("Poorvi","Nevermind that. Point is that Ellie, instead of unplugging the desktop, was playing Doodle Jump the entire time.")
        dial("Ellie","Sorry...")
        dial("Poorvi","After getting scolded by Ms. Presley, Ella and I wanted to check up on her cause we’re good friends, right?")
        dial("Ella","No.")
        dial("Poorvi","And let’s just say I... uh...")
        dial("Ella","She locked the door from the inside.")
        dial("Poorvi","ELLA!")
        dial("Katherine","...how?") 
        dial("Ella","All you have to know is that Ms. Ramasamy’s door is just... magical.")
        dial("Katherine","Is Ms. Ramasamy even there?")
        dial("Ellie","She's, most likely, suffering from Chronic Pseudocode Overdose Syndrome.")
        dial("Poorvi","...")
        dial("Ellie","Oh... sorry. .-.")
        dial("Poorvi","...")
        dial("Poorvi","Katherine, it seems that you're skilled at lockpicking... is that right?")
        dial("Katherine","... yeah?")
        dial("Katherine","... but this door is right next to the Engineering Lab, which has a CCTV for some reason.")
        dial("Poorvi","... and?")
        dial("Katherine","If the Harvard admission officers hear about this incident they'll reject me for sure!")
        dial("Katherine","My future will be ruined and I'll have to work at K-Mart!")
        dial("Katherine","AND I DON'T WANT TO WORK AT K-MART!")
        dial("Poorvi","Ugh. How about you find a key, anything along those lines would be sufficient.")
        dial("Katherine","That... seems significantly less incriminating.")
        dial("Peter","... where are we supposed to check? The entire school?")
        dial("Poorvi","...")
        dial("Poorvi","They say that there aren't any stupid questions...")
        dial("Poorvi","You've changed my mind.")
        dial("Peter","-_-")
        player.incrementQuestProgress(IronicCriminalPursuitQuest)
      elif player.questProgressIsAt(IronicCriminalPursuitQuest, 6): # Interaction 4
        dial("Poorvi","Huh? You found the key already?")
        dial("Peter","No, where would we even find such keys?")
        dial("Poorvi","I dunno, that's what you're supposed to do!")    
      elif player.questProgressIsAt(IronicCriminalPursuitQuest, 7):
        if player.hasItem(MasterKeysItem):
          dial("Poorvi","Did you find the key yet?")
          dial("Katherine","Yup!")
          dialNoSpeaker("You raise the keys near the window of the locked door.")
          dial("Ella","Thank god! I cannot tolerate Poorvi’s verbose monologues on Star Trek anymore.")
          dial("Poorvi","ELLA! >:(")
          dial("Ella","I completely lost track on who Captain Kirk is and why he supports space exploration.")
          dial("Poorvi","...")
          dial("Poorvi","My monologue was lacking some ethos. -_-")
          dialNoSpeaker("You unlock the door and free the three froggy girls from their eternal pseudocode torture.")
          dial("Poorvi","Thanks!")
          dial("Poorvi","Ellie, you brought the desktop right?")
          dial("Ellie","Right here in its full glory!")
          dialNoSpeaker("Ellie shows off the desktop she smuggled from Ms. Ramasamy’s room.")
          dial("Poorvi","Amazing!")
          dial("Peter","Are we just gonna-")
          dial("Katherine","*(Ignoring him)* We’re be heading to Ms. Palank’s room to return her master keys!")
          dial("Poorvi","M- Master keys?")
          dialNoSpeaker("You show off the master keys to Poorvi.")
          dial("Poorvi","Thos- those are master keys?")
          dial("Poorvi","I mean, we’re also heading to Ms. Palank’s as well since Ellie kinda forgot to turn in her SSL forms.")
          dial("Ellie","Knew I was forgetting something.")
          dial("Poorvi","I’m willing to take those keys and give them to Ms. Palank on our behalf.")
          dial("Katherine","Wha- of course not!")
          dial("Peter","Yeah, I know for a fact you're going to-")
          dial("Ella","*(Interupting Him)* Use them from malicious purposes?")
          dial("Poorvi","*(Offended)* Peter... I can’t believe you. We’re not like that!")
          dialNoSpeaker("Peter points at the desktop in Ellie’s hands.")
          dial("Poorvi","...")
          dial("Poorvi","... right.")
          dialNoSpeaker("Poorvi rushes up to you and snaches the master keys before bolting in the opposite direction while Ella and Ellie walk.")
          dial("Peter","HEY!")
          dial("Poorvi","*(While sprinting)* Don't worry Peter, we left a suprise for you in Ms. Ramasamy's room.")
          dial("Ella","*(While walking)* Although, it's not the greatest.")
          dial("Poorvi","*(While sprinting)* Hey, at least they can recoup some of their loss.")
          dial("Peter","But- but-")
          dial("Peter","I- I-")
          dial("Katherine","They're gone.")
          dial("Peter","Aww, we shouldn't have told them.")
          dial("Katherine","Yeah, Ms. Palank's... going to kill us.")
          dial("Katherine","And my English score will diminish at an exponentional rate!")
          dial("Peter","Okay, no more grade talk... please.")
          dial("Katherine","Why are they even doing this? They have to have some sort of motive.")
          dial("Peter","Right, want to see what that suprise is about?")
          dial("Katherine","Can't be that bad, can it?")
          dial("Peter","It's Poorvi.")
          dial("Katherine","How could I forget.")
          player.incrementQuestProgress(IronicCriminalPursuitQuest)
          player.removeItem(MasterKeysItem)
        else:
          dial("Poorvi","Did you find the key yet?")
          dial("Katherine","Yup!")
          dial("Katherine","{}, show them the keys!".format(player.getName()))
          dialNoSpeaker("You... don't have the keys?")
          dial("Pilliam", "bro wtf omkar did you break the code again i swear")
          raise ContentError()
      elif player.questProgressIsAt(IronicCriminalPursuitQuest, 8):
        dial("Katherine", "Do you think we should really go in there right now?")
        dial("Peter", "Yeah, why? It can't be that bad, right?")
        dial("Katherine", "I have a bad feeling about going in there.")
        dial("Peter", "Don't be silly Katherine, you always say everything feels ominous and it turns out just fine.")
        dial("Katherine", "This is for real though...")
        dial("Katherine", "{}, do you have anything else you need to do?".format(player.getName()))
        choice = dropdownMenu(None, ["|R|Yeah, I remembered I have to do my 97th Day of Onshape.", "|Y|No, let's get this over with."])
        if choice == 1:
          dial("Katherine", "Oh yeah, we should really do that first.")
          dial("Peter", "Seriously? You're both cowards.")
          dialNoSpeaker("Peter reluctantly leaves the classroom with the two of you.")
          player.classroom = None
          return
  
        dial("Katherine", "*(Sigh)* It's worth a try.")
        dialNoSpeaker("The three of you enter the classroom, and discover...")
        dial("Katherine","Oh... it’s just a frog.")
        dial("Gummy","Greetings!")
        dial("Katherine","IT CAN TALK!?!?")
        dialNoSpeaker("Katherine falls to the ground, startled.")
        dial("Gummy","I’m glad you’ve noticed my linguistic prowess... I’ve been working on it!")
        dial("Peter","Huh?")
        dial("Gummy","Queen Poorvi taught me and my siblings this wonderful language, although still a bit confused on pronunciation.")
        dial("Gummy","Seriously, ‘though’ and ‘tough’ read similarly but are pronounced completely different. Who thought of that?")
        dial("Gummy","Hang on... that’s another one... ‘thought’.")
        dial("Katherine","I’m scared.")
        dial("Gummy","You shouldn’t be, I’m just a frog that loves English.")
        dialNoSpeaker("Gummy unveils a miniature dictionary sitting beside them and scrolls to a random page.")
        dial("Gummy","Here’s a word, ‘love’.")
        dial("Gummy","We should all go one by one, telling each other the things we love.")
        dial("Peter","Uh...")
        dial("Gummy","I’ll go first, I love my dictionary.")
        dial("Peter","Umm... I love... volleyball?")
        dial("Katherine","... Chobani yogurt?")
        dial("Gummy","Wonderful! Now *(pointing to you)* what about you?")
        dropdownMenu("What do you 'love'?",["Frog Meat","Frog Risotto","Frog Legs","Frog Soup"])
        dial("Gummy","...")
        dial("Gummy","I... I’m just a frog that loves English.")
        dial("Gummy","And you... and you... gave me a death threat?")
        dial("Katherine","Oh no.")
        dialNoSpeaker("With a dictionary clutched in their webbed hand, the English-loving frog stares at you menacingly...")
        dial("Gummy","Want to know something about English?")
        dial("Gummy","Knowledge is more powerful than any spell will ever be...")

        if not runBattle(player, GummyBattleFrog()):
          return
                  
        dial("Gummy","...")
        dial("Gummy","I’m just a frog that loves English...")
        dialNoSpeaker("The frog, despite the preconceived notion that spell battles don’t result in death, bursts into many pieces.")
        dial("Katherine","... ew-")
        dialNoSpeaker("Ms. Ramasamy steps into the room.")
        dial("Ms. Ramasamy","Wha- what’s been going on in here?")
        dial("Peter","Um...")
        dial("Katherine","*(Nervous)* Ms- Ms. Ramasamy- we’ve been- been- dissecting frogs you know. The seventh grade curriculum- it's kinda- kinda-")
        dial("Ms. Ramasamy","You’re not even in seventh grade...")
        dial("Katherine","*(Very nervous)* Well- my severse and uh- uh- continous uh- overlapse in judgement has prompted-")
        dial("Ms. Ramasamy","Out. (Pointing to the door of her room)")
        dial("Katherine","Sorry...")
        
        player.incrementQuestProgress(IronicCriminalPursuitQuest)
        player.act = 2
        player.classroom = None
        return

    elif player.act == 2:
      clear()
  
      printBoxedText("Room 236A - Ms. Ramasamy's Computer Lab")
      print() 
      
      # Classroom Description
      printC("You're in Ms. Ramasamy's room, the 8th grade computer lab.")
      if player.hasFlag("236A_Int1_PilliamHatesCoding") == False:
        printC("You can spot Pilliam talking to Ms. Ramasamy.")
        choice = dropdownMenu("What do you do?",["Listen to the conversation.","Leave the classroom."])
        if choice == 1:
          dial("Pilliam","Please?")
          dial("Ms. Ramasamy","No. -_-")
          dial("Pilliam","But pseudocode is useless! Why do I have to write it every single time?")
          dial("Ms. Ramasamy","Pseudocode helps you understand the logic of your program before you start actually coding it.")
          dial("Pilliam","...")
          dial("Pilliam","I'd rather grind Celeste Strawberry Jam Heartsides than deal with this.")
          dial("Ms. Ramasamy","Pilliam, it isn't that difficult. Trust me.")
          dial("Pilliam","...")
          dial("Pilliam","Fine.")
          player.addFlag("236A_Int1_PilliamHatesCoding")
        elif choice == 2:
          player.classroom = None
          return
      else:
        if player.hasFlag("236A_Int2_PilliamLeavesClassroom") == False:
          print()
          printC("You can spot Pilliam crying in the corner of the room.")
        choice = dropdownMenu("What do you do?",["Talk to Pilliam","Talk to Ms. Ramasamy","Leave the classroom."])
        if choice == 1:
          if player.hasFlag("236A_Int2_PilliamLeavesClassroom") == False:
            dial("Pilliam","I just don't understand why writing pseudocode is necessary.")
            if player.hasFlag("121_Int1_PilliamBestFriend"):
              dialNoSpeaker("You tell Pilliam about Ms. Palank's email.")
              dial("Pilliam","She... wants me to... read her email?")
              dial("Pilliam","Uhh...")
              dial("Pilliam","Sure.")
              dialNoSpeaker("Pilliam leaves the classroom, presumably to meet up with Ms. Palank.")
              player.incrementQuestProgress(GrammarCheckerQuest)
              player.addFlag("236A_Int2_PilliamLeavesClassroom")
              player.sendEmail(CodeHSAnswersEmail)
          else:
            dial("???","Bro who are you talking to, Pilliam isn't here.")
        elif choice == 2:
          dial("Ms. Ramasamy","I don't understand.")
          dial("Ms. Ramasamy","What's the big deal with pseudocode?")
          dial("Ms. Ramasamy","Aren't you magnet kids good at English, or am I deeply mistaken?")
        elif choice == 3:
          player.classroom = None
          return
          
class Room236BClassroom(Classroom):
  def __init__(self):
    self.name = "Room 236B"
    self.locked = [1, 2, 3, 4, 5]

class Room236CClassroom(Classroom):
  def __init__(self):
    self.name = "Room 236C"
    self.locked = [1, 2, 3, 4, 5]

class Room237AClassroom(Classroom):
  def __init__(self):
    self.name = "Room 237A"
    self.locked = [1, 2, 3, 4, 5]

class Room237BClassroom(Classroom):
  def __init__(self):
    self.name = "Room 237B"
    self.locked = [1, 2, 3, 4, 5]

class Room239Classroom(Classroom):
  def __init__(self):
    self.name = "Room 239 - The Gemstone Gallery"
    self.locked = [1]

  def run(self, player):
    if player.act == 2:
      # Clear the map
      clear()
  
      printBoxedText("Room 239 - The Gemstone Gallery")
      print()
  
      printC("This room seems to be decorated very fancily - there are jewels and gemstones all around echoing the sunlight.")
      print()
      printC("In the midst of the warm and bright ambience is Jessika, propped behind a storefront.")

      if player.hasFlag("239_Int1_JessikaFirstTalk") == False:
        choice = dropdownMenu("What do you do?",["Talk to Jessika","Leave the classroom"])
        if choice == 1:
          dial("Jessika","Greetings! I assume you're here to purchase something delightful!")
          dial("Jessika","Is that right?")
          choice = dropdownMenu(None,["Yes, I am!","Nah, I'm good."])
          if choice == 1:
            dial("Jessika","Very well.")
            dial("Jessika","I usually have a curation of many gemstone wands...")
            dial("Jessika","... but currently, the most popular options are sold out.")
            dial("Jessika","Luckily, I'm getting a new batch of wands shipped here very soon.")
            dial("Jessika","Amazon won't let me track the number so I've been waiting patiently.")
            dial("Jessika","...")
            dial("Jessika","At least I still have a |DB|Sapphire|B| and |R|Ruby|B| wand in stock.")
            player.addFlag("239_Int1_JessikaFirstTalk")
          elif choice == 2:
            dial("Jessika","Get the heck out of here!")
            player.classroom = None
            return
        elif choice == 2:
          player.classroom = None
          return  
      else:
        choice = dropdownMenu("What do you do?",["Buy something from Jessika","Ask Jessika about any succulents","Leave the classroom."])
        if choice == 1:
          runShop([[SapphireWand, 400, True], [RubyWand, 400, True]], "Jessika's Gemstone Gallery", "B", player)
        elif choice == 2:
          if player.hasFlag("239_Int1_JessikaSucculent") == False:
            dial("Jessika","Huh? Succulents-") 
            dial("Jessika","I'm assumming you're talking about this:")
            dialNoSpeaker("Jessika pulls out a bright orange succulent.")
            dial("Jessika","Not sure of it's scientific name but at least it looks nice.")
            dial("Jessika","Usually, I have this up for decoration...")
            dial("Jessika","...but today, I forgot.")
            dial("Jessika","Thanks for reminding me!")
            choice = dropdownMenu(None,["May I have it?","It looks nice."])
            if choice == 1:
              dial("Jessika","Absolutely not, this succulent is only for decoration.")
              choice = dropdownMenu(None,["I'll partake in a spell battle for it.","Okay, fine."])
              if choice == 1:
                dial("Jessika","...")
                dial("Jessika","...guess you're an eager one.")
                dial("Jessika","Very well then, if you want it that badly...")
                dial("Jessika","I have no choice but to accept your offer.")

                if not runBattle(player, JessikaBattleStudent()):
                  return
                  
                dial("Jessika","At least I was close...")

                player.giveItem(OrangeEcherviaSucculentItem)
                printFlair("You Receive an Orange Echervia Succulent!")
                
                player.addFlag("239_Int1_JessikaSucculent")
            elif choice == 2:
              dial("Jessika","I agree.")
          else:
            dial("Jessika","Look, I don't have any more succulents to give you.")
        elif choice == 3:
          player.classroom = None
          return
    elif player.act == 3:
      clear()
      
      printBoxedText("Room 239 - The Gemstone Gallery")
      print()
  
      printC("This room seems to be decorated very fancily - there are jewels and gemstones all around echoing the sunlight.")
      print()
      printC("In the midst of the warm and bright ambience is Jessika, propped behind a storefront.")
      if player.hasFlag("239_Int1_JessikaRestockedTalk"):
        dial("Jessika","Oh hey, you're back!")
        dial("Jessika","Everything good?")
        dial("Katherine","Yup! That back ache wore off pretty quickly!")
        dial("Jessika","Nice to hear! I shouldn't have let those intrusive thoughts win...")
        dial("Katherine","Yeah. ._.")

      if player.hasFlag("239_Int1_JessikaRestockedTalk") == False:
        choice = dropdownMenu("What do you do?",["Talk to Jessika","Leave the classroom"])
        if choice == 1:
          dial("Jessika","Greetings, Katherine and {}! Another shipment of wands from Amazon just arrived.".format(player.name))
          dial("Jessika","An |LG|Emerald Wand|B| and a |PU|Amethyst Wand|B|, to be exact!")
          dial("Jessika","These wands will continuously increase your |Y|boost|B| and |G|shield|B| during battles.")
          dial("Jessika","You can buy them from here for the low, low price of 600 tickets each!") 
          dial("Katherine","...")
          dial("Katherine","Jessika... weren't you supposed to be looking for that Aloe Vera?")
          dial("Jessika","My apologies Katherine, but, put simply, finding Aloe Vera is... extremely boring.")
          dial("Jessika","I mean, I can't leave this place unattended, can I?")
          dial("Katherine","But- but- Jessika, we really need that-")
          dial("Jessika","Hang on, do you sense that?")
          dial("Katherine","Sense what?")
          dial("Jessika","I seem to be sensing some Deus Ex Machina nearby...")
          dial("Katherine","What-")
          dialNoSpeaker("Jessika glances over to the window in her gallery and peers at the vibrant green field on the other side.")
          dial("Jessika","Ah, my intuition was right!")
          dial("Jessika","Behold! Those remarkable green thorny leaves, can't be mistaken for anything otherwise!")
          dialNoSpeaker("You and Katherine and walk over to the window and peer outside.")
          dialNoSpeaker("You get a glipse of what Jessika was referring to, a bright green thorny plant, undoubtedly Aloe Vera.")
          dial("Katherine","Woah, you could sense that plant from two stories above?")
          dial("Jessika","Yup! Wand collecting has expanded my range in all senses, now I have five different ways to admire the beauty of these delicate collectables.")
          dial("Katherine","That's amazing! I didn't know they grew Aloe Vera here!")
          dial("Jessika","There's a lot of wonderful things you don't know about this school!")
          dial("Katherine","Interesting. Now, how will we get down there...")
          dial("Katherine","I mean, we could just walk down the stairs but that would be cumbersome-")
          dial("Jessika","Looking for a something more hasty? There's a much faster way then walking!")
          dial("Katherine","Hm?")
          dialNoSpeaker("Jessika opens up the window of her gemstone gallery, the cold breeze outside gushes into the room, rattling all the fragile wands.")
          dial("Jessika","You ever gone skydiving Katherine?")
          dial("Katherine","I mean, if iFly counts then-")
          dialNoSpeaker("All of a sudden, Jessika grabs you and Katherine by the arm and lunges you striaght out of the window.")
          dial("Katherine","*(While falling)* JESSIKA!")
          dialNoSpeaker("You and Katherine abruptly land on the ground. The grass beneath cushions your fall, preventing the two of you from contracting anything worse than a minor back pain.")
          dial("Katherine","Ow~ my hip~")
          dial("Katherine","JESSIKA, YOU NEARLY KILLED US!")
          dial("Jessika","*(From above)* I'm sorry, I wasn't the one who asked for a faster route!")
          dial("Katherine","Well- that's- that's true but- but-")
          dialNoSpeaker("You crawl over to the Aloe Vera, your back aching in pain. You attempt to pull out the watery plant from the ground beneath but it's completely lodged in.")
          dial("Katherine","At least give us some way to dislodge the plant from the ground!")
          dial("Jessika","*(From above)* Fine.") 
          dialNoSpeaker("Jessika launches out a shovel from her gallery, as it comes down, it bonks Katherine straight on the head.")
          dial("Katherine","Ow... Jessika, I swear, you're trying to kill me!")
          dial("Jessika","*(From above)* That's not my fault, air resistance should've been working harder to protect you.")
          dial("Katherine","...")
          dial("Katherine","I- well- I- I- guess- uh-")
          dial("Katherine","Maybe I'm the problem here...")
          dial("Jessika","*(From above)* Oh don't say that, now you're making me feel bad!")
          dial("Katherine","Well, do you?")
          dial("Jessika","*(From above)* I mean- I- well-")
          dial("Jessika","*(From above)* *(Sigh)* I'm sorry for nearly killing you.")
          dial("Katherine","That's more like it. :D")
          dialNoSpeaker("Using the shovel as a lever, you dislodge the Aloe Vera straight from the ground.")
          printFlair("You Receive an Aloe Vera Succuent!")
          dial("Katherine","Nice work! :)") 
          dial("Jessika","*(From above)* Everything alright down there?")
          dial("Katherine","Yup, the Aloe Vera has been retrieved!")
          dial("Jessika","*(From above)* That's great! I'll stay here to greet any visitors to my gallery, good luck with collecting everything else!")
          dial("Katherine","Thanks!")
          dialNoSpeaker("Katherine turns to you.")
          dial("Katherine","Any ideas on how we'll get back inside?")
          dialNoSpeaker("You point to a dull, red door behind Katherine with the text \"You Bruh, Do Not Enter\" plastered in bold white letters.")
          dial("Katherine","Oh, how convenient.")
          dialNoSpeaker("You and Katherine approach the door, slightly nervous.")
          dial("Katherine","You think they'll know?")
          dialNoSpeaker("You shake your head.")
          dial("Katherine","Oh well.")
          dialNoSpeaker("Katherine opens the door and the two of you enter the school, Aloe Vera in hand.")
          player.addFlag("239_Int1_JessikaRestockedTalk")
          # TODO: Modify Waypoint (Pilliam, if you're reading this, DM me on discord and I'll explain what this means.) - akish charan
        elif choice == 2:
          player.classroom = None
          return  
      else:
        choice = dropdownMenu("What do you do?",["Buy something from Jessika","Leave the classroom."])
        if choice == 1:
          runShop([[SapphireWand, 400, True], [RubyWand, 400, True], [EmeraldWand, 600, True], [AmethystWand, 600,True]], "Jessika's Gemstone Gallery", "B", player)
        else:
          player.classroom = None
          return
          
class Room240Classroom(Classroom):
  def __init__(self):
    self.name = "Room 240 - Art"
    self.locked = []

  def run(self, player):
    # Clear the map
    clear()

    # Boxed text for room name
    printBoxedText("Room 240 - Art")
    print() 
    
    # Classroom Description
    printC("You're in the art classroom. Beautiful paintings & sculptures line the walls, a majority of which were made by Brooke Yin.")

    interactionName = "Go to the self-portrait station"
    if not player.hasFlag("240_Int1_TalkedWithArtTeacher"):
      interactionName = "Talk to the art teacher"

    choice = dropdownMenu("What will you do?", [interactionName, "Leave the classroom"])

    if choice == 2:
      player.classroom = None
      return
    else:
      if player.hasFlag("240_Int1_TalkedWithArtTeacher"):
        dialNoSpeaker("You walk over to the self-portrait station.")
        dialNoSpeaker("You currently look like this: {}".format(player.getName()))
        crayonColors = {
          RedCrayonItem: ["Red", "R"],
          OrangeCrayonItem: ["Orange", "O"],
          YellowCrayonItem: ["Yellow", "Y"],
          GreenCrayonItem: ["Green", "G"],
          BlueCrayonItem: ["Blue", "B"],
          PurpleCrayonItem: ["Purple", "PU"],
          BrownCrayonItem: ["Brown", "BR"]
        }

        options = []
        for pair in crayonColors.items():
          if player.hasItem(pair[0]):
            options.append(pair[1])
        options.append(["Nah I'm Good", "DG"])

        choice = dropdownMenu("What color do you want to change your name to?", ["|{}|{}".format(x[1], x[0]) for x in options])
        if choice == len(options):
          dialNoSpeaker("You decide that you like the way you look right now.")
        else:
          choice -= 1
          dialNoSpeaker("You take your |{}|{} Crayon|--| and draw a *very flattering* self-portrait of yourself.".format(options[choice][1], options[choice][0]))
          dialNoSpeaker("Your name color is now |{}|{}|--|!".format(options[choice][1], options[choice][0]))
          player.nameColor = options[choice][1]
      else:
        dialNoSpeaker("You walk over to the art teacher and ask what to do.")
        dial("Art Teacher", "|PI|Hello {}|PI|! Welcome to the art room!".format(player.getName()))
        dial("Art Teacher", "|PI|... oh dear.")
        dial("Art Teacher", "|PI|A bland old |B|blue name |PI|won't do here, will it?")
        dial("Art Teacher", "|PI|Add some |R|color|PI|, some |Y|diversity|PI|, something that |G|stands out|PI|!")
        dial("Art Teacher", "|PI|You've undoubtedly noticed students around here with |LB|different-colored |PU|nametags|PI|, right?")
        dial("Art Teacher", "|PI|Well, here's the place where you can choose what color you want your name to be!")
        dial("Art Teacher", "|PI|If you ever find a |LB|crayon|PI| lying around the school, you can bring it here to change your name to that color!")
        dial("Art Teacher", "|PI|Don't worry about whether you'll like it or not; crayons can be applied infinitely and you can change your color whenever you want!")
        dial("Art Teacher", "|PI|...")
        dial("Art Teacher", "|PI|Although, I *suppose* if you want to keep your name as |B|blue|PI|...")
        dial("Art Teacher", "|PI|Here, have this |B|Blue Crayon|PI|. Not many people around here use them, and I've been meaning to get this one off my hands.")

        player.giveItem(BlueCrayonItem)
        printFlair("You receive a Blue Crayon!")

        dial("Art Teacher", "|PI|Happy coloring!")
        player.addFlag("240_Int1_TalkedWithArtTeacher")
          
        

class Room234Classroom(Classroom):
  def __init__(self):
    self.name = "Room 234"
    self.locked = [1, 2, 3, 4, 5]

class Room238Classroom(Classroom):
  def __init__(self):
    self.name = "Room 238"
    self.locked = [1, 2, 3, 4, 5]

class Room232Classroom(Classroom):
  def __init__(self):
    self.name = "Room 232"
    self.locked = [1, 2, 3, 4, 5]

class Room230Classroom(Classroom):
  def __init__(self):
    self.name = "Room 230"
    self.locked = [1, 2, 3, 4, 5]

class MediaCenterClassroom(Classroom):
  def __init__(self):
    self.name = "The Media Center"
    self.locked = []

  def run(self, player):
    # Clear the map
    clear()

    # Boxed text for room name
    printBoxedText("The Media Center - Mr. Poker")
    print() 
    
    # Classroom Description
    printC("You’re in the Media Center, the place where Lillian spends a majority of her day.")

    if player.act == 1:
      if not player.questProgressIsAtLeast(IronicCriminalPursuitQuest, 5) and player.hasFlag("MediaCenter_Int1_StubbornEllaLeavesTable") == False:
        print()
        printC("You can see Poorvi, Ella, and Ellie scheming something at a long white table alongside an interesting-looking poster in front of you.")
  
      choice = dropdownMenu("What do you do?",["Sit at the white table uninvited.","Examine the poster in front of you.","Leave the classroom"])
  
      if choice == 1: # Interaction 1
        if not player.questProgressIsAtLeast(IronicCriminalPursuitQuest, 5) and player.hasFlag("MediaCenter_Int1_StubbornEllaLeavesTable") == False:
          dialNoSpeaker("You sit at the white table uninvited and pretend to start working. Somehow, the girls don't notice you...")

          dial("Poorvi","So if we manage to-")
          dial("Ella","Did you hear something or was it the wind?")
          dial("Ellie","The wind has been acting up lately, I’m sure it’s nothing.")
          dial("Poorvi","...")
          dial("Poorvi","Guys...")
          dial("Poorvi","Are you ignoring me on purpose? We have some real important matters to discuss here-")
          dial("Ella","Yeah, the winds been getting real annoying lately-")
          dial("Poorvi","GUYS!")
          dial("Ella","What do you want?")
          dial("Poorvi","Have you been listening to anything I’ve said for the past thirty minutes?")
          dial("Ellie","I haven’t, I’ve been playing Google Snake the entire time.")
          dial("Poorvi","Seriously? I thought you were taking notes.")
          dial("Ellie","Who does that?")
          dial("Poorvi","-_-")
          dial("Poorvi","What about you *(pointing to Ella)*, have you been listening?")
          dial("Ella","Why should I? I’m not the person who's been crowned a queen by a bunch of frogs, that's your problem. And besides, I’ve been playing Minesweeper.")
          dial("Poorvi","-_-")
          dial("Poorvi","Okay, I’ll just recap.")
          dial("Poorvi","After I opened up the Arduino Closet, all of the frogs escaped and I was crowned their queen.") 
          dial("Poorvi","They gave me the wisdom required to construct an all-powerful device, capable of the once theoretically impossible.")
          dial("Ellie","The P.L.A.N.T?")
          dial("Poorvi","Precisely.")
          dial("Poorvi","Using a plethora of wires, I've stayed up countless nights at-home constructing the device.")
          dial("Poorvi","After the job was complete, I was eagerly awaiting-")
          dial("Ella","Just show us your prototype already.")
          dial("Poorvi","About that. Unfortunately, I wasn't able to transfer the code from my home laptop-")
          dial("Ella","Excuse me? Don't you have a chromebook-")
          dial("Ella","Oh right, you got your privileges taken away.")
          dial("Poorvi","Don’t mention it-")
          dial("Ellie","What-")
          dial("Ella","Basically Ellie, Poorvi was annoyed that her old chromebook’s appearance didn’t align with her color preferences.")
          dial("Poorvi","-_-")
          dial("Ella","As a result, she had a mild temper tantrum, destroyed her chromebook, and requested another from Mr. Poker.")
          dial("Ella","But, instead of receiving a new one, she was banned from using any chromebook since she was deemed ‘irresponsible’.") 
          dial("Poorvi","In my defense, beige would be a more aesthetically pleasing chromebook color than black. Yuck.")
          dial("Ella","*(Sigh)* You're so difficult.")
          dial("Poorvi","...")
          dial("Poorvi","Anyways-")
          dial("Poorvi","You know those large, slow desktops that Ms. Ramasamy has in her computer lab?")
          dial("Ella","Yeah?")
          dial("Poorvi","I've been pondering...")
          dial("Poorvi","Why not use one of those?")
          dial("Poorvi","Unfortunately, Ms. Ramasamy's always lurking in that room so she'll definetly get a glimpse of what we're up too.")
          dial("Poorvi","So, to keep our operation covert, I've assigned the two of you to steal one of those fancy desktops.")
          dial("Ella","WHAT! Are you serious?")
          dial("Ella","Wouldn't that be even more incriminating?")
          dial("Poorvi","Ella, It's our safest option.")
          dial("Ellie","You don't like stealing things Ella?")
          dial("Ellie","I do it all the time!")
          dial("Poorvi","... wha-")
          dial("Ella","Oh my names with phonetic resemblance, do I have to?")
          dial("Ellie","Come on Ella, It’ll be fun!")
          dial("Ella","Fun... committing crimes?")
          dial("Ella","*(Sigh)* Katherine would be proud of us.")
          dial("Ellie","... uh...")
          dial("Poorvi","Ella, just stop. We’re stealing a desktop, your opinion isn’t going to change anything.")
          dial("Ella","... this is my punishment for associating myself with you two.")
          dialNoSpeaker("As the three girls get up from the table, they finally notice you.")
          dial("Poorvi","Oh, uh... hi? How long have you been sitting here?")
          dial("Ella","They sat down around the time you started recapping for us.")
          dial("Poorvi","ELLA! Why didn't you say anything?")
          dial("Ella","They don't seem very unfriendly. I don't think I've actually seen them before.")
          dial("Ella","I was going to ask for their name, but you kept talking.")
          dial("Poorvi","...")
          dial("Ella","Anyways...")
          dialNoSpeaker("Ella turns to you.")
          dial("Ella"," What's your name?")
          # Change this to the old dropdown if necessary
          dialNoSpeaker("You tell them your name.")
          dial("Ella","{}? Nice to meet you.".format(player.getName()))
          dial("Poorvi","Ella, stop socializing with the eavesdropper.")
          dial("Poorvi","Uhhh... {}, we're going to Ms. Presley's room to... retake a quiz...".format(player.getName()))
          dial("Poorvi","It's a pretty important one, you probably shouldn't interrupt us...")
          dial("Poorvi","See you around.")
          dialNoSpeaker("Poorvi drags Ellie and a very reluctant Ella away from the table.")
          player.addFlag("MediaCenter_Int1_StubbornEllaLeavesTable")
        elif player.questProgressIsAtLeast(IronicCriminalPursuitQuest, 5): 
          dialNoSpeaker("There’s no one sitting at the table anymore.")
          dial("Katherine","Shouldn’t we be in Ms. Ramasamy’s room?")
          dial("Peter","I perfer the tranquility of this white table over the harsh and brutal enviornment that-")
          dial("Katherine","It’s just a table. -_-")
          dial("Peter","*(Sigh)* Why do nice things never last for long.")
      
        elif player.hasFlag("MediaCenter_Int1_StubbornEllaLeavesTable"): 
          dialNoSpeaker("There’s no one sitting at the table anymore. Our deepest condolences go to our fallen soldier Ella Park, taken away so soon from her domicile.")
          
        
        
      elif choice == 2:
        if player.hasFlag("MediaCenter_Int2_LillianPosterRipped") == False: 
          dialNoSpeaker("You examine the interesting poster of an attack helicopter in front of you. There’s a caption below...")
          dialNoSpeaker("“No helicopters in the library, pretty please with a cherry on top.”")
          dial("Lillian","I see you’re examining the poster I put up.")
          dialNoSpeaker("Quite startled you back up into the poster, tearing it off the wall.")
          dial("Lillian","My- my poster...")
          dialNoSpeaker("Lillian turns to you.")
          dial("Lillian","You fiend. What was that?")
          dial("Lillian","I mean, a paper clip and a hook may or may not have been the most secure method of installation but still, you should’ve known better.")
          dial("Lillian","I demand a spell battle.")

          if not runBattle(player, LillianBattleStudent()):
            return
          
          dial("Lillian","*(Sigh)* Guess I’ll have to put up another one eventually.") 
          dial("Lillian","You can take what's left of the poster, I can’t use it anyway.") 
          printFlair("You receive a Half-Ripped Poster!")
          printFlair("You receive a Paperclip!")
          player.giveItem(HalfRippedPosterItem)
          player.giveItem(PaperclipItem) 
          player.addFlag("MediaCenter_Int2_LillianPosterRipped")
  
        elif player.questProgressIsAtLeast(IronicCriminalPursuitQuest, 5): 
          dialNoSpeaker("Do you have short-term memory loss? You literally ripped the poster, what’s there to examine?")
          dial("Katherine","{}, are you just staring at the wall?".format(player.getName()))
          dial("Katherine","Gosh, and I thought Peter was weird.")
          dial("Peter","Hey! >:(")
        elif player.hasFlag("MediaCenter_Int2_LillianPosterRipped"): # Previous interaction occured
          dialNoSpeaker("Do you have short-term memory loss? You literally ripped the poster, what’s there to examine?")
  
      if choice == 3:
        player.classroom = None
        return
    else:
      if not player.hasFlag("MediaCenter_TalkedWithPokerOpening"):
        dial("Mr. Poker", "Hey, {}!".format(player.getName()))
        dial("Mr. Poker", "Thanks for stopping by, it's always nice to see a new reader visit our center.")
        dial("Mr. Poker", "Good timing, too; the latest collection of student-recommended books just arrived!")
        dial("Mr. Poker", "Feel free to sit down and read some of them; I'm sure there's something in there that will fit your tastes.")
        player.addFlag("MediaCenter_TalkedWithPokerOpening")
        return
      else:
        printC("There's a large collection of books to read.")
        choice = dropdownMenu("What will you do?", ["Read some books", "Leave the Media Center"])
        if choice == 2:
          dial("Mr. Poker", "Goodbye! Feel free to drop by again whenever we're open!")
          player.classroom = None
          return
        else:
          dialNoSpeaker("You walk over to a red shelf with a wide variety of books to read.")
          books = [
            "*Aesop's Fables: The Legend of the Arduino Closet*",
            "*Cryptography w/ Furries: A children's guide to Cryptography*",
            "*Color By Number: Furry Edition*",
            "*100 Pages of Onshape*",
            "*Under the Mosquito*",
            "*Monster*",
            "*Never Caught (Almost)*",
            "*RCMS 2021-2022 Yearbook*",
            "*The Constitution of RCMS*",
            "A Singular Wrinkled Piece of Paper",
            "|R|No thanks, I hate reading"
          ]
          
          choice = dropdownMenu("What will you read?", books)

          if choice == len(books):
            dialNoSpeaker("You decide not to read anything.")
            return
          elif choice == len(books) - 1:
            if player.hasFlag("MediaCenter_ReturnedStolenBook"):
              dialNoSpeaker("Despite you just returning the Stolen Furry Book, it's been stolen... again...")
              dialNoSpeaker("The old and faded piece of paper is back, but the writing on it has changed.")
              dialNoSpeaker("*\"TODO: Remember not to sell Stolen Books to customers\"* - Shrem Masala")
              dialNoSpeaker("|DG|*Figures...*")
            else:
              dialNoSpeaker("You pull the book out of the... Hey, wait... this isn't a book!")
              dialNoSpeaker("It appears to be an old and faded piece of paper, with writing on it.")
              dialNoSpeaker("You can barely make out what it says...")
              dialNoSpeaker("*\"TODO: Return Stolen Book\"* - Shrem Masala")
              if player.hasItem(StolenFurryBookItem):
                dialNoSpeaker("Realizing what this means, you take out the Stolen Furry Book and slide it back into the shelf.")
                if player.hasItem(ScrollOfDiversityItem):
                  dialNoSpeaker("Suddenly, a faded envelope magically appears in your hands.")
                  dialNoSpeaker("You open it and receive |W|1,000|B| tickets.")
                  player.removeItem(StolenFurryBookItem)
                else:
                  player.giveItem(ScrollOfDiversityItem)
                  dialNoSpeaker("Suddenly, a faded scroll magically appears in your hands.")
                  dialNoSpeaker("You found the |BR|Scroll of Diversity|B|!")
                  dialNoSpeaker("Your maximum health was increased by |R|30|B|.")
                  player.removeItem(StolenFurryBookItem)
                player.addFlag("MediaCenter_ReturnedStolenBook")
              else:
                dialNoSpeaker("You ponder over what this might mean.")
          else:
            dialNoSpeaker("You pull the book out of the shelf and start reading it.")
            story = "If you're reading this, it's a bug! TwT"
            if choice == 1:
              player.sendEmail(RCMSLoreEmail)
              story = '''\
*Aesop's Fables: The Legend of the Arduino Closet*

In a time long ago, the halls of RCMS echoed with the laughter and chatter of harmonious students.
Among them, one student had a peculiar fascination with a mysterious puddle in the field outside.
This was no ordinary puddle, for it was home to a family of five frogs.
Filled with joy, the student decided to adopt the frog quintuplets, showering them with love, care, and attention.

However, as the frogs settled into their new environment, they became increasingly greedy and demanding.
The student, known as "the frog whisperer" among their peers, struggled to balance caring for the frogs and
maintaining their position as a valedictorian.
Eventually, overwhelmed by the frogs' needs, the student made the difficult decision to confine their amphibian
companions within the depths of an engineering classroom closet.

Locked away and feeling abandoned, the frogs harbored resentment towards their former caretaker.
In the confines of the closet, they grew stronger, their hearts filled with a desire for revenge.
They eagerly awaited the day when the closet doors would swing open, granting them freedom and the chance to wreak havoc.

Their prayers were answered when a current student at Clemente, desperately in need of a tub of white paint for her arcade game,
stumbled upon the Arduino Closet. Though the closet had remained untouched for ages, she ventured inside driven by her desperation.
To her surprise, she discovered the five captive frogs awaiting her release.
In recognition of her act of liberation, she was declared the Queen of the Frogs by her newfound amphibious subjects.

Embracing her newfound authority, the Queen of the Frogs commanded her amphibian companions to unleash chaos upon the school.
Their mischief and mayhem transformed the once thriving hallways into desolate corridors, as students and laughter disappeared.

...

*There's also a note on the last page.*

"This tale serves as a reminder that even the best intentions can lead to unintended consequences.
The student's initial act of compassion and care for the frogs had unintended outcomes, culminating in chaos.
It highlights the importance of finding a balance in our actions, considering the long-term consequences and effects on others."
- Mr. Smith
'''
            elif choice == 2:
              story = '''\
*Cryptography w/ Furries: A children's guide to Cryptography*
|DG|*Last checked out by Shrem Masala*|B|

=== TABLE OF CONTENTS ===

Introduction:
Welcome to the magical world of cryptography, where we'll embark on an exciting adventure with our furry friends!
In this children's guide, we'll learn about secret codes, encryption, and decoding messages.
Join the furry characters on a journey filled with mystery and fun!

Chapter 1: Meet the Furry Friends
Introduce the adorable furry characters who will accompany us throughout the book.
Each character represents a different aspect of cryptography, making learning entertaining and engaging.

Chapter 2: The Secret Code Forest
Our furry friends venture into the Secret Code Forest, where they encounter their first challenge.
Learn about the importance of secrecy and how cryptography helps protect sensitive information.

Chapter 3: The Enigma Machine
Meet the tech-savvy furry who introduces the Enigma Machine, a historical encryption device.
Discover how this machine was used during World War II to send secret messages and how it revolutionized cryptography.

Chapter 4: The Cipher Paw Print
Our furry team discovers a mysterious paw print cipher on their adventure.
Dive into the world of substitution ciphers, where letters are replaced with symbols or other letters.
Help the furry friends crack the code and uncover hidden messages!

Chapter 5: The Fur-tastic Transposition Dance
Join the furry characters as they dance their way through a transposition cipher challenge.
Explore the concept of rearranging letters to create secret codes and learn how to decrypt them.

Chapter 6: The Crypto Treasure Hunt
Embark on a thrilling treasure hunt with our furry friends.
Uncover clues hidden within complex cryptographic puzzles like the Caesar cipher,
Vigenère cipher, and even some modern-day algorithms.
Sharpen your problem-solving skills as you solve each challenge!

Chapter 7: Sharing Secrets with Furrsends
Our furry characters explore the importance of securely sharing secrets with trusted friends.
Learn about public-key cryptography and the furry friend who guards the magical key ring!

Chapter 8: The Future of Furriptography
Discover the exciting world of modern cryptography and how it's used to protect information online.
Learn about encryption algorithms, secure communication protocols, and the furry heroes
working behind the scenes to keep our digital world safe.

...

You don't want to read any more.
'''
            elif choice == 3:
              story = '''\
*Color By Number: Furry Edition*
|DG|*Last checked out by Shrem Masala*|B|


'''
            elif choice == 4:
              story = '''\
100 Pages of Onshape
'''
            elif choice == 5:
              story = '''\
Under the Mosquito
'''
            elif choice == 6:
              story = '''\
Monster'''
            elif choice == 7:
              story = '''\
Never Caught (Almost)'''
            elif choice == 8:
              story = '''\
RCMS 2021-2022 Yearbook'''
            elif choice == 9:
              story = '''\
The Constitution of RCMS'''

            storyParagraphs = story.strip().split('\n\n')

            for line in storyParagraphs:
              dialNoSpeaker(line)

class ElevatorClassroom(Classroom):
  def __init__(self):
    self.name = "The Elevator"
    self.locked = [1, 2, 3, 4]

class Room225Classroom(Classroom):
  def __init__(self):
    self.name = "Room 225"
    self.locked = [1, 2, 3, 4, 5]

class Room224Classroom(Classroom):
  def __init__(self):
    self.name = "Room 224 - Maya's Magical Merchandise"
    self.locked = []

  def run(self, player):
    # Clear the map
    clear()

    # Boxed text for room name
    printBoxedText("Room 224 - Maya's Magical Merchandise")
    print() 
    
    # Classroom Description
    printC("This place feels pretty cozy - allegedly, a lot better than Goran's mushy shop.")

    if player.hasFlag("Room224_IntroducedToMaya"):
      choice = dropdownMenu("What will you do?", ["Buy something from Maya", "Ask how items work again", "Leave the classroom"])
      if choice == 3:
        player.classroom = None
        return
      if choice == 1:
        clear()
        availableCrayon = BlueCrayonItem
        if player.timeBefore(90):
          availableCrayon = RedCrayonItem
        elif player.timeBefore(180):
          availableCrayon = OrangeCrayonItem
        elif player.timeBefore(270):
          availableCrayon = YellowCrayonItem
        elif player.timeBefore(360):
          availableCrayon = GreenCrayonItem
        else:
          availableCrayon = PurpleCrayonItem

        runShop([[StrawberryShakeItem, 75, False], [TectonicSnacksItem, 75, False], [PopcornItem, 150, False],\
                 [SmoresItem, 150, False], [availableCrayon, 100, True], [ScrollOfSupportItem, 250, True]],\
                "Maya's Magical Merchandise", "B", player)
      else:
        dial("Maya", "Oh, glad you asked! Items are one of the most versatile utilities in this school.")
        dial("Maya", "Items can be separated into four major categories.")
        dial("Maya", "The first is |R|Battle Items|B|. These can be used in battles to improve your performance.")
        dial("Maya", "|R|Battle Items|B| can have a wide variety of effects, from increasing your boost to dealing damage.")
        dial("Maya", "However, each |R|Battle Item|B| disappears after being used, so use them wisely!")
        dial("Maya", "|Y|Overworld Items|B| are items that have significance with people in this school.")
        dial("Maya", "They can be used to unlock doors, give as gifts to students, and more!")
        dial("Maya", "|G|Collectible Items|B| are items that serve no real significance.")
        dial("Maya", "They're just nice ways to show off your achievements at this school!")
        dial("Maya", "Finally, |LB|Misc Items|B| are items that don't fit into the last three categories.")
        dial("Maya", "|LB|Tickets|B| fall into this category, and can be used to purchase items in shops from other students.")
        dial("Maya", "|BR|Scrolls|B| are also |LB|Misc Items|B|, and permanently raise your max health in battles once acquired!")
        dial("Maya", "In fact, I happen to be selling a |BR|Scroll |B|in my very own shop!")
        dial("Maya", "|BR|Scrolls|B| are quite rare and valuable; you should try to get your hands on any that you might find!")
        dial("Maya", "Welp, that's all that I have to teach you about items.")
        dial("Maya", "You should consider buying some from here; these are the best prices & items you'll find in this school!")   
    else:
      choice = dropdownMenu("What will you do?", ["Talk to Maya", "Leave the classroom"])
      if choice == 2:
        player.classroom = None
        return

      dial("Maya", "Is that... a customer?")
      dial("Maya", "Oh my, this hasn't happened to me in so long.")
      dial("Maya", "This is a momentous occasion, I should’ve had a script prepared.")
      dial("Maya", "Greetings {}! Welcome to Maya’s Magical Merchandise!".format(player.getName()))
      dial("Maya", "Are you in need of any items? I sell all sorts of goodies ranging from community scrolls to Parle-G biscuits.")
      dial("Maya","...")
      dial("Maya","*(Sigh)* It's not the same anymore...")
      dial("Maya","This place used to be thriving! Now it's just me and my elephant stuffed animal.")
      dial("Maya","...")
      dial("Maya","I hate you Goran.")
      choice = dropdownMenu(None,["Goran?","He's a pretty nice guy...", "I hate him too."])
      if choice == 1:
        dial("Maya","Goran? Yeah, I don't like him.")
      elif choice == 2:
        dial("Maya","Oh, he got to you too? No wonder.")
        dial("Maya","You probably don't REALLY know him, though.")
      elif choice == 3:
        dial("Maya", "Yay, finally someone's on my side.")
      dial("Maya","After Goran saw the sucess of my shop, he decided to set up his own near the school's entrance.")
      dial("Maya","People now find his shop more convenient, leaving this place desolate.")
      dial("Maya","WE DON'T EVEN SELL THE SAME ITEMS!")
      dial("Maya","Sorry, I can get a bit temper when mentioning his name.")
      dial("Maya","At least you and Katherine find this place cozy.")
      dial("Maya","Speaking of which...")
      dial("Maya", "If you ever see Katherine, give her this |Y|Chobani Yogurt|B|, she loves the drink.")

      player.giveItem(ChobaniYogurtItem)
      
      printFlair("You Receive a Chobani Yogurt from Maya")
      
      dial("Maya","...                         ")
      dial("Maya","It'll mean a lot if you purchase something here.")
      dial("Maya","No pressure.")
      player.addFlag("Room224_IntroducedToMaya")
      
class Room222Classroom(Classroom):
  def __init__(self):
    self.name = "Room 222"
    self.locked = [1, 2, 3, 4, 5]

class Room221Classroom(Classroom):
  def __init__(self):
    self.name = "Room 221 - The Gameshow Quarters"
    self.locked = [1, 2,4,5]

  def run(self, player):
    clear()

    printBoxedText("Room 220 - The Gameshow Quarters")
    print() 
    
    # Classroom Description
    printC("You're in the... Gameshow Quarters? What does that mean- oh my-\n\nYou can spot Nathan behind a stand donning an exquisite top hat and clutching a thin cane.")
    print()
    printC("Khang and Lillian can be seen behind some smaller stands, seemingly annoyed at Nathan's presence.")
  
    interactionName = "Get Nathan's attention"
    if player.hasFlag("221_Int1_ReceiveAdhesivePrize"):
      interactionName = "Talk to Lillian"
    elif player.hasFlag("Room221_Player_Won_Gameshow"):
      interactionName = "Claim the Grand Prize"
    elif player.hasFlag("Room221_Lillian_Won_Gameshow"):
      interactionName = "Watch Lillian claim the Grand Prize"
      
    choice = dropdownMenu("What do you do?",[interactionName,"Leave the quarters"])
    if choice == 1:
      if player.hasFlag("221_Int1_ReceiveAdhesivePrize"):
        dial("Lillian","I'm pretty sure Khang's getting a long lecture from Nathan...")
        dial("Lillian","Luckily, we won't have to deal with any of that.")
      elif player.hasFlag("Room221_Played_Gameshow"):
        if player.hasFlag("Room221_Player_Won_Gameshow"):
          dialNoSpeaker("You step up to Nathan's stand to receive your prize.")
          dial("Nathan","This should've been you Khang.")
          dialNoSpeaker("Nathan attempts to give you the Gorilla Glue Adhesive but, immediately, revokes it away from you.")
          dial("Nathan","Hang on... this is my gameshow...")
          dial("Nathan","The cameras are off... I don't need to follow through with anything.")
          dial("Katherine","But- but- {} won fair and square!".format(player.name))
          dial("Nathan","Too bad.")
          dialNoSpeaker("Nathan tosses the Gorilla Glue Adhesive to Khang.")
          dial("Khang","Thanks buddy!")
          dial("Lillian","Hang on. You can't do that!")
          dial("Katherine","Yeah, what gives? We need that adhesive urgently!")
          dial("Nathan","What are you going do about it?")
          dial("Katherine","Well- I- I-")
        elif player.hasFlag("Room221_Lillian_Won_Gameshow"):
          dialNoSpeaker("Lillian steps up to Nathan's stand to receive her prize.")
          dial("Nathan","*(Sigh)* This should've been you Khang.")
          dialNoSpeaker("Nathan attempts to hand Lillian the Gorilla Glue Adhesive but, immediately, revokes it away from her.")
          dial("Lillian","Hey! >:(")
          dial("Nathan","Hang on Lillian, this is my gameshow.")
          dial("Nathan","I don't need to follow through with anything!")
          dial("Katherine","But- but- she won it fair and square!")
          dial("Nathan","Too bad.")
          dialNoSpeaker("Nathan tosses the Gorilla Glue Adhesive to Khang.")
          dial("Khang","Thanks buddy!")
          dial("Lillian","Wha- you can't do that!")
          dial("Nathan","What are you going do about it?")
          dial("Lillian","Well- I- I-")
        dialNoSpeaker("All of a sudden, you pull out your wand and aim it directly at Khang.")
        dial("Khang","Huh? You want the adhesive?")
        dialNoSpeaker("You aim the wand more sternly at him.")
        dial("Khang","...")
        dial("Khang","*(Sigh)* If you really want a spell battle, you could've just asked...")

        #if not runBattle(player, KhangBattleStudent()):
        #  return
        # TODO: Implement
        # BTW How much health do Act III students have
        dial("Khang","...")
        dialNoSpeaker("Khang looks down at the Gorilla Glue Adhesive in his arms...")
        dial("Khang","*(Sigh)* That's unfortunate-")
        dial("Nathan","No Khang, don't you dare give them the adhesive!")
        dial("Katherine","Why not?")
        dial("Nathan","This is my gameshow, therefore, my rules are the only rules applicable...")
        dialNoSpeaker("Nathan pulls out his wand menacingly.")
        dial("Nathan","And we don't tolerate rule-breakers here...")
        # TODO: NATHAN BATTLE

        dial("Nathan","bruh.")
        printFlair("You Receive a Gorilla Glue Adhesive!")
        dial("Katherine","Take that Nathan! You're gameshow was rigged anyways!")
        dial("Nathan","-_-")
        dialNoSpeaker("Katherine turns to you and Lillian.")
        dial("Katherine","Nice work guys! ^-^")
        dial("Lillian","Yeah, we definetly outsmarted him!")
        dial("Lillian","Or, I guess, \"out-battled\" him.")
        dial("Lillian","...")
        dial("Lillian","Nice job {}, you're spell casting skills were immaculate!".format(player.name))
        dial("Katherine","Yeah, you're amazing!")
        dialNoSpeaker("You smile in glee. :D")
        dial("Lillian","...")
        dial("Lillian","I'll just sit around here till you need me, this place is pretty cozy!")
        dial("Katherine","Sure, no problem!")
        dial("Lillian","Good luck with collecting the remaining parts!")
        dial("Katherine","Thanks! :)")
        player.addFlag("221_Int1_ReceiveAdhesivePrize")
      else:
        dialNoSpeaker("You raise your hand high in the air, trying to get Nathan's attention.")
        dialNoSpeaker("Nathan spots you and Katherine from the corner of his eye...")
        dial("Nathan","Yo, there's more people here!")
        dial("Nathan","Do you two want to participate in my gameshow?")
        dial("Katherine","Gameshow? Lillian, why would you come here for an adhesive?")
        dial("Lillian","I have my reasons...")
        dial("Nathan","You didn't answer my question man. We only need two more people to begin the gameshow!")
        dial("Katherine","But... what even is this \"gameshow\" about?")
        dial("Nathan","I'm glad you asked.")
        dial("Nathan","\"It's a Game: The Gameshow\" is a game where participants embark on a trivia journey!")
        dial("Nathan","Your goal is to correctly answer questions in order to receive points.")
        dial("Nathan", "The participant that ends up with the highest number of points wins the game and receives the grand prize!")
        dial("Katherine","G- Grand prize? :O")
        dial("Nathan","Of course! The grand prize is this wonderful appliance:")
        dialNoSpeaker("Nathan pulls out a Gorilla Glue Adhesive from beneath his stand.")
        dial("Lillian","You understand why I came here, Katherine?")
        dial("Katherine","Now I do! {}, we're going to win that waterproof adhesive!".format(player.name))
        dial("Khang","Oi, did you forget about me?")
        dial("Katherine","Oh noes.")
        dial("Khang","I'm not sure what you three need that adhesive for, but I have some OSU keyboards that need mending!")
        dial("Katherine","...")
        dial("Katherine","Don't worry guys, it's only Khang, at least we won't be against someone like... Pilliam Wark.")
        dial("Katherine","Speaking of which, I haven't seen Pilliam recently... I wonder what he's up to.")
        dial("Lillian","Haven't you heard? Pilliam's dead, it's all over Current Clemente!")
        dial("Katherine","._.")
        dial("Katherine","I swear to the OnShape gods, everyone's been dying nowadays!")
        dial("Lillian","Tell me about it, this school's getting so rampageous lately-")
        dial("Nathan","Hey! Are we gonna start the game or what? >:(")
        dial("Katherine","Sorry. ._.")
        dial("Nathan","Okay, cue the lights!")
        dialNoSpeaker("Suddenly, the lights in the Gameshow Quarters fade out...")
        dial("Nathan","It's time to play the most popular gameshow ever hosted in Roberto Clemente Middle School!")
        enter()
  
        scores = {
          (player.nameColor, player.name): 0,
          ("PI", "Katherine Xu"): 0,
          ("PU", "Lillian Jauquet"): 0,
          ("LG", "Khang Troung"): 0
        }
  
        def printLeaderboard(scores):
          printC("=== Leaderboard ===", "Y")
          scores_sorted = sorted(scores.items(), key = lambda x : x[1])
          
          printC("|Y|1. {} |B|- {} points".format("|" + scores_sorted[3][0][0] + "|" + scores_sorted[3][0][1] + " " * (30 - len(scores_sorted[3][0][1])), scores_sorted[3][1]))
          printC("|W|2. {} |B|- {} points".format("|" + scores_sorted[2][0][0] + "|" + scores_sorted[2][0][1] + " " * (30 - len(scores_sorted[2][0][1])), scores_sorted[2][1]))
          printC("|BR|3. {} |B|- {} points".format("|" + scores_sorted[1][0][0] + "|" + scores_sorted[1][0][1] + " " * (30 - len(scores_sorted[1][0][1])), scores_sorted[1][1]))
          printC("|DG|4. {} |B|- {} points".format("|" + scores_sorted[0][0][0] + "|" + scores_sorted[0][0][1] + " " * (30 - len(scores_sorted[0][0][1])), scores_sorted[0][1]))
  
        clear()
        printBoxedText("It's A Game: The Gameshow", "Y")
        print()
        printLeaderboard(scores)
        dial("Nathan", "Welcome back to another episode of |Y|It's A Game: The Gameshow|B|, the best trivia game show you'll find at Clemente!")
        dial("Nathan", "Today, we have four contestants competing to earn this episode's grand prize: a full bottle of Gorilla Glue Adhesive.") 
        dial("Nathan", "Let's hear from each of our contestants in more detail.")
        dial("Katherine", "Oh- uh- hi, my name is Katherine! I'm super excited to participate in this-")
        dial("Nathan","Okay, that's enough of you.")
        dial("Katherine","Wait-")
        dial("Nathan","Moving on!")
        dial("Khang", "Greetings! I'm Khang Troung! I play OSU, Tetris.io, and Hypixel Skyblock in my free time!")
        dial("Lillian", "...")
        dial("Nathan","Lillian, you're next!")
        dial("Lillian","Oh... I'd rather skip introductions...")
        dial("Nathan","...")
        dial("Nathan","Fine. -_-")
        dial("Nathan","And last but not least we have... {}!".format(player.name))
        dialNoSpeaker("You timidly wave to the camera in a dark corner of the room.")
        dial("Nathan", "Alright, guys! Now that we've gotten to know each of our four contestants, it's time to start playing!")
        dial("Nathan", "You'll all have to answer the same |W|Ten Trivia Questions|B| independently on your |W|answering device|B|.")
        dialNoSpeaker("Nathan passes a specialized tablet to each of you. It has a glaring yellow logo on the cover...")
        dial("Nathan", "After each round, the correct answer will be revealed and people who answered correctly will get points.")
        dial("Nathan", "The person with the most points at the end wins!")
        dial("Nathan", "Alright guys, that's enough talking... it's time to get solving!")
        enter()
  
        clear()
        printBoxedText("It's A Game: Question #1", "Y")
        print()
        printLeaderboard(scores)
        print()
        printC("Question 1 Scoring: 1 Point")
        choice = dropdownMenu("What is the Law of Cosines?", ["a^2+b^2=c^2", "(ax1+by1+c)/sqrt(a^2+b^2)", "c^2=a^2+b^2-2ab(cosC)", "a/sinA=b/sinB=c/sinC=2"])
  
        dialNoSpeaker("You lock your answer into the device.")
        dial("Nathan", "All right, everyone answered Question #1!")
        dial("Nathan", "The correct answer was |W|c^2=a^2+b^2-2ab(cosC)|B|.")
        dial("Nathan", "Let's see what everyone got...")
  
        if choice == 3:
          dial("Nathan", "{} got it right! They've earned |W|1 point|B|.".format(player.getName()))
          scores[(player.nameColor, player.name)] += 1
        else:
          dial("Nathan", "Looks like {} selected the wrong answer... too bad for them!".format(player.getName()))
        dial("Nathan", "|PI|Katherine|B| got it right, too... she gets |W|1 point|B| as well!")
        dial("Katherine","I knew this one right from the top of my head!")
        dial("Katherine","After all, MAP-M studying has taken up a majority of my free time-")
        dial("Nathan", "Sadly, |PU|Lillian|B| got it correct as well, so she also gets |W|1 point|B|!")
        dial("Lillian","What do you mean by \"sadly\"?")
        dial("Nathan","*(Sigh)* This is why you aren't the fan favorite!")
        dial("Lillian","What-")
        dial("Nathan","Always yelping out nonsensical remarks...")
        dial("Lillian","-_-")
        dial("Nathan","Anyways...")
        dial("Nathan", "|LG|Khang|B| also got it correct as...")
        dial("Nathan", "Wait, my bad... it looks like he selected the wrong answer!")
        dial("Nathan", "He gets no points, but don't worry, he can always catch up in the later rounds!")
        dial("Nathan", "|DG|*Khang you little expired grapefruit... how did you get this question wrong? I literally gave you the answers!*")
        dial("Khang","|DG|*I might've gotten it mixed up with the Law of Sines...*")
        dial("Nathan","|DG|*Oh my days...*")
        enter()
  
        scores[("PI", "Katherine Xu")] += 1
        scores[("PU", "Lillian Jauquet")] += 1
  
        clear()
        printBoxedText("It's A Game: The Gameshow")
        print()
        printLeaderboard(scores)
        print()
        printC("Question 2 Scoring: 1 Point")
        choice = dropdownMenu("What is Ellie's last name?", ["Deshpande", "Huang", "Park", "Rivera"])
  
        dialNoSpeaker("You lock your answer into the device.")
        dial("Nathan", "That's Question #2 done!")
        dial("Nathan", "The correct answer was |W|Huang|B|.")
        dial("Nathan", "To speed things up a bit, we'll be using this specialized projector to show each person's results!")
        dialNoSpeaker("Nathan discreetly clicks a button on his cane to reveal an old clanky projector, and turns it on.")
  
        dial("Nathan","For some reason, most of you decided to choose Park!")
        dial("Nathan","Are you guys stupid?")
        dial("Lillian","... her last name isn't Park?")
        dial("Nathan","-_-")
        if choice == 2:
          dial("Nathan", "{} and |PI|Katherine|B| were the only two to get the question right.".format(player.getName()))
          scores[(player.nameColor, player.name)] += 1
        else:
          dial("Nathan", "Somehow, |PI|Katherine|B| was the only person who got the question right!".format(player.getName()))
        dial("Katherine","I knew becoming best friends with Ellie had its perks!")
        dial("Nathan","Yeah whatever, moving on...")
        dial("Nathan","The next question is a bit tricky so it'll be worth 2 points!")
        enter()
        scores[("PI", "Katherine Xu")] += 1
  
        clear()
        printBoxedText("It's A Game: Question #3", "Y")
        print()
        printLeaderboard(scores)
        print()
        printC("Question 3 Scoring: 2 Points")
        choice = dropdownMenu("On average, how many times does Brooke Yin change her discord status in a day?", ["2", "10", "15", "2763"])
  
        dialNoSpeaker("You lock your answer into the device.")
        dial("Nathan", "The correct answer was |W|2763|B|!")
        dial("Katherine","Wait, what?")
        dial("Khang","Yes! I finally got a question right!")
        dial("Nathan","Thank goodness |LG|Khang|B|, I was worried you'd end up in last place!")
        enter()
        if choice == 4:
          scores[(player.nameColor, player.name)] += 2
        scores[("LG", "Khang Troung")] += 2
        scores[("PU", "Lillian Jauquet")] += 2
  
        clear()
        printBoxedText("It's A Game: Question #4", "Y")
        print()
        printLeaderboard(scores)
        print()
        printC("Question 4 Scoring: 2 Points")
        choice = dropdownMenu("What color straps does Poorvi prefer?", ["Beige", "Blue", "Black", "Pink"])
        dialNoSpeaker("You lock your answer into the device.")
        dial("Nathan", "The correct answer was |W|Beige|B|.")
        dial("Lillian","Phew, I was worried about that one.")
        dial("Katherine","But- but- how was I supposed to know Poorvi's color preferences-")
        dial("Nathan","Moving on! The next question will be worth a whopping 3 points!")
        enter()
        if choice == 1:
          scores[(player.nameColor, player.name)] += 2
        scores[("PU", "Lillian Jauquet")] += 2
  
        clear()
        printBoxedText("It's A Game: Question #5", "Y")
        print()
        printLeaderboard(scores)
        print()
        printC("Question 5 Scoring: 3 Points")
        choice = dropdownMenu("How many zoos are at this school?", ["0", "2", "3", "5"])
        dialNoSpeaker("You lock your answer into the device.")
        dial("Nathan", "The correct answer was |W|3|B|.")
        dial("Katherine","Wait... I actually got it correct?")
        dial("Lillian","Excuse me |Y|Nathan|B|, how on Earth are there any zoos at this school?")
        dial("Nathan","Simple. There's \"Pea Tear Zoo\",\"An Nah Zoo\", and \"Cat Tear Inn Zoo\"!")
        dial("Lillian","Wow. -_-")
        enter()
        if choice == 3:
          scores[(player.nameColor, player.name)] += 3
        scores[("PI", "Katherine Xu")] += 3
        scores[("LG", "Khang Troung")] += 3
  
        clear()
        printBoxedText("It's A Game: Question #6", "Y")
        print()
        printLeaderboard(scores)
        print()
        printC("Question 6 Scoring: 3 Points")
        choice = dropdownMenu("What is Anna (The Wicked Witch)'s last name?", ["Zhao", "Zhou", "Xu", "Klover"])
        dialNoSpeaker("You lock your answer into the device.")
        dial("Nathan", "The correct answer was |W|Zhou|B|!")
        dial("Nathan","Wait... everyone got this question right...")
        if choice == 2:
          scores[(player.nameColor, player.name)] += 3
        else:
          dial("Nathan","Except {}, what a loser!".format(player.getName()))
          dial("Katherine","Hey, don't say that to my friend! >:(")
          dial("Nathan","Whatever...")
        enter()
        scores[("PI", "Katherine Xu")] += 3
        scores[("PU", "Lillian Jauquet")] += 3
        scores[("LG", "Khang Troung")] += 3
  
        clear()
        printBoxedText("It's A Game: Question #7", "Y")
        print()
        printLeaderboard(scores)
        print()
        printC("Question 7 Scoring: 3 Points")
        choice = dropdownMenu("Find the first syntax error in this program:\n\n1    a = 1\n2    b = a\n3    print('100' '200')\n4    b =+ a\n5    a < b > c\n6    a && b", ["Line 3", "Line 4", "Line 5", "Line 6"])
        dialNoSpeaker("You lock your answer into the device.")
        dial("Nathan", "The correct answer was |W|Line 6|B|!")
        dial("Katherine","Yes! I got it correct by guessing!")
        dial("Nathan","*(Sigh)* Khang, how are you getting all of these wrong?")
        dial("Khang","I have... no idea what any of this means.")
        dial("Nathan","Screw this, the next question will be worth 5 points!")
        dial("Katherine","Ooh! :O")
        enter()
        if choice == 4:
          scores[(player.nameColor, player.name)] += 3
        scores[("PI", "Katherine Xu")] += 3
  
        clear()
        printBoxedText("It's A Game: Question #8", "Y")
        print()
        printLeaderboard(scores)
        print()
        printC("Question 8 Scoring: 5 Points")
        choice = dropdownMenu("What is Nathan's favorite color?", ["Red", "Blue", "Yellow", "Green"]) 
        dialNoSpeaker("You lock your answer into the device.")
        dial("Nathan", "The correct answer was |W|{}|B|!".format(["Red", "Blue", "Yellow", "Green"][choice-2]))
        dial("Nathan","Only one person got this question right...")
        dial("Lillian","Seriously |Y|Nathan|B|, did you expect any of us to know this?")
        dial("Nathan","Well, tell that to the person who got it correct...")
        dial("Nathan","Who just so happens to be K-")
        dial("Nathan","KATHERINE?!?!")
        dial("Katherine","Wait- really? I'm amazing! :)")
        dial("Nathan","...")
        dial("Nathan","You know what...")
        dial("Nathan","If any of you get this next question wrong, I'll dock 3 points off your score...")
        dial("Katherine","._.")
        enter()
        scores[("PI", "Katherine Xu")] += 5
  
        clear()
        printBoxedText("It's A Game: Question #9", "Y")
        print()
        printLeaderboard(scores)
        print()
        printC("Question 9 Scoring: 3 Points")
        choice = dropdownMenu("Does Peter Zhao have rizz?", ["Absolutely not.", "Possibly.", "Only when speaking to certain people.", "Of course he does!"])
        dialNoSpeaker("You lock your answer into the device.")
        dial("Nathan", "The correct answer was |W|Of course he does!|B|")
        dial("Katherine","Excuse me? I thought he didn't have any rizz!")
        dial("Lillian","Katherine, don't tell me you're disrespecting the deceased!")
        dial("Katherine","But-")
        dial("Lillian","Shame on you!")
        if choice == 4:
          dial("Nathan","Yeah, shame on you Katherine! You'll be losing 3 points for that unorthodox response!")
          scores[(player.nameColor, player.name)] += 3
        else:
          dial("Nathan","Yeah, shame on you Katherine! You and {} will be losing 3 points for your unorthodox responses!".format(player.getName()))
          scores[(player.nameColor, player.name)] -= 3
        dial("Katherine","TwT")
        scores[("PI", "Katherine Xu")] -= 3
        scores[("PU", "Lillian Jauquet")] += 3
        scores[("LG", "Khang Troung")] += 3
        dial("Nathan","Anyways, onto our final question!")
        dial("Nathan","This one will be worth 10 points so, Khang, you better get it right.")
        dial("Khang","We'll see...")
        enter()
  
        clear()
        printBoxedText("It's A Game: Question #10", "Y")
        print()
        printLeaderboard(scores)
        print()
        printC("Question 10 Scoring: 10 Points")
        choice = dropdownMenu("What generation is the Tiny Bird Pokémon, Natu, from? (If you're seeing this Brooke, you should get this right...)", ["Generation I", "Generation II", "Generation III", "Generation IV"])
        dialNoSpeaker("You lock your answer into the device.")
        dial("Nathan", "The correct answer was |W|Generation II|B|.")
        dial("Lillian","Oh, thank god.")
        dial("Nathan","Sadly, |LG|Khang|B| didn't even answer this question. -_-")
        dial("Khang","I was formulating the answer in my head, I didn't have enough time to finish!")
        dial("Nathan","-_-")
        dial("Nathan","Well, that's okay...")
        if choice == 2:
          scores[(player.nameColor, player.name)] += 10
        scores[("PU", "Lillian Jauquet")] += 10
  
        dialNoSpeaker("Suddenly, rainbow-colored lights start flashing around the room...")
        dial("Nathan", "It's time for the |R|Bo|Y|nu|G|s |B|Ro|PU|un|PI|d|B|!") # also ignore how cursed the formatting on this looks
        dial("Nathan", "This question will be Open-Ended and worth 1,000 points!")
        dial("Nathan", "*|DG|Khang, for the love of all gameshows, you better get this right...*")
        enter()
  
        clear()
        printBoxedText("It's A Game: Bonus Question", "Y")
        print()
        printLeaderboard(scores)
        print()
        printC("Bonus Question Scoring: 1,000 Points")
        printC("\n|R||R|Bo|Y|nu|G|s |LB|Qu|B|es|PU|ti|PI|on: |B|In Hypixel Skyblock, how much does a Griffin Feather cost on the Bazaar?")
        print()
        printC("|B|Enter your answer: ", end="")
        answer = input().strip().lower()
        
        dialNoSpeaker("You lock your answer into the device.")
  
        if "150" in answer:
          dial("Nathan", "The correct answer was |W|151k|B| coins!")
        else:
          dial("Nathan", "The correct answer was |W|150k|B| coins!")
  
        dial("Nathan","Congratulations to the winner of the bonus question, and the winner of this episode...")
        dial("Nathan","...")
        dial("Nathan","Wait, Khang didn't get it?")
        dial("Nathan","|DG|*Khang you expired grapefruit, how did you not get this question right?!?! You literally play Hypixel Skyblock in your sleep!")
        dial("Khang","|DG|*Oh... so that's why I lost money on my investment in Griffin Feathers.*")
        dial("Nathan","|DG|*(sigh)* |B|Well folks, looks like nobody claims the bonus 1,000 points this time.")
        dial("Nathan","Let's just see the results...")
        
        clear()
        printBoxedText("It's A Game: Results", "Y")
        print()
        printLeaderboard(scores)
        print()
        dial("Nathan","...")
        dial("Nathan","|DG|*(obviously faking happiness)*|B| Well, that's a wrap for this week's episode of |Y|It's A Game: The Gameshow|B|!")
        dial("Nathan","|DG|*(obviously faking happiness)*|B| Thanks for watching, everyone, and have a nice rest of your day!")
        dial("Nathan","...")
  
        scores_sorted = sorted(scores.items(), key = lambda x : x[1])
        winner = scores_sorted[3][0]
        if winner[1] == player.name and winner[0] == player.nameColor:
          player.addFlag("Room221_Player_Won_Gameshow")
          dial("Nathan", "Well... congratulations {}... I guess...".format(player.getName()))
          dial("Nathan", "Why don't you come right up to my desk off-stage to claim your grand prize?")
        else:
          player.addFlag("Room221_Lillian_Won_Gameshow")
          dial("Nathan", "Well... congratulations Lillian... I guess...")
          dial("Nathan", "Why don't you come right up to my desk off-stage to claim your grand prize?")
          dial("Lillian","Sure thing!")
        player.addFlag("Room221_Played_Gameshow")
  
      
    elif choice == 2:
      player.classroom = None
      return


class Room220Classroom(Classroom):
  def __init__(self):
    self.name = "Room 220 - The Arcade"
    self.locked = [1,2,3]

  def run(self, player):
    clear()

    printBoxedText("Room 220 - The Arcade")
    print() 
    
    # Classroom Description
    printC("You're in the Arcade! Various engineering arcade games & stalls fill the room.")
    print()  
    printC("You feel excited to play the games and potentially earn some tickets.")
    print()
    printC("(You currently have |W|{}|DG| tickets.)".format(player.tickets))
    choice = dropdownMenu("What arcade game will you play?", ["The PLTW Valley", "OnSpace Mafia", "Stone the House", "Feed the Frogs", "Celestial Mastermind", "The REPLIT Casino: CPU Bar Edition", "... Footy?", "|R|Leave the Arcade"]) 

    if choice == 1:
      printC("\n=== The PLTW Valley ===", "G")
      printC("Cost Type: |G|One-Time Purchase", "DG")
      printC("*An ongoing campaign where you grow engineering products over the school days and sell them for tickets.\nMake sure to check up on your products every three days, or else they'll expire!*", "DG")
      print()
      
      if player.hasFlag("Room220_BoughtPLTWValley"):
        printC("You have already purchased a ticket to this game!", "G")
      else:
        printC("It costs 250 tickets to play this game.", "B")
      
      
      choice = dropdownMenu("Play the Game?", ["|G|Yep!", "|R|Nah I'm Good"])
      
      if choice == 1:
        canPlay = player.hasFlag("Room220_BoughtPLTWValley")
        
        if not canPlay:
          canPlay = player.takeTickets(250)
          if not canPlay:
            dialNoSpeaker("|R|Unfortunately, you don't have enough tickets to play this game.")
          else:
            player.addFlag("Room220_BoughtPLTWValley")

        if canPlay:
          #updateSavefile()
          clear()

          currentTime = int(player.day * 1000 + player.time)
          valley_savefile = "{}_PLTWVALLEY".format(player.name.upper())

          def getValleySavefile(attr):
            try:
              return db["{}_{}".format(valley_savefile, attr)]
            except:
              return None

          def updateValleySavefile(attr, val):
            db["{}_{}".format(valley_savefile, attr)] = val
              
          try:
            assert getValleySavefile("TUTORIAL") != None
          except:
            printBoxedText("The PLTW Valley", "G")
            dial("Aadhavan", "Oh hey, looks like you're new to the |G|PLTW Valley|B|!")
            dial("Aadhavan", "Here in the |G|PLTW Valley|B|, we get around by farming various products!")
            dial("Aadhavan", "These products take a while to farm in the |G|fertile PLTW soil|B|, but you won't be able to find them anywhere else!")
            dial("Aadhavan", "Farming these products are pretty simple; first, buy a sketch plane and plant it, then make sure to check up on it with 3D modeling tools until it's ready for printing!")
            dial("Aadhavan", "But make sure to check up on your products regularly, or else they might develop |R|constraint errors|B| and be ruined!")
            dial("Aadhavan", "You can exchange resources and buy materials over at the |G|OnSpace Plaza|B|, and can also trade your products for |LB|tickets|B|.")
            dial("Aadhavan", "The main currency here is |G|OnSpace Bucks|B|, you can have $100 of them to start.")
            dial("Aadhavan", "Welp, that's all you need to know. Good luck in the |G|PLTW Valley|B|!")

            updateValleySavefile("TUTORIAL", True)
            updateValleySavefile("MONEY", 100)
            updateValleySavefile("CROP_STATUS_1", [True, False, "No Product", 0, 10, 1000, 1000])
            updateValleySavefile("CROP_STATUS_2", [True, False, "No Product", 0, 10, 1000, 1000])
            updateValleySavefile("CROP_STATUS_3", [True, False, "No Product", 0, 10, 1000, 1000])
            updateValleySavefile("CROP_STATUS_4", [False, False, "No Product", 0, 10, 1000, 1000])
            updateValleySavefile("CROP_STATUS_5", [False, False, "No Product", 0, 10, 1000, 1000])
            
            
          loc = 1
          clear()

          money = getValleySavefile("MONEY")
          crops = []
          for i in (1, 2, 3, 4, 5):
            crops.append(list(getValleySavefile("CROP_STATUS_{}".format(i))).copy())

          def getCropString(crop):
            if not crop[0]:
              return "|R|Locked Product Slot"
            else:
              if not crop[1]:
                return "|DG|No Product"
              else:
                if currentTime > crop[6]:
                  return "{}|--| (|R|Expired|--|)".format(crop[2])
                elif currentTime > crop[5]:
                  return "{}|--| ({}/{} Progress, NEEDS CARE, Expires on Day {} {})".format(crop[2], crop[3], crop[4], int(crop[6]/1000), getTimeStringFromInt(crop[6] % 1000))
                else:
                  return "{}|--| ({}/{} Progress, Needs Care at Day {} {})".format(crop[2], crop[3], crop[4], int(crop[5]/1000), getTimeStringFromInt(crop[5] % 1000))


          def calculateNewTime(old, inc):
            old += inc
            if old % 1000 >= 510:
              old += 1000
              old -= 510
            return old
            
          cropTypes = {
            "|BR|Automata Cam": (60, 100),
            "|DB|Engineering Notebook": (80, 300),
            "|G|Figure 4 Onshape": (100, 700),
            "|R|Strawberry Charm": (120, 1500),
            "|Y|Toy Train": (240, 3000)
          }
                  
          while True:
            clear()
            if loc == 1:
              printBoxedText("The PLTW Valley", "G")
              printC("OnSpace Bucks: ${}".format(money))
              printC("Current Time: Day {}, {}".format(int(currentTime / 1000), getTimeStringFromInt(currentTime % 1000)))
              print()
              printC("(1) {}".format(getCropString(crops[0])), "B")
              printC("(2) {}".format(getCropString(crops[1])), "B")
              printC("(3) {}".format(getCropString(crops[2])), "B")
              printC("(4) {}".format(getCropString(crops[3])), "B")
              printC("(5) {}".format(getCropString(crops[4])), "B")
              print()
              choice = dropdownMenu("What will you do?", ["Check on your Product Slots", "Go to the OnSpace Plaza", "Exit Minigame"])
              if choice == 3:
                break

              if choice == 1:
                choice = dropdownMenu("Choose a Product Slot to check on:", ["Slot 1", "Slot 2", "Slot 3", "Slot 4", "Slot 5"])
                print()
                crop = crops[choice-1]
                if not crop[0]:
                  printC("This slot has not been unlocked yet!", "R")
                elif currentTime < crop[5]:
                  printC("This product does not need any care at this time.", "B")
                  choice2 = dropdownMenu("Do you want to destroy this product?", ["|G|Of course not!", "|R|... it needs to go."])
                  if choice2 == 1:
                    printC("\nYou let the product keep evolving.", "B")
                  else:
                    printC("\nFor some reason, you decide to destroy the product, freeing up a production slot.", "R")
                    crops[choice-1] = [True, False, "No Product", 0, 10, 1000, 1000]
                elif currentTime < crop[6]:
                  printC("You carefully extrude, revolve, and sweep the product sketch until it no longer needs care.", "B")
                  printC("It is now on Growth Stage {}/{}!".format(crop[3] + 1, crop[4]), "B")
                  crop[3] += 1
                  crop[5] = calculateNewTime(currentTime, cropTypes[crop[2]][0])
                  crop[6] = calculateNewTime(currentTime, 3000 + cropTypes[crop[2]][0])
                  if crop[3] >= crop[4]:
                    printC("The product is ready for sale!", "G")
                    printC("|B|You earned |G|${}|B| from selling your {}.".format(cropTypes[crop[2]][1], crop[2]))
                    money += cropTypes[crop[2]][1]
                    
                    crops[choice-1] = [True, False, "No Product", 0, 10, 1000, 1000]
                elif not crop[1]:
                  printC("Currently, there is no product being developed in this slot.", "B")
                  printC("Visit the Sketches Stall in the OnSpace Plaza to start development on some new products!", "B")
                else:
                  printC("Unfortunately, the product gained constraint errors after being neglected.", "R")
                  printC("You destroy the product and open up the production slot for another sketch.", "R")
                  crops[choice-1] = [True, False, "No Product", 0, 10, 1000, 1000]

                enter()
              elif choice == 2:
                loc = 2
            elif loc == 2:
              printBoxedText("The OnSpace Plaza", "G")
              printC("OnSpace Bucks: ${}".format(money))
              printC("Current Time: Day {}, {}".format(int(currentTime / 1000), getTimeStringFromInt(currentTime % 1000)))
              print()
              printC("(1) Buy Product Sketches", "B")
              printC("(2) Unlock More Production Slots", "B")
              printC("(3) Convert Onshape Bucks to Tickets", "B")
              print()
              choice = dropdownMenu("What will you do?", ["Go to a Stall", "Go the the PLTW Valley", "Exit Minigame"])
              if choice == 3:
                break

              if choice == 1:
                choice = dropdownMenu("Choose a Stall to go to:", ["Sketches Stall", "Production Slot Stall", "Conversion Stall"])
                if choice == 1:
                  dialNoSpeaker("You walk over to the Sketch Stall...")
                  dial("Aadhavan", "Hi again! Here are some product sketches that you can plant in your valley to start growing them.")
                  choice = dropdownMenu(None, ["Nah I'm Good", "|BR|Automata Cam (FREE, 3 Stages, 60 Min Care Interval, Sells for $100)", "|DB|Engineering Notebook (Costs $50 to Plant, 4 Stages, 80 Min Care Interval, Sells for $300)", "|G|Figure 4 Onshape (Costs $150 to Plant, 5 Stages, 100 Min Care Interval, Sells for $700)", "|R|Strawberry Charm (Costs $250 to Plant, 5 Stages, 120 Min Care Interval, Sells for $1500)", "|Y|Toy Train (Costs $500 to Plant, 6 Stages, 240 Min Care Interval, Sells for $3000)"])

                  plantingSlot = None
                  # Really Inefficient But I'm Lazy
                  if not crops[0][1]:
                    plantingSlot = 0
                  elif not crops[1][1]:
                    plantingSlot = 1
                  elif not crops[2][1]:
                    plantingSlot = 2
                  elif not crops[3][1] and crops[3][0]:
                    plantingSlot = 3
                  elif not crops[4][1] and crops[4][0]:
                    plantingSlot = 4

                  if plantingSlot == None:
                    dial("Aadhavan", "Oops... looks like you don't have any production slots open right now...")
                  else:
                    worked = True
                    if choice == 2:
                      crops[plantingSlot] = [True, True, "|BR|Automata Cam", 0, 3, calculateNewTime(currentTime, 60),  calculateNewTime(currentTime, 1060)]
                    elif choice == 3:
                      if money >= 50:
                        money -= 50
                        crops[plantingSlot] = [True, True, "|DB|Engineering Notebook", 0, 4, calculateNewTime(currentTime, 80),  calculateNewTime(currentTime, 1080)]
                      else:
                        worked = False # okay let me update the code rq
                    elif choice == 4:
                      if money >= 150:
                        money -= 150
                        crops[plantingSlot] = [True, True, "|G|Figure 4 Onshape", 0, 5, calculateNewTime(currentTime, 100),  calculateNewTime(currentTime, 1100)]
                      else:
                        worked = False
                    elif choice == 5:
                      if money >= 250:
                        money -= 250
                        crops[plantingSlot] = [True, True, "|PI|Strawberry Charm", 0, 5, calculateNewTime(currentTime, 120),  calculateNewTime(currentTime, 1120)]
                      else:
                        worked = False
                    elif choice == 6:
                      if money >= 500:
                        money -= 500 # wait don't change this part
                        crops[plantingSlot] = [True, True, "|Y|Toy Train", 0, 6, calculateNewTime(currentTime, 240),  calculateNewTime(currentTime, 1240)]
                      else:
                        worked = False

                    if choice == 1:
                      dial("Aadhavan", "... Then why did you come over here?")
                    elif not worked:
                      dial("Aadhavan", "Sorry, looks like you can't afford that sketch right now.")
                    else:
                      dial("Aadhavan", "Okay, I successfully placed that sketch in Production Slot {}!".format(plantingSlot+1))
                  
                  
                elif choice == 2:
                  dialNoSpeaker("You walk over to the Production Slot Stall...")
                  dial("Akshaj", "Hey there, do you want to be able to produce more things at once?")
                  if crops[3][0] and crops[4][0]:
                    dial("Akshaj", "Oh wait... you already bought the extra PLTW Valley slots...")
                    dial("Akshaj", "Never mind.")
                  elif crops[3][0]:
                    dial("Akshaj", "Looks like you haven't unlocked your fifth PLTW Valley slot.")
                    dial("Akshaj", "I'm willing to open it up for you for $750...")
                    choice = dropdownMenu(None, ["Nah I'm Good", "Sure"])
                    if choice == 1:
                      dial("Akshaj", "... sad.")
                    elif choice == 2:
                      if money >= 750:
                        money -= 750
                        crops[4][0] = True
                        dial("Akshaj", "I've opened up your fifth production slot!")
                      else:
                        dial("Akshaj", "Wait, you can't afford it? Sad.")
                  else:
                    dial("Akshaj", "Looks like you haven't unlocked your fourth PLTW Valley slot.")
                    dial("Akshaj", "I'm willing to open it up for you for $300...")
                    choice = dropdownMenu(None, ["Nah I'm Good", "Sure"])
                    if choice == 1:
                      dial("Akshaj", "... sad.")
                    elif choice == 2:
                      if money >= 300:
                        money -= 300
                        crops[3][0] = True
                        dial("Akshaj", "I've opened up your fourth production slot!")
                      else:
                        dial("Akshaj", "Wait, you can't afford it? Sad.")
                elif choice == 3:
                  dialNoSpeaker("You walk over to the Conversion Stall...")
                  dial("Edem", "Hi there! Would you like to convert your OnSpace Bucks to tickets?")
                  choice = dropdownMenu(None, ["Nah I'm Good", "$100 -> 25 Tickets", "$500 -> 150 Tickets", "$1000 -> 400 Tickets"])
                  if choice == 1:
                    dial("Edem", "Oh... That's okay too!")
                  else:
                    worked = False
                    if choice == 2:
                      if money >= 100:
                        worked = True
                        money -= 100
                        player.giveTickets(25)
                        dialNoSpeaker("Edem trades your $100 for 25 tickets.")
                    elif choice == 3:
                      if money >= 500:
                        worked = True
                        money -= 500
                        player.giveTickets(150)
                        dialNoSpeaker("Edem trades your $500 for 150 tickets.")
                    elif choice == 4:
                      if money >= 1000:
                        worked = True
                        money -= 1000
                        player.giveTickets(400)
                        dialNoSpeaker("Edem trades your $1000 for 400 tickets.")

                    if worked:
                      dial("Edem", "Here you go!")
                    else:
                      dial("Edem", "Sorry, you don't have enough OnSpace Bucks to do that.")
                
                      
                    
                    
              elif choice == 2:
                loc = 1

        updateValleySavefile("MONEY", money)
        updateValleySavefile("CROP_STATUS_1", crops[0])
        updateValleySavefile("CROP_STATUS_2", crops[1])
        updateValleySavefile("CROP_STATUS_3", crops[2])
        updateValleySavefile("CROP_STATUS_4", crops[3])
        updateValleySavefile("CROP_STATUS_5", crops[4])
      else:
        dialNoSpeaker("You decide not to spend your hard-earned tickets on this game.")
    elif choice == 2:
      printC("\n=== OnSpace Mafia ===", "R")
      printC("Cost Type: |G|One-time Purchase", "DG")
      printC("*Save the OnSpace Sketch Plane from the evil Trim Tools! No actual rewards.*", "DG")
      print()

      if player.hasFlag("Room220_BoughtOnspaceMafia"):
        printC("You have already purchased a ticket to this game!", "G")
      else:
        printC("It costs 50 tickets to play this game.", "B")
      
      
      choice = dropdownMenu("Play the Game?", ["|G|Yep!", "|R|Nah I'm Good"])
      
      if choice == 1:
        canPlay = player.hasFlag("Room220_BoughtOnspaceMafia")
        
        if not canPlay:
          canPlay = player.takeTickets(50)
          if not canPlay:
            dialNoSpeaker("|R|Unfortunately, you don't have enough tickets to play this game.")
          else:
            player.addFlag("Room220_BoughtOnspaceMafia")

        if canPlay:
          clear()
          printBoxedText("The OnSpace Mafia", "R")
          print()
          printC("For a long time, the OnSpace Sketch Elements lived together in harmony on the sketch plane.", "B")
          printC("However, unbeknownst to them, some of the Sketch Elements secretly wielded the |R|Trim Tool|B|.", "B")
          printC("These rebellious elements used the |R|Trim Tool|B| to slowly cut away at the other sketch elements.", "B")
          printC("But two other sketch elements also had special tools of their own.", "B")
          printC("One sketch element was bestowed with the |G|Constraint Tool|B|, which allowed them to save any sketch element from being trimmed.", "B")
          printC("The other was bestowed with the |Y|Inspect Tool|B|, which allowed them to see which other sketch elements had certain tools.", "B")
          printC("Can the peaceful sketch elements stop the two rebellious ones from destroying the sketch plane with |R|trims?", "B")
          printC("Or will the rebellious sketch elements |R|trim|B| away the sketch plane and destroy the OnSpace project?", "B")

          printC("\n=== Roles ===", "R")
          printC("Normal Sketch Element - No Special Powers", "B")
          printC("Trim Tool - Choose Sketch Elements to Delete", "R")
          printC("Constraint Tool - Protect a Sketch Element from being Deleted", "G")
          printC("Inspect Tool - See which tools (if any) each Sketch Element has", "Y")
          print()
          printC("For more information on playing OnSpace Mafia, visit the following link below:", "DG")
          printC("https://en.wikipedia.org/wiki/Mafia_(party_game)", "DG")
          print()
          enter()

          import CONTENT_mafia

          res = CONTENT_mafia.runMafiaGame(player.name)

          pass
      else:
        dialNoSpeaker("You decide not to spend your hard-earned tickets on this game.")
    elif choice == 3:
      dialNoSpeaker("|R|This arcade game isn't implemented yet! Sorry!")
    elif choice == 4:
      printC("\n=== Feed the Frogs ===", "G")
      printC("Cost Type: |Y|Tickets Per Play", "DG")
      printC("*Use a magical catapult to launch ping pong balls into *", "DG")
      print()
      
      printC("It costs 25 tickets per game.", "B")
      
      choice = dropdownMenu("Play the Game?", ["|G|Yep!", "|R|Nah I'm Good"])
      if choice == 1:
        canPlay = player.takeTickets(25)
        if not canPlay:
          dialNoSpeaker("|R|Unfortunately, you don't have enough tickets to play this game.")
        else:
          pass
            
      
      else:
        dialNoSpeaker("You decide not to spend your hard-earned tickets on this game.")
    elif choice == 5:
      printC("\n=== Celestial Mastermind ===", "LB")
      printC("Cost Type: |R|Tickets Per Play (Risky)", "DG")
      printC("*Objectively the best game in existence.*", "DG")
      print()
      
      printC("It costs 25 tickets per game.", "B")
      
      choice = dropdownMenu("Play the Game?", ["|G|Yep!", "|R|Nah I'm Good"])
      if choice == 1:
        canPlay = player.takeTickets(25)
        if not canPlay:
          dialNoSpeaker("|R|Unfortunately, you don't have enough tickets to play this game.")
        else:
          clear()
          
          printBoxedText("Celestial Mastermind", "LB")
          printC("\"Inspired\" by Krishan's Mastermind Game", "LB")

          print()
          print()
          
          printC("Instructions (Very Easy to Understand):", "LB")
          try:
            _ = db["{}_GOT_CELESTIALLY_SCAMMED".format(player.name.upper())]
            printC("|W|Krishnan|DG| will choose a five-length code comprising of red, yellow, green, and blue.")
          except:
            printC("|W|Krishnan|DG| will choose a five-length code comprising of red, yellow, and green.")
            
          printC("You will have three guesses to input a correct code using a spell hitbar.")
          printC("If you input the same color three times in a row, you take one damage.")
          printC("Oh yeah, there's also a health bar, because health bars & damage make things cooler.")
          printC("If you input less than three correct colors, |W|Krishnan|DG| will deal one damage to you.")
          printC("However, inputting exactly three correct colors will cause |W|Krishnan|DG| to deal two damage instead.")
          printC("You start with |W|5 health|DG| and heal for 2 health for every red you input in your code.")
          printC("However, if your health goes above 25 or below 2.7, you will die and lose the game.")
          printC("You win if you input the correct color code within five guesses.")
          printC("If you do not guess the correct color within five guesses, you lose as well.")
          printC("Oh yeah, after each turn |W|Krishnan|DG| will give you information on your inputted code.")
          printC("If the code contains the right color in the wrong position, |W|Krishnan|DG| will say the letters |W|abjhwmI|DG| in that order.")
          printC("If the code contains the right color in the right position, |W|Krishnan|DG| will say the letters |W|abjhwm1|DG| in that order.")
          printC("If you win the game, |W|Krishnan|DG| will give you 1,000,000 tickets.")

          print()
          printC("These rules should be pretty simple, if you don't understand them you're a bozo.", "LB")
          printC("Good luck!", "G")

          flush_input()
          enter()
          


          guesses = 0
          correct_code = []
          for i in range(4):
            correct_code.append(random.choice(["|R|R", "|Y|Y", "|G|G"]))
          correct_code.append("|B|B")
          health = 5 
          krishnan_meter = 5
          panic_meter = 10
          rigged_meter = 99
          omkar_meter = 25
          epic_game_meter = 100

          while True:
            krishnan_meter = random.randint(1, 95)
            panic_meter = random.randint(20, 80)
            omkar_meter = random.randint(25, 75)
            
            clear()
            printBoxedText("Celestial Mastermind", "LB")
            print()
            printC("Guesses: {}".format(guesses), "B")
            printC("Health: {}".format(health), "R")
            printC("Krishnan Meter: {}%".format(krishnan_meter), "G")
            printC("Omkar Proximity Meter: {}%".format(omkar_meter), "BR")
            printC("Panic Mode: {}%".format(panic_meter), "PI")
            printC("Rigged Probability: {}%".format(rigged_meter), "R")
            printC("Epicness Meter: {}%".format(epic_game_meter), "PU")
            print()
            printC("Enter a code below:")
            inputted_code = []
            for i in range(5):
              inputted_code.append(("|R|R","|Y|Y","|G|G")[getZone(timedHitbar(1, [3, 3, 3, 3, 3]), [3, 3, 3, 3, 3])])

            printC("You inputted the code: {}".format("".join(inputted_code)))

            inputted_code = "".join(x[3] for x in inputted_code)
            
            # Calculate Code Stats
            colorStreak = 0
            threeInARow = False
            numReds = 0
            lastColor = None
            
            for col in inputted_code:
              if col == "R":
                numReds += 1
                
              if col == lastColor:
                colorStreak += 1
                if colorStreak >= 3:
                  threeInARow = True
              else:
                colorStreak = 1
                lastColor = col

            if threeInARow:
              printC("You inputted the same three colors in a row, taking 1 damage!", "R")
              health -= 1
            if numReds > 0:
              printC("Your code contains |R|{} red(s)|B|, healing you for {} health!".format(numReds, numReds * 2), "B")
              health += numReds * 2

            res = []
            numCorrect = 0
            for i in range(5):
              res.append(inputted_code[i] == correct_code[i][3])
              if res[-1]:
                numCorrect += 1

            printC("\n|W|Krishnan|B| gives you the following feedback on your code:")
            for r in res:
              if r:
                printC("\n|LB|abjhwm1")
              else:
                printC("\n|LB|abjhwmI")

            print()
            if numCorrect < 3:
              printC("Your code had less than three correct colors, so |W|Krishnan|R| deals 1 damage to you!", "R")
              health -= 1
            elif numCorrect == 3:
              printC("Your code had exactly three correct colors, so |W|Krishnan|R| deals 2 damage to you!", "R")
              health -= 2

            if health > 25:
              printC("You became so healthy that you died! Don't question it...", "R")
            elif health < 2.7:
              printC("You died of unhealthiness!!!111!!11", "R")
            elif guesses != 4:
              printC("You got this, keep trying!", "R")
            
            guesses += 1
            enter()
            if health > 25 or health < 2.7 or guesses == 5:
              break

          if guesses == 5:
            printC("You ran out of guesses...", "R")
          print()
          printC("The correct code was {}|DG|.".format("".join(correct_code)), "DG")
          printC("Better luck next time!", "DG")
          enter()
          dial("Krishnan", "... what?")
          dial("Krishnan", "... \"Blue wasn't allowed to be in the code?\"")
          dial("Krishnan", "... Skill issue. You should have read the instructions better.")
          dial("Krishnan", "... what, you \"Couldn't hit blue in the spell bar?\"")
          dial("Krishnan", "... L bozo, there's clearly a blue border on the spell bar.")
          dial("Krishnan", "... If you can't hit it, that's a skill issue.")
          dialNoSpeaker("|R|You walk away upset and feel celestially scammed...")
          db["{}_GOT_CELESTIALLY_SCAMMED".format(player.name.upper())] = True
              
            
      
      else:
        dialNoSpeaker("You decide not to spend your hard-earned tickets on this game.")
    elif choice == 6:
      try:
        if db["{}_ANTICASINOCTRLC".format(player.name.upper())]:
          dial("The Replit Casino", "|Y|...")
          dial("The Replit Casino", "|Y|You think you're clever like that?")
          dial("The Replit Casino", "|Y|Exiting the program right after you realize you've lost, to try to cheat the system?")
          dial("The Replit Casino", "|Y|Well, {}|Y|, let me tell you something...".format(player.getName()))
          dial("The Replit Casino", "|Y|\*ahem\*")
          dial("The Replit Casino", "|Y|Everybody, please put your Chromebooks on the table.")
          dial("The Replit Casino", "|Y|I want to talk about the dangers that come with these Chromebooks that you have in your backpack.")
          dial("The Replit Casino", "|Y|Just recently, a student CHEATED the school by attempting to EXIT the program after gambling away their tickets.")
          dial("The Replit Casino", "|Y|Every year, we see this type of behavior specifically from this group of students.")
          dial("The Replit Casino", "|Y|The eight grade magnet cohort.")
          dial("The Replit Casino", "|Y|And you all are guests in this school. You should be treating this school with respect.")
          dial("The Replit Casino", "|Y|You do not go to an arcade and break a machine after losing your money.")
          dial("The Replit Casino", "|Y|The Pong machine does not like being broken. And you shouldn't either.")
          dial("The Replit Casino", "|Y|Nothing good comes out of 8th grade magnet arcade players. Nothing at all.")
          dial("The Replit Casino", "|Y|And the fact that none of you reported this incident shows how dangerous it is.")
          dial("The Replit Casino", "|Y|Because I'm sure at least one of you saw this dangerous incident.")
          dial("The Replit Casino", "|Y|...")
          dial("The Replit Casino", "|Y|I'd like you to think about what you've done.")
          
          res = min(50, player.tickets)
          player.takeTickets(res)
          dialNoSpeaker("|R|Suddenly, you feel {} tickets vanish from your pocket...".format(res))
          
          dial("The Replit Casino", "|Y|Don't do it again.")
          db["{}_ANTICASINOCTRLC".format(player.name.upper())] = False
          return
      except:
        pass
        
      printC("\n=== The REPLIT Casino: CPU Bar Edition ===", "Y")
      printC("Cost Type: |R|Tickets Per Play (Risky)", "DG")
      printC("*Will the REPLIT CPU bar usage go up or down?\nEarn more tickets with each correct guess, but one wrong one and you lose your winnings!*", "DG")
      print()
      
      printC("It costs 25 tickets per game.", "B")
      
      choice = dropdownMenu("Play the Game?", ["|G|Yep!", "|R|Nah I'm Good"])
      if choice == 1:
        canPlay = player.takeTickets(25)
        if not canPlay:
          dialNoSpeaker("|R|Unfortunately, you don't have enough tickets to play this game.")
        else:
          barUsage = random.randint(5, 20)
          winnings = 0
          winningsPerTurn = 5
          turns = 1

          def won(old, new, guess):
            if guess == 1:
              return new > old
            elif guess == 2:
              return new < old
              
              
          while True:
            clear()
            printBoxedText("The REPLIT Casino", "Y")
            print()
            printC("Current Winnings:  {} Tickets".format(winnings), "B")
            printC("Winnings Per Turn: {} Tickets".format(winningsPerTurn), "B")
            printC("Turn #: {}".format(turns), "B")
            print()
            printC("Replit CPU Usage: {}%".format(barUsage), "B")
            print()
              
            choice = dropdownMenu("|Y|Will the REPLIT CPU Usage |R|increase|Y| or |B|decrease|Y|?", ["|R|Increase", "|B|Decrease", "|Y|Bail Out With Winnings"])
            if choice == 3:
              break

            dialNoSpeaker("|B|Let's see what happens to the CPU bar...")

            cpuResult = random.randint(1, 100)

            if turns <= 2:
              if not won(barUsage, cpuResult, choice) and random.randint(1, 100) < 80:
                cpuResult = random.randint(1, 100)
            elif turns <= 4:
              if not won(barUsage, cpuResult, choice) and random.randint(1, 100) < 60:
                cpuResult = random.randint(1, 100)
            elif turns <= 6:
              if not won(barUsage, cpuResult, choice) and random.randint(1, 100) < 33:
                cpuResult = random.randint(10, 90)
            elif turns <= 8:
              if won(barUsage, cpuResult, choice) and random.randint(1, 100) < 33:
                cpuResult = random.randint(20, 80)
            elif turns <= 10:
              if won(barUsage, cpuResult, choice) and random.randint(1, 100) < 66:
                cpuResult = random.randint(30, 70)
            elif turns <= 13:
              if won(barUsage, cpuResult, choice):
                cpuResult = random.randint(30, 70)
            elif turns <= 16:
              if won(barUsage, cpuResult, choice):
                cpuResult = random.randint(30, 70)
                if won(barUsage, cpuResult, choice):
                  cpuResult = random.randint(30, 70)
            else:
              if won(barUsage, cpuResult, choice):
                cpuResult = random.randint(30, 70)
                if won(barUsage, cpuResult, choice):
                  cpuResult = random.randint(40, 60)

            if not won(barUsage, cpuResult, choice):
              db["{}_ANTICASINOCTRLC".format(player.name.upper())] = True
            
            dialNoSpeaker("|B|The CPU Bar is now at |Y|{}%|B|!".format(cpuResult))
            print()

            if won(barUsage, cpuResult, choice):
              winnings += winningsPerTurn
              turns += 1
              printC("|G|You guessed correctly! Great Job!")
              printC("|B|Your winnings increased by {} tickets!".format(winningsPerTurn))
              enter()
              if turns % 5 == 0:
                winningsPerTurn += 5
                printC("|G|You reached Turn {}!".format(turns))
                printC("|B|Each correct turn now rewards {} tickets!".format(winningsPerTurn))
                enter()
            else:
              winnings = 0
              printC("|R|Oh noes, better luck next time!")
              printC("|R|You lost all your winnings...")
              enter()
              break

            barUsage = cpuResult
            
          
          player.giveTickets(winnings)
          print()
          if winnings != 0:
            printC("|B|You earned {} tickets from the casino!".format(winnings))
            printC("|B|Come again next time to earn even bigger wins!")
          else:
            printC("|B|Don't give up!")
            printC("|B|Remember, 90% of gambling addicts quit right before hitting it big!")
            printC("|DG|~~Presumably.~~")

          enter()
          db["{}_ANTICASINOCTRLC".format(player.name.upper())] = False
      else:
        dialNoSpeaker("You decide not to spend your hard-earned tickets on this game.")
    elif choice == 7:
      dialNoSpeaker("The game doesn't appear to be functional...")
      dialNoSpeaker("There's a note on the cardboard box...")
      dialNoSpeaker("\"Made by Pilliam|DG|... and two others, I guess...|B|\"")
      dialNoSpeaker("|DG|\"The two unnamed individuals completey threw our arcade game ._.\"")
      dialNoSpeaker("|DG|\"Good thing we got to choose our groups for this very computer science game you're playing!\"")
    elif choice == 8:
      dialNoSpeaker("You reluctantly decide to go back to work and leave the Arcade.")
      player.classroom = None
      return
    


class Room219Classroom(Classroom):
  def __init__(self):
    self.name = "Room 219"
    self.locked = [1, 2, 3, 4, 5]

class Room218Classroom(Classroom):
  def __init__(self):
    self.name = "Room 218"
    self.locked = [1, 2, 3, 4, 5]

class Room217Classroom(Classroom):
  def __init__(self):
    self.name = "Room 217"
    self.locked = [1, 2, 3, 4, 5]

class Room216Classroom(Classroom):
  def __init__(self):
    self.name = "Room 216"
    self.locked = [1, 2, 3, 4, 5]

class Room213Classroom(Classroom):
  def __init__(self):
    self.name = "Room 213"
    self.locked = [1, 2, 3, 4, 5]

class Room212Classroom(Classroom):
  def __init__(self):
    self.name = "Room 212"
    self.locked = [1, 2, 3, 4, 5]

class Room211Classroom(Classroom):
  def __init__(self):
    self.name = "Room 211"
    self.locked = [1, 2, 3, 4, 5]


class Room128Classroom(Classroom):
  def __init__(self):
    self.name = "Room 128 - Ms. Presley, Science"
    self.locked = []

  def run(self, player):
    if player.act == 1:
      clear()
      printBoxedText("Room 128 - Ms. Presley's Science Classroom")
      print() 
    
      if not player.questProgressIsAtLeast(IronicCriminalPursuitQuest, 5):
        printC("Unfortunately, the door's locked.\n")
        printC("The door lock seems pretty flimsy, though.")

        if player.questProgressIsAt(IronicCriminalPursuitQuest, 4) and player.hasItem(PaperclipItem):
          print()
          printC("A crowd of three students are standing next to door, watching in awe as Katherine tries to find a way to break in.")
        elif player.getQuestProgress(IronicCriminalPursuitQuest) in [3,4]:
          printC("Katherine's standing next to the door, trying to find a way to break in.")
        else: 
          dialNoSpeaker("If only you knew someone who could lockpick doors...")
          player.classroom = None
          return
      elif player.questProgressIsAt(IronicCriminalPursuitQuest, 5):
        printC("The door's supposed to be locked, but Katherine's broken the lock open.")
        
      interaction = "Talk with Katherine"
      if player.questProgressIsAt(IronicCriminalPursuitQuest, 4):
        interaction = "Give Katherine the Paperclip"
      elif player.questProgressIsAtLeast(IronicCriminalPursuitQuest, 5):
        interaction = "Enter the classroom"
  
      choice = dropdownMenu("What will you do?", [interaction, "Leave"])
      if choice == 2:
        player.classroom = None
        return
      
      if player.questProgressIsAt(IronicCriminalPursuitQuest, 3):
        dial("Katherine","You’re heading to Ms. Presley’s room too?")
        dial("Katherine","She seems to have locked the door but I can hear noises inside.")
        dial("Katherine","If only I had something that could be used as a lockpick... that would be convenient.")
        dial("Katherine","I've heard a |W|paperclip|B| works best.")
        dial("Katherine","May you perhaps find me one?")
        player.incrementQuestProgress(IronicCriminalPursuitQuest)
      elif player.questProgressIsAt(IronicCriminalPursuitQuest, 4):
        if player.hasItem(PaperclipItem):
          dialNoSpeaker("There are now three more people spectating Katherine as she tries to lockpick the door.")
        dial("Katherine","Have you gotten a paper clip yet?")
        if player.hasItem(PaperclipItem):
          dial("Katherine","You have? Great!")
          dialNoSpeaker("You hand the paper clip over to Katherine.")
          player.removeItem(PaperclipItem)
          dial("Peter","I'm not so sure about this... won't Ms. Presley be mad?")
          dial("Poorvi", "Silence Peter, I want to see Katherine partake in criminal activity!")
          dial("Peter","You're endorsing this behavior?")
          dial("Katherine","Peter please, I'm trying to concentrate-")
          dial("Poorvi","Of course! Why wouldn't I be?")
          dial("Poorvi","It makes up for all those times Ms. Presley forgot Valeria was in her Period 5 class.")
          dial("Poorvi","Don't you remember Ella?")
          dial("Ella","...")
          dial("Ella","Guess you forgot that I'm NOT in Period 5...")
          dial("Poorvi","...")
          dial("Poorvi","... right.")
          dial("Poorvi","I couldn't imagine having to do NASA TechRise.")
          dial("Ella","Shut up. -_-")
          dialNoSpeaker("*A click can be heard from the lock.*")
          dial("Katherine","Got it!")
          dialNoSpeaker("Katherine carefully pries the door open, on the other side of the room she can spot Ms. Presley giving her a dirty look.")
          dial("Katherine","Hello Ms. Presley, may I-")
          dial("Ms. Presley","...")
          dial("Ms. Presley","Katherine... locked door means locked door...")
          dialNoSpeaker("Ms. Presley stands up from her seat, walks carefully to the door, then proceeds to slam it shut with full acceleration.")
          dial("Katherine","...")
          dial("Ella","See. This is a prime example of *Katherine Education Syndrome*.")
          dial("Ella","The phenomenon where Katherine becomes so obsessed with her grades that she forgets the littlest bit of common sense.")
          dial("Katherine","...")
          dial("Katherine","Look Ella. Do I look like someone who wants to work at K-Mart?")
          dial("Ella","The heck are you talking about?")
          dial("Ella","Point is, lockpicking didn't solve your issue... at all.")
          dial("Katherine","...")
          dial("Ella","At least when Poorvi and I commit crimes, we have the decency to provide a motive.")
          dial("Peter","C-C-Crimes? What is wrong with you all?")
          dial("Poorvi","Peter... please.") 
          dial("Peter","...")
          dial("Poorvi","Let the adults talk.")
          dial("Katherine","So you're telling me that I shouldn't care about my grades?")
          dial("Ella","Wha- that's not what I said at all!")
          dial("Ella","Can you stop being so difficult?")
          dial("Ella","Poorvi, let's just check up on how Ellie's stealing Ms. Ramasamy's desktop.")
          dial("Poorvi","ELLA!")
          dial("Poorvi","YOU'RE NOT SUPPOSED TO SAY THAT IN FRONT OF EVERYONE!")
          dial("Ella","Heh- big deal, let's go.")
          dial("Poorvi",">:(")
          dialNoSpeaker("Poorvi and Ella leave your view.")
          dial("Katherine","...")
          dial("Katherine","I don't like them.")
          dial("Peter","...")
          dial("Peter","Didn't they say they were going to steal a desktop?")
          dial("Katherine","Oh right... should we... stop them?")
          dial("Peter","Sure, I'm down to mess up anything Poorvi-related.")
          dial("Katherine","And I need to get back on Ms. Ramasamy's good side.")
          dialNoSpeaker("Katherine turns to you.")
          dial("Katherine","Hey, you were pretty helpful...")
          dial("Katherine","...want to stop Poorvi with the two of us?")
          dialNoSpeaker("You nod your head.")
          dial("Katherine","Wonderful!")
          dial("Peter","... who is this?")
          dial("Katherine","Oh they're... uh...")
          dialNoSpeaker("You tell them your name.")
          dial("Katherine","{}? That's nice.".format(player.getName()))
          dialNoSpeaker("Peter and Katherine join your party.")
          player.incrementQuestProgress(IronicCriminalPursuitQuest)
          player.sendEmail(MESAEmail)
        else:
          dial("Katherine", "No? Then go find one!")
      elif player.questProgressIsAtLeast(IronicCriminalPursuitQuest, 5): # interaction 3
        dial("Ms. Presley","Katherine, what did I tell you?")
        dial("Katherine","Sorry.")
        dialNoSpeaker("The three of you leave the classroom.")
        player.classroom = None
        return

    if player.act == 2:
      # Clear the map
      clear()
      # Boxed text for room name
      printBoxedText("Room 128 - Ms. Presley's Science Classroom")
      print()

      if player.hasFlag("128_Int1_OmkarDisruptsLesson") == False:
        printC("Ms. Presley seems to be a doing a demonstration on transpiration using Aloe Vera succulents.")
        print()
        printC("Omkar, Sri, Sherry, and Don have their full attention on the demonstration.")
  
        choice = dropdownMenu("What do you do?",["Pay attention to the demonstration.","Leave the classroom."])
        if choice == 1:
          dial("Ms. Presley","Transpiration is a process that occurs in plants by which plants lose water vapor due to the natural process of evaporation.")
          dial("Ms. Presley","Any questions?")
          dialNoSpeaker("Omkar raises his hand, overshadowing everyone else in the room.")
          dial("Ms. Presley","...")
          dial("Ms. Presley","Anyone else have a question?")
          dial("Sherry","...")
          dial("Don","...")
          dial("Ms. Presley","*(Sigh)*")
          dial("Ms. Presley","What's your question Omkar?")
          dial("Omkar","May I say a joke?")
          dial("Ms. Presley","No-")
          dial("Omkar","Why do plants never reveal their gender?")
          dial("Ms. Presley","...")
          dial("Omkar","Because they are always trans-piring.")
          dial("Ms. Presley","...")
          dial("Ms. Presley","Anyways...")
          dial("Ms. Presley","As you can see in the Aloe Vera plants, the rate of transpiration seems to-")
          dial("Omkar","MS. PRESLEY!")
          dial("Ms. Presley","WHAT.")
          dial("Omkar","SRI KEEPS ON TOUCHING ME!")
          dial("Sri","What, no I'm not-")
          dial("Omkar","HE'S STEALING MY ONSHAPE FIL-")
          dial("Ms. Presley","GOODNESS! I'm tired of you two causing ruckus in my classroom.")
          dial("Ms. Presley","You're even more disruptive than Katherine!")
          dial("Omkar","... and?")
          dial("Ms. Presley","Out. *(Ms. Presley points to her door.)*")
          dial("Omkar","But Sri was-")
          dial("Ms. Presley","Out.")
          dial("Omkar","...")
          dialNoSpeaker("Sri and Omkar look at each other and then proceed to walk straight out of the classroom.")
          dial("Ms. Presley","...")
          dial("Ms. Presley","Are they gone?")
          dial("Ms. Presley","You know what, I'll continute this lab tomorrow.")
          dial("Ms. Presley","The rest of you can open your chromebooks and complete your vocabulary assignment.")
          player.addFlag("128_Int1_OmkarDisruptsLesson")
          player.sendEmail(MESAFollowUpEmail)
        elif choice == 2:
          player.classroom = None
          return

      else:
        printC("Ms. Presley seems to be clicking away on her computer...")
        print()
        printC("A strange noise can be heard from her closet.")
        interaction = None
        if player.hasFlag("128_Int2_UnlockingTheCloset"):
          interaction = "Enter Ms. Presley's closet"
        else:
          interaction = "Investigate the strange noise"
        choice = dropdownMenu("What do you do?",["Ask Ms. Presley about the Aloe Vera Succulents",interaction,"Leave the classroom."])
        if choice  == 1:
          if player.hasFlag("128_Int1_PresleyAloeVera") == False:
            dial("Ms. Presley","Like the one I used in the lab?")
            dial("Ms. Presley","What do you need them for?")
            choice = dropdownMenu(None,["For Ellie Huang","For Ella Park."])
            if choice == 1:
              dial("Ms. Presley","... is she gardening again?")
              dial("Ms. Presley","Well, lucky for her...")
              dial("Ms. Presley","... I have a spare Aloe Vera succulent right here.")
              
              player.giveItem(AloeVeraSucculentItem)
              printFlair("You Receive an Aloe Vera Succulent!")
      
              dial("Ms. Presley","You're welcome!                        ")
              player.addFlag("128_Int1_PresleyAloeVera")
            elif choice == 2:
              dial("Ms. Presley","I know Ella, she doesn't like Aloe Vera.")
          else:
            dial("Ms. Presley","Sorry, I have no more to give her. Please stop asking.")
          
        elif choice == 2:
          if not player.hasFlag("128_Int2_PresleyNeedsLubricant"):
            dialNoSpeaker("You attempt to jostle the handle of the door, it doesn't seem to budge.")
            dial("Ms. Presley","No use in doing that, that door has been locked shut for the past week.")
            dial("Ms. Presley","I've tried loosening the door's handle but none of the products I've tried have worked.")
            dial("Ms. Presley","If you have something up your sleeve, please try it.")
            dial("Ms. Presley","Most of my lab materials are in that room and I urgently need them.")
            dial("Ms. Presley","...")
            dial("Ms. Presley","I've heard lubricant works best but I haven't gotten a hold of some yet.")
            player.addFlag("128_Int2_PresleyNeedsLubricant")
          elif player.hasItem(SpeedcubeLubeItem) or player.hasFlag("128_Int2_UnlockingTheCloset"): 
            if player.hasFlag("128_Int2_UnlockingTheCloset") == False:
              dialNoSpeaker("You apply all the Speedcube Lubricant on the handle and toss it away.")
              player.removeItem(SpeedcubeLubeItem)
              dialNoSpeaker("The door handle finally gives out and you enter the closet.")
              player.addFlag("128_Int2_UnlockingTheCloset")
            player.classroom = ShriramsShadySalesClassroom()
          else: 
            dialNoSpeaker("Try finding some lubricant to loosen the handle.")
            

        elif choice == 3:
          if player.hasFlag("128_Int3_OmkarAndSriBullyYou") == False:
          
            dialNoSpeaker("You leave the classroom.")
            dialNoSpeaker("You spot Omkar and Sri right next the classroom's door.")
            dial("Omkar","See Sri, this is all your fault!")
            dial("Omkar","If you hadn't touched me then we would've been able to complete the lab!")
            dial("Sri","But you were-")
            dialNoSpeaker("Sri makes eye contact with you.")
            dial("Sri","Uhh...")
            dial("Omkar","What?")
            dialNoSpeaker("Omkar makes eye contact with you.")
            dial("Omkar","Oh.")
            dial("Sri","Is Ms. Presley here?")
            dial("Omkar","She... kicked us out a minute ago. -_-")
            dial("Sri","Good. I've been needing to get some free XP.")
            dial("Sri","Come here.")

            if not runBattle(player, SriBattleStudent()):
              return
              
            dial("Sri","...")
            dial("Omkar","Sri, you absolute pungent potato! How did you lose?")
            dial("Sri","Hey man, I'm just special.")
            dial("Omkar","You need special education. -_-")

            player.giveTickets(100)
            printFlair("You earned 100 tickets from the battle!")
            
            player.addFlag("128_Int3_OmkarAndSriBullyYou")
          player.classroom = None
          return

class ShriramsShadySalesClassroom(Classroom):
  def __init__(self):
    self.name = "Shriram's Shady Sales"
    self.locked = [1]

  def run(self, player):
    if player.act == 2:
      clear()
  
      printBoxedText("Room 127 - Shriram's Shady Sales")
      print()

      if not player.hasFlag("127_Int1_BurrosTailAquired"):
        printC("You're in... wait, where are you?")
        print()
        printC("Shriram can be seen huddling around a bunch of strange objects, ignoring your presence.")
  
        choice = dropdownMenu("What do you do?",["Tap Shriram on the shoulder","Leave the closet"])
        if choice == 1:
          dial("Shriram","Huh?")
          dial("Shriram","AHHHH, WHAT IN TARNATION ARE YOU DOING HERE?")
          dialNoSpeaker("Shriram's shriek grabs Ms. Presley's attention.")
          dial("Ms. Presley","Huh?")
          dial("Ms. Presley","Shriram, what are you doing in my closet?")
          dial("Shriram","It's not what it looks like, Ms. Presley.")
          dial("Ms. Presley","And what is this? A list of numerous adjectives?")
          dialNoSpeaker("Ms. Presley wields a piece of paper from the ground.")
          dial("Ms. Presley","Were you the one who's been generating all those adjectives that precede 'scholar' in my slideshows?")
          dial("Shriram","...")
          dial("Ms. Presley","And why would you ever consider \"we the useless scholars\"?")
          dial("Shriram","...")
          dial("Ms. Presley","We're supposed to uplift each other in this classroom!")
          dial("Shriram","...")
          dial("Shriram","But, Ms. Presley, this is my lifestyle!")
          dial("Ms. Presley","How do you even manage this?")
          dial("Shriram","When everyone's gone, I sneak out of this closet to try and scavange leftover food in the Cafeteria.")
          dial("Shriram","Along the way, I try to collect many interesting objects and stash them here.")
          dial("Shriram","Like this one!")
          dialNoSpeaker("Shriram shows you and Ms. Presley a magnetic hourglass.")
          dial("Ms. Presley","You stole that from me. Didn't you?")
          dial("Shriram","Short answer: Yes. Long answer: May I pretty please stay here?")
          dial("Ms. Presley","You know what, I'm impressed with your dedication.")
          dial("Ms. Presley","As long as you keep the closet door open, I'll be happy to let you reside here.")
          dial("Shriram","Thanks!")
          dial("Shriram","Ms. Presley, may I offer you something for your kindness?")
          dial("Ms. Presley","I don't take bribes.")
          dial("Shriram","Aw man.")
          dialNoSpeaker("Shriram turns to you.")
          dial("Shriram","You can have it then.")
          
          player.giveItem(BurrosTailSucculentItem)
          printFlair("You Receive a Burro's Tail Succulent!")
          
          dial("Shriram","I have a lot of these items, I should really sell them.")
          dial("Shriram","Actually, yeah, that is a good idea! Why don't I sell them?")
          dial("Shriram","You can be my very first customer!")
          player.addFlag("127_Int1_BurrosTailAquired")
        elif choice == 2:
          player.classroom = Room128Classroom()
      else:
        player.sendEmail(WantedCriminalEmail)
        printC("Shriram is organizing his products by size, he should really use a sorting algorithm.")
        choice = dropdownMenu("What do you do?",["Purchase something from Shriram","Leave the closet."])
        if choice == 1:
          if player.hasFlag("127_BoughtStolenFurryBook"):
            runShop([(ShriramSpell, 25, True), (BrownCrayonItem, 200, True), (LifeformAnalyzerItem, 250, True)], "Shriram's Shady Sales", "BR", player)
          else:
            runShop([(ShriramSpell, 25, True), (BrownCrayonItem, 200, True), (LifeformAnalyzerItem, 250, True), (StolenFurryBookItem, 400, True)], "Shriram's Shady Sales", "BR", player)
            if player.hasItem(StolenFurryBookItem):
              player.addFlag("127_BoughtStolenFurryBook")
        elif choice == 2:
          player.classroom = Room128Classroom()
         
class Room129Classroom(Classroom):
  def __init__(self):
    self.name = "Room 129"
    self.locked = [1, 2, 3, 4, 5]

class Room130Classroom(Classroom):
  def __init__(self):
    self.name = "Room 130"
    self.locked = [1, 2, 3, 4, 5]

class Room131Classroom(Classroom):
  def __init__(self):
    self.name = "Room 131 - Ms. Santiago, Science"
    self.locked = [1]

  def run(self, player):
    if player.act == 2:
      clear()
  
      printBoxedText("Room 131 - Ms. Santiago's Science Classroom")
      print()

      printC("There seems to be no teacher in the room.")
      print()
      printC("Bryce can be seen analyzing some hydroponic projects.")
      
      choice = dropdownMenu("What do you do?",["Talk to Bryce.","Leave the classroom."])
      if choice == 1:
        if player.hasFlag("131_Int1_BryceMoonCactus") == False:
          dial("Bryce","Have you heard?")
          dial("Bryce","Ms. Presley accidentally ~~sacrificed~~ 'safari-ed' the seventh graders in Africa.")
          dial("Bryce","Guess she misunderstood what Journey to Africa was.")
          dial("Bryce","Wouldn't that have been fun last year?")
          dial("Bryce","A bunch of magnet students... in Africa.")
          dial("Bryce","...")
          dial("Bryce","I'm assuming too much, aren't I?")
          dial("Bryce","...")
          dial("Bryce","Anyways, in the absence of the seventh graders, I'll be monitoring their hydroponics projects.")
          dial("Bryce","(In exchange for SSL hours from Ms. Santiago of coure.)")
          dial("Bryce","Take a look at this one.")
          dialNoSpeaker("Bryce points to a hydroponics project that seems to be cultivating water to grow a beautiful Moon Cactus succulent.")
          dial("Bryce","I couldn't have imagined growing a cactus with hydroponics, wouldn't that be tricky?")
          dropdownMenu(None,["Steal the succulent.","Let the intrusive thoughts win."])
          dial("Bryce","Hey, are you trying to ruin Aryan's hydroponics project?")
          dial("Bryce","Actually, it's Aryan... that's fine-")
          dial("Bryce","Hang on, I'm doing this for SSL hours...")
          dial("Bryce","... that changes everything.")

          if not runBattle(player, BryceBattleStudent()):
            return
            
          dial("Bryce","...")
          dial("Bryce","On the bright side...")
          dial("Bryce","At least it's only Aryan.")

          player.giveItem(MoonCactusSucculentItem)
          printFlair("You Receive a Moon Cactus Succulent!")
          
          player.addFlag("131_Int1_BryceMoonCactus")
        else:
          dial("Bryce","I'm not letting you ruin any more hydroponics projects.")
          dial("Bryce","Go away.")
  
      elif choice == 2:
        player.classroom = None
        return

class Room136Classroom(Classroom):
  def __init__(self):
    self.name = "Room 136"
    self.locked = [1, 2, 3, 4, 5]

class Room137Classroom(Classroom):
  def __init__(self):
    self.name = "Room 137"
    self.locked = [1, 2, 3, 4, 5]

class Room140Classroom(Classroom):
  def __init__(self):
    self.name = "Room 140 - Ms. Poole's"
    self.locked = [1, 2]

  def run(self, player):
    if player.act == 3:
      clear()
  
      printBoxedText("Room 140 - Ms Poole's Computer Science Classroom")
      print()
  
      printC("You're in Ms. Poole's Classroom, the 6th grade computer lab that us 8th graders never had the pleasure of experiencing.")
      print()
      printC("You can spot Ms. Poole, Ryan, Luke, Percy, and Sergi crowded around a long table playing Dungeons & Dragons.")

      choice = dropdownMenu("Entice yourself in the D&D game","Leave the classroom")
      if choice == 1:
        dial("You and Katherine ask if you may join the D&D game.")
        dial("Ms. Poole","Yeah, of course you ca-")
        dial("Ryan","Halt thy adventures!")
        dial("Katherine","Huh?")
        dial("Ryan","For we shall not permit the likes of thee to partake in this noble quest unless thou art endowed with the mettle to brave the treacherous path that unfurls before us!")
        dial("Katherine","I- I don't really- understand what- what- that means.")
        dial("Percy","*(Sigh)* It's just a fancy D&D way of asking if you understand the rules to this game.")
        dial("Ryan","Cease thy tongue noble Percy, this be not a mere game, but a grand adventure thou brimming with the slaying of mighty dragons and the intricate art of... money laundering!")
        dial("Katherine","Uh... may I have a refresher of... thy~ rules? ._.")
        dial("Ryan","It appears thou unworthy of partaking upon this grand adventure. Heneceforth, I bid you scram and venture far, far away!")
        dial("Ms. Poole","Ryan, just give them a chance!")
        dial("Ryan","*(Sigh)* If thy must...")
        dialNoSpeaker("Ryan hands Katherine a D20.")
        dial("Ryan","Behold, let this be a whimsical game of chance! Should thou roll a coveted 20, then thou shalt be granted the honor of participating in our enthralling quest. But should thou roll anything else, then I command thou swiftly depart and find thy adventures elsewhere.")
        dial("Katherine","Umm.. sure!")
        dialNoSpeaker("Katherine rolls the D20... it lands on a {}.".format(random.randint(12, 16)))
        dial("Katherine","*(Sigh)* I'm so unlucky. :(")
        dial("Ryan","It seems the forces of fate have conspired against you. As a consequence, I am left with no choice but to punish thee with a perilous spell battle!")
        dial("Katherine","Uh... no thanks.")
        dial("Ryan","Don't act cowardly under fate!")
        dial("Katherine","...")
        dialNoSpeaker("Katherine hides behind you, afraid of making eye contact with the seemingly possessed Ryan, captivated in his own game.")
        dial("Ryan","I sense timidness coming from thou, thou seems far too weak to be a good opponent against my reign.")
        dial("Katherine","How rude. >:(")
        dial("Ryan","Alas it's true, friend of thou shall henceforth be a much more worthy opponent against I, Die & Reel!")
        dialNoSpeaker("Ryan turns to you.")
        dial("Ryan","How thou feel to be up against thy mighty conqueror?")
        dialNoSpeaker("You stand motionless.")
        dial("Ryan","Ha! Silence belies no weakness within me. A grand mage such as I shalt make thou silenced when thou experiences the wrath of my spells, piercing through you like a thousand silver knives!")
        # TODO: RYAN BATTLE
        dial("Ryan","Well.. that's... not what I expected.")
        dial("Luke","Ryan! You're supposed to stay in character!")
        dial("Ryan","Oh.. right.")
        dial("Ryan","For defeating me, I have deemed thous worthy of such admirable honor!")
        dial("Katherine","So does that mean we can join?")
        dial("Ryan","Ah! In no mind shall I concieve such a vicious thought for you have made nothing more than a fool of me!")
        dial("Ryan","...")
        dial("Ryan","Yet I respect that.")
        dialNoSpeaker("Ryan hands you and Katherine each a paper bag, containing one D20.")
        dial("Ryan","Why don't thous start thy adventure for thouselves?")
        
        
    
      elif choice == 2:
        player.classroom = None
        return

class Room143Classroom(Classroom):
  def __init__(self):
    self.name = "Room 143 - Anna's Hideout"
    self.locked = [3]

  def run(self, player):
    if player.act == 1:
      clear()
  
      printBoxedText("Room 143 - Anna's Hideout")
      print()
  
      printC("Be real, you don’t know what this room is for either.")
      print()
      printC("You can spot Anna in the corner of the room doing some math work.")
  
      choice = None
      if player.questProgressIsAt(IronicCriminalPursuitQuest, 6):  
        choice = dropdownMenu("What do you do?",["Ask Anna what she's doing.","Ask Anna why she's here.","Ask Anna about her Replit account.","Leave the classroom."])
        if choice == 4:
          player.classroom = None
          return
      else:
        choice = dropdownMenu("What do you do?",["Ask Anna what she's doing.","Ask Anna why she's here.","Leave the classroom."])
        if choice == 3:
          player.classroom = None
          return
  
      if choice == 1:
        if player.questProgressIsAtLeast(IronicCriminalPursuitQuest, 5): 
          dial("Anna","I’m doing Peter’s AoPS homework.")
          dial("Peter","._.")
          dial("Katherine","What... Peter? Getting other people to do your homework for you? I can’t believe you!")
          dial("Katherine","Have you forgotten academic integrity?")
          dial("Peter","Uh... I have many volleyball games to worry about.")
          dial("Katherine","That’s not an excuse! My mother made me sign up for twenty-five different extracurriculars since colleges apparently look for that.")
          dial("Katherine","Even so, I still get my work done.")
          dial("Peter","... you’re... literally Katherine.")
          dial("Katherine","Glad you’ve noticed.")
        else:
          dial("Anna","Erm...")
          dial("Anna","I’m doing Peter’s AoPS homework.")
          dial("Anna","Indeed so. He lacks any motivation to do it since he’s always busy practicing for his volleyball tournaments.")
          dial("Anna","Hey, at least I get good Precalculus practice.")
  
      elif choice == 2:
        if player.questProgressIsAtLeast(IronicCriminalPursuitQuest, 5):
          dial("Anna","Um... I live here now!")
          dial("Katherine","You... what?")
          dial("Anna","Sometimes, I don’t feel like doing anything; I’ve practically given up on the cello.")
          dial("Anna","I just sit here and do nothing. It’s nice.")
          dial("Peter","Anna, you’re really boring.")
          dial("Anna","Peter, your entire personality is about volleyball, despite that, you’re not even better than Sherry.")
          dial("Peter","...that’s not very nice. TwT")
          dial("Anna","It’s okay Peter, at least you’re better than Katherine.")
          dial("Katherine",".-.")
          player.sendEmail(BrainSTEMOrderEmail)
          player.sendEmail(BrainSTEMOrderFollowUpEmail)
        else:
          dial("Anna","Um... this is my home.")
          dial("Anna","I’m not answering any questions, thank you for your cooperation.")
  
      elif choice == 3:
        if player.hasFlag("143_Int3_MasterKeysCollected") == False:
          dial("Anna","My... my Replit account? Well, I’ve followed Peter, Katherine, but not-")
          dial("Katherine","You followed me? How did you even-")
          dial("Anna","I stalk people for a living.")
          dial("Katherine","I’m impressed.")
          dialNoSpeaker("The sound of students chattering can be heard outside the room.")
          dial("Akshaj","*(From outside)* Is that every classroom on the list?")
          dial("Sayf","*(From outside)* Not yet, we’re still missing 143.")
          dialNoSpeaker("Akshaj and Sayf open the door to the classroom and look around.")
          dial("Sayf","...")
          dial("Sayf","Where’s the teacher?")
          dial("Anna","Uh.. the teacher? Yeah... uhh... they're just uhhh...")
          dial("Peter","There isn't any teacher.")
          dial("Sayf","That's unfortunate.")
          dial("Sayf","Ms. Palank wanted us to hand out yearbook permission forms to every teacher.")
          dial("Sayf","Sorry for bothering you.")
          dialNoSpeaker("Akshaj and Sayf turn around to leave the room, the sound of keys rattling can be heard from Sayf’s pocket.")
          dial("Peter","...")
          dial("Peter","Hey- wait.")
          dial("Sayf","What is it?")
          dial("Peter","Do you have keys in your pocket?")
          dial("Sayf","...")
          dial("Sayf","...these?")
          dialNoSpeaker("Sayf pulls out the keys from his pocket.")
          dial("Sayf","These are the master keys.")
          dial("Sayf","They pretty much unlock every classroom in the school.")
          dial("Sayf","Ms. Palank gave them to us for temporary use.")
          dial("Peter","...")
          dial("Peter","This might sound of the blue but... may we borrow them?")
          dial("Sayf","...")
          dial("Sayf","...of course not!")
          dial("Sayf","Why do you even need them?")
          dial("Peter","...")
          dial("Katherine","Poorvi shenanigans.")
          dial("Sayf","...huh?")
          dial("Sayf","Look, we kinda need to give these back to-")
          dial("Akshaj","*(Interrupting him)* If you really want those keys then you're going to have to battle the both of us!")
          dial("Sayf","...")
          dial("Sayf","Excuse me-")
          dial("Katherine","Deal!")
          dial("Sayf","Akshaj you dimwit, what are you doin-")
          dial("Katherine","{}, you’re the best at spell battles here, you got this right?".format(player.getName()))
          dialNoSpeaker("You nod your head.")
          dial("Akshaj","Easy.")
          dial("Akshaj","I’ll go first, then Sayf.")
          dial("Akshaj","If you defeat the both of us then you get the keys.")
          dial("Sayf","Bro-")
          dial("Akshaj","Bring it on!")

          if not runBattle(player, AkshajBattleStudent()):
            return
          
          dial("Akshaj","... darn it.")
          dial("Akshaj","Sayf, you’re up next.")
          dial("Sayf","...")
          dial("Sayf","... fine. -_-")

          if not runBattle(player, SayfBattleStudent()):
            return
                      
          dial("Sayf","Akshaj, you dimwit! This was a terrible idea.")
          dial("Akshaj","Come on, we have to keep our promise.")
          dial("Akshaj","Give them the keys!")
          dial("Sayf","This is your fault.")
          printFlair("You receive the Master Keys")
          player.giveItem(MasterKeysItem)
          dial("Katherine","We’ll promise to give them back... eventually.")
          dial("Sayf","You better.")
          dial("Sayf","Otherwise, Ms. Palank’s going to commence the sixth major mass extinction upon this school.")
          dial("Peter","...")
          dial("Peter","If she does, tell her to specifically target Poorvi.")
          dial("Akshaj","...")
          dial("Akshaj","... no.")
          dialNoSpeaker("Sayf and Akshaj leave the classroom, shutting the door behind them.")
          dial("Anna","...")
          dial("Anna","...that was weird.")
          player.addFlag("143_Int3_MasterKeysCollected")
          player.incrementQuestProgress(IronicCriminalPursuitQuest)
          player.sendEmail(BaldastanEmail)
        else:
          dial("Anna","My replit account is very secretive.")
          dial("Katherine","._.")
          
    if player.act == 2:
      # Clear the map
      clear()
  
      printBoxedText("Room 143 - Anna's Hideout")
      print()
  
      printC("Be real, you don’t know what this room is for either.")
      print()
      printC("You can spot Anna in the corner of the room doing some math work.")  
      dial("Anna","Please, leave me alone.")
      dial("Anna","I'm busy.")
      dial("Anna","Thanks.")
      player.sendEmail(NameChangeEmail)
      player.classroom = None
      return

class Room145Classroom(Classroom):
  def __init__(self):
    self.name = "Room 145"
    self.locked = [1, 2, 3, 4, 5]

class Room146Classroom(Classroom):
  def __init__(self):
    self.name = "Room 146"
    self.locked = [1, 2, 3, 4, 5]

class Room147Classroom(Classroom):
  def __init__(self):
    self.name = "Room 147"
    self.locked = [1, 2, 3, 4, 5]

class Room148Classroom(Classroom):
  def __init__(self):
    self.name = "Room 148 - Mr. Kepler, English"
    self.locked = [1, 2, 3, 4, 5]

class Room149Classroom(Classroom):
  def __init__(self):
    self.name = "Room 149"
    self.locked = [1, 2, 3, 4, 5]

class Room150Classroom(Classroom):
  def __init__(self):
    self.name = "Room 150"
    self.locked = [1, 2, 3, 4, 5]

class Room154Classroom(Classroom):
  def __init__(self):
    self.name = "Room 154 - Ms. MacDonald, History"
    self.locked = [1, 2, 3, 4, 5]

class Room155Classroom(Classroom):
  def __init__(self):
    self.name = "Room 155"
    self.locked = [1, 2, 3, 4, 5]

class Room156Classroom(Classroom):
  def __init__(self):
    self.name = "Room 156"
    self.locked = [1, 2, 3, 4, 5]

class Room126Classroom(Classroom):
  def __init__(self):
    self.name = "Room 126"
    self.locked = [1, 2, 3, 4, 5]

class Room125Classroom(Classroom):
  def __init__(self):
    self.name = "Room 125"
    self.locked = [1, 2, 3, 4, 5]

class Room124Classroom(Classroom):
  def __init__(self):
    self.name = "Room 124"
    self.locked = [1, 2, 3, 4, 5]

class Room122Classroom(Classroom):
  def __init__(self):
    self.name = "Room 122"
    self.locked = [1, 2, 3, 4, 5]

class Room121Classroom(Classroom):
  def __init__(self):
    self.name = "Room 121 - Ms. Palank"
    self.locked = []

  def run(self, player):
    if player.act == 1:
      print()
      printC("Unfortunately, the door's locked.")
      input()
  
      if player.hasFlag("113_Int1_BrookeSSLForms"):
        dial("Katherine","Darn...")
        dial("Peter","Are you kidding me?")
        dial("Katherine","We should come back later.")
        dial("Katherine","These forms are already overdue as is, it won’t hurt.")
  
      player.classroom = None
      return
    if player.act == 2:
      clear()
      printBoxedText("Room 121 - Ms. Palank's English Classroom")
      print()

      printC("Ms. Palank seems to be in a bad mood...")
      
      if player.hasFlag("236A_Int2_PilliamLeavesClassroom") and player.hasFlag("121_Int1_PilliamDies") == False:
        print() 
        printC("Pilliam can be seen helping Ms. Palank with her email.")
        choice = dropdownMenu("What do you do?",["Talk to Ms. Palank","Leave the classroom."])
        if choice == 1:
          dial("Pilliam","And you used the wrong form of there/their/they're again, let me fix that real quick.")
          dial("Ms. Palank","... right.")
          dial("Pilliam","Okay, the email looks fine from what I can tell.")
          dial("Ms. Palank","Thanks Pilliam!")
          dial("Pilliam","You're welcome, I guess...")
          dial("Ms. Palank","Here, I have a gift for you:")
          dialNoSpeaker("Ms. Palank brings out a potted |R|Strawberry-Colored Succulent|B| and hands it to Pilliam.")
          dial("Pilliam","..!")
          dial("Pilliam","Thank you so much!")
          dial("Pilliam","This should complete my collection of 175 red berries.")
          dial("Ms. Palank","Oh yeah, make sure to cut the grass in the pot regularly so it doesn't grow too much.")
          dial("Pilliam","...")
          dial("Pilliam","...")
          dial("Pilliam","...")
          dial("Pilliam","*WHAT-*")
          
          dialNoSpeaker("|R|Pilliam has an allergic reaction from close proximity to the grass and dies.")
          dial("Ms. Palank", "...")
          dial("Ms. Palank","Why is he on the floor? There's tons of germs there!")
          dial("Ms. Palank","Is he always this overreactive?")
          dialNoSpeaker("Ms. Palank turns to you.")
          dial("Ms. Palank","Since Pilliam won't accept my gift, I guess you can have it.")

          player.giveItem(StrawberrySempervivumSucculentItem)
          
          printFlair("You receive a Strawberry Sempervivum Succulent from Ms. Palank.")
          player.incrementQuestProgress(GrammarCheckerQuest)
          player.addFlag("121_Int1_PilliamDies")
        elif choice == 2:
          player.classroom = None
          return
      else:
        choice = dropdownMenu("What do you do?",["Ask Ms. Palank something.","Leave the classroom."])
  
        if choice == 1:
          if player.hasItem(SSLFormsItem):
            choice = dropdownMenu("What do you ask?",["Do you need any help?","About those master keys...","May I turn in these SSL forms for Brooke?"])
          else:
            choice = dropdownMenu("What do you ask?",["Do you need any help?","About those master keys..."])
          if choice == 1: 
            if player.hasFlag("121_Int1_PilliamDies"):
              dial("Ms. Palank","The only help I need is getting Pilliam Wark off my floor.")
              dial("Ms. Palank","Although, that may look incriminating...")
            elif player.hasFlag("121_Int1_PilliamBestFriend") == False:
              dial("Ms. Palank","Help?")
              dial("Ms. Palank","Of course I need help! I'm a teacher!")
              dial("Ms. Palank","Ah, I'm just joking.")
              dial("Ms. Palank","I do have this email I've wrriten...")
              dial("Ms. Palank","Just need to make sure it's professional enough.")
              dial("Ms. Palank","...")
              dial("Ms. Palank",".. do you know Pilliam Wark by any chance?")
              dial("Ms. Palank","He's my best friend, I know he's capable of perfecting my writing.")
              dial("Ms. Palank","If so, may you bring him here?")
              dial("Ms. Palank","Thank you.")
              player.addFlag("121_Int1_PilliamBestFriend")
              player.startQuest(GrammarCheckerQuest)
            else:
              dial("Ms. Palank","My best friend needs to help me... not you.")
          elif choice == 2:
            dial("Ms. Palank","...")
            dial("Ms. Palank","So you were the fool who stole my master keys from those yearbook kids...")
            dial("Ms. Palank","What's that? You don't have them anymore?")
            dial("Ms. Palank","I expect those keys to be in my hand soon.")
            dial("Ms. Palank","Otherwise, I might just have to commence the sixth major mass extinction...")
          elif choice == 3:
            dial("Ms. Palank","Sure, let me see them.")
            dialNoSpeaker("You hand Ms. Palank Brooke's SSL forms.")
            player.removeItem(SSLFormsItem)
            dial("Ms. Palank","...")
            dial("Ms. Palank","...these are overdue by a year!")
            dial("Ms. Palank","Even worse, she didn't even complete the bottom section.")
            dialNoSpeaker("Ms. Palank turns to her shredder and shreds Brooke's SSL forms.")
            dial("Ms. Palank","Tell her to complete the forms again, this time correctly.")
            printFlair("You Receive Brooke's Shredded SSL Forms")
            player.giveItem(ShreddedSSLFormsItem)
            player.incrementQuestProgress(OverdueSSLFormsQuest)
        elif choice == 2:
          player.classroom = None
          return
  
class Room120Classroom(Classroom):
  def __init__(self):
    self.name = "Room 120 - Mr. Smith, English"
    self.locked = [1]

  def run(self, player):
    if player.act == 2:
      clear()
  
      printBoxedText("Mr. Smith's English Classroom")
      print() 
      printC("Mr. Smith is currently teaching the class what an indefinite article is.")
      player.sendEmail(PoolesvilleAcceptanceEmail)

      choice = dropdownMenu("What do you do?",["Listen to the lesson.","Play loud Deltarune music.","Leave the classroom."])
      if choice == 1:
        if player.hasFlag("120_Int1_SmithPhoneTangent") == False:
          dial("Mr. Smith","I don't understand how none of you know what an indefinite article is.")
          dial("Mr. Smith","You know the reason for that?")
          dial("Mr. Smith","It's because of those darn cell phones.")
          dial("Mr. Smith","When I taught back in Florida, almost everyone I knew talked face to face.")
          dial("Mr. Smith","Now, people text each other even when they're sitting beside one another.")
          dial("Mr. Smith","Why don't you all just quit-")
          dial("Mr. Smith","Hang on, William, are you on your phone?")
          dial("William","My bad.")
          dialNoSpeaker("William attempts to put his phone away but it's evident that he's still squinting at it.")
          dial("Mr. Smith","These phones are the devil. -_-")
          player.addFlag("120_Int1_SmithPhoneTangent")
        else:
          dial("Mr. Smith","Where was I again?")
          dial("Akshaj","Indefinite articles?")
          dial("Mr. Smith","Right, how could I forget.")
      elif choice == 2:
        if player.hasFlag("120_Int1_WilliamSacrificesKing") == False:
          dialNoSpeaker("You decide to play Pandora's Palace at full volume.")
          dial("Mr. Smith","Hey, turn that down.")
          dial("William","...")
          dial("William","THAT... THAT OBNOXIOUS MUSIC CAUSED ME TO BLUNDER IN CHESS!")
          dial("William","MY ELO IS TANKED NOW!")
          dialNoSpeaker("William turns to you.")
          dial("William","I'M GONNA HAVE TO SACRIFICE YOU LIKE HOW YOU MADE ME SACRIFICE MY KING!")

          if not runBattle(player, WilliamBattleStudent()):
            return
          
          dial("William","... seriously?")

          player.giveTickets(100)
          printFlair("You earned 100 tickets from the battle!")
          
          player.addFlag("120_Int1_WilliamSacrificesKing")
        else:
          dialNoSpeaker("You decide to play Pandora's Palace at full volume.")
          dial("Mr. Smith","Do you want me to confiscate your phone or not?")
      elif choice == 3:
        player.classroom = None
        return
          

        


class Room119Classroom(Classroom):
  def __init__(self):
    self.name = "Room 119"
    self.locked = [1, 2, 3, 4, 5]

class Room118Classroom(Classroom):
  def __init__(self):
    self.name = "Room 118"
    self.locked = [1, 2, 3, 4, 5]

class Room117Classroom(Classroom):
  def __init__(self):
    self.name = "Room 117 - Ms. Mahon, History"
    self.locked = []

  def run(self, player):
    if player.act == 1:
      # Clear the map
      clear()
  
      # Boxed text for room name
      printBoxedText("Room 117 - Ms. Mahon's History Classroom")
      print() 
      
      # Classroom Description
      printC("You're in Ms. Mahons's room... she seems to be teaching the class about popular sovereignty for the seventh time.")
  
      choice = dropdownMenu("What do you do?",["Read the memes on the board.", "Pay attention to the lesson.","Airdrop a video of the Water Cycle Song to everyone.","Leave the classroom."])
  
      if choice == 1:
        dialNoSpeaker("You read the “hilarious” memes that are on the board.")
        dialNoSpeaker("“What is Pilliam always so punctual? Because he can easily find a Park-ing spot.”")
        dialNoSpeaker("“What is nearly impossible to defeat Lillian? Because NPCs can respawn.”")
        dialNoSpeaker("“Why did Arjun become a detective? Because he can easily quack the case.”")
        dialNoSpeaker("“Why did Poorvi not attend the school dance? Because it was fully book-ed.”")
        dialNoSpeaker("You’re dying of laughter. -_-")
      elif choice == 2:
        if player.hasFlag("117_Int2_ValeriaGetsIgnored") == False:
          dial("Ms. Mahon","Alright class, does anyone know what the Kansas-Nebraska Act instituted?")
          dial("Ms. Mahon","I’ll give you a hint, it’s two words.")
          dialNoSpeaker("No one raises their hand.")
          dial("Ms. Mahon","Wow, in my other periods, everyone’s hands were up.")
          dialNoSpeaker("Still, no one raises their hand.")
          dial("Ms. Mahon","...")
          dial("Ms. Mahon","... I’ll offer candy to anyone who answers.")
          dialNoSpeaker("Everyone’s hands shoot up.")
          dial("Ms. Mahon","There we go, let’s see...")
          dial("Ms. Mahon","Poorvi, why don’t you answer the question?")
          dial("Valeria","Poorvi isn’t here Ms. Mahon. -_-")
          dial("Ms. Mahon","Sorry about that, it’s my natural instinct to call on her.")
          dial("Ms. Mahon","Let’s see...")
          dial("Ms. Mahon","Aadhavan, why don’t you answer?")
          dial("Valeria","Aadhavan also isn’t here. -_-")
          dial("Ms. Mahon","Gosh, my natural instincts are getting the better of me.")
          dial("Valeria","You can always call on me Ms. Mahon!")
          dial("Ms. Mahon","No.")
          dial("Ms. Mahon","Hmmm... Edem what do you have to say?")
          dial("Valeria","EDEM ALSO ISN’T HERE! JUST CALL ON ME!")
          dial("Ms. Mahon","*(Sigh)* Guess no one knows the answer.")
          dial("Valeria","WHAT!")
          dial("Ms. Mahon","It’s popular sovereignty by the way. Seriously, it’s all that we’ve been talking about.")
          dial("Valeria",">:(")
          dial("Valeria","I’m going to kill someone.")
          dial("Ariam","See something, say something. Am I right?")
          dial("Valeria","It’s an idiom. -_-")
          player.addFlag("117_Int2_ValeriaGetsIgnored")
        else:
          dial("Valeria","No one cares about me. :(")
          if player.questProgressIsAtLeast(IronicCriminalPursuitQuest, 5):
            dial("Peter","Tell me about it-")
            dial("Valeria","Peter, this is not your time to talk!")
            dial("Peter","Wow.")
      elif choice == 3:
        if player.questProgressIsAtLeast(IronicCriminalPursuitQuest, 5):
          if player.hasFlag("117_Int3_AirdroppingWaterCycleSong") == False:
            dial("Peter","That’s an amazing idea!")
            dial("Katherine","... what?")
            dial("Peter","Come on, it’ll be funny.")
            dial("Peter","Think of Ms. Mahon’s face when she hears The Water Cycle Song playing in all directions.")
            dial("Katherine","Well, alright.")
            dial("Katherine","Do you have an iPhone?".format(player.getName()))
            dial("Katherine","No? Then how are we going to airdrop anything?")
            dial("Peter","Can’t we use your phone?")
            dial("Katherine","My mom stole my phone after she saw that my grade in computer science was a 99.78.")
            dial("Katherine","Don’t you have a phone Peter?")
            dial("Peter","Well... I do. But I don’t really want to use it right now.")
            dial("Katherine","I’m not going to check your search history and, come on, you said you wanted to do it.")
            dial("Peter","Well.. fine.")
            dialNoSpeaker("Peter hands Katherine his phone.")
            dial("Katherine","I lied, I’m curious what you search up.")
            dial("Peter","Wait, no-")
            dial("Katherine","“How to rizz someone up?” Excuse me?")
            dial("Peter","Uh-")
            dial("Katherine","Peter, you’re weird.")
            dial("Peter","Just airdrop the video and give me my phone back.")
            dial("Katherine","Fine.")
            dialNoSpeaker("Katherine airdrops the video of The Water Cycle Song.")
            dialNoSpeaker("Suddenly, the water cycle song can be heard at full volume all throughout the classroom. The sound ruptures everyone’s eardrums.")
            dial("Ariam","AHHHH, WHAT’S THAT?")
            dial("Valeria","My ears are bleeding. Make it stop.")
            dial("Ms. Mahon","Gosh, what is that?")
            dialNoSpeaker("Everyone frantically silences their phone to nullify the ear-screeching noise of the water cycle moving up and down and all around.")
            dial("Ariam","DO YOU KNOW WHO AIRDROPPED THAT? I’M GOING TO TWIST THEM INTO A PRETZEL.")
            dial("Valeria","It says here it came from... *TheVolleyballAceMan*.")
            dial("Ms. Mahon","I wonder who that could be.")
            dial("Ms. Mahon","... Peter.")
            dial("Peter","...")
            dial("Ms. Mahon","What do you have to say for yourself?")
            dial("Peter","... Katherine made me do it.")
            dial("Ms. Mahon","Oh my god, always blaming everyone.")
            dial("Valeria","Peter, we know it’s you. You don’t have to hide it.")
            dial("Peter","But-")
            dial("Valeria","Who else would *TheVolleyballAceMan* be?")
            dial("Peter","... Sherry?")
            dial("Valeria","-_-")
            dial("Ariam","PETER, I’M GOING TO KILL YOU!")
            dial("Ariam","THANKS TO YOU, I HAVE STAGE 4 EAR CANCER!")
            dialNoSpeaker("Ariam pulls out his wand.")
            dial("Peter","...")
            dial("Peter","Oh no.")
            dialNoSpeaker("Peter turns to you.")
            dial("Peter","Can you please help? I’m not very good at spell battles.")
            while True:
              choice = dropdownMenu(None,["Sure.","Nah, I'm good. ~~Valeria Moment~~"])
              if choice == 1:
                break
              elif choice == 2:
                dial("Peter","Pretty please with a cherry on top.")
                dial("Katherine",".-.")
            dial("Peter","Thank you.")
            dial("Ariam","I may be deaf in both ears but I still should be able to hear the sound of you losing.")
            dial("Ariam","Let’s see what you got.")
            
            if not runBattle(player, AriamBattleStudent()):
              return
              
            dial("Ariam","Gosh darn it.")

            player.giveTickets(50)
            printFlair("You earned 50 tickets from the battle!")
            
            player.addFlag("117_Int3_AirdroppingWaterCycleSong")
          else:
            dial("Peter","Don't you even think about it...")
        else:
          dialNoSpeaker("You decide to airdrop a video of the water cycle song to everyone in class... then realize that you don’t have an iPhone.")
      elif choice == 4:
        player.classroom = None
        return
    if player.act == 2:
      clear()
  
      printBoxedText("Room 117 - Ms. Mahon's History Classroom")
      print() 

      if player.hasFlag("117_Int1_ValeriaDecimatesPandas"):
        printC("Ms. Mahon seems to be grieving the loss of her pandas, taken so soon by Valeria's wrath.")
      else:
        printC("Ms. Mahon seems to be hosting a Blooket for the class...")

      choice = dropdownMenu(None,["Participate in the Blooket.","Leave the classroom."])
      if choice == 1:
        if player.hasFlag("117_Int1_ValeriaDecimatesPandas") == False:
          dialNoSpeaker("You decide to join the Blooket, pitted against Valeria, Ryan, Krishan, Khang, and Aadhavan.")
          dial("Ms. Mahon","What mode should I choose?")
          dial("Ms. Mahon","My Period 5 class liked the cooking one a lot.")
          dial("Ryan","NO!")
          dial("Ryan","The cooking one reminds me of a certain infamous IED arcade game.")
          dial("Ms. Mahon","Well, what do you suggest?")
          dial("Ryan","Monster Brawl, Gold Rush, Crypto Hack, Fishing Frenzy, and Panda Math are pretty good modes.")
          dial("Krishan","Isn't Panda Math the new one?")
          dial("Ms. Mahon","You're right, we should play that.")
          dialNoSpeaker("Ms. Mahon chooses the mode to be Panda Math.")
          dialNoSpeaker("The rules are read on the screen...")
          dialNoSpeaker("\"Answer questions to collect Rachel Ranch and Bryce Rice to feed your enclosure of pandas.\"")
          dialNoSpeaker("\"Be careful of your opponents setting your pandas ablaze.\"") 
          dialNoSpeaker("\"Player with the most pandas alive wins!\"")
          dial("Ms. Mahon","I love pandas. :O")
          dial("Ms. Mahon","I'll offer candy and Ni Hao Kai-Lan stickers to anyone who places top 5.")
          dialNoSpeaker("The game begins and everyone frantically answers history trivia to collect the most pandas.")
          dial("Krishan","Hey Aadhavan, wanna work together to overtake Ryan?")
          dial("Aadhavan","Sure.")
          dial("Ryan","You can't team, that's cheating!")
          dial("Ms. Mahon","Yeah, we don't like any cheaters here.")
          dial("Krishan","Fine.")
          dialNoSpeaker("The game is almost about to end, Ms. Mahon currently has the most pandas with Valeria in second.")
          dial("Ms. Mahon","Awww, these pandas are so cute. I'm going to start naming them!")
          dialNoSpeaker("Valeria, desparate, decides to commit arson amongst Ms. Mahon\'s panda enclosure, decimating the old victor's population.")
          dial("Ms. Mahon","...")
          dial("Ms. Mahon","Valeria... did you just... kill all my pandas?")
          dial("Valeria","...")
          dial("Valeria","Can I still get candy?")
          dial("Ms. Mahon","No.")
          dial("Valeria","._.")
          player.addFlag("117_Int1_ValeriaDecimatesPandas")
        else:
          dialNoSpeaker("Ms. Mahon isn't starting another Blooket...")
          dial("Ms. Mahon","Why did you kill my pandas Valeria? TwT")
          dial("Valeria","It reminded me of a certain Poorvi Desh Panda.")
        
      elif choice == 2:
        player.classroom = None
        return
      
  
class Room116Classroom(Classroom):
  def __init__(self):
    self.name = "Room 116"
    self.locked = [1, 2, 3, 4, 5]

class Room113Classroom(Classroom):
  def __init__(self):
    self.name = "Room 113 - Ms. Lee, Math"
    self.locked = []

  def run(self, player):
    if player.act == 1:
      clear()
      
      printBoxedText("Room 113 - Ms. Lee's Math Classroom")
      print() 
      
      printC("You enter Ms. Lee’s room, the, undeniable, best classroom in the entire school.")
      print()
      printC("There seems to be no teacher in the room. You can spot Brooke and Gloria playing Uno in the middle of the classroom.")
  
      choice = dropdownMenu("What do you do?",["Ask to join the Uno game.","Ask where the teacher is.","Leave the classroom"])
  
      if choice == 1:
        if player.questProgressIsAtLeast(IronicCriminalPursuitQuest, 5):
          if player.hasFlag("113_Int1_KatherineAndPeterUnoGame") == False:
            dial("Peter","Hey guys, may we join the game?")
            dialNoSpeaker("Brooke and Gloria stare at the three of you and then wave at Peter.")
            dial("Brooke","Hello Oyster!")
            dial("Katherine","Oyster?")
            dial("Peter","... don’t ask.")
            dial("Brooke","Did you finish your AoPS homework in time?")
            dial("Peter","... um...")
            dial("Brooke","Peter, did you forget?")
            dial("Gloria","Wow Peter, even I wouldn’t forget to do my AoPS homework.")
            dial("Peter","It’s hard! I doubt you two know how to multiply matrices.")
            dial("Brooke","Multiplying matrices? You have to be joking.")
            dial("Gloria","Peter, that’s second-grade math.")
            dial("Brooke","No wonder you’re awful at it.")
            dial("Peter","All I wanted was to play Uno. TwT")
            dial("Katherine","... same. :\(")
            player.addFlag("113_Int1_KatherineAndPeterUnoGame")
          else:
            dial("Peter","Can we please play Uno?")
            dial("Brooke","Actually... Gloria, let's play Scrabble!")
            dial("Gloria","Sure!")
            dial("Peter","What, no- my Map R was abysmal!")
            dial("Brooke","Exactly.")
            dial("Katherine","Well, my Map R was a 317 so I'd be happy to-")
            dial("Peter","No! We are not playing Scrabble!")
            dial("Katherine","Fine. :(")
        else:
          if player.hasFlag("113_Int1_BrookeQuitsUno") == False:
            dialNoSpeaker("You ask to join the Uno game.")
            dial("Brooke","Sure, you can wait till after this round.")
            dial("Gloria","They won’t need to wait for long since I *(Gloria puts down another card)* have Uno.")
            dial("Brooke","._.")
            dial("Gloria","What are you going to do now? You have four cards left, play wisely.")
            dial("Brooke","Simple.")
            dialNoSpeaker("Brooke puts down four cards, all with the same number.")
            dial("Gloria","What. I didn’t agree that stacking was a rule.")
            dial("Brooke","Too bad, I win again.")
            dial("Gloria","Come on, you’ve won the past fourteen games, give me a chance.")
            dial("Brooke","One second, I need to update my Discord status real quick.")
            dial("Gloria","-_-")
            dial("Brooke","“Fun Fact: I’m as good at Uno as I am at AMC 12”. Perfect!")
            dial("Gloria","-_-")
            dialNoSpeaker("Gloria points to you.")
            dial("Brooke","Oh... right.")
            dial("Brooke","You can sit down, I’ll reshuffle the deck.")
            dialNoSpeaker("Brooke reshuffles the deck and passes seven cards to everyone.")
            dial("Brooke","Okay, I’m going first!")
            dialNoSpeaker("Brooke puts down a wild card.")
            dial("Gloria","._.")
            dial("Brooke","The color is blue! ^_^")
            dial("Gloria","...! That’s perfect!")
            dialNoSpeaker("Gloria plays a blue +2.")
            dialNoSpeaker("You play a red +2.")
            dial("Brooke","Hah~ You’ve fallen right for my trap!")
            dialNoSpeaker("Brooke plays a blue +2.")
            dial("Gloria","Oh really?")
            dialNoSpeaker("Gloria plays a yellow +2.")
            dialNoSpeaker("You play a green +2.")
            dialNoSpeaker("Brooke plays a red +2.")
            dial("Brooke","If you guys have another one, I’m going to scream!")
            dialNoSpeaker("Gloria plays a yellow +2.")
            dialNoSpeaker("You play a green +2.")
            dial("Brooke","._.")
            dial("Gloria","Come on Brooke, draw 16 cards!")
            dial("Brooke","You know what, I quit. This game is rigged anyways.")
            dial("Gloria","Took you long enough to come to that conclusion.")
            player.addFlag("113_Int1_BrookeQuitsUno")
          else:
            dial("Brooke","I'm never playing Uno ever again!")
            dial("Brooke","Actually... I'll get over it soon.")
            dial("Gloria","You better not.")
      elif choice == 2:
        if player.questProgressIsAtLeast(IronicCriminalPursuitQuest, 5): 
          if player.hasFlag("113_Int1_BrookeSSLForms") == False:
            dial("Katherine","Why are you two here unsupervised? Are you here to get extra credit or SSL hours or...")
            dial("Brooke","SSL HOURS? Oh my word, thanks for reminding me!")
            dial("Peter","Huh?")
            dial("Brooke","I kinda... forgot to turn in my SSL forms... from last year.")
            dial("Gloria","... seriously?")
            dial("Brooke","I have to turn them to Ms. Palank and she’s kind of... scary.")
            dial("Peter","Brooke... Ms. Palank is fine, she’s a good teacher.")
            dial("Brooke","But... I don’t know.")
            dial("Peter","If you’re scared, get someone else to turn in your forms.")
            dial("Brooke","Like who?")
            dial("Peter","Like... {}, they’re pretty trustworthy.".format(player.getName()))
            dial("Brooke","You sure?")
            dial("Katherine","I’ve just met them and they seem like a nice person!")
            dial("Brooke","... alright.")
            player.giveItem(SSLFormsItem) 
            printFlair("You Receive Brooke's SSL Forms")
            player.startQuest(OverdueSSLFormsQuest)
            player.addFlag("113_Int1_BrookeSSLForms")
            dial("Brooke","Thanks, {}! I’ll make sure to add you to my Discord status!".format(player.getName()))
            dial("Peter","... what?")
        
          else:
            dial("Brooke","Who cares where the teacher is?")
        else:
          if player.hasFlag("113_Int2_BrookeAndGloriaHateIED") == False:
            dialNoSpeaker("You ask where Ms. Lee has gone.")
            dial("Gloria","I believe she’s substituting as the Intro To Engineering Design teacher, the old teacher’s been... missing.")
            dial("Brooke","Intro to Engineering Design? Thank god I’m not in that class, Anna keeps on nagging me on how she’s gotten two points taken off every assignment.")
            dial("Gloria","Tell me about it. She also keeps on talking about struggling to memorize the Incenter/Excenter Lemma, whatever that is.")
            dial("Brooke","I... I don’t think that’s engineering.")
            dial("Gloria","You never know, the work those kids do is as hard as circumscribing triangles... without a compass.")
            dial("Brooke","Yikes.")
            player.addFlag("113_Int2_BrookeAndGloriaHateIED")
          else:
            dial("Gloria","We... told you she's substituting as the Intro To Engineering Design teacher. -_-")
      elif choice == 3:
        player.classroom = None
    elif player.act == 2:
      clear()
      
      printBoxedText("Room 113 - Ms. Lee's Math Classroom")
      print() 
      
      printC("You enter Ms. Lee’s room... but Ms. Lee isn't present.")
      print()
      printC("You can spot Brooke, Gloria, Lillian, and Jashlee having a conversation.")
      if player.questProgressIsAt(OverdueSSLFormsQuest,1):
        choice = dropdownMenu(None,["Join the conversation.","Give Brooke her SSL forms back","Leave the classroom."])
      else:
        choice = dropdownMenu(None,["Join the conversation.","Leave the classroom."])

      if choice == 1:
        if not player.hasFlag("113_Int1_MortalOnesCommunityCircle"):
          dialNoSpeaker("You decide to sit next to the cluster of people and join the conversation...")
          dial("Jashlee","Preston wanted me to 'dap him up', yesterday.")
          dial("Lillian","Did you?")
          dial("Jashlee","Nah, I punched him directly in the face.")
          dial("Lillian","...")
          dial("Jashlee","He deserved it.")
          dial("Lillian","... I-")
          dial("Gloria","That's nice to hear Jashlee.")
          dial("Gloria","Thanks for contributing to the annual Mortal One's Metropolis community circle.")
          dial("Gloria","Unlike Anna, Jessika, Sherry, and especially Peter.")
          dial("Gloria","They seem to have excused themselves from this momentous day.")
          dial("Gloria","...")
          dial("Gloria","... moving on.")
          dial("Gloria","You're next Brooke. What do you have to offer?")
          dial("Brooke","...")
          dial("Gloria","Uh... Brooke?")
          dial("Brooke","Huh? Oh sorry, I'm just blocking some people on Replit right now.")
          dial("Brooke","I'll be back with you shortly.")
          dial("Gloria","Great. -_-")
          dialNoSpeaker("Gloria spots you sitting next to the other Mortals.")
          dial("Gloria","Hang on, you're not supposed to be here.")
          dialNoSpeaker("You sit motionless with a blank stare on your face...")
          dial("Gloria","...")
          dial("Gloria","*(Calling the other Mortals)* What do I do?")
          dial("Jashlee","You should battle them!")
          dial("Lillian","Agree.")
          dial("Gloria","Wha- me?")
          dial("Jashlee","Come on, I haven't seen you cast spells yet, you're always so...")
          dial("Gloria","Tranquil?")
          dial("Jashlee","Exactly! ")
          dial("Gloria","*(Sigh)* If you really want to see me fight then so be it.")
          dial("Gloria","This is for you Jashlee...")

          if not runBattle(player, GloriaBattleStudent()):
            return
          
          dial("Gloria","Unfortunate.")
          dial("Jashlee","Awww, I wanted Gloria to win. .-.")
          dial("Brooke","Huh? What's this commotion about?")
          dial("Jashlee","You're back Brooke! Why were you incapacitated for so long?")
          dial("Brooke","In- incapacitated?")
          dial("Jashlee","I wanna use long words to sound just like Gloria! ^_^")
          dial("Brooke","Oh.")
          dial("Gloria","Whatever you say 'Joshlee'.")

          player.giveTickets(100)
          printFlair("You earned 100 tickets from the battle!")
          
          player.addFlag("113_Int1_MortalOnesCommunityCircle")
        else:
          dial("Gloria","Brooke, you wanna say anything?")
          dial("Brooke","Hang on. I'm busy playing Gartic Phone with Anna.")
          dial("Gloria","So that's why she isn't here. -_-")
      elif choice == 2:
        if player.questProgressIsAt(OverdueSSLFormsQuest,1):
          dialNoSpeaker("You give Brooke her shredded SSL forms.")
          
          dial("Brooke","...")
          dial("Gloria","So... I'm not sure if you knew this but...")
          dial("Gloria","Brooke explicity said to \"turn in her SSL forms\", not shred them up.")
          dial("Brooke","I- I-")
          dial("Lillian","...")
          dial("Jashlee","...")
          dial("Brooke","How- how have you messed up this badly.")
          dial("Brooke","I- I- can't even comphrend the fact the forms that I gave you in pristine condition are now torn into a quintillion pieces.")
          dial("Brooke","I don't care much for Peter's opinion but EVEN Katherine said you were trustworthy.")
          dial("Brooke","...")
          dial("Brooke","I'm going to make sure that you're forever memorialized in my Discord status...")
          dial("Brooke","...")
          dial("Brooke","... as a eulogy.")

          if not runBattle(player, BrookeBattleStudent()):
            return
            
          dial("Brooke","...")
          dial("Brooke","I'm going to block you on Replit now.")
          dial("Jashlee","Okay, I think you're acting a bit too mean.")
          dial("Jashlee","I mean, this is probably just a huge misunderstanding, right {}?".format(player.name))
          dialNoSpeaker("You stand quietly.")
          dial("Brooke","*(Sigh)*")
          dial("Brooke","I'm sure it is...")
          dial("Brooke","I'll forgive you, okay?")
          dialNoSpeaker("You nod your head in acceptance.")
          dial("Brooke","^_^")
          
          player.removeItem(ShreddedSSLFormsItem)
          player.incrementQuestProgress(OverdueSSLFormsQuest)  
        else:
          player.classroom = None
          return
      elif choice == 3:
        player.classroom = None
        return
  
class Room112Classroom(Classroom):
  def __init__(self):
    self.name = "Room 112"
    self.locked = [1, 2, 3, 4, 5]

class Room111Classroom(Classroom):
  def __init__(self):
    self.name = "Room 111 - Ms. Akano, Math"
    self.locked = []

  def run(self, player):
    if player.act == 1:
      clear()
  
      printBoxedText("Room 111 - Ms. Akano's Math Classroom")
      print() 
      
      printC("You’re in Ms. Akano’s room, the class where students mathematically inferior to Anna Zhou reside.")
      print()
      printC("You grab a warm-up sheet and sit at a table.")
  
      if player.hasFlag("111_Int1_PlayingGimkit") == False: 
        printC("You can spot Aadhavan, Edem, and Krishan arguing about something in the corner of the room.")
  
      choice = dropdownMenu("What do you do?",["Overhear the argument between Aadhavan, Edem, and Krishan.","Sit down at a table.","Leave the classroom."])
      if choice == 1:
        if player.questProgressIsAtLeast(IronicCriminalPursuitQuest, 5):
          if player.hasFlag("111_Int1_AadhavanGetsBonked") == False:
            dial("Edem","You moron, question five is -4, not 17.5.")
            dial("Krishan","Aadhavan, how did you even get that?")
            dial("Aadhavan","I forgot basic arithmetic. TwT")
            dial("Edem","*(Sigh)* No wonder you got rejected from Poolesville.")
            dial("Aadhavan","EDEM, YOU ALSO GOT REJECTED!")
            dial("Edem","I got rejected because my parents abandoned me to go to Africa.")
            dial("Edem","Meanwhile, you got rejected because you’re just stupid.")
            dial("Ms. Akano","Guys, please stop arguing.")
            dial("Edem","Fine.")
            dial("Peter","*(Whispering to you and Peter)* Do you even know what they’re talking about?")
            dial("Katherine","*(Whispering)* No idea.")
            dialNoSpeaker("Krishan glances at you, Katherine, and Peter.")
            dial("Krishan","Hey, there’s people eavesdropping on our conversation.")
            dialNoSpeaker("Aadhavan and Edem look at the three of you.")
            dial("Katherine","*(Whispering)* Uh... what should I do?")
            dial("Peter","*(Whispering)* I recommend standing very still and acting like an NPC.")
            dial("Katherine","*(Whispering)* What?")
            dial("Peter","*(Whispering)* Trust me, they’ll ignore you completely.")
            dial("Katherine","*(Whispering)* Uh... ok?")
            dial("Peter","*(Whispering)* You understand {}?".format(player.getName()))
            dialNoSpeaker("You nod your head.")
            dial("Krishan","What are they doing?")
            dial("Edem","Why are they standing like that? It makes me uncomfortable.")
            dial("Aadhavan","Edem, literally everything makes you uncomfortable-")
            dial("Edem","*(Squealing in a very high-pitched noise)* SHUT UP AADHAVAN, NOW’S NOT THE TIME!")
            dial("Katherine","Okay... I’m sick of this.")
            dialNoSpeaker("Katherine breaks free from her immobility.")
            dial("Krishan","Wha- What were you even doing?")
            dial("Katherine","Peter wanted me to act like an ‘NPC’, not sure what that means.")
            dial("Krishan","What... why? Lillian’s the only true ‘NPC’, no one else can compare.")
            dial("Katherine","I’m... very confused.")
            dial("Peter","Okay... I’m tired of this as well.")
            dialNoSpeaker("Peter breaks free from his immobility.")
            dial("Peter","{}, you can stop now.".format(player.getName()))
            dialNoSpeaker("You continue to stand still.")
            dial("Peter","{}?".format(player.getName()))
            dialNoSpeaker("You continue to stand still.")
            dial("Aadhavan","Peter... let me deal with this.")
            dial("Peter","Sure.")
            dialNoSpeaker("Aadhavan stands up from his desk and walks over to you.")
            dial("Katherine","Don’t... don’t hurt them.")
            dial("Aadhavan","Why would I do that? I’m only going to say the most revolting thing imaginable that’ll surely break them out of their motionless state.")
            dialNoSpeaker("Aadhavan takes a deep breath.")
            dial("Aadhavan","Your... mom.")
            dialNoSpeaker("The room goes silent.")
            dial("Katherine","I’m... confused. The humor people find in such trivial things baffles me.")
            dial("Peter","Tell me about it.")
            dialNoSpeaker("Your arm gradually rises only to swiftly descend to bonk Aadhavan on the head, Princess Bride style.")
            dial("Aadhavan","OW!")
            dial("Aadhavan","MY CRANIUM!")
            dial("Peter","What? Cranium?")
            dial("Aadhavan","It’s the scientific term to describe the skull, the bone that encloses the brain, and other important-")
            dial("Peter","Forget I asked.")
            dial("Aadhavan","But seriously? What on earth was that for?")
            dialNoSpeaker("You continue to stand still.")
            dial("Aadhavan","You know that could have killed me right? The energy of the collision, approaching an asymptotic limit of velocity, could have exerted an immeasurable force on my cranium, ultimately leading to my demise.")
            dial("Peter","I... didn’t understand half the words you said.")
            dial("Aadhavan","*(Ignoring him)* Two can play at that game; {}, this wand will put you in a state of constant motion for the rest of your life. Good luck!".format(player.getName()))

            if not runBattle(player, AadhavanBattleStudent()):
              return

            dial("Aadhavan","...")
            dial("Aadhavan","...I’m better at science than I am at spell battles.")
            dial("Peter","Makes sense. I mean, science does contradict the notion of magic itself.")
            dial("Aadhavan","You do have a point.")

            player.giveTickets(50)
            printFlair("You earned 50 tickets from the battle!")
            
            player.addFlag("111_Int1_AadhavanGetsBonked")
          else:
            dialNoSpeaker("There's no argument anymore.")
        else:
          if player.hasFlag("111_Int1_PlayingGimkit") == False:
            dial("Edem","Hey Krishan, I’ve been analyzing the new Breath of The Wild trailer and-")
            dial("Krishan","BRO, SHUT UP! You’ve been telling me this exact same thing for the past two weeks!")
            dial("Aadhavan","Yeah Edem, be more original-")
            dial("Ms. Akano","Guys... stop arguing.")
            dial("Krishan","*(Sigh)* Fine, I’ll just complete my warmup.")
            dial("Ms. Akano","You still haven’t finished?")
            dial("Krishan","Sadly, no.")
            dial("Aadhavan","Krishan, you’ve been doing your warmup for an eternity!")
            dial("Krishan","But I don’t want to do any work!")
            dial("Aadhavan","You should really do it, you know Ms. Akano’s going to be grading it, right?")
            dial("Krishan","Yeah...")
            dial("Krishan","I’m just going to play a Gimkit.")
            dial("Edem","That’s a great idea!")
            dial("Aadhavan","Alright.")
            dial("Krishan","The code is 2-7-6-3.")
            dial("Edem","What mode are you even choosing? Snowbrawl?")
            dial("Aadhavan","Edem you silly goose, Snowbrawl sucks.")
            dial("Krishan","I’m choosing Capture the Flag.")
            dial("Aadhavan","But... we have three people, the teams won’t be even.")
            dial("Krishan","Shoot, you’re right.")
            dialNoSpeaker("Krishan looks around the room.")
            dial("Krishan","(Pointing to you) Want to play a Gimkit with us?")
            choice = dropdownMenu(None,["Sure!","Nah, I'm good."])
            if choice == 1:
              dial("Krishan","Alright, join the game.")
              dialNoSpeaker("You join the Gimkit game.")
              dialNoSpeaker("The game starts and you are placed on a team with Aadhavan.")
              dial("Krishan","NOOOO, I’M TEAMED WITH EDEM!")
              dial("Edem","-_-")
              dialNoSpeaker("You and Aadhavan proceed to demolish the competition.")
              dial("Krishan","That wasn’t even fair, Edem was doing nothing.")
              dial("Edem","-_-")
            elif choice == 2:
              dial("Krishan","*(Sigh)* Let’s just play Fishtopia.")
            player.addFlag("111_Int1_PlayingGimkit")
          else:
            dialNoSpeaker("They aren't arguing anymore, in fact, they are having fun playing Gimkit. How wholesome!")
      elif choice == 2:
        
        if player.questProgressIsAtLeast(IronicCriminalPursuitQuest, 5):
          if player.hasFlag("111_Int2_KatherineCommitsKatherineAfterSeeingASpider") == False:
            dialNoSpeaker("The three of you decide to sit down at the table furthest from Ms. Akano’s desk.")
            dialNoSpeaker("There’s another person sitting at the table wearing a hoodie that’s obscuring the majority of their face.")
            dial("Tyler","...")
            dial("Katherine","Is he... ok?")
            dial("Peter","... {}, can you please wake him up?".format(player.getName()))
            dialNoSpeaker("You tap Tyler on the shoulder, he doesn’t move an inch.")
            dial("Peter","Katherine, why don’t you scream really loudly. That’ll for sure get his attention.")
            dial("Katherine","Why would I do that?")
            dial("Peter","... I’ll give you a blueberry flavored Chobani yogurt if you do.")
            dial("Katherine","Deal!")
            dialNoSpeaker("Katherine proceeds to scream in the most high-pitched voice imaginable.")
            dial("Tyler","ACK!")
            dialNoSpeaker("Everyone stares at the three of you.")
            dial("Ms. Akano","... what was that Katherine?")
            dial("Katherine","... I saw a spider.")
            dial("Tyler","Dude, your scream took me out of my nap!")
            dial("Peter","Is that why you wear your hood like that?")
            dial("Tyler","Yeah, so that no one catches me dozing off.")
            dial("Tyler","Now who’s this ‘Katherine’ fellow? I’m going to have to teach them a lesson.")
            dial("Katherine","Oh.. uh... it was... them. *(Katherine points to you)*")
            dial("Tyler","If you’re pointing to someone then remember that... I can’t see.")
            dial("Katherine","... It’s the person in front of you.")
            dial("Tyler","I see... I mean...  I can’t see but... you know what I mean.")
            dial("Tyler","Prepare to be bested Katherine. *(Tyler points his wand at you.)*")
            dial("Katherine","What have I done?")

            if not runBattle(player, TylerBattleStudent()):
              return
              
            dial("Tyler","Did I lose? I can’t tell.")
            dial("Peter","Yeah, you did.")
            dial("Tyler","Darn it.")
            dial("Katherine","Don’t think I forgot Peter.")
            dial("Peter","Huh? Oh right.")
            dialNoSpeaker("Peter hands Katherine a blueberry flavored Chobani yogurt.")
            dial("Katherine","Thanks, I’ll add it to my collection.")

            player.giveTickets(50)
            printFlair("You earned 50 tickets from the battle!")
            
            player.addFlag("111_Int2_KatherineCommitsKatherineAfterSeeingASpider")
          else:
            dialNoSpeaker("The three of you decide to sit down next to Tyler at the table furthest from Ms. Akano’s desk.")
            dial("Tyler","Did you really see a spider?")
            dial("Katherine","Totally.")
        else:
          dialNoSpeaker("You decide to sit down at the table furthest from Ms. Akano’s desk.")
          dialNoSpeaker("There’s another person sitting at the table wearing a hoodie that’s obscuring the majority of their face.")
          dial("Tyler","...")
          choice = dropdownMenu("What do you do?",["Punch them.","Wave to them.","Leave the table."])
          if choice == 1:
            dial("???","Excuse me? There is absolutely no way I’m letting you do that.")
            dial("???","Mind you, this is a family friendly game.")
            dial("???","Seriously, don’t consider doing stuff like that.")
          if choice == 2:
            dialNoSpeaker("You wave to them slowly.")
            dial("Tyler","...")
          
      elif choice == 3:
        player.classroom = None
        return

    if player.act == 2:
      clear()
  
      printBoxedText("Room 111 - Ms. Akano's Math Classroom")
      print() 
      
      printC("You’re in Ms. Akano’s room, the class where students mathematically inferior to Pilliam Wark reside.")
      print()
      printC("You grab a compass and sit at a table.")
      if player.hasFlag("111_Int2_KnockingDownCardTower") == False:
        print()
        printC("Benedicte and Yulia can be seen creating a tower out of playing cards.")

      choice = dropdownMenu("What do you do?",["Do your trigonometry packet.","Knock down the tower of cards.","Leave the classroom."])
      if choice == 1:
        dialNoSpeaker("You decide to do your trigonometry packet.")
        dialNoSpeaker("...")
        dialNoSpeaker("And you somehow forgot the Law of Cosines again.")
        dial("Ms. Akano","Great job! At least you\'re doing your packet...")
        dial("Ms. Akano","... unlike a certain Krishan.")
      elif choice == 2:
        if player.hasFlag("111_Int2_KnockingDownCardTower") == False:
          dialNoSpeaker("You knock down the tower of cards.")
          dial("Yulia","...")
          dial("Benedicte","...")
          dial("Benedicte","I can't believe you would do that.")
          dial("Benedicte","You little digusting rat!")
          dial("Benedicte","I know I've said I'm not supposed to hurt animals...")
          dial("Benedicte","... but the rats are an exception.")

          if not runBattle(player, BenedicteBattleStudent()):
            return
            
          dial("Benedicte","...")
          dial("Yulia","...")
          dial("Yulia","Benedicte...")
          dial("Yulia","... let me show you how it's done.")

          if not runBattle(player, YuliaBattleStudent()):
            return
            
          dial("Yulia","...")

          player.giveTickets(200)
          printFlair("You earned 200 tickets from the battle! (... are you proud of yourself?)")
          
          player.addFlag("111_Int2_KnockingDownCardTower")
        else:
          dial("Benedicte","I ain't building another tower just for you to knock it down.")
      elif choice == 3:
        player.classroom = None
        return
  
    

class MainGymClassroom(Classroom):
  def __init__(self):
    self.name = "Main Gym"
    self.locked = [1]
    
  def run(self, player):
    if player.act == 2:        
      #clear()
      
      if player.hasItem(GymKeysItem):
        clear()
        printBoxedText("Main Gym")
        print()
        printC("You're in the gym, the place where magnet students get panic attacks and faint due to Vitamin D deficiency.")
        choice = dropdownMenu("What do you do?",["Get a paddle from the closet.","Stare at the ceiling.","Leave the gym."])
        if choice == 1:
          if player.hasFlag("MainGym_Int1_PoorviEllaRacket") == False:
            dialNoSpeaker("Before you enter the closet, you hear voices coming from inside.")
            dial("Poorvi","*(From behind the door)* I disagree, badminton is an amazing sport!")
            dial("Ella","*(From behind the door)* Badminton is just glorified Indian tennis.")
            dial("Poorvi","*(From behind the door)* Ella, these rackets are made of steel, I've studied for long enough to know that steel's an excellent conductor.")
            dial("Poorvi","Equiping the frogs with these rackets will make them unstoppable!")
            dial("Ella","*(From behind the door)* It's just a racke- you know what, Whatever you say. ¯\\_(ツ)_/¯")
            dial("Poorvi","*(From behind the door)* I knew you'd be along eventually.") 
            dialNoSpeaker('Poorvi and Ella slide open the gym closet door as you slid behind a conviently shaped metal beam before they notice you.')
            dial("Ella","What's Effie up to?")
            dial("Poorvi","The frog? She's preparing something colossal.")
            dial("Ella","Come on, you never tell me anything.")
            dial("Poorvi","I like to keep things a suprise. :)")
            dial("Ella","-_-")
            dialNoSpeaker("Poorvi and Ella exit the gymnasium, master keys in hand.")
            dialNoSpeaker("The gym closet is now open...")
            player.addFlag("MainGym_Int1_PoorviEllaRacket")
          elif player.hasFlag("MainGym_Int1_WhiteSucculent") == False:
            dialNoSpeaker("You enter the gym closet...")
            dialNoSpeaker("Inside, you find a pile of badminton rackets on the ground alongside a shelf containing a table tennis paddle and, convienently, a white succulent.")

            player.giveItem(WhiteHaworthiaSucculentItem)
            player.giveItem(TableTennisPaddleItem)
            
            printFlair("You Receive a Table Tennis Paddle.")
            printFlair("You Receive a White Haworthia Succulent.")
            player.addFlag("MainGym_Int1_WhiteSucculent")
            player.incrementQuestProgress(TableTennisQuest)
          else:
            dialNoSpeaker("The gym closet has nothing else of use inside.")
        elif choice == 2:
          dialNoSpeaker("You stare at the Gym's ceiling...")
          dialNoSpeaker("Balls of varying sizes can be seen lodged in the support beams above.")
          dialNoSpeaker("You envision yourself as one of those balls, stuck in that very ceilin-")
          dialNoSpeaker("Okay, this is just getting weird.")
        elif choice == 3:
          player.classroom = None
          return
      else:
        dialNoSpeaker("Unfortunately, the door's locked.")

        player.classroom = None
        return

class DanceStudioClassroom(Classroom):
  def __init__(self):
    self.name = "Dance Studio"
    self.locked = [1]

  def run(self, player):
    if player.act == 2:
        

        if player.hasFlag("Weight_Int3_EnterDanceStudio"):
          clear()
    
          printBoxedText("Dance Studio")
          print() 
          printC("You're in the Dance Studio, where all you do is play Table Tennis.")
          print()
          if player.hasFlag("Dance_Int1_UnproppedDoor") == False:
            printC("The entrance door seems to be propped up with a chair... you decide to remove it.")
            player.addFlag("Dance_Int1_UnproppedDoor")
             
          printC("Ms. Gleich can be spotted peering at, what appears to be a registration form.")
  
          choice = dropdownMenu("What do you do?",["Talk to Ms. Gleich","Leave the classroom."])
          if choice == 1:
            if not player.hasFlag("Dance_Int1_HuntingAPaddle"):
              dial("Ms. Gleich","Hmm...?")
              dialNoSpeaker("Ms. Gleich turns to you.")
              dial("Ms. Gleich","...")
              dial("Ms. Gleich","You aren't supposed to be here...")
              dial("Ms. Gleich","This place needs to be suitable for the annual Table Tennis tournmanet tomorrow.")
              dropdownMenu(None,["Tournament? That sounds fun!","May I join?"])
              dial("Ms. Gleich","Of course! If you want to join please sign your first and last name on this form:")
              dialNoSpeaker("Ms. Gleich hands you a registeration form that you eagerly sign before giving back to her.")
              dial("Ms. Gleich","The annual Table Tennis tournament is a ferocious competition that attracts countless RCMS students.")
              dial("Ms. Gleich","Notable students who'll be participating in tomorrow's tournament (your competition) include Peter, Sherry, Tyler, and Arjun.")
              choice = dropdownMenu(None,["Peter?","Sherry?","Tyler?","Arjun?"])
              if choice == 1:
                dial("Ms. Gleich","Yeah, he's pretty decent at the sport.")
              elif choice == 2:
                dial("Ms. Gleich","Have you see her? She can play table tennis AND volleyball!")
                dial("Ms. Gleich","What can't she do?")
              elif choice == 3:
                dial("Ms. Gleich","He's just there for the food.")
              elif choice == 4:
                dial("Ms. Gleich","He's one of the best Table Tennis players at this school.")
                dial("Ms. Gleich","But he can't seem to beat the three time champion, Sherry Wang.")
              dial("Ms. Gleich","...")
              dial("Ms. Gleich","Shoot... you need a paddle.")
              dial("Ms. Gleich","I believe there's one in the Main Gym Closet, why don't you fetch it yourself?")
              dial("Ms. Gleich","...")
              dial("Ms. Gleich","Oh wait, I'm pretty sure the Main Gym doors are locked...")
              printFlair("You Receive The Gym Keys From Ms. Gleich.")

              player.giveItem(GymKeysItem)
              
              dial("Ms. Gleich","I trust you. Okay?")
              dialNoSpeaker("You nod your head, cutely.")
              dial("Ms. Gleich","Good. Get in, get the paddle, and get out.")
              player.startQuest(TableTennisQuest)
              player.addFlag("Dance_Int1_HuntingAPaddle")
            elif not player.hasItem(TableTennisPaddleItem) and not player.hasFlag("Dance_Int1_ReturnGymKeys"):
              dial("Ms. Gleich","Talk to me again when you have that paddle!")
            elif player.hasItem(TableTennisPaddleItem) and player.hasItem(GymKeysItem):
              
              player.removeItem(GymKeysItem)
              dialNoSpeaker("You give the Gym Keys back to Ms. Gleich.")
              dial("Ms. Gleich","Nice, you kept your promise.")
              player.addFlag("Dance_Int1_ReturnGymKeys")
              player.incrementQuestProgress(TableTennisQuest)
            else:
              dial("Ms. Gleich","You excited for the table tennis tournament?")
              dialNoSpeaker("You nod your head.")
              dial("Ms. Gleich","Wonderful! :)")
  
          elif choice == 2:
            player.classroom = None
            return
        else:
          print()
          dialNoSpeaker("Unfortunately, the door's locked.")
          dialNoSpeaker("There seems to be a chair propped up on the other side, if only there was another way in.")
          player.classroom = None
          return



class WeightRoomClassroom(Classroom):
  def __init__(self):
    self.name = "Weight Room"
    self.locked = [1]

  def run(self, player):
    if player.act == 2:
        clear()
    
        printBoxedText("Weight Room")
        print() 
  
        if player.hasFlag("Auxilary_Int1_EnterWeightRoom"):
          printC("You're in the weight room... presumebly to hit some gains (I hate that phrase).")
          if player.hasFlag("Weight_Int1_UnproppedDoor") == False:
            print()
            printC("The entrance door seems to be propped up with a chair... you decide to remove it.")
            player.addFlag("Weight_Int1_UnproppedDoor")
  
          choice = dropdownMenu("What do you do?",["Lift some weights.","Roll the excercise die.","Enter the door to the Dance Studio.","Leave the room."])
          if choice == 1:
            dialNoSpeaker("You try lifting some weights but end up crushing yourself into a pancake.")
            dialNoSpeaker("Not actually, but you feel like a pancake, at least.")
          elif choice == 2:
            dialNoSpeaker("You roll the excercise die... you have to do 20 push-ups.")
            choice = dropdownMenu("Do you follow through?",["Do the push-ups.","Cry in sorrow."])
            if choice == 1:
              dialNoSpeaker("You do the push-ups...")
              dialNoSpeaker("But you forgot you were a magnet student...")
              dialNoSpeaker("...")
              dialNoSpeaker("You calculate the average velocity of your chest movement to determine to most optimal force to apply to each push-up, thus cutting the amount of pain you experience in half.")
              dialNoSpeaker("Like typical.. magnet student behavior.")
            elif choice == 2:
              dialNoSpeaker("You cry in sorrow...")
              dialNoSpeaker("... like Anna Zhou when no one accepts her Discord friend request...")
              dialNoSpeaker("...")
              dialNoSpeaker("... or when Katherine ghosts her.")
          elif choice == 3:
            player.classroom = DanceStudioClassroom()
            player.loc = ["HALLWAY_GYM", "HALLWAY_GYM_BOTTOM_1"]
            if not player.hasFlag("Weight_Int3_EnterDanceStudio"):
              player.addFlag("Weight_Int3_EnterDanceStudio")
            return
          elif choice == 4:
            player.classroom = None
            return
            
        else:
          printC("Unfortunately, the door's locked.")
          print()
          printC("If only there was another way to get in...")
          choice = dropdownMenu("What do you do?",["Open the Chamber of Secrets.","Leave."]) 
          if choice == 1:
            dial("???","...")
            dial("???","I know this is a game about spells and wands but...")
            dial("???","...")
            dial("???","What's next? Are you going to put your name in Goblet of Fire?")
            dial("???", "Get married to your best friends sister?")
            dial("???", "Conveniently survive after countless near-death encounters despite everyone around you perishing by interacting with a single blade of grass?")
            dial("???","|DG|*(Cough Cough)* Pilliam Wark.")
            dial("???","|DG|\"um actually it's wingardium leviOsa amirite- *dies from heat exposure*\"")
            dial("???","...")
          elif choice == 2:
            player.classroom = None
            return

      


class AuxiliaryGymClassroom(Classroom):
  def __init__(self):
    self.name = "Auxiliary Gym"
    self.locked = [1]

  def run(self, player):
    if player.act == 2:
      clear()
  
      printBoxedText("Auxilary Gym")
      print() 

      printC("You are in the... Auxilary Gym? Where you... do Gymnastics?")
      print()

      if player.hasFlag("Auxilary_Int1_GabrielleUnlocksDoor"):
        printC("Gabrielle isn't guarding the door anymore...")
        choice = "Enter the door to the Weight Room."
      else:
        printC("You can spot Gabrielle guarding the door to the weight room, peering at her chromebook.")
        choice = "Try to enter the guarded door."

      
      choice = dropdownMenu("What do you do?",[choice,"Do some Gymnastics.","Leave the room."])
      if choice == 1:
        if player.hasFlag("Auxilary_Int1_GabrielleUnlocksDoor") == False:
          dialNoSpeaker("You attempt to enter the door behind Gabrielle.")
          dial("Gabrielle","... what are you doing?")
          choice = dropdownMenu(None,["I'm trying to hit some gains at the gym man.","Nah I'm good. (Valeria Moment. -_-)"])
          if choice == 1:
            dial("Gabrielle","Sorry... the weight room is currently unavailable.")
            dial("Gabrielle","Ms. Gleich told me to guard this door while she's monitoring the dance studio.")
            dial("Gabrielle","This technically counts as child labor... ")
            dial("Gabrielle","...but I'm being paid in exposure on the RCMS twitter account. It's fine.")
            dial("Gabrielle","Tell your friends to follow @GabrielleArtDaily on Instagram! ~~(For legal reasons: This account handle is made up.)~~")
            choice = dropdownMenu(None,["Please, I just want to lift some weights.","Nah I'm good. (Valeria, how does this response even make sense?)"])
            if choice == 1:
              dial("Gabrielle","...")
              dial("Gabrielle","Give me a better reason, I don't get persuaded that easily.")
              choice = dropdownMenu(None, ["I have a vitamin D deficiency I need to make up for.","Nah I'm good. (Valeria, I swear you're controlling these choices.)"])
              if choice == 1:
                dial("Gabrielle","Okay... fine.")
                dialNoSpeaker("Valeria... *AHEM*... I mean, Gabrielle unlocks the door for you.")
                player.addFlag("Auxilary_Int1_GabrielleUnlocksDoor")
              elif choice == 2:
                dial("Gabrielle","That's not a reason.")
            elif choice == 2:
              dial("Gabrielle","I swear, the art is tame...")
              dial("Gabrielle","...even Peter Zhao could handle it.")
          elif choice == 2:
            dial("Gabrielle","Uh... what?")
        else:
          if player.hasFlag("Auxilary_Int1_EnterWeightRoom") == False:
            player.addFlag("Auxilary_Int1_EnterWeightRoom")
          player.classroom = WeightRoomClassroom()
          player.loc = ["HALLWAY_GYM", "HALLWAY_GYM_BOTTOM_2"]
          return
          
      elif choice == 2:
        dialNoSpeaker("You try to do a backflip but, instead, tumble over like Pilliam Wark's IED grade after the dial caliper quiz. :sob:") # :sob:
      elif choice == 3:
        player.classroom = None
        return

class BoysLockerInnerClassroom(Classroom):
  def __init__(self):
    self.name = "Boys Locker Room"
    self.locked = []

  def run(self, player):
    dial("???","I'm genuinely not sure if you're a boy or a girl.")
    dial("???","To keep things safe, I just won't let you in.")      

class GirlsLockerInnerClassroom(Classroom):
  def __init__(self):
    self.name = "Girls Locker Room"
    self.locked = []

  def run(self, player):
    dial("???","I'm genuinely not sure if you're a boy or a girl.")
    dial("???","To keep things safe, I just won't let you in.")    


class GreatOutdoorsEntranceClassroom(Classroom):
  def __init__(self):
    self.name = "The Great Outdoors"
    self.locked = [1]

  def run(self, player):
    if player.hasItem(TeachersPassItem):
      player.loc = ["SIDE_ENTRANCE", "OUTSIDE_SIDE_ENT"]
      dialNoSpeaker("You decide to walk outside into the Great Outdoors...")
      if player.hasItem(GymKeysItem) and player.hasFlag("MainGym_Int1_WhiteSucculent"):
        dialNoSpeaker("Before you exit, you can spot Ms. Gleich sprinting towards you.")
        dial("Ms. Gleich","What did I say?")
        dial("Ms. Gleich","You're supposed to return the Gym Keys to me when you've collected that paddle.")
        dial("Ms. Gleich","...")
        dialNoSpeaker("Ms. Gleich snaches the Gym Keys straight out of your hands.")
        dial("Ms. Gleich","Let that be a lesson.")
        player.removeItem(GymKeysItem)
        player.incrementQuestProgress(TableTennisQuest)
    else:
      dialNoSpeaker("You decide to walk outside into the Great Outdoors...")
      dialNoSpeaker("But before you do so, you realize that you have no way back in...")
      dialNoSpeaker("Unfortunate.")
      
    player.classroom = None
    

class GreatIndoorsEntranceClassroom(Classroom):
  def __init__(self):
    self.name = "The Great Indoors"
    self.locked = [1]

  def run(self, player):
    if player.hasItem(TeachersPassItem):      
      dialNoSpeaker("You use the Teacher's Pass to unlock the door and walk inside.")
      player.loc = ["HALLWAY_GYM", "HALLWAY_GYM_OUTSIDE_EXIT"]
    else:
      dialNoSpeaker("The door's locked... unfortunate.")
    
    player.classroom = None

class DuckPondClassroom(Classroom):
  def __init__(self):
    self.name = "Duck Pond"
    self.locked = [1]

  def run(self, player):
    if player.act == 2:

      clear()
  
      printBoxedText("The Duck Pond")
      print() 
      
      # Classroom Description
      printC("It's a pond... with ducks.")
      print()      
      printC("Arjun can be seen feeding the ducks some croutons.")

      choice = dropdownMenu("What do you do?",["Talk to Arjun.","Jump into the pond and beat up the ducks.","Leave the pond."])
      if choice == 1:
        if player.hasFlag("DuckPond_Int1_SavingSmartyDucky") == False:
          dial("Arjun","Hey man, I'm just feeding my ducks right now.")
          dial("Arjun","Leave me alone.")
          dialNoSpeaker("Suddenly, a duck starts to choke in the middle of the pond.")
          dial("Arjun","SMARTYDUCKY!")
          dialNoSpeaker("You rush into the pond and perform the Heimlich Maneuver on the choking duck until it spits out a tiny crouton.")
          dial("Arjun","Wow, thanks man.")
          dial("Arjun","You just saved my duck from going extinct.")
          dial("Arjun","The SmartyDucky variant of the duck species is elusive for being endangered.")
          dial("Arjun","Despite the name, the duck is pretty stupid.")
          dial("Arjun","It once assumed that a rock was a piece of food.")
          dial("Arjun","No wonder the species is going extinct.")
          dial("Arjun","...")
          dial("Arjun","I should reward you for saving my duck...")
          dial("Arjun","Here, take this succulent. Found it drifting in this very pond once.")

          player.giveItem(BallCactusSucculentItem)
          printFlair("You Receive a Ball Cactus Succulent!")
          
          player.addFlag("DuckPond_Int1_SavingSmartyDucky")
        else:
          dial("Arjun","These ducks like to commit Katherine a lot.")
          dial("Arjun","I have to replace them every now and then with fresh ones from the supermarket.")
      elif choice == 2:
        dial("???","Ain't no way I'm letting you do that.")
      elif choice == 3:
        player.classroom = None
        return

class BlacktopClassroom(Classroom):
  def __init__(self):
    self.name = "Blacktop"
    self.locked = [1]

  def run(self, player):
    if player.act == 2 and player.hasItem(TeachersPassItem):
      clear()
  
      printBoxedText("The Blacktop")
      print() 
      printC("You're in the top that's also conveniently black.") 
      
      if player.hasFlag("Blacktop_Int1_FourSquareShenanigans") == False:
        print()
        printC("You notice Shameer, Henry, Justin, and Dasha playing four square.")

      choice = dropdownMenu("What do you do?",["Join the game.","Leave."])
      if choice == 1:
        if player.hasFlag("Blacktop_Int1_FourSquareShenanigans") == False:
          dialNoSpeaker("You ask to join the game.")
          dial("Shameer","Hang on, just need to get Dasha out of the king square...")
          dialNoSpeaker("Shameer proceeds to plunge the ball onto the ground at a high velocity, obliterating Dasha.")
          dial("Henry","Hey, that's a ~~Jerry Wong~~ cherry bomb.")
          dial("Dasha","That was racially motivated, wasn't it Shameer?")
          dial("Shameer","._.")
          dial("Dasha","You're specifically targetting the Cuban, aren't you?")
          dial("Shameer","Wha-")
          dial("Justin","Shameer, blatant racism isn't tolerated here.")
          dial("Shameer","Bro- it's not against the rules.")
          dial("Dasha","Are you implying that you accept the degradation of Cubans when it isn't mentioned explicity in the four square rules?")
          dial("Shameer","...")
          dial("Henry","Just leave Shameer.")
          dial("Shameer","Fine.")
          dialNoSpeaker("Shameer steps out of the game, brining you into square one.")
          dial("Dasha","Alright Justin...")
          dial("Dasha","You know the rules? Don't target square one.")
          dial("Justin","... fine.")
          dialNoSpeaker("Dasha passes the ball to Justin.")
          dialNoSpeaker("Despite what Dasha said, Justin passes the ball to you.")
          dialNoSpeaker("...")
          dialNoSpeaker("You channel the force of two-hundred thousand newtons, your head filled with the math knowledge gained from Sofya Ro's PandaMath Thunkable App.")
          dialNoSpeaker("You proceed to smash Justin in the face with the ball traveling at an asymptotic acceleration apporaching infinity.")
          dial("Justin","*(Wiping his face)* ...")
          dial("Justin","I- I-")
          dial("Justin","I don't like you.")
          dial("Justin","You're just another meanie zucchini...")
          dial("Justin","... like Valeria Rivera with her ambiguous and disrespectful Google Form responses.") 

          if not runBattle(player, JustinBattleStudent()):
            return
            
          dial("Justin","...")
          dial("Justin","THAT BALL HURTS YOU KNOW!")
          dial("Dasha","Don't worry Justin, we can transport you to the local hospital.")
          dial("Henry","Yeah, you'll get to meet Preston there. Wouldn't that be a fun reuinion?")
          dial("Justin",">:(")
          dialNoSpeaker("Justin, Dasha, Henry, and Shameer leave your vicinity, presumably heading to the hospital where Preston's residing.")

          player.giveTickets(100)
          printFlair("You earned 100 tickets from the battle!")
          
          player.addFlag("Blacktop_Int1_FourSquareShenanigans")
        else:
          dialNoSpeaker("There's no one to play four square with. :(")
  
      elif choice == 2:
        player.classroom = None
        return
    else:
      dialNoSpeaker("There's nobody on the blacktop.")
      dialNoSpeaker("You walk around for a bit...")
      dialNoSpeaker("...")
      dialNoSpeaker("... this isn't very fun.")
      dialNoSpeaker("You leave to do better things with your time.")
      player.classroom = None
      return

class GreenhouseClassroom(Classroom):
  def __init__(self):
    self.name = "Greenhouse"
    self.locked = [1, 3]

  def run(self, player):
    if player.act == 2:
      if player.hasItem(GymKeysItem) and player.hasFlag("MainGym_Int1_WhiteSucculent"):
        dialNoSpeaker("As you try to open the Greenhouse door, you can spot Ms. Gleich sprinting towards you.")
        dial("Ms. Gleich","What did I say?")
        dial("Ms. Gleich","You're supposed to return the Gym Keys to me when you've collected that paddle.")
        dial("Ms. Gleich","Although I have to admit that sneaking out during dismissal was a smart way to try to steal them.")
        dial("Ms. Gleich","Not smart enough, though.")
        dialNoSpeaker("Ms. Gleich snaches the Gym Keys straight out of your hands.")
        dial("Ms. Gleich","Let that be a lesson.")
        player.removeItem(GymKeysItem)
        player.incrementQuestProgress(TableTennisQuest)
    
      clear()
  
      printBoxedText("The Greenhouse")
      print() 
      
      # Classroom Description
      printC("You’re in the greenhouse, the place contrasts heavily from the barren grassland outside. Flourishing flowers of different colors envelop you.")
      print()
      printC("You can spot Ellie along with your good friends Katherine and Peter gardening.")

      interactionName = "Talk to Ellie."
      if player.hasFlag("Greenhouse_Int1_EllieSucculentHunting"):
        interactionName = "Give Ellie some succulents."
        
      choice = dropdownMenu("What do you do?",[interactionName,"Talk to Peter.","Talk to Katherine.","Leave the greenhouse."])

      if choice == 1:
        if player.hasFlag("Greenhouse_Int1_EllieSucculentHunting") == False:
          dialNoSpeaker("Ellie seems to be eyeing a paticular shelf with great interest.")
          dial("Ellie","You ever feel like that shelf? Empty and lost inside.")
          dial("Ellie","Me neither, who thinks of that?")
          dialNoSpeaker("Ellie turns to you.")
          dial("Ellie","Hey, I remember you!")
          dial("Ellie","You're the person that freed us from Ms. Ramasamy's room!")
          dial("Ellie","Thank goodness for your help! I didn't like being in the same room as Poorvi and Ella for that long.")
          dialNoSpeaker("Ellie turns back to the empty shelf.")
          dial("Ellie","*(Sigh)* Still can't figure what to place there.")
          dial("Ellie","I was think of filling the space with some succulents but I only have one.")
          dialNoSpeaker("Ellie pulls out a beautiful yellow succulent.")
          dial("Ellie","This right here is a |Y|Yellow Sempervivum|B|, isn't it gorgeous?")
          dial("Ellie","Its bright yellow petals shine pretty beneath the sun.")
          dial("Ellie","Although... it just feels so... lonely.")
          dial("Ellie","I wanted to buy it some friends but all my birthday money went to my mother's down payments.")
          dial("Ellie","...")
          dial("Ellie","Hey wait...")
          dial("Ellie","Can you, by any chance, find some succulents for me?")
          dial("Ellie","I've seen plenty scattered throughout Clemente but I only need nine to fill up this shelf.")
          dial("Ellie","Huh? What's that? The school entrance is locked?")

          printFlair("Ellie gives you a Teacher's Pass.")
          player.giveItem(TeachersPassItem)

          dial("Ellie","Poorvi managed to swipe three of these passes from Ms. Presley, one for her, one for Ella, and one for me.")
          dial("Ellie","I don't use mine often, I'll gladly let you keep it as long as you find those succulents.")
          dial("Ellie","Thanks in advance! :)")

          player.startQuest(SucculentQuest)
          player.incrementQuestProgress(SucculentQuest)
    
          player.addFlag("Greenhouse_Int1_EllieSucculentHunting")
        else:
          numSucculents = 1
          succulentFlags = {
            OrangeEcherviaSucculentItem: ["Greenhouse_Int1_OrangeEcherviaReturned", "Wow, this one is so pretty, it even glistens!"],
            AloeVeraSucculentItem: ["Greenhouse_Int1_AloeVeraReturned", "Spectacular! Aloe Vera is Ms. Presley's favorite succulent, I think."],
            LavenderEcherviaSucculentItem: ["Greenhouse_Int1_LavenderEcherviaReturned", "Lavender... a Celestial Cheater would like that color. Nonetheless, it's still amazing."],
            MoonCactusSucculentItem: ["Greenhouse_Int1_MoonCactusReturned", "My oh my, a moon cactus succulent is just what this greenhouse needs!"],
            StrawberrySempervivumSucculentItem: ["Greenhouse_Int1_StrawberrySempervivumReturned", "Aww, this one even has miniature grass. I'm sure that won't cause any problems."],
            RedEcherviaSucculentItem: ["Greenhouse_Int1_RedEcherviaReturned", "This one feels a bit... unnerving. The color is still beautiful."],
            BurrosTailSucculentItem: ["Greenhouse_Int1_BurrosTailReturned", "Oh... I personally find this succulent a bit odd. Still, I'll accept it."],
            WhiteHaworthiaSucculentItem: ["Greenhouse_Int1_WhiteHaworthiaReturned", "A Haworthia with a a gorgeous white color? What a spectacular combination!"],
            BallCactusSucculentItem: ["Greenhouse_Int1_BallCactusReturned", "I presume this one was plucked recently. That makes it all the more better!"]
          }

          for succ in succulentFlags.values():
            if player.hasFlag(succ[0]):
              numSucculents += 1

          dialNoSpeaker("The shelf currently has |W|{}/10|B| succulents.".format(numSucculents))
          
          dial("Ellie","Hi again! Do you have any more succulents?")

          succulentsReturned = 0
          
          for pair in succulentFlags.items():
            if player.hasItem(pair[0]):
              try:  
                assert not player.hasFlag(pair[1][0])
              except:
                raise ContentError()
                
              player.removeItem(pair[0])

              nameOfSucculent = pair[0]().name
              
              if nameOfSucculent[0].lower() in "aeiou":
                dialNoSpeaker("You give Ellie an {}.".format(pair[0]().getName()))
              else:
                dialNoSpeaker("You give Ellie a {}.".format(pair[0]().getName()))
                
              dial("Ellie", pair[1][1])

              player.addFlag(pair[1][0])
              numSucculents += 1
              succulentsReturned += 1
            
          if succulentsReturned == 0:
            dial("Ellie","No? That's okay, make sure to keep your eye out for them around the school!")
            return
          else:
            dial("Ellie", "Thanks for the succulents!")
            player.giveTickets(100 * succulentsReturned)
            dialNoSpeaker("Ellie gives you {} tickets for the returned succulents.".format(100 * succulentsReturned))
            
          if numSucculents == 10:
            dial("Ellie","Wait, that's the last succulent...")
            dial("Ellie","My collection is complete! :)")
            dial("Ellie","Thank you so much {} for your help!".format(player.getName()))
            dial("Peter","Finally, I can't bear to garden for any longer. -_-")
            dial("Katherine","Aww, I liked it. :(")
            dial("Ellie","I mean, if you want you c-")
            dial("Poorvi","ELLIE!")
            dialNoSpeaker("Poorvi and Ella enter the greenhouse, weilding badminton rackets.")
            dial("Poorvi","IS THIS WHERE YOU'VE BEEN? GARDENING?")
            dial("Ellie","Uh... yeah?")
            dial("Ellie","But fear not Poorvi, for these three *(pointing at you, Katherine, and Peter)* aren't strangers. They're my friends!")
            dial("Poorvi","Friends?")
            dial("Ellie","Yeah! I'm so popular. ^_^")
            dial("Poorvi","-_-")
            dial("Poorvi","*(Sigh)* Enough jabbering...")
            dial("Poorvi","What we really came for was this.")
            dialNoSpeaker("Poorvi grabs the Aloe Vera succulent from Ellie's shelf.")
            dial("Ellie","Hey. >:(")
            dial("Poorvi","You see, there's something very special about Aloe Vera that most overlook.")
            dial("Poorvi","Ms. Presley taught me that this green watery plant has the ability to transpire life.")
            dial("Peter","Transpire... life?")
            dial("Katherine","Silly Poorvi, all plants can transpire!")
            dial("Katherine","I would know since I've been studying plant genetics to ensure full marks on Ms. Santigo's AP biology-")
            dial("Poorvi","*(Ahem)* Ella?")
            dial("Ella","*(Rolls eyes)* Oh, right.")
            dialNoSpeaker("Ella pulls out an Arduino circuit that uses an assorted selection of wire colors.")
            dialNoSpeaker("Poorvi cements some of the male-to-male wires in the circuit near the base of the Aloe Vera succulent.")
            dial("Katherine","Wh- what is that?")
            dial("Poorvi","This here is a P.L.A.N.T.")
            dial("Poorvi","A \"Perceptive Life-Awakening Nexus of Transpiration\"!")
            dial("Poorvi","By harnessing the Arduino's vast network of libraries, I've deduced a suitable way to extract the enzyme Chalcone Isomeras-")
            dial("Ella","It simply revives people.")
            dial("Poorvi","ELLA!")
            dial("Peter","... you created a device that can... bring people back from the dead?")
            dial("Poorvi","Of course! And we can test it out right now!")
            dialNoSpeaker("Poorvi rips out a piece of paper from her engineering notebook and lunges it straight at Katherine.")
            dial("Katherine","*(As the paper hits her)* Ack!")
            dialNoSpeaker("|R|Katherine gets a papercut and... doesn't die?")
            dial("Katherine","Don't worry Poorvi, I have plot armor. ^-^")
            dial("Poorvi","Are you kidding me?")
            dial("Poorvi","Ella, you said this would work!")
            dial("Ella","You really thought that people could perish after... a papercut?")
            dial("Ella","Shame on you.")
            dial("Poorvi","...")
            dial("Poorvi","Luckily... I had something else in mind...")
            dialNoSpeaker("Poorvi gracefully snaps her fingers, a gesture that effortlessly commands attention.")
            dialNoSpeaker("Abruptly, an ornate frog statue positioned behind Ellie begins to fracture, revealing a slimy frog donning an exquisite meidival attire and weilding a delicate sword.")
            dialNoSpeaker("You, Katherine, and Peter have a distasteful look on your face.")
            dial("Effie","Greetings my queen!")
            dial("Effie","I have been summonded henceforth to serve you under the divine blessing from the god that surrounds us all.")
            dial("Effie","How shall I serve you today?")
            dial("Poorvi","Kill Katherine.")
            dial("Katherine","WHAT!")
            dial("Effie","I see my queen, but who exactly is this 'Katherine'?")
            dial("Effie","For I, with upmost respect, cannot interpert your orders until you provide me enough clarification.")
            dial("Poorvi","Uh- the person in-")
            dial("Effie","Thank you your majesty, I have detected who this 'person' is and shall commence your wishes.")
            dialNoSpeaker("Effie points her sword at you.")
            dial("Poorvi","...")
            dial("Poorvi","...that works as well.")
            dial("Effie","Hello. My name is Effie Montoya. You killed my father. Prepare to die.")
            dial("Ella","The heck does that mean?")
            dial("Effie","Shush, It's an expression!")

            if not runBattle(player, EffieBattleFrog()):
              return
              
            dial("Effie","...")
            dial("Effie","Inconceivable.")
            dialNoSpeaker("Effie bursts into many pieces, Slime Rancher style.")
            dial("Poorvi","...")
            dial("Ella","Poorvi, can't you use the device to, yknow, recover her?")
            dial("Poorvi","Well- I- I mean- I could...")
            dial("Ella","And?")
            dial("Poorvi","The device is one-time use, it'll suck out all the life out of this poor Aloe Vera...")
            dial("Poorvi","I'll have to save it for someone more desirable.")
            dial("Poorvi","And I have just the person in mind...")
            dial("Ella","... who?")
            dial("Poorvi","Wouldn't want Ellie's friends to get a glimpse of what we're up to, would we?")
            dial("Poorvi","Speaking of which...")
            dial("Poorvi","Ellie, you're going to be big asset in this operation.")
            dial("Poorvi","We need you over here.")
            dial("Ellie","But- but-")
            dial("Poorvi","Just... get over here.")
            dial("Ellie","*(Sigh)* Fine.")
            dialNoSpeaker("Ella, Poorvi, and Ellie scurry out of the greenhouse.")
            
            player.incrementQuestProgress(SucculentQuest)
            
            dial("Katherine","...                                                    ")
            dial("Peter","...")
            dial("Katherine","They just stole Ellie like that...")
            dial("Peter","...")
            dial("Peter","...")
            dial("Peter","So Katherine...")
            dial("Peter","How- How your day been-")
            dial("Katherine","I'm going to steal her back.")
            dial("Peter","Wha- that- that- that wording is a bit- ")
            dial("Katherine","Oh, is there a better alternative?")
            dial("Peter","You could've phrased it as-")

            player.act = 3
            player.classroom = None
            return
          else:
            dial("Ellie","The shelf's still a bit empty, though... Can you try finding some more?")


      
      elif choice == 2:
        if player.hasFlag("Greenhouse_Int2_PeterGardening") == False:
          dial("Peter","I don't know why Katherine roped me into this.")
          dial("Peter","I'm not even a Global student!")
          dial("Peter","Who cares about nature?")
          dial("Ellie","Peter...")
          dial("Ellie","I exist, you know?")
          dial("Peter","But- but you're not a global student either. Are you?")
          dial("Ellie","Well- uh- what about you? Are you going to Poolesville?")
          dial("Peter","Nah. I'm going to RM.")
          dial("Ellie","RM?")
          dial("Peter","Richard Montgomery High School.")
          dial("Ellie","Oh... disgusting.")
          dial("Peter",">:(")
          player.addFlag("Greenhouse_Int2_PeterGardening")
        else:
          dial("Peter","I despise gardening. >:(")
      elif choice == 3:
        if player.hasFlag("Greenhouse_Int3_KatherineGardening") == False:
          dial("Katherine","Oh hey {}, nice to see you again!".format(player.getName()))
          dial("Katherine","Ellie looked so lonely gardening by herself, I figured that helping her out would keep her company.")
          dial("Katherine","...")
          dial("Katherine","Gardening is, for lack of a better word, weirdly enjoyable.")
          dial("Katherine","Like, it's actually pretty relaxing.")
          dial("Katherine","No wonder Ellie loves it!")
          dial("Katherine","...")
          dial("Katherine","At least, I hope she loves it.")
          dial("Katherine","I mean, the writers are pretty incompetent.")
          dial("Katherine","They hardly know Ellie!")
          dial("Katherine","They just wanted her and Ella to be polar opposites so that their personalities won't clash.")
          dial("Katherine","...")
          dial("Katherine","I won't be able to keep you company till my gardening duties are complete, sorry.")
          dial("Katherine","But knowing you, you're capable of being independent! :)")
      
          player.addFlag("Greenhouse_Int3_KatherineGardening")
        else:
          dial("Katherine","I love gardening. >:)")
      elif choice == 4:
        player.classroom = None
        return 
