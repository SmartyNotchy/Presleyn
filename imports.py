# Exteral Imports
from threading import Thread
import pickle
import sys
import time
import random
import math
import os
  
# Gotta Love Getkey: The Gameshow
#from replit import db

db = {}

def loadDatabase():
  global db
  try:
    fin = open("SAVEDATA.presleyn", mode="rb")
    db = pickle.load(fin)
    fin.close()
  except:
    syncDatabase()
    loadDatabase()
    
def syncDatabase():
  global db
  fin = open("SAVEDATA.presleyn", mode="wb")
  pickle.dump(db, fin)
  fin.close()

loadDatabase()

#from getkey import getkey as orig_getkey

#def getkey():
#  res = orig_getkey()
#  if len(res) == 1:
#    return res.lower()
#  return res


# Gotta Love Getkey: The Gameshow
import msvcrt
os.system("") # <---- DO NOT DELETE THIS IT MAKES THE ANSI CODES WORK

def getkey():
  res = msvcrt.getch()
  if res == b'\xe0':
    return {b"H": "\x1b[A", b"P": "\x1b[B", b"M": "\x1b[C", b"K": "\x1b[D"}[msvcrt.getch()]
  
  res = str(res)[2:-1]
    
  if res == "\\r":
    return "\n"
  if len(res) == 1:
    return res.lower()
  return res



# Internal Imports
from helpers import *
from BATTLE_spells import *
from BATTLE_wands import *
from BATTLE_player import *
from BATTLE_enemies import *
from MAP_school import *
from MISC_emails import *
from MISC_items import *
from MISC_quests import *
from MISC_shops import *

from CONTENT_spells import *
from CONTENT_wands import *
from CONTENT_quests import *
from CONTENT_items import *
from CONTENT_emails import *
from CONTENT_enemies import *
from MAP_classrooms import *
from BATTLE_battles import *
from CONTENT_classrooms import *
from CONTENT_school import *

from MAP_player import *

from SAVING_INTERNAL_IDS import *
