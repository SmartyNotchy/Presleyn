from imports import *

class MapPlayer: # THIS IS THE OVERWORLD PLAYER NOT THE BATTLE PLAYER ok myan
  def __init__(self):
    self.name = "Unnamed Player"
    self.nameColor = "B"

    self.loc = None
    self.classroom = None
    
    self.tickets = 0
    
    self.wands = []
    self.selectedWand = None
    self.spells = []
    self.arsenal = []
    self.items = []

    self.act = 1
    
    self.quests = []
    self.emails = []

    self.flags = []
    self.deaths = 0
    self.missedBuses = 0
    
    self.day = 1 # Starts at Day 1, increments by 1 for each completed school day
    self.time = 0 # Number of minutes past 8:00 AM
    self.inSchool = True
    self.justPerished = False
    
  def perish(self):
    self.deaths += 1
    self.justPerished = True
    self.classroom = NursesOfficeClassroom()
    self.loc = ["MAIN_ENTRANCE", "ENTRANCE_HALLWAY_6"]
    
  def getName(self):
    return "|" + self.nameColor + "|" + self.name + "|--|"

  def addFlag(self, flag): # Modifier
    self.flags.append(flag)

  def hasFlag(self, flag): # Checker
    return flag in self.flags

  def removeFlag(self, flag): # Modifier
    assert self.hasFlag(flag)
    self.flags.remove(flag)
    
  def giveTickets(self, amount): # Modifier
    self.tickets += amount

  def hasEnoughTickets(self, amount): # Checker
    return self.tickets >= amount

  def takeTickets(self, amount): # Modifier
    if self.hasEnoughTickets(amount): 
      self.tickets -= amount
    else:
      return False
    return True
     
  def timePast(self, time): # Checker
    return self.time >= time

  def timeBefore(self, time): # Checker
    return self.time <= time

  def timeBetween(self, lower, upper): # Checker
    return self.timePast(lower) and self.timeBefore(upper)
    
  def incrementTime(self, amount): # Modifier
    self.time += amount
    
  def giveWand(self, wand): # Modifier
    self.wands.append(wand())
    
  def hasWand(self, wand): # Checker
    wand = wand()
    for w in self.wands:
      if w.name == wand.name:
        return True
    return False

  def giveSpell(self, spell): # Modifier
    self.spells.append(spell())

  def hasSpell(self, spell): # Checker
    spell = spell()
    for s in self.spells:
      if s.name == spell.name:
        return True
    return False

  def getItem(self, item): # Getter
    item = item()
    for i in self.items:
      if i.name == item.name:
        return i
    return None

  def giveItem(self, item): # Modifier
    i = self.getItem(item)
    if i == None:
      self.items.append(item())
    else:
      self.getItem(item).quantity += 1
    
  def hasItem(self, item): # Checker
    return self.getItem(item) != None

  def removeItem(self, item): # Modifier
    i = self.getItem(item) 
    assert i != None
    i.quantity -= 1
    if i.quantity == 0:
      self.items.remove(i)
      

  def sendEmail(self, email): # Modifier
    self.emails.append(email(False, True))

  def hasReceivedEmail(self, email): # Checker
    email = email(False, True)
    for e in self.emails:
      if e.name == email.name:
        return True
    return False

  def startQuest(self, quest): # Modifier
    self.quests.append(quest(0, False))

    printFlair("Quest Started: " + self.quests[-1].name)

  def getQuest(self, quest):
    quest = quest(0, False)
    for q in self.quests:
      if q.name == quest.name:
        return q
    return None
    
  def startedQuest(self, quest): # Checker
    return self.getQuest(quest) != None
    
  def completedQuest(self, quest): # Checker
    q = self.getQuest(quest)
    if q == None:
      return False
    return q.isComplete()

  def incrementQuestProgress(self, quest): # Modifier
    rewards_subtask = {3: 100, 2: 75, 1: 50, 0: 25}
    rewards_completion = {3: 1000, 2: 300, 1: 150, 0: 75}
    
    q = self.getQuest(quest)
    assert q != None
    assert not q.isComplete()

    reward = rewards_subtask[q.priority]
    subtask = q.subtasks[q.stage]
    printFlair("Objective Complete: " + subtask + " (+{} Tickets)".format(reward))
    q.stage += 1
    if q.isComplete():
      reward += rewards_completion[q.priority]
      printFlair("Quest Complete: " + q.name + " (+{} Tickets)".format(rewards_completion[q.priority]))
    else:
      printC("\n|W|New Objective:|B| " + q.subtasks[q.stage] + "\n")
      enter()

    self.giveTickets(reward)

  def getQuestProgress(self, quest): # Getter
    q = self.getQuest(quest)
    if q == None:
      return -1
    return q.stage
    
  def questProgressIsAt(self, quest, progress): # Checker
    return self.getQuestProgress(quest) == progress
    
  def questProgressIsAtLeast(self, quest, progress): # Checker
    return self.getQuestProgress(quest) >= progress

  def printControls(self, reprint):
    totalMinutes = int(self.time)
    hour = 8 + totalMinutes // 60
    minutes = totalMinutes % 60
    timemode = "AM"
    if hour >= 12:
      timemode = "PM"
      if hour > 12:
        hour -= 12
    hour = str(hour)
    if len(hour) == 1:
      hour = "0" + hour
    minutes = str(minutes)
    if len(minutes) == 1:
      minutes = "0" + minutes

    if reprint:
      printC("╔══════════════════════════════════════════════╗", "B")
      #printC(str(self.loc) + " " * 10, "B")
      printC("║                   {}:{} {}                   ║".format(hour, minutes, timemode), "B")
      printC("║ [R] View Spellbook & Arsenal                 ║", "B")
      printC("║ [F] Equip Wand                               ║", "B")
      printC("║ [E] Open Item Inventory                      ║", "B")
      printC("║ [C] Open Chromebook                          ║", "B")
      printC("╚══════════════════════════════════════════════╝", "B")
    else:
      printC("\x1b[B", end="")
      #printC(str(self.loc) + " " * 10, "B", end="")
      printC("║                   {}:{} {}                   ║".format(hour, minutes, timemode), "B", end="")
      printC("\x1b[5B")

  def viewSpellbookArsenal(self):
    cursor.hide()
    
    # Quick Spell-Sort
    self.spells = sorted(self.spells, key = lambda s : s.name)

    # Arsenal Printing
    clear()
    print()
    printC('''\
╔════════════════════════  YOUR ARSENAL  ════════════════════════╗
║                                                                ║
║                                                                ║
║                                                                ║
║                                                                ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║                                                                ║
║                                                                ║
║                                                                ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║                                                                ║
║                                                                ║
║                                                                ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║                                                                ║
║                                                                ║
║                                                                ║ 
╚════════════════════════════════════════════════════════════════╝

|G|[ENTER] - Choose Spell for Arsenal          |R|[X] - Exit Menu''', "B")
    printC("\x1b[3;0H")
    for ars_spell in self.arsenal:
      ars_spell.printDesc(2)
      printC("\x1b[1B", end="")

    # Spellbook Printing
    spellNumSelected = 1
    pageNum = 1
    SPELLS_PER_PAGE = 10
    pages = len(self.spells) // SPELLS_PER_PAGE + 1
    if len(self.spells) % SPELLS_PER_PAGE == 0:
      pages -= 1
  
    while True: # btw i reserve the right to rollback this if it explodes
      printC("\x1b[3;70H", end="")
  
      if pageNum == 1:
        printC("|DG|<- ", end="")
      else:
        printC("|W|<- ", end="")
      printC("YOUR SPELLBOOK (PAGE {} of {})".format(pageNum, pages), "B", end="")
      if pageNum == pages:
        printC("|DG| ->")
      else:
        printC("|W| ->")

      spellsInPage = self.spells[(pageNum - 1) * SPELLS_PER_PAGE:pageNum * SPELLS_PER_PAGE]
      idx = 1
      print("\x1b[B", end="")
      for spellInPage in spellsInPage:
        printC("\x1b[70C", end="")
        if idx == spellNumSelected:
          if spellInPage in self.arsenal:
            printC("|PU|> |--|" + spellInPage.getDisabledMenuName() + "\x1b[K")
          else:
            printC("|PU|> |--|" + spellInPage.getMenuName() + "\x1b[K")
        else:
          if spellInPage in self.arsenal:
            printC("  " + spellInPage.getDisabledMenuName() + "\x1b[K")
          else:
            printC("  " + spellInPage.getMenuName() + "\x1b[K")
        idx += 1
      print("\x1b[70C\x1b[K\x1b[B" * (SPELLS_PER_PAGE-idx + 4), end="")
      printC("\x1b[0F\x1b[70CSelected Spell: \x1b[0F\x1b[3B", "B", end="")
      spellsInPage[spellNumSelected-1].printDesc(70, clearLine = True)

      while True:
        cursor.hide()
        choice = getkey()
        if choice in ["\x1b[A", "w"]:
          spellNumSelected -= 1
          if spellNumSelected < 1:
            spellNumSelected = 1
            continue
        elif choice in ["\x1b[B", "s"]:
          spellNumSelected += 1
          if spellNumSelected > len(spellsInPage):
            spellNumSelected -= 1
            continue
        elif choice == ["\x1b[C", "d"]:
          pageNum += 1
          if pageNum > pages:
            pageNum -= 1
            continue
          spellNumSelected = 1
        elif choice == ["\x1b[D", "a"]:
          pageNum -= 1
          if pageNum < 1:
            pageNum += 1
            continue
          spellNumSelected = 1
        elif choice == "x":
          return
        elif choice == "\n":
          allowed = True
          for s in self.arsenal:
            if s.name == spellsInPage[spellNumSelected-1].name:
              print("\x1b[26;80H")
              printC("You have already equipped that spell in your arsenal!", "R")
              allowed = False
              enter()
              deleteLines(2)
              break
          if allowed:
            print("\x1b[25;80H")
            choice = dropdownMenu("Choose an arsenal spell to replace:", [s.getMenuName() for s in self.arsenal] + ["|R|Cancel"])
            if choice != 5:
              self.arsenal[choice-1] = spellsInPage[spellNumSelected-1]
              return self.viewSpellbookArsenal()
            else:
              deleteLines(8)
              cursor.hide()
              continue
          else:
            continue
        else:
          continue
        spellNumSelected = clamp(spellNumSelected, 1, len(spellsInPage))
        pageNum = clamp(pageNum, 1, pages)
        break
  
  def viewSelectedWand(self, viewingWandNum = 1):
    clear()
    cursor.hide()
    self.wands = sorted(self.wands, key = lambda x : x.name)
    
    print()
    printC('''\
╔═══════════════════════════════════════  SELECTED WAND  ═══════════════════════════════════════╗
║                                                                                               ║
║                                                                                               ║
║                                                                                               ║
║                                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════════════════════╝

|G|[ENTER] - Equip Wand                   |R|[X] - Exit Menu


|B|Your Wands:                            Currently Viewing:\n''', "B")

    printC("\x1b[3;1H")
    self.selectedWand.printDesc(offset=2, clearLine=False)
    printC("\x1b[14;1H")
    
    idx = 1
    for wand in self.wands:
      if idx == viewingWandNum:
        printC("|PU|> |--|" + wand.getName())
      else:
        printC("  " + wand.getName())
      idx += 1

    
    wandNumSelected = viewingWandNum
    changed = True
    
    while True:
      cursor.hide()
      
      if changed:
        printC("\x1b[15;1H", end="")
        self.wands[wandNumSelected-1].printDesc(offset=39, clearLine=True)
        changed = False

      choice = getkey()
      if choice in ["\x1b[A", "w"]:
        wandNumSelected -= 1
        if wandNumSelected <= 0:
          wandNumSelected = 1
        else:
          printC("\x1b[{};1H  ".format(15 + wandNumSelected), end="")
          printC("\x1b[{};1H|PU|> ".format(14 + wandNumSelected), end="")
          changed = True
      elif choice in ["\x1b[B", "s"]:
        wandNumSelected += 1
        if wandNumSelected > len(self.wands):
          wandNumSelected = len(self.wands)
        else:
          printC("\x1b[{};1H  ".format(13 + wandNumSelected), end="")
          printC("\x1b[{};1H|PU|> ".format(14 + wandNumSelected), end="")
          changed = True
      elif choice == "\n":
        newWand = self.wands[wandNumSelected - 1]
        if self.selectedWand.name != newWand.name:
          self.selectedWand = newWand
          return self.viewSelectedWand(wandNumSelected)
      elif choice == "x":
        return

  def openInventory(self, currentMenu = 0):
    clear()
    cursor.hide()

    # 0 = battle
    # 1 = overworld
    # 2 = collectible
    # 3 = misc stats
    
    if currentMenu == 0:
      printC('''\
    |R|╔══════════════╗  |Y|╔═════════════════╗  |G|╔══════════════╗  |B|╔══════╗       |PU|╔═══════════════╗
    |R|║ Battle Items ║  |Y|║ Overworld Items ║  |G|║ Collectibles ║  |B|║ Misc ║       |PU|║ [X] Exit Menu ║|R|
 ╔══╝              ╚══════════════════════════════════════════════════════════════════════════╗
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ╚════════════════════════════════════════════════════════════════════════════════════════════╝''')
    elif currentMenu == 1:
      printC('''\
    |R|╔══════════════╗  |Y|╔═════════════════╗  |G|╔══════════════╗  |B|╔══════╗       |PU|╔═══════════════╗
    |R|║ Battle Items ║  |Y|║ Overworld Items ║  |G|║ Collectibles ║  |B|║ Misc ║       |PU|║ [X] Exit Menu ║|Y|
 ╔════════════════════╝                 ╚═════════════════════════════════════════════════════╗
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ╚════════════════════════════════════════════════════════════════════════════════════════════╝''')
    elif currentMenu == 2:
      printC('''\
    |R|╔══════════════╗  |Y|╔═════════════════╗  |G|╔══════════════╗  |B|╔══════╗       |PU|╔═══════════════╗
    |R|║ Battle Items ║  |Y|║ Overworld Items ║  |G|║ Collectibles ║  |B|║ Misc ║       |PU|║ [X] Exit Menu ║|G|
 ╔═════════════════════════════════════════╝              ╚═══════════════════════════════════╗
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ╚════════════════════════════════════════════════════════════════════════════════════════════╝''')
    elif currentMenu == 3:
      printC('''\
    |R|╔══════════════╗  |Y|╔═════════════════╗  |G|╔══════════════╗  |B|╔══════╗       |PU|╔═══════════════╗
    |R|║ Battle Items ║  |Y|║ Overworld Items ║  |G|║ Collectibles ║  |B|║ Misc ║       |PU|║ [X] Exit Menu ║|B|
 ╔═══════════════════════════════════════════════════════════╝      ╚═════════════════════════╗
 ║                                                                                            ║
 ║                                                                                            ║
 ║                                                                                            ║
 ║                                                                                            ║
 ║                                                                                            ║
 ║                                                                                            ║
 ║                                                                                            ║
 ║                                                                                            ║
 ║ |BR|Community Scrolls Found:|B|                                                                   ║
 ║                                                                                            ║
 ║ |DG|?????|B|                                                                                      ║
 ║ |DG|?????|B|                                                                                      ║
 ║ |DG|?????|B|                                                                                      ║
 ║ |DG|?????|B|                                                                                      ║
 ║ |DG|?????|B|                                                                                      ║
 ║ |DG|?????|B|                                                                                      ║
 ║ |DG|?????|B|                                                                                      ║
 ║                                                                                            ║
 ║                                                                                            ║
 ╚════════════════════════════════════════════════════════════════════════════════════════════╝''')
      print("\x1b[5;4H", end="")
      printC("|B|Tickets: |LB|{}T".format(self.tickets))
      printC("\x1b[3C|DG|*Use tickets in shops to purchase spells, wands, items, and more.*")
      print()

      totalMinutes = int(self.time)
      hour = 8 + totalMinutes // 60
      minutes = totalMinutes % 60
      timemode = "AM"
      if hour >= 12:
        timemode = "PM"
        if hour > 12:
          hour -= 12
      hour = str(hour)
      if len(hour) == 1:
        hour = "0" + hour
      minutes = str(minutes)
      if len(minutes) == 1:
        minutes = "0" + minutes
      
      printC("\x1b[3C|B|It is Day |LB|{}|B|, at |LB|{}:{} {}|B|.".format(self.day, hour, minutes, timemode))
      printC("\x1b[3C|DG|*The school day starts at 8:00 AM and ends at 3:00 PM.*")
      printC("\x1b[3C|DG|*You can stay up to 4:30 PM, but don't miss your bus before it leaves!*")
      print()
      print()
      print()
      print()
      if self.hasItem(ScrollOfSupportItem):
        printC("\x1b[3C|BR|⎎ Scroll of Support      |R|(+20 HP)")
      else:
        print()
      if self.hasItem(ScrollOfDiversityItem):
        printC("\x1b[3C|BR|⎎ Scroll of Diversity    |R|(+30 HP)")
      else:
        print()
      if self.hasItem(ScrollOfPresenceItem):
        printC("\x1b[3C|BR|⎎ Scroll of Presence     |R|(+50 HP)")
      else:
        print()
      if self.hasItem(ScrollOfCompassionItem):
        printC("\x1b[3C|BR|⎎ Scroll of Compassion   |R|(+50 HP)")
      else:
        print()
      if self.hasItem(ScrollOfOwnershipItem):
        printC("\x1b[3C|BR|⎎ Scroll of Ownership    |R|(+50 HP)")
      else:
        print()
      if self.hasItem(ScrollOfWellbeingItem):
        printC("\x1b[3C|BR|⎎ Scroll of Wellbeing    |R|(+100 HP)")
      else:
        print()
      if self.hasItem(ScrollOfEqualityItem):
        printC("\x1b[3C|BR|⎎ Scroll of Equality     |R|(+100 HP)")
      else:
        print()


    pass

    allItems = []

    for item in self.items:
      if item.type == currentMenu:
        allItems.append(item)

    allItems = sorted(allItems, key = lambda x : x.name)
    numItems = len(allItems)
    selectedItem = 0
    newSelectedItem = 0
    
    numPages = numItems // 15 + 1
    if numItems % 15 == 0:
      numPages -= 1

    pageNum = 1

    if numItems == 0 or currentMenu == 3:
      print("\x1b[5;4H", end="")
      if currentMenu != 3:
        printC("No items yet!", "DG")
      else:
        print()
      while True:
        choice = getkey()
        if choice in ["\x1b[C", "d"]:
          newMenu = currentMenu + 1
          if newMenu <= 3:
            return self.openInventory(currentMenu = newMenu)
          else:
            newMenu = 3
        elif choice in ["\x1b[D", "a"]:
          newMenu = currentMenu - 1
          if newMenu >= 0:
            return self.openInventory(currentMenu = newMenu)
          else:
            newMenu = 0
        elif choice == "x":
          return
      
    
    while True:
      viewingItems = allItems[pageNum * 15 - 15:pageNum * 15]

      print("\x1b[5;1H", end="")
      clearArea(18, 2, 32)
      print("\x1b[5;4H", end="")
      printC("Page |W|{}|B| of |W|{}\n".format(pageNum, numPages), "B")

      
      firstItem = True
      for viewedItem in viewingItems:
        if firstItem:
          printC("\x1b[3C|PU|> " + viewedItem.getInventoryName())
          firstItem = False
        else:
          printC("\x1b[3C  " + viewedItem.getInventoryName())

      print("\x1b[5;1H")

      if newSelectedItem != selectedItem:
        print("\x1b[{};3H  ".format(7 + selectedItem))
        printC("\x1b[{};3H|PU| >".format(7 + newSelectedItem))
        print("\x1b[5;1H")
        clearArea(16, 37, 57)
        print("\x1b[5;1H")
        selectedItem = newSelectedItem
        
      viewingItems[selectedItem].printDesc(37)
        
      while True:
        if newSelectedItem != selectedItem:
          print("\x1b[{};3H  ".format(7 + selectedItem))
          printC("\x1b[{};3H|PU| >".format(7 + newSelectedItem))
          print("\x1b[5;1H")
          clearArea(16, 37, 57)
          print("\x1b[5;1H")
          viewingItems[newSelectedItem].printDesc(37)
          selectedItem = newSelectedItem
          
        choice = getkey()
        if choice in ["\x1b[A", "w"]:
          newSelectedItem = selectedItem - 1
          if newSelectedItem < 0:
            if pageNum > 1:
              selectedItem = 0
              newSelectedItem = 14
              pageNum -= 1
              break
            else:
              newSelectedItem = 0
        elif choice in ["\x1b[B", "s"]:
          newSelectedItem = selectedItem + 1
          if newSelectedItem >= 15:
            if pageNum < numPages:
              selectedItem = 0
              newSelectedItem = 0
              pageNum += 1
              break
          newSelectedItem = clamp(newSelectedItem, 0, len(viewingItems) - 1)
        elif choice in ["\x1b[C", "d"]:
          newMenu = currentMenu + 1
          if newMenu <= 3:
            return self.openInventory(currentMenu = newMenu)
          else:
            newMenu = 3
        elif choice in ["\x1b[D", "a"]:
          newMenu = currentMenu - 1
          if newMenu >= 0:
            return self.openInventory(currentMenu = newMenu)
          else:
            newMenu = 0
        elif choice == "x":
          return

      
  def openChromebook(self, currentMenu = 0):
    clear()
    cursor.hide()

    # 0 = GoranMail
    # 1 = CurrentMenu

    pageNum = 1

    if currentMenu == 0:
      printC('''\
    |B|╔═══════════╗  |DG|╔═══════════╗                                             |R|╔═══════════╗
    |B|║ GoranMail ║  |DG|║ Todo-List ║                                             |R|║ [X] Close ║|B|
 ╔══╝           ╚═════════════════════════════════════════════════════════════════════════════╗
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ╚════════════════════════════════════════════════════════════════════════════════════════════╝''')

      def getEmailSortableName(email):
        if email.starred:
          return "  " + email.subject
        elif email.unread:
          return " " + email.subject
        return email.subject

      emails = sorted(self.emails, key=getEmailSortableName)
      numEmails = len(emails)
      selectedEmail = 0
      newSelectedEmail = 0
      
      numPages = numEmails // 15 + 1
      if numEmails % 15 == 0:
        numEmails -= 1

      while True:
        viewingEmails = emails[pageNum * 15 - 15:pageNum*15]
        
        print("\x1b[5;1H", end="")
        clearArea(18, 2, 32)
        print("\x1b[5;4H", end="")
        printC("Showing Emails |W|{}|B| - |W|{}|B| of |W|{}\n".format(pageNum * 15 - 14, \
                                                                pageNum * 15 - 15 + len(viewingEmails), numEmails), "B")
  
        
        firstEmail = True
        for viewedEmail in viewingEmails:
          if firstEmail:
            printC("\x1b[3C|PU|>" + viewedEmail.getName())
            firstEmail = False
          else:
            printC("\x1b[3C " + viewedEmail.getName())
  
        printC("\x1b[23;37H|LB|Press [ENTER] to Star/Unstar this Email!")
        print("\x1b[5;1H")

        if newSelectedEmail != selectedEmail:
          print("\x1b[{};3H  ".format(7 + selectedEmail))
          printC("\x1b[{};3H|PU| >".format(7 + newSelectedEmail))
          print("\x1b[5;1H")
          clearArea(16, 37, 57)
          print("\x1b[5;1H")
          selectedEmail = newSelectedEmail
        viewingEmails[selectedEmail].printDesc(37)
          
        while True:
          viewingEmails[selectedEmail].unread = False
          
          if newSelectedEmail != selectedEmail:
            print("\x1b[{};3H  ".format(7 + selectedEmail))
            printC("\x1b[{};3H|PU| >".format(7 + newSelectedEmail))
            print("\x1b[5;1H")
            clearArea(16, 37, 57)
            print("\x1b[5;1H")
            viewingEmails[newSelectedEmail].printDesc(37)
            selectedEmail = newSelectedEmail
            
          choice = getkey()
          if choice in ["\x1b[A", "w"]:
            newSelectedEmail = selectedEmail - 1
            if newSelectedEmail < 0:
              if pageNum > 1:
                selectedEmail = 0
                newSelectedEmail = 14
                pageNum -= 1
                break
              else:
                newSelectedEmail = 0
          elif choice in ["\x1b[B", "s"]:
            newSelectedEmail = selectedEmail + 1
            if newSelectedEmail >= 15:
              if pageNum < numPages:
                selectedEmail = 0
                newSelectedEmail = 0
                pageNum += 1
                break
            newSelectedEmail = clamp(newSelectedEmail, 0, len(viewingEmails) - 1)
          elif choice in ["\x1b[C", "d"]:
            return self.openChromebook(currentMenu = 1)
          elif choice == "\n":
            affectedEmail = viewingEmails[selectedEmail]
            affectedEmail.starred = not affectedEmail.starred
            newSelectedEmail = selectedEmail
            selectedEmail = 0
            break
          elif choice == "x":
            return
    else:
      printC('''\
    |DG|╔═══════════╗  |B|╔═══════════╗                                             |R|╔═══════════╗
    |DG|║ GoranMail ║  |B|║ Todo-List ║                                             |R|║ [X] Close ║|B|
 ╔═════════════════╝           ╚══════════════════════════════════════════════════════════════╗
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ╚════════════════════════════════════════════════════════════════════════════════════════════╝''')


      def getPriority(q):
        if q.pinned:
          return 4 - q.priority
        else:
          return 8 - q.priority

      

      allQuests = sorted(self.quests, key=getPriority)
      quests = []
      for quest in allQuests:
        if not quest.isComplete():
          quests.append(quest)
          
      numQuests = len(quests)
      selectedQuest = 0
      newSelectedQuest = 0
      
      numPages = numQuests // 15 + 1
      if numQuests % 15 == 0:
        numPages -= 1

      if numPages == 0:
        clear()
        cursor.hide()
        printC('''\
    |DG|╔═══════════╗  |B|╔═══════════╗                                             |R|╔═══════════╗
    |DG|║ GoranMail ║  |B|║ Todo-List ║                                             |R|║ [X] Close ║|B|
 ╔═════════════════╝           ╚══════════════════════════════════════════════════════════════╗
 ║ |DG|No Quests Yet!|B|                 ║                                                           ║
 ║                                ║  Go to the Media Center or explore the school to figure   ║
 ║                                ║  out what to do next!                                     ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ║                                ║                                                           ║
 ╚════════════════════════════════════════════════════════════════════════════════════════════╝''')
        while True:
          choice = getkey()
          if choice in ["\x1b[D", "a"]:
            return self.openChromebook(currentMenu = 0)
          elif choice == "x":
            return

      
      while True:
        viewingQuests = quests[pageNum * 15 - 15:pageNum*15]
        
        print("\x1b[5;1H", end="")
        clearArea(18, 2, 32)
        print("\x1b[5;4H", end="")
        printC("Showing Quests |W|{}|B| - |W|{}|B| of |W|{}\n".format(pageNum * 15 - 14, \
                                                                pageNum * 15 - 15 + len(viewingQuests), numQuests), "B")
  
        
        firstQuest = True
        for viewedQuest in viewingQuests:
          if firstQuest:
            printC("\x1b[3C|PU|>" + viewedQuest.getName())
            firstQuest = False
          else:
            printC("\x1b[3C " + viewedQuest.getName())
  
        printC("\x1b[23;37H|LB|Press [ENTER] to Pin/Unpin this Quest!")
        print("\x1b[5;1H")
        
        if newSelectedQuest != selectedQuest:
          print("\x1b[{};3H  ".format(7 + selectedQuest))
          printC("\x1b[{};3H|PU| >".format(7 + newSelectedQuest))
          print("\x1b[5;1H")
          clearArea(16, 37, 57)
          print("\x1b[5;1H")
          selectedQuest = newSelectedQuest
        viewingQuests[selectedQuest].printDesc(37)
        
        while True:
          if newSelectedQuest != selectedQuest:
            print("\x1b[{};3H  ".format(7 + selectedQuest))
            printC("\x1b[{};3H|PU| >".format(7 + newSelectedQuest))
            print("\x1b[5;1H")
            clearArea(16, 37, 57)
            print("\x1b[5;1H")
            viewingQuests[newSelectedQuest].printDesc(37)
            selectedQuest = newSelectedQuest
            
          choice = getkey()
          if choice in ["\x1b[A", "w"]:
            newSelectedQuest = selectedQuest - 1
            if newSelectedQuest < 0:
              if pageNum > 1:
                selectedQuest = 0
                newSelectedQuest = 14
                pageNum -= 1
                break
              else:
                newSelectedQuest = 0
          elif choice in ["\x1b[B", "s"]:
            newSelectedQuest = selectedQuest + 1
            if newSelectedQuest >= 15:
              if pageNum < numPages:
                selectedQuest = 0
                newSelectedQuest = 0
                pageNum += 1
                break
            newSelectedQuest = clamp(newSelectedQuest, 0, len(viewingQuests) - 1)
          elif choice in ["\x1b[D", "a"]:
            return self.openChromebook(currentMenu = 0)
          elif choice == "\n":
            affectedQuest = viewingQuests[selectedQuest]
            affectedQuest.pinned = not affectedQuest.pinned
            newSelectedQuest = selectedQuest
            selectedQuest = 0
            break
          elif choice == "x":
            return