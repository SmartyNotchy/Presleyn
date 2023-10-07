from imports import *

POSSIBLE_NAMES = ["SmartyNotchy","Unequip","AnnaZhou2","itzrach","SchoolDucc","EllaP310","KatherineX","APerkyWizard","SmartyKoala","RadEnderKing","redblue99","PeterZhao4","Magicarp","xmoto200","OmkarBantanur1","GloriaBadibanga","ValeriaRivera2","hobby2159","CarViz","starlaxiia★","xtcfyvguhbn"]


##############
## MAFIA AI ##
##############

class MafiaPlayer:
  def __init__(self, name, role):
    self.name = name
    self.role = role
    self.isPlayer = False
    # 0 = Normal
    # 1 = Mafia
    # 2 = Doctor
    # 3 = Inspector

    self.alive = True
    self.memory = {}

    self.socialAnxiety = random.randint(0, 2)
    # How "uncertain" this player's dialog is in normal scenarios

    self.lying = random.randint(-4, 4)
    # Add this to self.socialAnxiety by this when lying

    self.gullible = random.randint(1, 10)
    # How much this player's memory is swayed by statements
    # hey look, if you go to line 120 in BATTLE_PLAYER.py you win $1,000,000!!!

    self.deduction = random.randint(1, 10)
    # If a player's statement contradicts their current memory,
    # The amount that their memory of the player being in mafia increases  
    
    self.intelligence = random.randint(0, 10)
    # Affects chance to make contradictory statements

    self.roleRevealedToPlayer = False

  def dial_change_memory(self, speaker, target, change):
    mem = self.memory[speaker]
    trust = mem.get(0) + mem.get(2) + mem.get(3) - mem.get(1) * 2
    trust += self.gullible * 2

    if trust >= 90:
      self.manual_change_memory(target, change)
      return 0
    elif max(abs(change[0]), abs(change[1]), abs(change[2]), abs(change[3])) >= (100 - 1 * self.deduction):
      self.manual_change_memory(speaker, (-20, 20, -20, -20))
      return 3
    elif random.randint(0, 100) <= trust:
      self.manual_change_memory(target, (x // 2 for x in change))
      return 1
    else:
      return 2

    
  def dial_set_memory(self, speaker, target, change):
    mem = self.memory[target]
    return self.dial_change_memory(speaker, target, (change[0] - mem.get(0), change[1] - mem.get(1), change[2] - mem.get(2), change[3] - mem.get(3)))
    
  def manual_change_memory(self, target, change):
    self.memory[target].change(*change)

  def manual_set_memory(self, target, new):
    self.memory[target].set(*new)
    

class MafiaMemory:
  def __init__(self):
    self.chanceOfNormal = 60
    self.chanceOfMafia = 20
    self.chanceOfDoctor = 10
    self.chanceOfInspector = 10

  def set(self, m0, m1, m2, m3):
    if m0 != None:
      self.chanceOfNormal = m0
    if m1 != None:
      self.chanceOfMafia = m1
    if m2 != None:
      self.chanceOfDoctor = m2
    if m3 != None:
      self.chanceOfInspector = m3

  def change(self, m0, m1, m2, m3):
    self.chanceOfNormal += m0
    self.chanceOfMafia += m1
    self.chanceOfDoctor += m2
    self.chanceOfInspector += m3

  def calc_change(self, m0, m1, m2, m3):
    return abs(m0) + abs(m1)

  def get(self, role):
    if role == 0:
      return self.chanceOfNormal
    elif role == 1:
      return self.chanceOfMafia
    elif role == 2:
      return self.chanceOfDoctor
    elif role == 3:
      return self.chanceOfInspector



#########################
## MAFIA CONVO HELPERS ##
#########################


def getMafia(players):
  res = []
  for p in players:
    if p.role == 1:
      res.append(p)
  return res

def getDoctor(players):
  for p in players:
    if p.role == 2:
      return p
  raise ContentError()

def getInspector(players):
  for p in players:
    if p.role == 3:
      return p
  raise ContentError()
  
def getAlivePlayers(players, excludePlayer = False):
  res = []
  for p in players:
    if p.alive and (not excludePlayer or not p.isPlayer):
      res.append(p)
  return res

def getPlayerFromName(name, players):
  for p in players:
    if p.name == name:
      return p
  raise ContentError()
  
def addUncertainty(dialog, amountOfUncertainties):
  if len(dialog) < 10:
    return dialog
  if amountOfUncertainties * 8 > len(dialog):
    amountOfUncertainties = len(dialog) // 8
    
  stutters = int((4/7) * amountOfUncertainties)
  fillers = int((3/7) * amountOfUncertainties)

  while stutters + fillers < amountOfUncertainties:
    fillers += 1

  words = dialog.split()
  stuttered_words = []
  weightage = [20] * len(words)

  for _ in range(stutters):
    index = random.choices(range(len(words)), weights=weightage)[0]
    word = words[index]
    stutter_count = word.count('-')

    if stutter_count >= 2:
        weightage[index] = 0
    elif stutter_count == 1:
        weightage[index] = 5
    else:
        weightage[index] = 1

    first_letter = word[0]
    stuttered_word = f"{first_letter}-{word}"
    words[index] = stuttered_word
    stuttered_words.append(stuttered_word)

  filler_words = ["- um-", "- uh-", "..."] # <---- akeeesh
  for _ in range(fillers):
    loc = random.randint(1, len(words) - 1)
    words[loc-1] = words[loc-1]
    words = words[:loc] + [random.choice(filler_words)] + words[loc:]

  return " ".join(words)


def mafiaDial(player, text, lying = False):
  if lying:
    dial(player.name, addUncertainty(text, player.socialAnxiety + player.lying))
  else:
    dial(player.name, addUncertainty(text, player.socialAnxiety))

#######################
## MAFIA GUI HELPERS ##
#######################


def printListOfPlayers(players):
  printC("=== Players ===", "B")
  for p in players:
    name = p.name
    color = "B"
    if p.isPlayer:
      name += " (You)"
    if p.roleRevealedToPlayer:
      if p.role == 0:
        name += " (Normal)"
      elif p.role == 1:
        name += " (Trim Tool)"
        color = "R"
      elif p.role == 2:
        name += " (Constraint Tool)"
        color = "G"
      elif p.role == 3:
        name += " (Inspect Tool)"
        color = "Y"
    if not p.alive:
      name += " (Deleted)"
      color = "DG"
    printC(name, color)



############################
## MAFIA CONVOS (CONTENT) ##
############################

goofyConvos = [
  (4, '''\
0-What's your favorite OnSpace sketch plane tool?
1-Mine's the Circle tool.
2-No, the Linear Pattern tool is objectively the best!
3-My favorite tool is the Trim tool.
2-O_o
3-... I didn't mean it like that...'''),
  (4,'''\
0-Once this sketch plane is resolved, where do you think we'll go?
1-We're probably going to be extruded or revolved.
2-Does that mean I'm finally going to become three dimensional?
3-Not you, you don't count.
2-TwT'''),
  (2,'''\
0-Hey, does anyone want to play Rock Paper Scissors with me?
1-We can't talk simultaneously, we can only talk in succession.
0-Oh, right.'''),
  (4,'''\
0-Hang on, this is literally just glorified Among Us.
1-Good job! You're a genius!!!
2-I would have never known that!!!
3-My mind is blown!!!
0-Okay guys I get it.'''),
]

def goofyMafiaConvo(players):
  availableConvos = []
  for c in goofyConvos:
    if c[0] <= len(players):
      availableConvos.append(c)

  for i in range(random.randint(3, 5)):
    if len(availableConvos) == 0:
      break
    chosen = random.choice(availableConvos)
    availableConvos.remove(chosen)
    
    involved = []
    while len(involved) < chosen[0]:
      p = random.choice(players)
      if p not in involved:
        involved.append(p)
        
  
    for line in chosen[1].split("\n"):
      line = line.split("-")
      mafiaDial(involved[int(line[0])], line[1])

    dialNoSpeaker("...")
      

def inspectorFoundMafiaConvo(initiator, target, realInspector, realMafia, alivePlayers):
  if initiator.name == realInspector.name:
    mafiaDial(initiator, "I was investigating {} last night, and I learned that they had the |R|Trim Tool|B|!".format(target.name))
    mafiaDial(target, random.choice(("O_o", "What-", "?????", "Wait-")))
    mafiaDial(target, "... I knew it! You're actually the one with the |R|Trim Tool|B|!", True)
    mafiaDial(target, "You thought you could try to sabotage me in order to make yourself look innocent!", True)
    mafiaDial(target, "Well, even if I get voted out, the others will know you're a liar soon enough!", True)
    mafiaDial(initiator, "...")
    mafiaDial(initiator, "Come on guys, you've got to trust me! They're obviously lying!")
    randomSample = []
    for p in alivePlayers:
      if p not in [initiator, target] + realMafia:
        p.dial_change_memory(initiator.name, initiator.name, (0, 0, 0, 80))
        res = p.dial_change_memory(initiator.name, target.name, (0, 80, 0, 0))
        if len(randomSample) == 0 and not p.isPlayer:
          randomSample.append((p, res))
        elif len(randomSample) < 3 and random.randint(1, 2) == 1 and not p.isPlayer:
          randomSample.append((p, res))
      elif p in realMafia:
        p.manual_set_memory(initiator.name, (0, 0, 0, 100))
        
    for i in randomSample:
      if i[1] == 0:
        mafiaDial(i[0], "I'm agreeing with {}, {} seems pretty sus.".format(initiator.name, target.name))
      elif i[1] == 1:
        mafiaDial(i[0], "I'm pretty sure {} is telling the truth right now.".format(initiator.name))
      elif i[1] == 2:
        mafiaDial(i[0], "I dunno, {} seems pretty innocent to me...".format(target.name))
      elif i[1] == 3:
        mafiaDial(i[0], "{} is definitely lying, I'm sure of it! {} is innocent!".format(target.name, initiator.name))
  else:
    mafiaDial(initiator, "I was investigating {} last night, and I learned that they had the |R|Trim Tool|B|!".format(target.name), True)
    mafiaDial(target, random.choice(("O_o", "What-", "?????", "Wait-")))
    mafiaDial(target, "... I knew it! You're actually the one with the |R|Trim Tool|B|!")
    mafiaDial(target, "You thought you could try to sabotage me in order to make yourself look innocent!")
    mafiaDial(target, "Well, even if I get voted out, the others will know you're a liar soon enough!")
    mafiaDial(initiator, "...")
    mafiaDial(initiator, "Come on guys, you've got to trust me! They're obviously lying!", True)

    choice = 2
    if realInspector.isPlayer:
      choice = dropdownMenu("You're the Real Inspector. Object?", ["|G|Yes", "|R|No"])
      if choice == 1:
        mafiaDial(realInspector, "Hey, I'm the real inspector! {} is definitely lying!".format(initiator.name))
        mafiaDial(initiator, "...")
        mafiaDial(initiator, "You're the other person with the |R|Trim Tool|B|, aren't you?", True)
        mafiaDial(initiator, "Both of you are lying, I knew it!", True)
      
    randomSample = []
    for p in alivePlayers:
      if p not in [initiator, target] + realMafia:
        res = 0
        if choice == 1:
          p.dial_change_memory(realInspector.name, realInspector.name, (0, 0, 0, 40))
          p.dial_change_memory(initiator.name, initiator.name, (0, 0, 0, 40))
          res = p.dial_change_memory(initiator.name, target.name, (0, 40, 0, 0))
        else:
          p.dial_change_memory(initiator.name, initiator.name, (0, 0, 0, 80))
          res = p.dial_change_memory(initiator.name, target.name, (0, 80, 0, 0))
        if len(randomSample) == 0 and not p.isPlayer:
          randomSample.append((p, res))
        elif len(randomSample) < 3 and random.randint(1, 2) == 1 and not p.isPlayer:
          randomSample.append((p, res))
      elif p == target:
        p.manual_set_memory(initiator.name, (0, 100, 0, 0))
        if choice == 1:
          p.manual_set_memory(realInspector.name, (0, 0, 0, 100))
      elif p in realMafia:
        if choice == 1:
          p.manual_set_memory(realInspector.name, (0, 0, 0, 100))
    for i in randomSample:
      if i[1] == 0:
        mafiaDial(i[0], "I'm agreeing with {}, {} seems pretty sus.".format(initiator.name, target.name))
      elif i[1] == 1:
        mafiaDial(i[0], "I'm pretty sure {} is telling the truth right now.".format(initiator.name))
      elif i[1] == 2:
        mafiaDial(i[0], "I dunno, {} seems pretty innocent to me...".format(target.name))
      elif i[1] == 3:
        mafiaDial(i[0], "{} is definitely lying, I'm sure of it! {} is innocent!".format(target.name, initiator.name))

    
        

def doctorFoundInnocentConvo(initiator, target, realDoctor, others):
  if initiator == realDoctor:
    mafiaDial(initiator, "I protected {} last night, and nobody died, so that means they must be innocent!".format(target.name))
    mafiaDial(target, random.choice(("^-^", "Thanks man!", "Wow, thanks!")))

    mafia = getMafia(getAlivePlayers(others, False))
    
    if random.randint(1, 2) == 1 and len(mafia) != 1:
      m = mafia[0]
      if m.isPlayer:
        m = mafia[1]

      mafiaDial(m, "Hey, wait... I'M the one with the |G|Constraint Tool|B|!", True)
      mafiaDial(initiator, random.choice("What-", "????", "How the-"))
      mafiaDial(m, "You're actually the one with the |R|Trim Tool|B|, aren't you?", True)
      mafiaDial(m, "You're just pretending to have it to save both you and your partner!", True)
      mafiaDial(initiator, "...")
      mafiaDial(initiator, "Come on guys, you've got to trust me! {} is obviously lying!".format(m.name))
      mafiaDial(initiator, "I have the |G|Constraint Tool|B|, so {} must have the |R|Trim Tool|B|!".format(m.name))
      randomSample = []
      for p in alivePlayers:
        if p not in [initiator, target] + mafia:
          p.dial_change_memory(initiator.name, initiator.name, (0, 0, 80, 0))
          p.dial_change_memory(initiator.name, m.name, (0, 80, 0, 0))
          res = p.dial_change_memory(initiator.name, target.name, (20, -60, 10, 10))
          if len(randomSample) == 0 and not p.isPlayer:
            randomSample.append((p, res))
          elif len(randomSample) < 3 and random.randint(1, 2) == 1 and not p.isPlayer:
            randomSample.append((p, res))
        elif p in realMafia:
          p.manual_set_memory(initiator.name, (0, 0, 100, 0))
        elif p in [initiator, target]:
          if p == target:
            p.manual_set_memory(initiator.name, (0, 0, 100, 0))
          p.manual_set_memory(m.name, (0, 100, 0, 0))
          
      for i in randomSample:
        if i[1] == 0:
          mafiaDial(i[0], "I'm agreeing with {}, {} seems pretty sus.".format(initiator.name, m.name))
        elif i[1] == 1:
          mafiaDial(i[0], "I'm pretty sure {} is telling the truth right now.".format(initiator.name))
        elif i[1] == 2:
          mafiaDial(i[0], "I dunno, {} seems like they have the |G|Constraint Tool|B| to me...".format(m.name))
        elif i[1] == 3:
          mafiaDial(i[0], "{} is definitely lying, I'm sure of it! {} is innocent!".format(initiator.name, m.name))
    else:
      for p in alivePlayers:
        if p not in [initiator, target] + mafia:
          p.dial_change_memory(initiator.name, initiator.name, (0, 0, 80, 0))
          res = p.dial_change_memory(initiator.name, target.name, (20, -60, 0, 15))
        elif p in realMafia:
          p.manual_set_memory(initiator.name, (0, 0, 100, 0))
        elif p == target:
          p.manual_set_memory(initiator.name, (0, 0, 100, 0))
  else:
    mafiaDial(initiator, "I protected {} last night, and nobody died, so that means they must be innocent!".format(target.name), True)
    mafiaDial(target, random.choice(("^-^", "Thanks man!", "Wow, thanks!")))

    choice = 1
    if realDoctor.isPlayer:
      choice = dropdownMenu("You're the person who has the |G|Constraint Tool|B|. Object?", ["|G|Yes", "|R|No"])
    
    if choice == 1:
      mafiaDial(realDoctor, "Hey, wait... I'M the one with the |G|Constraint Tool|B|!")
      mafiaDial(initiator, random.choice("What-", "????", "How the-"))
      mafiaDial(realDoctor, "You're actually the one with the |R|Trim Tool|B|, aren't you?")
      mafiaDial(realDoctor, "You're just pretending to have it to save both you and your partner!")
      mafiaDial(initiator, "...")
      mafiaDial(initiator, "Come on guys, you've got to trust me! {} is obviously lying!".format(realDoctor.name), True)
      mafiaDial(initiator, "I have the |G|Constraint Tool|B|, so {} must have the |R|Trim Tool|B|!".format(realDoctor.name), True)

      
      randomSample = []
      for p in alivePlayers:
        if p not in [initiator, target, realDoctor]:
          p.dial_change_memory(initiator.name, initiator.name, (0, 0, 80, 0))
          p.dial_change_memory(initiator.name, realDoctor.name, (0, 80, 0, 0))
          res = p.dial_change_memory(initiator.name, target.name, (20, -60, 0, 15))
          if len(randomSample) == 0 and not p.isPlayer:
            randomSample.append((p, res))
          elif len(randomSample) < 3 and random.randint(1, 2) == 1 and not p.isPlayer:
            randomSample.append((p, res))
        elif p == realDoctor:
          p.manual_set_memory(initiator.name, (0, 100, 0, 0))
          p.manual_set_memory(target.name, (0, 50, 0, 0))
        elif p == initiator or p == target and p.role == 1:
          p.manual_set_memory(realDoctor.name, (0, 0, 100, 0))
        else:
          p.manual_set_memory(realDoctor.name, (0, 40, 40, 0))
          p.manual_set_memory(initiator.name, (0, 40, 40, 0))
          
      for i in randomSample:
        if i[1] == 0:
          mafiaDial(i[0], "I'm agreeing with {}, {} seems pretty sus.".format(initiator.name, realDoctor.name))
        elif i[1] == 1:
          mafiaDial(i[0], "I'm pretty sure {} is telling the truth right now.".format(initiator.name))
        elif i[1] == 2:
          mafiaDial(i[0], "I dunno, {} seems like they have the |G|Constraint Tool|B| to me...".format(realDoctor.name))
        elif i[1] == 3:
          mafiaDial(i[0], "{} is definitely lying, I'm sure of it! {} is innocent!".format(initiator.name, realDoctor.name))

#####################
## THE GAME WOOHOO ##
#####################

def runMafiaGame(player_name):
  clear()
  
  players = [MafiaPlayer(player_name, 0)]
  players[0].isPlayer = True
  
  # Add Players
  for i in range(9):
    nameToAdd = random.choice(POSSIBLE_NAMES)
    while nameToAdd.lower() == player_name.lower():
      nameToAdd = random.choice(POSSIBLE_NAMES)
    POSSIBLE_NAMES.remove(nameToAdd)
    players.append(MafiaPlayer(nameToAdd, 0))
  
  # Select Mafia
  for i in range(2):
    mafiaPlayer = random.choice(players)
    while mafiaPlayer.role == 1:
      mafiaPlayer = random.choice(players)
    mafiaPlayer.role = 1
  
  # Select Doctor
  doctorPlayer = random.choice(players)
  while doctorPlayer.role == 1:
    doctorPlayer = random.choice(players)
  doctorPlayer.role = 2
  
  # Select Inspector
  inspectorPlayer = random.choice(players)
  while inspectorPlayer.role != 0:
    inspectorPlayer = random.choice(players)
  inspectorPlayer.role = 3

  printBoxedText("OnSpace Mafia - Roles", "R")
  print()
  printListOfPlayers(players)
  print()
  
  enter()
  
  dialNoSpeaker("Each player's role has been assigned.")
  if players[0].role == 0:
    dialNoSpeaker("You are a normal Sketch Element!")
    dialNoSpeaker("Figure out who has the Trim Tools and vote them out to win the game!")
  elif players[0].role == 1:
    dialNoSpeaker("You possess the |R|Trim Tool|B|!")
    dialNoSpeaker("Each night, you and your partner can choose one Sketch Element to delete.")
    dialNoSpeaker("Eliminate the other Sketch Elements to win the game!")
    dialNoSpeaker("Your partner in crime is {}.".format(getMafia(players)[1].name))
    getMafia(players)[1].roleRevealedToPlayer = True
  elif players[0].role == 2:
    dialNoSpeaker("You possess the |G|Constraint Tool|B|!")
    dialNoSpeaker("Each night, you can choose one Sketch Element to protect.")
    dialNoSpeaker("Work together with the other Sketch Elements to eliminate the Trim Tools!")
  elif players[0].role == 3:
    dialNoSpeaker("You possess the |Y|Inspect Tool|B|!")
    dialNoSpeaker("Each night, you can choose one Sketch Element to investigate, and you will find their role.")
    dialNoSpeaker("Work together with the other Sketch Elements to eliminate the Trim Tools!")
  players[0].roleRevealedToPlayer = True
  
  enter()

  # Initial Memory Initialization
  for p in players:
    for p2 in players:
      if p.name == p2.name:
        continue
      p.memory[p2.name] = MafiaMemory()

  # The Mafia knows for certain who the other Mafia is
  mafia = getMafia(players)

  mafia[0].manual_set_memory(mafia[1].name, (0, 100, 0, 0))
  mafia[1].manual_set_memory(mafia[0].name, (0, 100, 0, 0))
  
  # The Doctor knows that Nobody Else is a Doctor
  doctor = getDoctor(players)
  
  for p in players:
    if p == doctor:
      continue
      
    doctor.manual_set_memory(p.name, (60, 20, 0, 20))
    
  # The Inspector knows that Nobody Else is an Inspector
  inspector = getInspector(players)
  for p in players:
    if p == inspector:
      continue
      
    inspector.manual_set_memory(p.name, (60, 20, 20, 0))


  turn = 1
  while True:
    eliminatedPlayer = None
    protectedPlayer = None

    if len(getMafia(getAlivePlayers(players, False))) == 0 or len(getMafia(getAlivePlayers(players, False))) * 2 >= len(getAlivePlayers(players, False)):
      clear()
      printBoxedText("OnSpace Mafia - Game Over", "R")
      print()
      for p in players[1:]:
        p.roleRevealedToPlayer = True
        
      printListOfPlayers(players)
      print()
    else:
      clear()
      printBoxedText("OnSpace Mafia - Night {}".format(turn), "R")
      print()
      printListOfPlayers(players)
      print()

    if len(getMafia(getAlivePlayers(players, False))) == 0:
      dial("The Sketchmaster", "All of the sketch elements with the |R|Trim Tools|B| were eliminated!")
      if players[0].role == 1:
        dial("The Sketchmaster", "Better luck next time, {}!".format(players[0].name))
        return False
      else:
        dial("The Sketchmaster", "Congratulations on winning, {}!".format(players[0].name))
        return True
    elif len(getMafia(getAlivePlayers(players, False))) * 2 >= len(getAlivePlayers(players, False)):
      dial("The Sketchmaster", "The sketch elements with the |R|Trim Tools|B| outnumber the other sketch elements!")
      if players[0].role == 1:
        dial("The Sketchmaster", "Congratulations on winning, {}!".format(players[0].name))
        return True
      else:
        dial("The Sketchmaster", "Better luck next time, {}!".format(players[0].name))
        return False

    
    dial("The Sketchmaster", "Players with the |R|Trim Tool|B|, awaken.")
    dial("The Sketchmaster", "Which sketch element will you delete tonight?")

    if players[0].role == 1 and players[0].alive:
      bestCandidates = []
      bestCandidateScore = -1

      alivePlayers = getAlivePlayers(players, True)
      mafia = getMafia(alivePlayers)
      for m in mafia:
        if m in alivePlayers:
          alivePlayers.remove(m)

      choice = dropdownMenu(None, [p.name for p in alivePlayers])
      playerChosenBestCandidate = alivePlayers[choice-1]

      for p in alivePlayers:
        if p in mafia:
          continue
        score = 0
        for m in mafia:
          score += m.memory[p.name].get(2) + m.memory[p.name].get(3) * 2
        
        if playerChosenBestCandidate == p:
          score += 300
          
        if score > bestCandidateScore:
          bestCandidates = [p]
          bestCandidateScore = score
        elif score == bestCandidateScore:
          bestCandidates.append(p)
      
      eliminatedPlayer = random.choice(bestCandidates)  
      if playerChosenBestCandidate != eliminatedPlayer:
        dialNoSpeaker("Unfortunately, your partner disagrees and chooses to delete {} instead.".format(eliminatedPlayer.name), "R")
        
    else:
      bestCandidates = []
      bestCandidateScore = -1

      alivePlayers = getAlivePlayers(players, False)
      mafia = getMafia(alivePlayers)

      for p in alivePlayers:
        if p in mafia:
          continue
        score = 0
        for m in mafia:
          score += m.memory[p.name].get(2) + m.memory[p.name].get(3) * 2
          
        if score > bestCandidateScore:
          bestCandidates = [p]
          bestCandidateScore = score
        elif score == bestCandidateScore:
          bestCandidates.append(p)

      eliminatedPlayer = random.choice(bestCandidates)
      while turn == 1 and eliminatedPlayer.isPlayer:
        eliminatedPlayer = random.choice(bestCandidates)
  
      dialNoSpeaker("...")


    dial("The Sketchmaster", "A sketch element has been set for deletion.")

    if getDoctor(players).alive:
      dial("The Sketchmaster", "Player with the |G|Constraint Tool|B|, awaken.")
      dial("The Sketchmaster", "Which sketch element will you protect tonight?")
      if players[0].role == 2:
        choice = dropdownMenu(None, [p.name for p in getAlivePlayers(players, True)])
        protectedPlayer = getAlivePlayers(players, True)[choice-1]
      else:
        bestCandidates = []
        bestCandidateScore = -1

        alivePlayers = getAlivePlayers(players, False)
        d = getDoctor(players)
        
        for p in alivePlayers:
          if p == d:
            continue
          score = d.memory[p.name].get(0) + d.memory[p.name].get(3) * 3
          if score > bestCandidateScore:
            bestCandidates = [p]
            bestCandidateScore = score
          elif score == bestCandidateScore:
            bestCandidates.append(p)
  
        protectedPlayer = random.choice(bestCandidates)        
        dialNoSpeaker("...")
      

      dial("The Sketchmaster", "A sketch element has been protected tonight.")

    if getInspector(players).alive:
      dial("The Sketchmaster", "Player with the |Y|Inspect Tool|B|, awaken.")
      dial("The Sketchmaster", "Which sketch element will you investigate tonight?")
      if players[0].role == 3:
        choice = dropdownMenu(None, [p.name for p in getAlivePlayers(players, True)])
        inspectedPlayer = getAlivePlayers(players, True)[choice-1]
        inspectedPlayer.roleRevealedToPlayer = True
      else:
        bestCandidates = []
        bestCandidateScore = -1

        alivePlayers = getAlivePlayers(players, False)
        i = getInspector(players)
        
        for p in alivePlayers:
          if i == p:
            continue
            
          score = i.memory[p.name].get(1)
          if score == 100:
            continue
            
          if score > bestCandidateScore:
            bestCandidates = [p]
            bestCandidateScore = score
          elif score == bestCandidateScore:
            bestCandidates.append(p)
  
        inspectedPlayer = random.choice(bestCandidates)

        if inspectedPlayer.role == 0:
          i.manual_set_memory(inspectedPlayer.name, (100, 0, 0, 0))
        elif inspectedPlayer.role == 1:
          i.manual_set_memory(inspectedPlayer.name, (0, 100, 0, 0))
        elif inspectedPlayer.role == 2:
          i.manual_set_memory(inspectedPlayer.name, (0, 0, 100, 0))
        elif inspectedPlayer.role == 3:
          i.manual_set_memory(inspectedPlayer.name, (0, 0, 0, 100))
          
        dialNoSpeaker("...")

      
      dial("The Sketchmaster", "The investigations have been carried out.")

      
    clear()
    printBoxedText("OnSpace Mafia - Day {}".format(turn), "R")

    if eliminatedPlayer != protectedPlayer:
      eliminatedPlayer.alive = False
      eliminatedPlayer.roleRevealedToPlayer = True

    print()
    printListOfPlayers(players)

    # Quick Player Vars
    doctor = getDoctor(players)
    protected = protectedPlayer
    inspector = getInspector(players)
    mafia = getMafia(players)
    mafia1 = mafia[0]
    mafia2 = mafia[1]

    alivePlayers = getAlivePlayers(players)
    alivePlayersExceptPlayer = getAlivePlayers(players, True)
    aliveNormalPlayers = alivePlayersExceptPlayer.copy()
    try:
      aliveNormalPlayers.remove(mafia1)
    except:
      pass
    try:
      aliveNormalPlayers.remove(mafia2)
    except:
      pass
    
    dial("The Sketchmaster", "The night has passed.")
    if eliminatedPlayer == protectedPlayer:
      dial("The Sketchmaster", "Luckily, no sketch elements were deleted last night!")
      doctor.manual_set_memory(protected.name, (None, 0, None, None))
    else:
      dial("The Sketchmaster", "Unfortunately, {} was deleted by the |R|Trim Tools|B| last night.".format(eliminatedPlayer.name))

    dial("The Sketchmaster", "You may now discuss amongst yourselves until you decide to vote a sketch element out.")

    specialConvoOccurred = False
    
    # Logic: Inspector Found Mafia
    
    if inspector.alive and not inspector.isPlayer:
      for i_item in inspector.memory.items():
        if i_item[1].get(1) == 100 and i_item[0] in (p.name for p in alivePlayers):
          specialConvoOccurred = True
          inspectorFoundMafiaConvo(inspector, getPlayerFromName(i_item[0], players), inspector, mafia, alivePlayers)     
          
    elif inspector.isPlayer and inspector.alive:
      choice = dropdownMenu("Share your investigation with the others?", ["|R|No", "|G|Yes"])
      if choice == 2:
        while True:
          choice = dropdownMenu("Choose an investigation result to share:", [p.name for p in alivePlayersExceptPlayer])
          revealedPlayer = alivePlayersExceptPlayer[choice-1]
          if revealedPlayer.roleRevealedToPlayer:
            if revealedPlayer.role in [0, 2, 3]:
              specialConvoOccurred = True
              pass
            elif revealedPlayer.role == 1:
              specialConvoOccurred = True
              inspectorFoundMafiaConvo(inspector, revealedPlayer, inspector, mafia, alivePlayers)
          else:
            dialNoSpeaker("|R|You have not investigated this person yet!")
          choice = dropdownMenu("Share any other investigations?", ["|G|Yes", "|R|No"])
          if choice == 2:
            break
    
              
    
    # Logic: Doctor Saved & Confirmed Innocent
    if eliminatedPlayer == protected:
      if doctor.isPlayer:
        dialNoSpeaker("A person was saved from the Trim Tools thanks to your constraints, confirming their innocence.")
        choice = dropdownMenu("Share these findings with the others?", ["|R|No", "|G|Yes"])
        if choice == 2:
          specialConvoOccurred = True
          doctorFoundInnocentConvo(doctor, protected, doctor, alivePlayers)
      else:
        if len(alivePlayers) <= 6 and len(mafia) == 2 or len(alivePlayers) <= 4 and len(mafia) == 1:
          specialConvoOccurred = True
          doctorFoundInnocentConvo(doctor, protected, doctor, alivePlayers)

    
        
    # Logic: Goofy Mafia Strats
    if not specialConvoOccurred:
      if players[0].isPlayer:
        if eliminatedPlayer == protected:
          choice = dropdownMenu("The person with the |G|Constraint Tool|B| didn't say anything. Would you like to pretend to be them?", ["|R|No", "|G|Yes"])
          if choice == 2:
            specialConvoOccurred = True
            candidates = alivePlayers.copy()
            for p in alivePlayers:
              if p.role == 1:
                try:
                  candidates.remove(p)
                except:
                  pass
            choice = dropdownMenu("Who will you pretend to have protected?", [c.name for c in candidates])
            doctorFoundInnocentConvo(players[0], candidates[choice-1], doctor, alivePlayers)
        if inspector.alive and not specialConvoOccurred:
          choice = dropdownMenu("The |Y|Inspector|B| didn't say anything. Would you like to pretend to be them?", ["|R|No", "|G|Yes"])
          if choice == 2:
            specialConvoOccurred = True
            candidates = alivePlayers.copy()
            for p in alivePlayers:
              if p.role == 1:
                try:
                  candidates.remove(p)
                except:
                  pass
            choice = dropdownMenu("Who will you pretend to have inspected?", [c.name for c in candidates])
            inspectorFoundMafiaConvo(players[0], candidates[choice-1], inspector, mafia, alivePlayers)
      elif len(mafia) == 2:
        if eliminatedPlayer == protected:
          if random.randint(1, 3) == 1:
            specialConvoOccurred = True
            doctorFoundInnocentConvo(mafia[0], mafia[1], doctor, alivePlayers)
          else:
            target = random.choice(alivePlayers)
            while target.role in [1, 2]:
              target = random.choice(alivePlayers)
            specialConvoOccurred = True
            doctorFoundInnocentConvo(mafia[0], target, doctor, alivePlayers)
        elif inspector.alive:
          target = random.choice(alivePlayers)
          while target.role in [1, 3]:
            target = random.choice(alivePlayers)
          specialConvoOccurred = True
          inspectorFoundMafiaConvo(mafia[1], target, inspector, mafia, alivePlayers)

    # Logic: Normal Conversations
    dialNoSpeaker("...")
    goofyMafiaConvo(alivePlayersExceptPlayer)
    dialNoSpeaker("...")
    
    dial("The Sketchmaker", "The voting is beginning! Who do you think has the |R|Trim Tool|B|?")

    sussiestCandidates = []
    sussiestScore = 0

    playerVotedPlayer = None

    if players[0].alive:
      choice = dropdownMenu("Who will you vote out?", [p.name for p in getAlivePlayers(players, True)])
      playerVotedPlayer = getAlivePlayers(players, True)[choice-1]

    for p in getAlivePlayers(players, False):
      score = 0
      for p2 in getAlivePlayers(players, False):
        if p == p2 or p2.isPlayer:
          continue
        if p2.role == 1:
          score += p2.memory[p.name].chanceOfInspector * 3 + p2.memory[p.name].chanceOfDoctor
        else:
          score += p2.memory[p.name].chanceOfMafia * 4
      
      if p == playerVotedPlayer:
        score += 400
        
      if score > sussiestScore:
        sussiestScore = score
        sussiestCandidates = [p]
      elif score == sussiestScore:
        sussiestCandidates.append(p)

    exiledPlayer = random.choice(sussiestCandidates)
    dial("The Sketchmaster", "...")
    dial("The Sketchmaster", "A decision has been made.")
    dial("The Sketchmaster", "By popular vote, {} will be deleted from the sketch plane this turn.".format(exiledPlayer.name))
    exiledPlayer.alive = False
    exiledPlayer.roleRevealedToPlayer = True

    clear()
    printBoxedText("OnSpace Mafia - Day {} Voting Results".format(turn), "R")
    print()
    printListOfPlayers(players)
    
    dial("The Sketchmaster", "...")
    dial("The Sketchmaster", "Night is about to fall.")
    
    turn += 1
    