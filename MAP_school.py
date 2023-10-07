from imports import *

#################
## MAP HELPERS ##
#################

WALL_SYMBOLS = {
  (False, True, True, False): "═",
  (False, True, False, False): "═",
  (False, False, True, False): "═",
  (False, False, True, True): "═",
  (False, False, True, True): "╔",
  (True, True, False, False): "╝",
  (True, False, True, False): "╚",
  (False, True, False, True): "╗",
  (True, False, False, True): "║",
  (True, False, False, False): "║",
  (False, False, False, True): "║",
  (True, True, False, True): "╣",
  (True, True, True, True): "╬",
  (False, False, False, False): "▫",
  (True, False, True, True): "╠",
  (True, True, True, False): "╩",
  (False, True, True, True): "╦"
}

DOOR_SYMBOLS = {
  (False, True, True, False): "━",
  (True, False, False, True): "┃"
}


def getWallSymbol(hasUp, hasLeft, hasRight, hasDown):
  return WALL_SYMBOLS[(hasUp, hasLeft, hasRight, hasDown)]

def getMapChar(map, pos):
  if pos[0] < 0 or pos[1] < 0:
    return " "
  try:
    return map[pos[0]][pos[1]]
  except:
    return " "

def convertMap(origMap):
  # SPECIAL SYMBOLS:
  # ".+@|_"
  origMap = origMap.split("\n")[1:-1]
  newMap = [[]]
  for rowPos in range(len(origMap)):
    for colPos in range(len(origMap[rowPos])):
      char = getMapChar(origMap, [rowPos, colPos])
      if char == ".":
        newMap[-1].append(getWallSymbol(getMapChar(origMap, [rowPos-1, colPos]) in "═╔╝╚╗║╣╬╠╩╦.@|",\
                                        getMapChar(origMap, [rowPos, colPos-1]) in "═╔╝╚╗║╣╬╠╩╦.@_",\
                                        getMapChar(origMap, [rowPos, colPos+1]) in "═╔╝╚╗║╣╬╠╩╦.@_",\
                                        getMapChar(origMap, [rowPos+1, colPos]) in "═╔╝╚╗║╣╬╠╩╦.@|"))
      elif char == "|":
        newMap[-1].append(getWallSymbol(True, False, False, True))
      elif char == "_":
        newMap[-1].append(getWallSymbol(False, True, True, False))
      elif char == "+":
        newMap[-1].append("·")
      elif char == "@":
        try:
          newMap[-1].append(DOOR_SYMBOLS[getMapChar(origMap, [rowPos-1, colPos]) in "═╔╝╚╗║╣╬╠╩╦.@|",\
                                        getMapChar(origMap, [rowPos, colPos-1]) in "═╔╝╚╗║╣╬╠╩╦.@_",\
                                        getMapChar(origMap, [rowPos, colPos+1]) in "═╔╝╚╗║╣╬╠╩╦.@_",\
                                        getMapChar(origMap, [rowPos+1, colPos]) in "═╔╝╚╗║╣╬╠╩╦.@|"])
        except:
          newMap[-1].append("!")
      else:
        newMap[-1].append(char)
    newMap[-1] = "".join(newMap[-1])
    newMap.append([])
  return "\n".join(newMap[:-1])

MAP_SYMBOL_COLORS = {
  "Δ": "G",
  "○": "PI",
  "·": "DG",
  "━": "BG",
  "┃": "BG",
  "!": "R"
}

def printMap(txt, base_col = "B"):
  char_idx = 0
  sys.stdout.write("\x1b[0m\x1b[1m" + COLOR_KEY[base_col])
  
  while char_idx < len(txt):
    if txt[char_idx] in MAP_SYMBOL_COLORS.keys():
      sys.stdout.write(COLOR_KEY[MAP_SYMBOL_COLORS[txt[char_idx]]] + txt[char_idx] + COLOR_KEY[base_col])
    else:
      sys.stdout.write(txt[char_idx])
    char_idx += 1
    
  sys.stdout.write("\n")

def getMapPos(map, pos):
  row = 1
  col = 0
  idx = 0
  for char in map:
    if idx == pos:
      return (row+1, col+1)
    if char == "\n":
      row += 1
      col = 1
    else:
      col += 1
    idx += 1
  return (row, col)
    



####################################
## SCHOOL OVERWORLD MAP FRAMEWORK ##
####################################

# HALLWAY_6
# HALLWAY_7
# HALLWAY_8
# HALLWAY_ELECTIVE
# HALLWAY_MAIN
# HALLWAY_GYM

class Location():
  def __init__(self, name, rooms, section, pos):
    self.locUp = None
    self.locRight = None
    self.locDown = None
    self.locLeft = None

    self.name = name
    self.rooms = rooms
    self.section = section
    self.pos = pos

# Location Helpers

def setSimpleLocation(name, section, location):
  global LOCATIONS
  LOCATIONS[name] = Location(name, [], section, {section: location})

def setComplexLocation(name, locations):
  global LOCATIONS
  LOCATIONS[name] = Location(name, [], None, locations)

def createHorizHallway(name, section, locations, start_idx = 1):
  global LOCATIONS
  idx = start_idx
  for location in locations:
    setSimpleLocation(name + "_{}".format(idx), section, location)
    idx += 1
  connectHoriz(*(name + "_{}".format(i) for i in range(start_idx, idx)))

def createVertHallway(name, section, locations, start_idx = 1):
  global LOCATIONS
  idx = start_idx
  for location in locations:
    setSimpleLocation(name + "_{}".format(idx), section, location)
    idx += 1
  connectVert(*(name + "_{}".format(i) for i in range(start_idx, idx)))
  
def classroomSetWaypoints(classroom, waypoints):
  global LOCATIONS
  for waypoint in waypoints:
    LOCATIONS[waypoint].rooms.append(classroom)
  
def connectHoriz(*locs):
  # From Left to Right
  for idx in range(len(locs)):
    if idx == 0:
      LOCATIONS[locs[0]].locRight = locs[1]
    elif idx == len(locs) - 1:
      LOCATIONS[locs[-1]].locLeft = locs[-2]
    else:
      LOCATIONS[locs[idx]].locLeft = locs[idx-1]
      LOCATIONS[locs[idx]].locRight = locs[idx+1]

def connectVert(*locs):
  # From Top to Bottom
  for idx in range(len(locs)):
    if idx == 0:
      LOCATIONS[locs[0]].locDown = locs[1]
    elif idx == len(locs) - 1:
      LOCATIONS[locs[-1]].locUp = locs[-2]
    else:
      LOCATIONS[locs[idx]].locUp = locs[idx-1]
      LOCATIONS[locs[idx]].locDown = locs[idx+1]


#################
## SCHOOL MAPS ##
#################
LOCATIONS = {}

class SchoolMap():
  def __init__(self):
    
    self.asciiMaps = {
      "PROLOGUE_AREA":\
      '''
                                     ..............
   Roberto Clemente Middle School   ..
................@@@@@................   Δ         Δ   
  .            .  +  .  
  ..           .     .......  .  .  .        Δ
   ..          .  +       +       +
    ............     .  .  .  .  .  .   Δ         Δ
  +       +       +       +       +       +
...................................................
      ''',
      
      "OUTSIDE_ENTRANCE":\
      '''
                                     ..............
   Roberto Clemente Middle School   ..
................@@@@@................   Δ         Δ   
  .            .  +  .  
  ..           .     .......  .  .  .        Δ
   ..          .  +       +       +
    ............     .  .  .  .  .  .   Δ         Δ
  +       +       +       +       +       +      CARPOOL LANE
...................................................
      ''',
      
      "CARPOOL_LANE":\
      ''' 
   SIDE ENTRANCE
.    .     .  ..........................
.  ...  +  ....                        .
....              ...............      .
        +        ..             ...    .       
                 .                ...  .
   Δ    +        .                  .  .
                 .                  .  .
        +        ....               .  .
                    ....            .  .
  +     +              .            .  .
........................            .  .
      ''',
      "SIDE_ENTRANCE":\
      '''      
         BLACKTOP
    .                  Δ            Δ
    .       +   Δ            Δ
.....
@ +    +    +   ...........
.....           .         .
    ..      +   @   GRE   .        Δ
     @          .         .
     . +    +   ...........             
     .                        Δ     .......
     . +    +                        . 
     .   .     .                     .    
     .   .  +  .       Δ             .
     @ + .     .                     .
     .   .  +  .                     .
     .....     .............................
         CARPOOL
      ''',
      "BLACKTOP":\
      '''
......                            Δ
     ..            Δ                             Δ
      .           ..................
      .       +   .                .    Δ
      .           .                .
      .       +   .                .             Δ
      .           .    BLACKTOP    .
      .       +   .                .       Δ
      .           .                .
      .       +   ..................             Δ
      .                                Δ
      .       +    ................
      .           ..         ~    .            Δ
      .       +   .  ~          ...  Δ
      .           ..      ~   ...          Δ
.......       +    ............ 
.                  Δ            Δ            Δ
        SIDE ENTRANCE
      ''',

      
      "MAIN_ENTRANCE":\
      '''
          ELECTIVE HALLWAY                CENTRAL AREA
       ╠.......╣   .     ╠.....╣       ╠...╣        .
 ....... Build . + . 246 .  .  .  242  .241.   +    .  
 .     ....@....   .....@..........@.....@..        .  
 .     @   +     +       +    +    +     +     +    .  
 .     .................   ................         .
 ..    .               .   .  .  .     .  .         .            
  .    .         ....... + ................    +    .        
...    .   248   . 251 .   .           .  .         ............. 
.      .         .......   .   STAGE   .  .         .     . .   .
..............   . 252 ..@.................    +    @ HEA .......
       . 248 .   .  ....                  .         ... ...     .
       ...........  .  .                  .         . . . .     .
         .   .   .  .  .                  @    +    ... ... .....
         ............  .       CAFE       .         .       .   .
         .             .                  .         @ MAIN  .....
         ..... KITCHEN .                  .    +    .........   .
         .   .         .                  .         .   .   .  ..
         .....................................@@@...............
      
      
      ''',
      "HALLWAY_ELECTIVE":\
      '''                               
  ...................                                      
...     240     .   .......                               
. .    ........ @   .     .                                 
........      ... + @ 239 .                          
.      . 237A . .   .......                   
.      ..........   .  .  .             .................
. 237B      @     + .......            ..               ..       
.................   .     .            .                 .            
.      .        . + @ 238 .            .     LIBRARY     .           
. 236B .  236C  @   .......            .                 .   
. ...............   .     ..............                 ......
...             . + . 234 .     .      .......     .......   
. .   236A      .   ...   . 232 .  230 .     ..@@@..     .     
.............@...     ..@.....@.....@.........     ............
.             @   +     +     +     +    +      +     6TH HALLWAY
.         .......   .........................       ...........
.   235   .||||   + .     .     .       . E @   +    ||||.
........╦.......╗   .     .     .       ╠...╣       ......
              CAFETERIA                   MAIN ENTRANCE 
''',

      "HALLWAY_6":\
      '''
                                        ..........................
                                        .         .___.     .    ..
                                        .   220   .___. 219 . 218 .
                                        ........@..   .............
                                        .     . +   +     + @     .
                                        . 221 @   .......   . 217 .
           .................            .......   .  .  .   .......
          ..               ..           .     .   .......   .     .
          .                 .           . 222 @ + .  .  . + @ 216 .
          .     LIBRARY     .           .......   .......   ....... 
          .                 .           .     .   .     .   .     .
      .....                 .............     .   .......   @ 213 .
          .......     .......     .     . 224 @ + .     @ + .......
          .     ..@@@..     .     . 225 .    ..   . 211 .   .     .
      ...........     ..............@.........    .......   @ 212 .
ELECTIVE HALL      +     +    +     +     +     +    +    + ....... 
      ..........       ............................   ....... 
           . E @   +    ||||.                     . +  ||||.
           ╠...╣       ......                     ..........
             MAIN ENTRANCE
      ''',
      "HALLWAY_7":\
      '''
                    .......                              
 ...........    ..@..     .                             
..    .    ..   .   @ 146 .                                 
. 148 . 147 .   . + .......                               
.................   .     .                                 
.     . +     +   + @ 145 .                          
. 149 @   .......   .......                             
.......   .  .  .   .     .            .......@.......
.     . + ....... + @ 143 .           ..    .   .    ..       
. 150 @   .  .  .   .......           . 130 @ + @ 129 .            
.......   .  .  .   .     .           .......   .......           
.     . + .  .  . + ....@..           .     .   .     .   
. 154 @   .......   .     ............. 131 @ + @ 128 ......
.......   .     .   .     .     .     ....@..   ..@....   
.     . + .     . + . 140 . 137 . 136 .     . + . 127 .     
. 155 @   .......   ....@.....@.....@........   ............
....... +         +          +        +       +        8TH HALLWAY
.     .   .................................       ..........
. 156 @ +  ||||.                      . E @   +    ||||.
................                      ....╣       ╔.....
                                             GYM
''',
       "HALLWAY_8":\
      '''
                                     ......   ................
                                    ..    ..@..___.     .    ..
                                    . 120 @ + .___. 119 . 118 .
                                    .......   .   .............
                                    .     @ +   +     + .     .
                                    . 121 .   .......   . 117 .
         .......@.......            .......   .  .  .   .......
        ..    .   .    ..           .     @   .......   .     .
        . 130 @ + @ 129 .           . 122 . + .  .  . + @ 116 .
        .......   .......           .......   .......   ....... 
        .     .   .     .           .     .   .     .   @     .
      ... 131 @ + @ 128 .............     .   .......   . 113 .
        ....@..   ..@....     .     . 124 . + .     @ + .......
        .     . + . 127 . 126 . 125 .    ..   . 111 .   @     .
      .........   ........@.....@.....@...    .......   . 112 .
7TH HALLWAY     +       +        +          +         + .......
      .......       .......................   ...........  
        . E @   +    ||||.                . +   ||||.   .
        ....╣       ╔.....                .   ......╬....
               GYM                         GYM
''',
      "HALLWAY_GYM":\
'''
    CENTRAL AREA                8TH HALLWAY
.......       .......................   ..........╣
  . E @   +    ||||.                . +   ||||.   .
  .....       ......                @   ...........
      . + .....                     . +    +  @    
      .   .   .         GYM         .   ...........
      .   .   .                     .   .         ..
      . + .   @                     . + @   BOYS   @
      .   .   .                     .   ..@.........
      .   ......@.................@..   .    .     .
      . +       +      +      +       + . ..........
      ......@.......@.......@.......@......        .
      .       .       .       .   .   @   ..........
      . DANCE . WEIGH .  AUX  ......  .....        @
      .       .       .       .    .     GIRLS     .
      ..............................................
'''
    }

    self.playerLastPos = None
    self.playerLastSection = None

  def run(self, player, immediatelyQuit = False):
    cursor.hide()
    playerLoc = LOCATIONS[player.loc[1]]
    reprint = True
    if player.loc[0] == self.playerLastSection:
      reprint = False

      iconColor = player.nameColor
      if player.nameColor == "B":
        iconColor = "PI"
    
      printC("\x1b[{};{}H|DG|·|B|".format(*getMapPos(self.asciiMaps[player.loc[0]], self.playerLastPos)))
      printC("\x1b[{};{}H|{}|○|B|".format(*getMapPos(self.asciiMaps[player.loc[0]], playerLoc.pos[player.loc[0]]), iconColor))
      printC("\x1b[{};{}H".format(*getMapPos(self.asciiMaps[player.loc[0]], len(self.asciiMaps[player.loc[0]]))))
    else:
      clear()
      print()
  
      mapToPrint = self.asciiMaps[player.loc[0]]
      mapToPrint = mapToPrint[:playerLoc.pos[player.loc[0]] + 1] + "○" + mapToPrint[playerLoc.pos[player.loc[0]] + 2:]
      mapToPrint = convertMap(mapToPrint) 
      printMap(mapToPrint, "B")

    self.playerLastPos = playerLoc.pos[player.loc[0]]
    self.playerLastSection = player.loc[0]
    print() 
    if player.act != 0:
      player.printControls(reprint)

    printC("Use WASD/Arrow Keys to move around the map!", "DG")
    adjRooms = playerLoc.rooms
    if player.act == 0:
      if len(adjRooms) > 0:
        printC("Press SPACE to enter the school!", "W")
      else:
        printC("Navigate to the school entrance!", "DG")
    else:
      if len(adjRooms) > 0:
        printC("Press SPACE to enter nearby classrooms!", "W")
      else:
        print("                                          ")
    while True:
      cursor.hide()

      # PAST 4:30 CODE OR IMMEDIATELY QUIT
      if player.timePast(510) or immediatelyQuit:
        self.playerLastPos = None
        self.playerLastSection = None
        return
    
      action = getkey()
      changed = False
      if action in ["\x1b[A", "w"]:
        if playerLoc.locUp != None:
          changed = True
          player.loc[1] = playerLoc.locUp
          player.incrementTime(0.5)
          if LOCATIONS[player.loc[1]].section != None and LOCATIONS[player.loc[1]].pos.get(player.loc[0], -1) == -1:
            player.loc[0] = LOCATIONS[player.loc[1]].section
      elif action in ["\x1b[B", "s"]:
        if playerLoc.locDown != None:
          changed = True
          player.loc[1] = playerLoc.locDown
          player.incrementTime(0.5)
          if LOCATIONS[player.loc[1]].section != None and LOCATIONS[player.loc[1]].pos.get(player.loc[0], -1) == -1:
            player.loc[0] = LOCATIONS[player.loc[1]].section
      elif action in ["\x1b[D", "a"]:
        if playerLoc.locLeft != None:
          changed = True
          player.loc[1] = playerLoc.locLeft
          player.incrementTime(0.5)
          if LOCATIONS[player.loc[1]].section != None and LOCATIONS[player.loc[1]].pos.get(player.loc[0], -1) == -1:
            player.loc[0] = LOCATIONS[player.loc[1]].section
      elif action in ["\x1b[C", "d"]:
        if playerLoc.locRight != None:
          changed = True
          player.loc[1] = playerLoc.locRight
          player.incrementTime(0.5)
          if LOCATIONS[player.loc[1]].section != None and LOCATIONS[player.loc[1]].pos.get(player.loc[0], -1) == -1:
            player.loc[0] = LOCATIONS[player.loc[1]].section
      elif action == "r" and player.act != 0:
        player.viewSpellbookArsenal()
        self.playerLastPos = None
        self.playerLastSection = None
        changed = True
      elif action == "f" and player.act != 0:
        player.viewSelectedWand()
        self.playerLastPos = None
        self.playerLastSection = None
        changed = True
      elif action == "e" and player.act != 0:
        player.openInventory()
        self.playerLastPos = None
        self.playerLastSection = None
        changed = True
      elif action == "c" and player.act != 0:
        player.openChromebook()
        self.playerLastPos = None
        self.playerLastSection = None
        changed = True
      elif action == " " and len(adjRooms) > 0:
        choice = dropdownMenu("Select a room to enter:", [room.getName(player.act) for room in adjRooms] + ["Cancel"])
        if choice == len(adjRooms) + 1:
          changed = True
          self.playerLastPos = None
          self.playerLastSection = None
          #deleteLines(len(adjRooms) + 4)
          #cursor.hide()
        else:
          changed = True
          self.playerLastPos = None
          self.playerLastSection = None
          player.classroom = adjRooms[choice-1]
      if changed:
        return
