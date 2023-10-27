from imports import *


printC("Hey, thanks for playing our game!\n", "B")
printC("Presleyn is now in an |W|Acts I-II Demo|B| release!\n", "B")
printC("Please remember that the game is still in development, and please report any issues you had with playing!\n", "B")
printC("Thank you so much <3", "B")
enter()
printC("Huge shoutout to Ella, Poorvi, and [REDACTED] for letting us use their amphibian arcade game, thanks!")
#printC("If the game crashes after this, it's not open to the public yet. Go away!", "R")
#printC("Although, we still love you for considering to play this early. <3")
#assert os.environ['REPL_OWNER'] == "Unequip"

######################
## SAVEFILE HELPERS ##
######################

def resetSaves():
  for key in db.keys():
    if key != "secretpasscode":
      del db[key]

# First Time Playing

try:
  _ = db["COMPLETED_TUTORIAL_BEFORE"]
except:
  db["COMPLETED_TUTORIAL_BEFORE"] = False
  
try:
  _ = db["SAVEFILES"]
except:
  clear()
  dial("???", "Hey there!")
  dial("???", "It looks like you're new around here...")
  dial("???", "I was told to advise you to play in |W|Fullscreen Mode|B| and |W|on a computer/device with a keyboard|B| to maximize enjoyment.")
  dial("???","UNLIKE A CERTAIN KATHERINE XU!")
  dial("???", "Got that?")
  dial("???", "Okay, good luck!")
  clear()
  
  db["SAVEFILES"] = []
  db["COMPLETED_GAME_BEFORE"] = False
  db["COMPLETED_TUTORIAL_BEFORE"] = False

SAVEFILE_PLAYER = MapPlayer()


def loadSavefile(SAVEFILE_NAME):
  global SAVEFILE_PLAYER
  
  SAVEFILE_PLAYER.name = SAVEFILE_NAME
  
  SAVEFILE_NAME = SAVEFILE_NAME.upper()
  
  SAVEFILE_PLAYER.nameColor = db["{}_NAME_COLOR".format(SAVEFILE_NAME)]
  
  SAVEFILE_PLAYER.loc = list(db["{}_LOCATION".format(SAVEFILE_NAME)]).copy()

  SAVEFILE_PLAYER.tickets = db["{}_TICKETS".format(SAVEFILE_NAME)]

  SAVEFILE_PLAYER.wands = list(INTERNAL_IDS[w] for w in db["{}_WANDS".format(SAVEFILE_NAME)])
  SAVEFILE_PLAYER.selectedWand = INTERNAL_IDS[db["{}_SELECTED_WAND".format(SAVEFILE_NAME)]]
  SAVEFILE_PLAYER.spells = list(INTERNAL_IDS[s] for s in db["{}_SPELLS".format(SAVEFILE_NAME)])
  SAVEFILE_PLAYER.arsenal = list(INTERNAL_IDS[s] for s in db["{}_ARSENAL".format(SAVEFILE_NAME)])

  SAVEFILE_PLAYER.items = []
  for i in db["{}_ITEMS".format(SAVEFILE_NAME)]:
    SAVEFILE_PLAYER.items.append(INTERNAL_IDS[i[0]](i[1]))
    
  SAVEFILE_PLAYER.quests = []
  for q in db["{}_QUESTS".format(SAVEFILE_NAME)]:
    SAVEFILE_PLAYER.quests.append(INTERNAL_IDS[q[0]](q[1], q[2]))
  
  SAVEFILE_PLAYER.emails = []
  for e in db["{}_EMAILS".format(SAVEFILE_NAME)]:
    SAVEFILE_PLAYER.emails.append(INTERNAL_IDS[e[0]](e[1], e[2])) 

  SAVEFILE_PLAYER.flags = []
  for f in db["{}_FLAGS".format(SAVEFILE_NAME)]:
    SAVEFILE_PLAYER.flags.append(f)
    # avoids goofy ah replit database error

  SAVEFILE_PLAYER.act = db["{}_ACT".format(SAVEFILE_NAME)]
  SAVEFILE_PLAYER.time = db["{}_TIME".format(SAVEFILE_NAME)]
  SAVEFILE_PLAYER.day = db["{}_DAY".format(SAVEFILE_NAME)]

  SAVEFILE_PLAYER.deaths = db["{}_DEATHS".format(SAVEFILE_NAME)]
  SAVEFILE_PLAYER.missedBuses = db["{}_MISSED_BUSES".format(SAVEFILE_NAME)]
  SAVEFILE_PLAYER.health = db["{}_HEALTH".format(SAVEFILE_NAME)]

  if SAVEFILE_PLAYER.nameColor == "B":
    MAP_SYMBOL_COLORS["◎"] = "PI"
  else:
    MAP_SYMBOL_COLORS["◎"] = SAVEFILE_PLAYER.nameColor

  

def updateSavefile():
  global SAVEFILE_PLAYER

  SAVEFILE_NAME = SAVEFILE_PLAYER.name.upper()

  db["{}_NAME_COLOR".format(SAVEFILE_NAME)] = SAVEFILE_PLAYER.nameColor
  db["{}_LOCATION".format(SAVEFILE_NAME)] = list(SAVEFILE_PLAYER.loc).copy()

  db["{}_TICKETS".format(SAVEFILE_NAME)] = SAVEFILE_PLAYER.tickets
  
  db["{}_WANDS".format(SAVEFILE_NAME)] = [getID(w) for w in SAVEFILE_PLAYER.wands]
  db["{}_SELECTED_WAND".format(SAVEFILE_NAME)] = getID(SAVEFILE_PLAYER.selectedWand)
  db["{}_SPELLS".format(SAVEFILE_NAME)] = [getID(s) for s in SAVEFILE_PLAYER.spells]
  db["{}_ARSENAL".format(SAVEFILE_NAME)] = [getID(s) for s in SAVEFILE_PLAYER.arsenal]
  db["{}_ITEMS".format(SAVEFILE_NAME)] = [(getID(i), i.quantity) for i in SAVEFILE_PLAYER.items]
  db["{}_QUESTS".format(SAVEFILE_NAME)] = [(getID(q), q.stage, q.pinned) for q in SAVEFILE_PLAYER.quests]
  db["{}_EMAILS".format(SAVEFILE_NAME)] = [(getID(e), e.starred, e.unread) for e in SAVEFILE_PLAYER.emails]
  db["{}_FLAGS".format(SAVEFILE_NAME)] = [f for f in SAVEFILE_PLAYER.flags]
  
  db["{}_ACT".format(SAVEFILE_NAME)] = SAVEFILE_PLAYER.act
  db["{}_TIME".format(SAVEFILE_NAME)] = SAVEFILE_PLAYER.time
  db["{}_DAY".format(SAVEFILE_NAME)] = SAVEFILE_PLAYER.day

  db["{}_DEATHS".format(SAVEFILE_NAME)] = SAVEFILE_PLAYER.deaths
  db["{}_MISSED_BUSES".format(SAVEFILE_NAME)] = SAVEFILE_PLAYER.missedBuses
  db["{}_HEALTH".format(SAVEFILE_NAME)] = SAVEFILE_PLAYER.health

  if SAVEFILE_PLAYER.nameColor == "B":
    MAP_SYMBOL_COLORS["◎"] = "PI"
  else:
    MAP_SYMBOL_COLORS["◎"] = SAVEFILE_PLAYER.nameColor

  syncDatabase()
  
################################
## MAIN GAME LOOP - MAIN MENU ##
################################
  
while True:
  clear()
  printC('''\
╔════════════════════════════════════════════════════════════════════════╗
║                                                                        ║
║   ██████╗ ██████╗ ███████╗ ██████╗██╗     ███████╗██╗   ██╗███╗  ██╗   ║
║   ██╔══██╗██╔══██╗██╔════╝██╔════╝██║     ██╔════╝╚██╗ ██╔╝████╗ ██║   ║
║   ██████╔╝██████╔╝█████╗  ╚█████╗ ██║     █████╗   ╚████╔╝ ██╔██╗██║   ║
║   ██╔═══╝ ██╔══██╗██╔══╝   ╚═══██╗██║     ██╔══╝    ╚██╔╝  ██║╚████║   ║
║   ██║     ██║  ██║███████╗██████╔╝███████╗███████╗   ██║   ██║ ╚███║   ║
║   ╚═╝     ╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚══╝   ║
║                                                                        ║
╚════════════════════════════════════════════════════════════════════════╝''', "B")


  savefiles = db["SAVEFILES"]
  savefile_names = []

  for savefile in savefiles:
    savefile_names.append((savefile, db["{}_ACT".format(savefile.upper())]))

  def getActName(x):
    if x >= 1:
      return "Act {}".format(ROMAN_NUM[x])
    else:
      return "Prologue"
      
  choice = dropdownMenu("Choose a savefile to view: ", ["|{}|".format(db["{}_NAME_COLOR".format(x[0].upper())]) + x[0] + " ({})".format(getActName(x[1])) for x in savefile_names] + ["|G|Create New Savefile", "|Y|View Credits"])
  if choice == len(savefile_names) + 1:
    printC("\nEnter the name for this profile: ", "B", end = "")
    name = input().strip()
    
    if name == "":
      printC("\nYour name can't be nothing, silly!", "R") 
      enter()
      continue
    elif len(name) >= 24:
      printC("\nWow, that's a long name! Try something shorter!", "R")
      enter()
      continue
    elif "|" in name or "\\" in name:
      printC("|R|Pilliam|B|: You think you're cool by trying to choose a name that breaks my code, right?\n")
      printC("|R|Pilliam|B|: Please choose a different name. Preferably one that people can actually pronounce.")
      enter()
      continue
    else:
      failed = False
      for savefile in savefiles:
        if savefile.upper() == name.upper():
          printC("\nYou already have a profile with this name!", "R")
          enter()
          failed = True
          break
      if failed:
        continue

    
    choice = dropdownMenu("\nCreate a new profile with name \"{}\"?".format(name), ["|G|Confirm", "|R|Cancel"])
    if choice == 1:
      printC("\nCreating new profile...", "DG")

      origName = name
      name = name.upper()

      db["{}_NAME_COLOR".format(name)] = "B"
      db["{}_WANDS".format(name)] = []
      db["{}_SELECTED_WAND".format(name)] = 0
      db["{}_SPELLS".format(name)] = []
      db["{}_ARSENAL".format(name)] = []
      db["{}_ITEMS".format(name)] = []

      db["{}_LOCATION".format(name)] = ["PROLOGUE_AREA", "PROLOGUE_SIDEWALK_5"]
      db["{}_TICKETS".format(name)] = 0

      db["{}_QUESTS".format(name)] = []
      db["{}_EMAILS".format(name)] = []
      db["{}_FLAGS".format(name)] = []
      
      db["{}_ACT".format(name)] = 0

      db["{}_TIME".format(name)] = 0
      db["{}_DAY".format(name)] = 1

      db["{}_DEATHS".format(name)] = 0
      db["{}_MISSED_BUSES".format(name)] = 0
      db["{}_HEALTH".format(name)] = 100
      
      db["SAVEFILES"].append(origName)
      
      printC("Profile created successfully!", "G")
      enter()
    elif choice == 2:
      printC("\nCancelled profile creation!", "R")
      enter()

  elif choice == len(savefile_names) + 2:
    clear()
    printC('''\
╔════════════════════════════════════════════════════════════════════════╗
║                                                                        ║
║   ██████╗ ██████╗ ███████╗ ██████╗██╗     ███████╗██╗   ██╗███╗  ██╗   ║
║   ██╔══██╗██╔══██╗██╔════╝██╔════╝██║     ██╔════╝╚██╗ ██╔╝████╗ ██║   ║
║   ██████╔╝██████╔╝█████╗  ╚█████╗ ██║     █████╗   ╚████╔╝ ██╔██╗██║   ║
║   ██╔═══╝ ██╔══██╗██╔══╝   ╚═══██╗██║     ██╔══╝    ╚██╔╝  ██║╚████║   ║
║   ██║     ██║  ██║███████╗██████╔╝███████╗███████╗   ██║   ██║ ╚███║   ║
║   ╚═╝     ╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚══╝   ║
║                                                                        ║
╚════════════════════════════════════════════════════════════════════════╝''', "B")
    print()
    printC('''\
                   ╔═════════════════════════════════════╗
                   ║               CREDITS               ║
                   ╚═════════════════════════════════════╝''', "B")
    print()
    printC("Programmers: ", "B")
    printC("- Pilliam Wark (@SmartyNotchy)    Frameworks, QoL, Overworld, Battles, Spells", "R")
    printC("- Akash Saran (@Unequip)          Storyline, Interactions, Mapping, Spells", "LB")
    printC("- Arjun Mujumdar (@QuackyDucc)    Interactions, Quests, Spells, Wands", "Y")
    printC("- Omkar Bantanur                  *sigh...* \"Early Spell... Prototyping???\"", "PU")
    print()
    print()
    printC("Early Playtesters (Found Major Game Issues, Thanks <3):", "B")
    printC("- Anna Zhou (@AnnaZhou2)","LG")
    printC("- Ryan Diehl (@RyanDiehl)","DB")
    printC("- Katherine Xu (@KatherineX)","PI")
    printC("- Krishan Maranchi (@SmartyKoala)","O")
    print()
    print()
    printC("Supporters:", "B")
    printC("- Anna Zhou (@AnnaZhou2)","DG")
    printC("- Srivatsan Ganesh (@redblue99)","DG")
    printC("- Gloria Badibanga (@GloriaBadibanga)","DG")
    print()
    print()
    printC("Special Thanks (Students):","B")
    printC("- Aadhavan M (@AadhavanMuralid)   - Khang T","DG")
    printC("- Aarya S                         - Krishan M (@SmartyKoala)","DG")
    printC("- Akshaj E (@AkshajEruventi1)     - Lillian J","DG")
    printC("- Ankush K                        - Luke N","DG")
    printC("- Anna Z (@AnnaZhou2)             - Maya K","DG")
    printC("- Ariam N (@AriamNehemiah)        - Nathan A (@Magicarp)","DG")
    printC("- Benedicte T                     - Percy C","DG")
    printC("- Brandon T                       - Peter Z <3 (@PeterZhao4)","DG")
    printC("- Brandon V (@BrandonVillafue)    - Poorvi D","DG")
    printC("- Brooke Y                        - Preston L","DG")
    printC("- Bryce F                         - Rachel K","DG")
    printC("- Caleb W                         - Roselyn M","DG")
    printC("- Chris W                         - Ryan D (@RyanDiehl)","DG")
    printC("- Daniel E (@iamsirsammy)         - Sayf B (@xmoto200)","DG")
    printC("- Dasha D                         - Sergi B","DG")
    printC("- Don N                           - Shameer S (@ShameerSiddiqui)","DG")
    printC("- Edem A                          - Sherry W","DG")
    printC("- Ella P                          - Shriram M (@ShriramMasanam)","DG")
    printC("- Ellie H                         - Sofya R","DG")
    printC("- Gabrielle K (@G4bbyK)           - Srivatsan G (@redblue99)","DG")
    printC("- Gloria B (@GloriaBadibanga)     - Terence K","DG")
    printC("- Goran N (@GoranNaydenov)        - Tyler M","DG")
    printC("- Henry P                         - Valeria R (@ValeriaRivera2)","DG")
    printC("- Jashlee D                       - William C","DG")
    printC("- Jessika J                       - Yulia A","DG")
    printC("- Justin R (@JustinRonchi)        - Cello-San (@AnnaZhou2)","DG")
    printC("- Katherine X (@KatherineX)       - Detah-Chan (@AnnaZhou2)","DG")
    printC("- Kedus A","DG")
    print()
    print()
    printC("Special Thanks (Teachers):","B")
    printC("- Ms. Ramasamy                    - Ms. Lee","DG")
    printC("- Ms. Mahon                       - Ms. Santiago","DG")
    printC("- Ms. Akano                       - Mr. Kepler","DG")
    printC("- Ms. Presley                     - Ms. Poole","DG")
    printC("- Ms. Gleich                      - Mr. Smith","DG")
    printC("- Ms. Palank                      - Ms. MacDonald","DG")
    
    
    
    
    flush_input()
    enter()
  else:
    username = savefile_names[choice-1][0]
    choice = dropdownMenu("\nViewing '{}' ({})".format(username, getActName(db["{}_ACT".format(username.upper())])), ["|G|Load Savefile", "|Y|Rename Savefile", "|R|Delete Savefile", "|DG|Cancel"])
    if choice == 1:
      printC("\nLoading savefile \"{}\"...".format(username), "B")
      try:
        loadSavefile(username)

        if SAVEFILE_PLAYER.act >= 3:
          #assert os.environ['REPL_OWNER'] == "Unequip"
          assert True
        if SAVEFILE_PLAYER.act >= 4:
          assert False

        printC("Savefile loaded successfully!", "G")
      
        flush_input()
        enter()
        break
      except:
        printC("Acts III and above are not available for playtesting at this moment. Sorry!", "R")
        printC("If you got this message while attempting to load a non-act III profile, please report this incident.", "R")
        enter()
        exit(1)
    elif choice == 2:
      printC("\nEnter the new name for this profile: ", "B", end="")
      new_username = input().strip()
      already_existing = False
      for existing_username in db["SAVEFILES"]:
        if existing_username.upper() == new_username.upper() and existing_username.upper() != username.upper():
          already_existing = True
          break
      if already_existing:
        printC("You already have a profile with this name!", "R")
      elif new_username == "":
        printC("Your name can't be blank, silly!", "R")
      elif len(new_username) >= 24:
        printC("Wow, that's a long name! Try something shorter!", "R")
      elif "|" in new_username or "\\" in new_username:
        printC("|R|Pilliam|B|: You think you're cool by trying to choose a name that breaks my code, right?\n")
        printC("|R|Pilliam|B|: Please choose a different name. Preferably one that people can actually pronounce.")
      elif new_username == username:
        printC("That's the same name!", "R")
      else:
        choice = dropdownMenu("Rename this profile to \"{}\"?".format(new_username), ["|G|Confirm", "|R|Cancel"])
        if choice == 1:
          printC("\nRenaming your savefile... |R|(Please do not exit the program!)", "B")
          loadSavefile(username)
          db["SAVEFILES"].remove(username)
          username = new_username
          SAVEFILE_PLAYER.name = username
          updateSavefile()
          db["SAVEFILES"].append(username)
          printC("\nProfile successfully renamed to \"{}\"!".format(username), "G")
        else:
          printC("\nCanceled profile renaming!", "R")
        
      flush_input()
      enter()
    elif choice == 3:
      printC("\nAre you sure?", "R")
      flush_input()
      printC("Type 'DELETE' in all caps (without the quotes) to confirm: ", "R", end = "")
      choice = input().strip()
      if choice == "DELETE":
        db["SAVEFILES"].remove(username)
        printC("\nSavefile deleted!", "R")
        flush_input()
        enter()
      else:
        printC("\nDeletion canceled!", "G")
        flush_input()
        enter()
    elif choice == 4:
      flush_input()
      enter()

      



###############################
## MAIN GAME LOOP - GAMELOOP ##
###############################

clear()

'''
schoolMap = SchoolMap()
idx = 0
clear()
MAP_TO_TEST = "BLACKTOP"
print(convertMap(schoolMap.asciiMaps[MAP_TO_TEST]))
print("\n\nFrom left-to-right, top-to-bottom")
for char in schoolMap.asciiMaps[MAP_TO_TEST]:
  if char == "+":
    print("Found waypoint at {}".format(idx-1))
  idx += 1
print()

exit(1)
#'''

# Give Debug Spell
# SAVEFILE_PLAYER.giveSpell(DebugSpell)

SCHOOL_MAP = SchoolMap()


# MAIN GAME LOOP
alertedDismissalYet = False
skipGoingToBedText = False

while True:
  lastCheckedAct = SAVEFILE_PLAYER.act

  if not alertedDismissalYet and SAVEFILE_PLAYER.timePast(420):
    dialNoSpeaker("|R|The bell chimes for dismissal!")
    dialNoSpeaker("Bus 2992 has pulled into the bus lane and is ready to leave.")
    if SAVEFILE_PLAYER.act == 1:
      dialNoSpeaker("You can leave the school now via the main entrance, or stay behind for a bit.")
    else:
      dialNoSpeaker("You can leave the school now via the main entrance or going to the bus lane from outside, or stay behind for a bit.")
    
    dialNoSpeaker("Make sure to leave by |W|4:30 PM|B| or else you'll miss your bus!")

    alertedDismissalYet = True
    SCHOOL_MAP.playerLastSection = None
    clear()
    
  # Left School
  if not SAVEFILE_PLAYER.inSchool:
    SAVEFILE_PLAYER.inSchool = True
    SAVEFILE_PLAYER.time = 0
    SAVEFILE_PLAYER.day += 1
    if SAVEFILE_PLAYER.act == 1:
      SAVEFILE_PLAYER.loc = ["MAIN_ENTRANCE", "ENTRANCE_HALLWAY_8"]
    else:
      SAVEFILE_PLAYER.loc = ["OUTSIDE_ENTRANCE", "OUTSIDE_SCHOOL_SIDEWALK_3"]

    if not skipGoingToBedText:
      clear()
      dialNoSpeaker("You finally arrive back home after a long bus ride, and eat a quick dinner before going to bed.")
      dialNoSpeaker("...")
      dialNoSpeaker("The next day, you wake up and hop on Bus 2992 to go back to school for another day...")
      clear()
    skipGoingToBedText = False

    updateSavefile()
    alertedDismissalYet = False
    
    continue

  # Is In Classroom
  if SAVEFILE_PLAYER.classroom != None:
    # Prologue Entrance
    if SAVEFILE_PLAYER.act == 0:
      SAVEFILE_PLAYER.incrementTime(13) # Start at 8:15 AM (The Player's Late)
      
    # If door is locked
    if SAVEFILE_PLAYER.act in SAVEFILE_PLAYER.classroom.locked:
      defaultLockedDoorInteraction(SAVEFILE_PLAYER)
    else:
      SAVEFILE_PLAYER.classroom.run(SAVEFILE_PLAYER)
      SAVEFILE_PLAYER.incrementTime(2)

    # Update Savefile If Not Left School AND Act Not Changed
    if SAVEFILE_PLAYER.inSchool and SAVEFILE_PLAYER.act == lastCheckedAct:
      updateSavefile()
    elif not SAVEFILE_PLAYER.inSchool:
      continue

  # Is in Overworld Map
  else:
    SCHOOL_MAP.run(SAVEFILE_PLAYER)

    # Can't time-out in these areas
    if SAVEFILE_PLAYER.loc[0] in ["PROLOGUE_AREA", "OUTSIDE_ENTRANCE", "CARPOOL_LANE"]:
      SAVEFILE_PLAYER.time = 0

  # Act Complete
  if SAVEFILE_PLAYER.act != lastCheckedAct:
    if lastCheckedAct == 0:
      updateSavefile()
      continue

    causeOfEarlyRelease = random.choice(["an incident that occurred in seventh grade physical education", "the lack of cafeteria food delivery", "the bathrooms running out of toilet paper", "multiple cases of Pseudocode Overdose Syndrome today", "a malfunctioning fire alarm", "the disappearance of a green box cutter","the Rainbow Hawks forgetting to meet up"])
    
    if lastCheckedAct == 1:
      clear()
      SCHOOL_MAP.run(SAVEFILE_PLAYER, immediatelyQuit=True)
      dialNoSpeaker("|R|Suddenly, the intercom sends a screeching noise throughout the school as it turns on...")
      dial("Peter", "Ow- my ears...")
      dial("Katherine", "Seriously? These messages always come at the most inconvenient times.")
      
      if SAVEFILE_PLAYER.timePast(420):
        dial("Announcement Lady", "Due to {}, we are calling all remaining students to leave the building.".format(causeOfEarlyRelease))
      else:
        dial("Announcement Lady", "Due to {}, we are calling an early release for all students & teachers.".format(causeOfEarlyRelease))
      dial("Announcement Lady", "If you are still in the building, please make your way to the front entrance to get on your bus or method of transportation.")
      dial("Katherine", "Well, guess we aren't seeing each other until tomorrow...")
      dial("Katherine", "Farewell, {}!".format(SAVEFILE_PLAYER.name))
      dial("Peter", "Goodbye...")
      dialNoSpeaker("You make your way to the front entrance, get on Bus 2992, and leave the school.")
      dialNoSpeaker("On the bus ride, you think about all that happened today and the events to inevitably come...")
      dialNoSpeaker("Until you're back at home, safe and sound.")
      dialNoSpeaker("You cuddle up in your bed and get a good night's rest for tomorrow...")
      
      printFlair("     Act I Complete     ")


      SAVEFILE_PLAYER.inSchool = False
      skipGoingToBedText = True

    if lastCheckedAct == 2:
      dialNoSpeaker("|R|Suddenly, the intercom sends a screeching noise throughout the greenhouse as it turns on...")
      dial("Peter", "... again?")
      dial("Katherine", "OK, now this is just sad.")

      
      if SAVEFILE_PLAYER.timePast(420):
        dial("Announcement Lady", "Due to {}, we are calling all remaining students to leave the building.".format(causeOfEarlyRelease))
      else:
        dial("Announcement Lady", "Due to {}, we are calling an early release for all students & teachers.".format(causeOfEarlyRelease))
      
      dial("Announcement Lady", "If you are still in the building, please make your way to the front entrance to get on your bus or method of transportation.")
      dial("Katherine", "Welp, goodbye {}... again...".format(SAVEFILE_PLAYER.getName()))
      dial("Peter", "... I- I- never got to complete my sentence...")
      dial("Katherine","We can discuss tomorrow.")
      dial("Katherine","For now, farewell you two!")

      dialNoSpeaker("You make your way to the front entrance, get on Bus 2992, and leave the school.")
      dialNoSpeaker("On the bus ride, you think about all that happened today and the events to inevitably come...")
      dialNoSpeaker("You question Poorvi's motives: What will she use the P.L.A.N.T for? Why did she need Ellie? What all has she done with the master keys?")
      dialNoSpeaker("All these questions linger in your hand until...")
      dialNoSpeaker("You're back home, safe and sound.")
      dialNoSpeaker("You cuddle up in your bed, play some warm Lofi Music, and get a good night's rest. :)")
      
      printFlair("     Act II Complete     ")

      try:
        assert os.environ['REPL_OWNER'] == "Unequip"
        SAVEFILE_PLAYER.inSchool = False
        skipGoingToBedText = True
        continue
      except:
        updateSavefile()
        dialNoSpeaker("Thanks for playing & completing Act II!")
        dialNoSpeaker("Please report any problems or issues you ran into while playing, and we will try our best to fix them!")
        dialNoSpeaker("A full game release is planned on March 30th 2023. |DG|*Haha, like that would have ever happened...*")
        dialNoSpeaker("Thanks for everything <3")
        break
      
      
  # Missed Bus
  if SAVEFILE_PLAYER.timePast(510):
    dialNoSpeaker("|R|As the clock strikes 4:30 PM, a shiver runs down your spine...")
    dialNoSpeaker("Suddenly, you realize that you missed your bus.")
    dialNoSpeaker("You tentatively excuse yourself and rush to the main entrance to call your parents...")
    dial("Parental Figure", "You WHAT? You missed the bus?")
    dial("Parental Figure", "I told you, you should be more responsible. You were probably goofing off, weren't you?")
    dial("Parental Figure", "I'll pick you up soon, but you'll be in big trouble when you get home!")
    dialNoSpeaker("Once your parents pick you up, they give you a long lecture on phone usage...")

    ticketsRemoved = 50
    if SAVEFILE_PLAYER.tickets > 50:
      SAVEFILE_PLAYER.tickets -= 50
    else:
      ticketsRemoved = SAVEFILE_PLAYER.tickets
      SAVEFILE_PLAYER.tickets = 0

    if ticketsRemoved != 0:
      dialNoSpeaker("They take away {} of your tickets as punishment... TwT".format(ticketsRemoved))
    
    dialNoSpeaker("You immediately go to bed once you get home, exhausted.")
    dialNoSpeaker("The next day, you hop on Bus 2992 quickly and go back to school for another day...")
    
    SAVEFILE_PLAYER.time = 0
    SAVEFILE_PLAYER.day += 1
    SAVEFILE_PLAYER.missedBuses += 1

    if SAVEFILE_PLAYER.act == 1:
      SAVEFILE_PLAYER.loc = ["MAIN_ENTRANCE", "ENTRANCE_HALLWAY_8"]
    else:
      SAVEFILE_PLAYER.loc = ["OUTSIDE_ENTRANCE", "OUTSIDE_SCHOOL_SIDEWALK_3"]
      
    updateSavefile()
    alertedDismissalYet = False
