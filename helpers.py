from imports import *

################
## TEXT MENUS ##
################

ROMAN_NUM = {
  1: "I",
  2: "II",
  3: "III",
  4: "IV",
  5: "V", 
  6: "VI",
  7: "VII",
  8: "VIII",
  9: "IX",
  10: "X"
}

def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

# Avoids a cursor import
# TBF it would be cleaner/more efficient to define functions showCursor and hideCursor but
# most of the code is already factored around the cursor module sooooo......

class Cursor:
  def __init__(self):
    pass

  def show(self):
    sys.stdout.write("\x1b[?25h")

  def hide(self):
    sys.stdout.write("\x1b[?25l")

cursor = Cursor()
cursor.show()

def dropdownMenu(title,choices,highlight_choice=False):
  cursor.hide()
  if title == None:
    print()
  else:
    printC("\n|B|"+title+"\n")
  printC("", "W", end="") # Resets formatting
  
  pointer = "|PI|>"
  for choice in enumerate(choices):
    text = f'  {choice[1]}'
    if choice[0] == 0:
      printC(text,"W",ignore_colors=highlight_choice)
    else:
      printC(text,"B")
  printC("\x1b[A" * (len(choices)) + pointer, end='')
  sys.stdout.flush()

  pos = 1
  while True:
    key = getkey()
    text = f'  {choices[pos-1]}'
    if (key == '\x1b[A' or key == 'w') and pos > 1:
      pos -= 1
      printC(f'\r{text}\r\x1b[A', "B", end="")
      printC(pointer, end="")
      printC(f'\x1b[5m {choices[pos-1]}', "W", end = "", ignore_colors = highlight_choice)
    elif (key == '\x1b[B' or key == 's') and pos < len(choices):
      pos += 1
      printC(f'\r{text}\r\x1b[B', "B", end="")
      printC(pointer, end="")
      printC(f'\x1b[5m {choices[pos-1]}', "W", end = "", ignore_colors = highlight_choice)
    elif key == '\n' or key == " ":
      printC("\x1b[B" * (len(choices)-pos))
      cursor.show()
      #print()
      return pos
    #elif key.isdecimal():
    #  number = int(key)
    #  if 0 < number <= len(choices):
    #    print(ansi_cursor.down()*(len(choices)-pos)+ansi_cursor.show())
    #    return number
    sys.stdout.flush()

def trollDropdownMenu(title, choices, correct):
  actuallyGotItRight = False
  
  choice = dropdownMenu(title, choices, False) - 1
  if choices[choice] == correct:
    actuallyGotItRight = True
    replacement = random.randint(1, len(choices)) - 1
    while replacement == choice:
      replacement = random.randint(1, len(choices)) - 1
    choices[replacement], choices[choice] = choices[choice], choices[replacement]
    printC("\x1b[{}A".format(len(choices) + 4))
    printC(title, "B")
    print()
    for idx in range(1, len(choices) + 1):
      if idx == choice + 1:
        printC("|PI|> |B|" + choices[idx-1], end="            \n")
      else:
        printC("|PI|  |B|" + choices[idx-1], end="            \n")
    print()

  return actuallyGotItRight
  
####################
## COLOR PRINTING ##
####################
# THIS CODE IS COPYRIGHTED UNDER THE LAW OF SMARTYDUCKY
# (Owned by Pilliam Wark, commissioned to the Friday CS Project Group)
# GO AWAY RYAN
# IF YOU STEAL THIS I HAVE THE LEGAL RIGHT TO PROSECUTE AND INCARCERATE YOU
# ESPECIALLY IF YOUR NAME IS RYAN
    
COLOR_KEY = {
  "R": "\x1b[38;2;255;0;0m",
  "O": "\x1b[38;2;255;153;0m",
  "BY": "\x1b[38;2;255;255;0m",
  "Y": "\x1b[38;2;255;200;0m",
  "LG": "\x1b[38;2;0;255;0m",
  "G": "\x1b[38;2;0;150;0m",
  "LB": "\x1b[38;2;0;225;255m",
  "B": "\x1b[38;2;0;180;255m",
  "DB": "\x1b[38;2;0;0;255m",
  "PU": "\x1b[38;2;150;0;255m",
  "PI": "\x1b[38;2;255;100;255m",
  "DG": "\x1b[38;2;128;128;128m",
  "W": "\x1b[38;2;255;255;255m",
  "BR": "\x1b[38;2;128;70;27m",
  "BG": "\x1b[38;2;60;64;62m"
}
COLOR_KEY_KEYS = ("R", "O", "BY", "Y", "LG", "G", "LB", "B", "DB", "PU", "PI", "DG", "W", "BR", "BG", "--")

def printC(txt, base_col = "DG", end = "\n", ignore_colors = False):
  inItalic = False
  inStrikethrough = False
  current_col = COLOR_KEY[base_col]
  char_idx = 0
  sys.stdout.write("\x1b[0m\x1b[1m")
  sys.stdout.write(current_col)
  while char_idx < len(txt):
    if txt[char_idx] == "|" and txt[char_idx+1] in COLOR_KEY_KEYS and txt[char_idx+2] == "|":
      if not ignore_colors:
        current_col = COLOR_KEY[txt[char_idx+1]]
        sys.stdout.write(current_col)
      char_idx += 2
    elif txt[char_idx] == "|" and txt[char_idx+1:char_idx+3] in COLOR_KEY_KEYS and txt[char_idx+3] == "|":
      if not ignore_colors:
        if txt[char_idx+1:char_idx+3] == "--":
          current_col = COLOR_KEY[base_col]
          sys.stdout.write("\x1b[0m\x1b[1m")
        else:
          current_col = COLOR_KEY[txt[char_idx+1:char_idx+3]]
        sys.stdout.write(current_col)
      char_idx += 3
    elif txt[char_idx] == "*" and (char_idx == 0 or txt[char_idx-1] != "\\"):
      if inItalic:
        sys.stdout.write("\x1b[0m\x1b[1m" + current_col)
        if inStrikethrough:
          sys.stdout.write("\x1b[9m")
      else:
        sys.stdout.write("\x1b[3m")
      inItalic = not inItalic
    elif char_idx < len(txt) - 1 and txt[char_idx:char_idx+2] == "~~" and (char_idx == 0 or txt[char_idx-1] != "\\"):
      if inStrikethrough:
        sys.stdout.write("\x1b[0m\x1b[1m" + current_col)
        if inItalic:
          sys.stdout.write("\x1b[3m")
      else:
        sys.stdout.write("\x1b[9m")
      inStrikethrough = not inStrikethrough
      char_idx += 1
    elif txt[char_idx] == "\\":
      pass
    else:
      sys.stdout.write(txt[char_idx])
    char_idx += 1
  sys.stdout.write(end)
  
def clear():
  #print("\x1b[2J\x1b[1;1H", end="")
  os.system("cls")
  printC("Presleyn Beta v0.2.0.2 - Acts I & II Playtesting Build (Windows Edition)")

def clearArea(lines, offset, amount):
  for i in range(lines):
    print("\x1b[{}C".format(offset) + " " * amount)
    
def enter():
  printC("\nPress Enter To Continue: ",end="")
  input()
  deleteLines(2)

'''
COLOR_KEY_KEYS = ("R", "O", "BY", "Y", "LG", "G", "LB", "B", "DB", "PU", "PI", "DG", "W", "BR", "BG", "--")
'''
# (just in case it's not obvious, BY = Bright Yellow, BR = Brown, BG = Replit Console Color)
# "": "",
nameDict = {
  "Pilliam": "PI",
  "Krishan": "LB",
  "Bryce": "PU",
  "Anna": "LG",
  "Aadhavan": "LG",
  "Chris": "Y",
  "Valeria": "PI",
  "Ms. Lee": "LB",
  "Lillian": "PU",
  "Sri": "Y", # forward the email to me once you get a reply ok!
  "Don": "DG",
  "Benedicte": "PU",
  "Ryan": "LB",
  "Sherry": "O",
  "Sofya": "Y",
  "Arjun": "Y",
  "Brandon T": "Y",
  "Gloria": "O",
  "Jashlee": "PI",
  "Jessika": "PU",
  "Sayf": "LB",
  "Ms. Ramasamy": "G",
  "Rachel": "PU",
  "Ms. Mahon": "O",
  "Akshaj": "LB",
  "Edem": "PU",
  "Ms. Presley": "LG",
  "Brandon V": "O",
  "Cello-San": "O",
  "Chase": "Y",
  "Daniel": "G",
  "Dasha": "LG",
  "Henry": "LB",
  "Gabrielle": "PU",
  "Detah": "W",
  "???": "W",
  "Justin": "PU",
  "Kedus": "Y",
  "Khang": "LG",
  "Luke": "O",
  "Mr. Poker": "Y",
  "Mr. Rea": "Y",
  "Ms. Gleich": "LB",
  "Ms. MacDonald": "O",
  "Ms. Poole": "G",
  "Ms. Santiago": "LG",
  "Sergi": "O",
  "Yulia": "BR",
  "Nathan": "Y",
  "William": "LB",
  "Preston": "O",
  "Shriram": "R",
  "Roselyn": "PI",
  "Ellie": "G", 
  "Poorvi":"O",
  "Ella":"DB",
  "Katherine":"PI",
  "Peter":"Y",
  "Goran":"G",
  "Maya":"LG",
  "Gummy":"G",
  "Effie":"G",
  "Gimli":"G",
  "Dobby":"G",
  "Mr. Adams":"G",
  "Brooke":"LB",
  "Shameer":"PU",
}
  
def dial(speaker, text):
  nameColor = "|" + nameDict.get(speaker, "R") + "|" 
  printC("\n{}{}|B|: {} ".format(nameColor, speaker, text), "B", end="")
  input()

def dialNoSpeaker(text):
  printC("\n" + text, "B", end="")
  input()

def typewrite(text, color = "B", waitTime=0.03):
  waitTimeBuildup = 0
  for char in text:
    printC(char, color, end="")
    sys.stdout.flush()
    waitTimeBuildup += waitTime
    if waitTimeBuildup >= 0.075:
      time.sleep(waitTimeBuildup)
      waitTimeBuildup = 0

def deleteLines(num):
  for _ in range(num):
    sys.stdout.write("\x1b[F\x1b[K")
  print("\r",end="")

def printBoxedText(txt, col="B"):
  printC("╔═" + "═" * len(txt) + "═╗", col)
  printC("║ " + txt + " ║", col)
  printC("╚═" + "═" * len(txt) + "═╝", col)

INTERNAL_FLAIR_TERMINATE = False
INTERNAL_FLAIR_ENDED = False

def printFlair(txt):
  global INTERNAL_FLAIR_TERMINATE, INTERNAL_FLAIR_ENDED
  INTERNAL_FLAIR_TERMINATE = False
  INTERNAL_FLAIR_ENDED = False
  
  def animateFlair():
    global INTERNAL_FLAIR_TERMINATE, INTERNAL_FLAIR_ENDED
    cursor.hide()
    messageLen = len(txt)

    print()
    printC("|R|>|Y|>|LG|> {} |LG|<|Y|<|R|<".format(" " * messageLen))
    print()
    printC("Press Enter to Continue:", "DG")
    print("\x1b[4A")

    colors = ("R", "Y", "G", "LB", "DB", "PU", "PI", "R", "Y", "G", "LB", "DB", "PU", "PI")

    i = 0
    while not INTERNAL_FLAIR_TERMINATE or (i * 3) < messageLen:
      colorsToPrint = colors[i % 3:i % 3 + 3]
  
      printC("|{}|>|{}|>|{}|> ".format(*colorsToPrint), end="")
      
      
      message = txt
  
      if i * 3 >= messageLen:
        message = "|B|" + message
      else:
        message = "|B|" + message[:i * 3] + "|W|" + message[i * 3:i*3 + 3] + " " * (messageLen - i * 3 - 3)
  
      printC(message+ " |{}|<|{}|<|{}|<".format(*colorsToPrint[::-1]))
      
      print("\x1b[2A")
      i += 1
      time.sleep(0.1)

    INTERNAL_FLAIR_ENDED = True

  def endAnimation():
    global INTERNAL_FLAIR_TERMINATE, INTERNAL_FLAIR_ENDED
    input()
    INTERNAL_FLAIR_TERMINATE = True
    return
  
  t1 = Thread(target=animateFlair)
  t2 = Thread(target=endAnimation)

  t1.start()
  t2.start()
  t2.join()

  while not INTERNAL_FLAIR_ENDED:
    pass
    
  print("\x1b[A")


####################
## NUMBER HELPERS ##
####################

def clamp(num, minVal, maxVal):
  return min(max(num, minVal), maxVal)
  
####################
## BATTLE HELPERS ##
####################

def getZone(num, zones): 
  zone_key = (REDZONE, YELLOWZONE, GREENZONE, YELLOWZONE, REDZONE)
  for i in range(1,6):
    if num < sum(zones[0:i]):
      return zone_key[i-1]
  return REDZONE

def randomZone(redProb, yellowProb, greenProb):
  try:
    assert abs(redProb + yellowProb + greenProb - 1) < 0.01
  except:
    raise ContentError()

  res = random.uniform(0.0, 1.0)
  if res < redProb:
    return REDZONE
  elif res < yellowProb + redProb:
    return YELLOWZONE
  elif res < greenProb + yellowProb + redProb:
    return GREENZONE
  else:
    raise ContentError()

def getTimeStringFromInt(totalMinutes):
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

  return "{}:{} {}".format(hour, minutes, timemode)
  
###################
## TIMED HIT BAR ##
###################

INTERNAL_WaitingForHit = True
INTERNAL_HitbarPos = 0
INTERNAL_HitbarDir = True # True = Right, False = Left
INTERNAL_HitbarSpeed = 1
INTERNAL_HitbarZones = [5,4,3,4,5]

REDZONE = 0
YELLOWZONE = 1
GREENZONE = 2

def timedHitbar(speedCoeff, zones):
  cursor.hide()
  global INTERNAL_WaitingForHit, INTERNAL_HitbarPos, INTERNAL_HitbarSpeed, INTERNAL_HitbarDir, INTERNAL_HitbarZones
  INTERNAL_WaitingForHit = True
  INTERNAL_HitbarPos = 0
  INTERNAL_HitbarDir = True
  INTERNAL_HitbarSpeed = speedCoeff
  INTERNAL_HitbarZones = zones
  
  def updateTimedHitbar():
    global INTERNAL_WaitingForHit, INTERNAL_HitbarPos, INTERNAL_HitbarSpeed, INTERNAL_HitbarDir, INTERNAL_HitbarZones
    print()
    print()
    printC("╠" + "═" * sum(INTERNAL_HitbarZones) + "╣", "B")
    printC("║|R|{}|Y|{}|LG|{}|Y|{}|R|{}|B|║".format(*map(lambda x : "=" * x, INTERNAL_HitbarZones)), "B")
    printC("╠" + "═" * sum(INTERNAL_HitbarZones) + "╣|W|", "B")
    print() 
    print("\x1B[5A", end="")
    while INTERNAL_WaitingForHit:
      print("\x1b[{}C V ".format(INTERNAL_HitbarPos), end="\r")
      
      time.sleep(0.06 / INTERNAL_HitbarSpeed)

      if INTERNAL_HitbarDir:
        INTERNAL_HitbarPos += 1
        if INTERNAL_HitbarPos >= sum(INTERNAL_HitbarZones)-1:
          INTERNAL_HitbarDir = False
      else:
        INTERNAL_HitbarPos -= 1
        if INTERNAL_HitbarPos <= -1:
          INTERNAL_HitbarDir = True

  def getUserHit():
    user_input = input()  

  t1 = Thread(target=updateTimedHitbar)
  t2 = Thread(target=getUserHit)

  t1.start()
  t2.start()
  t2.join()
  INTERNAL_WaitingForHit = False
  FinalHitbarPos = INTERNAL_HitbarPos # Avoids Race Condition

  # Hit animation
  # This might lag

  for i in range(6):
    print("\x1b[{}C".format(FinalHitbarPos) + " V ", end="\r")
    printC("╠" + "═" * sum(INTERNAL_HitbarZones) + "╣", "W")
    printC("║" + "\x1b[{}C".format(sum(INTERNAL_HitbarZones)) + "║", "W")
    printC("╠" + "═" * sum(INTERNAL_HitbarZones) + "╣", "W")
    
    time.sleep(0.05)
    
    print("\x1B[3A", end="")
    
    printC("╠" + "═" * sum(INTERNAL_HitbarZones) + "╣", "B")
    printC("║" + "\x1b[{}C".format(sum(INTERNAL_HitbarZones)) + "║", "B")
    printC("╠" + "═" * sum(INTERNAL_HitbarZones) + "╣", "B")
    
    time.sleep(0.05)

    print("\x1B[3A", end="")

  
  print("\x1B[4B", end="")
  
  cursor.show()
  return FinalHitbarPos


##################
## MISC HELPERS ##
##################

RARITIES = {
  0: "|W|Common",
  1: "|LG|Uncommon",
  2: "|DB|Rare",
  3: "|PU|Epic",
  4: "|Y|Legendary",
  5: "|PI|Mythic",
  6: "|LB|Divine"
}

class ContentError(Exception):
  def __init__(self):
    super().__init__(\
'''

Oh noes, a ContentError strikes again!

For programmers:
This error means that an issue occurred with the custom-coded
content of the game, rather than the underlying frameworks.

To fix this, go to the line where the error was thrown and check
that you are using the frameworks properly and with their intended use.

For playtesters/players:
Please report this error along with the line # & file where it occurred
in the comments! Screenshots of the error and what you were doing when
the error occurred are greatly appreciated.
''')
