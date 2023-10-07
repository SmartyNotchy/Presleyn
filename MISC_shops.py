from imports import *

class Listing:
  def __init__(self, product, price, oneTime, purchasable):
    self.product = product
    self.price = price
    self.oneTime = oneTime
    self.purchasable = purchasable

  def buy(self, player):
    assert self.purchasable
    assert player.takeTickets(self.price)

    productType = self.product.objectType
    if productType == "Spell":
      player.giveSpell(self.product)
    elif productType == "Wand":
      player.giveWand(self.product)
    elif productType == "Item":
      player.giveItem(self.product)
    else:
      assert productType in ["Spell", "Wand", "Item"]

    if self.oneTime:
      self.purchasable = False

  def getName(self):
    res = self.product().name

    # TODO: Figure Out & Test Proper Length
    res += " " * (27 - len(res))
    if self.purchasable:
      res += str(self.price) + "T"
    else:
      res += "OWNED"
    
    if not self.purchasable:
      res = "|DG|" + res
    else:
      res = "|{}|".format(self.product().nameColor) + res
      
    return res
      

  def printDesc(self, offset):
    offsetStr = "\x1b[{}C".format(offset)
    self.product().printShopDesc(offset)


def runShop(listings, shopName, color, player):
  # LISTINGS
  # [(item, price, oneTime), (item, price, oneTime), ...]
  clear()
  cursor.hide()
  
  printC('''\
 ╔═════════════════════════════════════╦═══════════════════════════════════════════════════════════╗
 ║                                     ║                                                           ║
 ║                                     ║                                                           ║
 ║                                     ║                                                           ║
 ║                                     ║                                                           ║
 ║                                     ║                                                           ║
 ║                                     ║                                                           ║
 ║                                     ║                                                           ║
 ║                                     ║                                                           ║
 ║                                     ║                                                           ║
 ║                                     ║                                                           ║
 ║                                     ║                                                           ║
 ║                                     ║                                                           ║
 ║                                     ║                                                           ║
 ║                                     ║                                                           ║
 ║                                     ╠═══════════════════════════════════════════════════════════╣
 ║                                     ║                                                           ║
 ║                                     ║                                                           ║
 ║                                     ║                                                           ║
 ║ |R|Press [X] to Exit Shop|--|              ║                                                           ║
 ╚═════════════════════════════════════╩═══════════════════════════════════════════════════════════╝''', color)
  
  converted = []
  for li in listings:
    li_item = li[0]
    li_price = li[1]
    li_oneTime = li[2]

    if li_oneTime:
      li_purchasable = True
      if li_item.objectType == "Item":
        li_purchasable = not player.hasItem(li_item)
      elif li_item.objectType == "Spell":
        li_purchasable = not player.hasSpell(li_item)
      elif li_item.objectType == "Wand":
        li_purchasable = not player.hasWand(li_item)

      converted.append(Listing(li_item, li_price, li_oneTime, li_purchasable))
    else:
      converted.append(Listing(li_item, li_price, li_oneTime, True))

  listings = converted

  printC("\x1b[3;4H" + shopName, color)
  printC("\x1b[3CYou have |W|{}|--| tickets.".format(player.tickets), color)
  print("\x1b[5;4H")

  firstListing = True
  for listing in listings:
    if firstListing:
      printC("\x1b[3C|PU|> " + listing.getName())
      firstListing = False
    else:
      printC("\x1b[3C  " + listing.getName())


  selectedListing = 0
  newSelectedListing = None

  while True:
    if newSelectedListing != selectedListing:
      if newSelectedListing != None:
        print("\x1b[{};3H  ".format(6+selectedListing))
        printC("\x1b[{};3H|PU| >".format(6+newSelectedListing))
      else:
        newSelectedListing = 0
      print("\x1b[2;1H")
      clearArea(14, 41, 58)
      print()
      clearArea(4, 41, 58)
      print("\x1b[2;1H")
      listing = listings[newSelectedListing]
      listing.printDesc(41)
      selectedListing = newSelectedListing
      print("\x1b[17H")

      if listing.purchasable:
        if not player.hasEnoughTickets(listing.price):
          printC("\x1b[41CYou cannot afford this! (You need {} more tickets.)".format(listing.price - player.tickets), "R")
        else:
          printC("\x1b[41CPress [ENTER] to buy this for {}T!".format(listing.price), "B")
      else:
        printC("\x1b[41CYou already own this item!", "R")
        
    choice = getkey()
    if choice in ["\x1b[A", "w"]:
      newSelectedListing = selectedListing - 1
      if newSelectedListing < 0:
        newSelectedListing = 0
      continue
    elif choice in ["\x1b[B", "s"]:
      newSelectedListing = selectedListing + 1
      if newSelectedListing >= len(listings):
        newSelectedListing = selectedListing
      continue
    elif choice == "\n":
      listing = listings[selectedListing]
      if listing.purchasable and player.hasEnoughTickets(listing.price):
        print("\x1b[17H")
        clearArea(4, 41, 58)
        print("\x1b[17H")
        printC("\x1b[41CBuy this for {} tickets?".format(listing.price), "B")
        printC("\x1b[41C|PU|> |R|Cancel")
        printC("\x1b[41C  |G|Confirm Purchase")
        selection = 0
        while True:
          choice = getkey()
          if choice in ["\x1b[A", "w"] and selection == 1:
            selection = 0
            print("\x1b[18H")
            printC("\x1b[41C|PU|> |R|Cancel")
            printC("\x1b[41C  |G|Confirm Purchase")
          elif choice in ["\x1b[B", "s"] and selection == 0:
            selection = 1
            print("\x1b[18H")
            printC("\x1b[41C  |R|Cancel")
            printC("\x1b[41C|PU|> |G|Confirm Purchase")
          elif choice == "x":
            return
          elif choice == "\n":
            break

        if selection == 0:
          print("\x1b[17H")
          clearArea(4, 41, 58)
          print("\x1b[17H")
          if listing.purchasable:
            if not player.hasEnoughTickets(listing.price):
              printC("\x1b[41CYou cannot afford this! (You need {} more tickets.)".format(listing.price - player.tickets), "R")
            else:
              printC("\x1b[41CPress [ENTER] to buy this for {}T!".format(listing.price), "B")
          else:
            printC("\x1b[41CYou already own this item!", "R")
        else:
          listing.buy(player)
          print("\x1b[17H")
          clearArea(4, 41, 58)
          print("\x1b[17H")
          printC("\x1b[41CPurchase Completed!", "G")
          if listing.purchasable:
            printC("\x1b[41CPress [ENTER] to buy this item again!", "B")
          else:
            printC("\x1b[{};3H|PU| > {}".format(6+selectedListing, listing.getName()))
          printC("\x1b[4;4HYou have |W|{}|--| tickets.     ".format(player.tickets), color)
          continue    
    elif choice == "x":
      print("\x1b[22;1H")
      return