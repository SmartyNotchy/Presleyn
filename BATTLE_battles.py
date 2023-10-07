from imports import *


def buildHealthBar(hp, maxHP, reversed):
  bars = int(hp / maxHP * 10)
  if bars == 0 and hp > 0:
    bars = 1
  elif hp <= 0:
    bars = 0

  if reversed:
    return "|W|[|DG|" + "-" * (10 - bars) + "|R|" + "=" * bars + "|W|]"

  return "|W|[|R|" + "=" * bars + "|DG|" + "-" * (10 - bars) + "|W|]"


def printBattleHeader(player, enemy):
  MODERN = True

  playerName = player.getName()
  enemyName = enemy.getName()
  playerHPBar = buildHealthBar(player.health, player.maxHealth, False)
  enemyHPBar = buildHealthBar(enemy.health, enemy.maxHealth, True)
  playerHealthStat = "{}/{}".format(player.health, player.maxHealth)
  enemyHealthStat = "{}/{}".format(enemy.health,
                                   enemy.maxHealth)  #hi pill the will johnson
  playerShieldStat = "{}% Shield".format(round(100 * (player.shield - 1)))
  enemyShieldStat = "{}% Shield".format(round(100 * (enemy.shield - 1)))
  playerBoostStat = "{}% Boost".format(round(100 * (player.boost - 1)))
  enemyBoostStat = "{}% Boost".format(round(100 * (enemy.boost - 1)))

  if MODERN:
    printC("\n╔" + "═" * 62 + "╗", "B")
    printC("|B|║ " + playerName + " " * (25 - len(player.name)) + "|B|/" +
           " " * (28 - len(enemy.name)) + enemyName + " |B|║")
    printC(
      "║ " + playerHPBar + " " * 18 + "|B|/" + " " * 17 + enemyHPBar + " |B|║",
      "B")
    printC(
      "║ |R|{}".format(playerHealthStat) + " " * (29 - len(playerHealthStat)) +
      "vs" + " " * (29 - len(enemyHealthStat)) +
      "|R|{}|B| ║".format(enemyHealthStat), "B")
    printC(
      "║ |G|{}".format(playerShieldStat) + " " * (29 - len(playerShieldStat)) +
      "|B|/" + " " * (30 - len(enemyShieldStat)) +
      "|G|{}|B| ║".format(enemyShieldStat), "B")
    printC(
      "║ |Y|{}".format(playerBoostStat) + " " * (28 - len(playerBoostStat)) +
      "|B|/" + " " * (31 - len(enemyBoostStat)) +
      "|Y|{}|B| ║".format(enemyBoostStat), "B")
    printC("╚" + "═" * 62 + "╝", "B")
  '''
  else:
    printC("\n║" + "=" * 62 + "║", "B")
    printC("║ " + playerName + " " * (31-len(player.name)-3*len(player.effects)) + "/" + " " * (28-len(enemy.name)-3*len(enemy.effects)) + enemyName + " ║", "B")
    printC("║ " + playerHPBar + " " * 18 + "/" + " " * 17 + enemyHPBar + " ║", "B")
    printC("║ |R|{}|R|".format(playerHealthStat) + " " * (29-len(playerHealthStat)) + "vs" + " " * (29-len(enemyHealthStat)) + "|R|{}|R| ║".format(enemyHealthStat), "B")
    printC("║ |G|{}|G|".format(playerShieldStat) + " " * (29-len(playerShieldStat)) + "/" + " " * (30-len(enemyShieldStat)) + "|G|{}|G| ║".format(enemyShieldStat), "B")
    printC("║ |PI|{}|PI|".format(playerBoostStat) + " " * (28-len(playerBoostStat)) + "/" + " " * (31-len(enemyBoostStat)) + "|PI|{}|PI| ║".format(enemyBoostStat), "B")
    printC("║" + "=" * 62 + "║", "B")'''

BATTLE_SCROLLS = {
  ScrollOfSupportItem: 20,
  ScrollOfDiversityItem: 30,
  ScrollOfPresenceItem: 50,
  ScrollOfCompassionItem: 50,
  ScrollOfOwnershipItem: 50,
  ScrollOfWellbeingItem: 100,
  ScrollOfEqualityItem: 100
}

def runBattle(player, enemy, defaultDeath=True):
  battlePlayer = BattlePlayer()
  battlePlayer.name = player.name
  battlePlayer.nameColor = player.nameColor
  battlePlayer.selectedWand = player.selectedWand
  battlePlayer.arsenal = player.arsenal
  battlePlayer.health = player.health

  for pair in BATTLE_SCROLLS.items():
    if player.hasItem(pair[0]):
      battlePlayer.maxHealth += pair[1]
  #battlePlayer.health = battlePlayer.maxHealth
  
  for player_item in player.items:
    if player_item.type == 0:
      battlePlayer.items.append(player_item)
      player.items.remove(player_item)

  mapPlayer = player
  player = battlePlayer

  clear()
  printBattleHeader(player, enemy)
  print()
  enemy.onBattleStart()
  player.selectedWand.onBattleStart(player, enemy)
  enemy.selectedWand.onBattleStart(enemy, player)
  flush_input()
  enter()
  clear()

  while True:
    printBattleHeader(player, enemy)
    if not player.update():
      print()
      printC("You lost the battle!", "R")
      flush_input()
      enter()
      if defaultDeath:
        mapPlayer.perish()

      for item in battlePlayer.items:
        mapPlayer.items.append(item)
        
      return False
    elif not enemy.update():
      print()
      printC("You won the battle!", "G")
      healed = int(player.maxHealth / 4)
      player.health += healed
      if player.health > player.maxHealth:
        healed -= (player.health - player.maxHealth)
        player.health = player.maxHealth
      if healed != 0:
        printC("The victory empowers you, healing you for |R|{}|B| health!".format(healed), "B")
      flush_input()
      enter()

      for item in battlePlayer.items:
        mapPlayer.items.append(item)
      
      mapPlayer.health = player.health
      return True

    if not player.attack(enemy):
      flush_input()
      enter()
      clear()
      continue

    flush_input()
    enter()

    if not enemy.update():
      clear()
      continue

    print()
    enemy.attack(player)

    enter()
    clear()

    player.update()
    enemy.update()
