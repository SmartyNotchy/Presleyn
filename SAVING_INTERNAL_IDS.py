from imports import *


# Wand IDs:                0000 + <#>
# Spell IDs:               1000 + <#>
# Battle Item IDs:         2000 + <#>
# Overworld Item IDs:      3000 + <#>
# Colllectible Item IDs:   4000 + <#>
# Quest IDs:               5000 + <#>
# Email IDs:               6000 + <#>
# Scroll IDs:              7000 + <#>

INTERNAL_IDS = {
  0: None,
  
  1: FeldsparWand(),
  2: RubyWand(),
  3: SapphireWand(),
  4: EmeraldWand(),
  5: AmethystWand(),
  6: OpalWand(),
  
  1001: AadhavanSpell(),
  1002: AaryaSpell(),
  1003: AkashSpell(),
  1004: AkshajSpell(),
  1005: AnkushSpell(),
  1006: AnnaSpell(),
  1007: AriamSpell(),
  1008: ArjunSpell(),
  1009: BenedicteSpell(),
  1010: BrandonTSpell(),
  1011: BrandonVSpell(),
  1012: BrookeSpell(),
  1013: BryceSpell(),
  1014: CalebSpell(),
  1015: ChaseSpell(),
  1016: ChrisSpell(),
  1017: DanielSpell(),
  1018: DashaSpell(),
  1019: DonSpell(),
  1020: EdemSpell(),
  1021: EllaSpell(),
  1022: EllieSpell(),
  1023: GabrielleSpell(),
  1024: GloriaSpell(),
  1025: GoranSpell(),
  1026: HenrySpell(),
  1027: JaniyahSpell(),
  1028: JashleeSpell(),
  1029: JessikaSpell(),
  1030: JustinSpell(),
  1031: KatherineSpell(),
  1032: KedusSpell(),
  1033: KhangSpell(),
  1034: KrishanSpell(),
#  1035: LeeSpell(), (Unused)
  1036: LillianSpell(),
  1037: LukeSpell(),
  1038: MayaSpell(),
  1039: NathanSpell(),
  1040: OmkarSpell(),
  1041: PercySpell(),
  1042: PeterSpell(),
  1043: PilliamSpell(),
  1044: PoorviSpell(),
#  1045: PresleySpell(), (Unused)
  1046: PrestonSpell(),
  1047: RachelSpell(),
  1048: RoselynSpell(),
  1049: RyanSpell(),
  1050: SayfSpell(),
  1051: SergiSpell(),
  1052: ShameerSpell(),
  1053: SherrySpell(),
  1054: ShriramSpell(),
  1055: SofyaSpell(),
  1056: SriSpell(),
  1057: TerenceSpell(),
  1058: TylerSpell(),
  1059: ValeriaSpell(),
  1060: WilliamSpell(),
  1061: YuliaSpell(),
  1069: DebugSpell(),
  
  2001: StrawberryShakeItem,
  2002: TectonicSnacksItem,
  2003: PopcornItem,
  2004: SmoresItem,
  2005: CokeSodaItem,
  2006: OrangeFantaSodaItem,
  2007: PineappleFantaSodaItem,
  2008: SpriteSodaItem,
  2009: IcedTeaSodaItem,
  2010: LifeformAnalyzerItem,

  3001: ChobaniYogurtItem,
  3002: PaperclipItem,
  3003: HalfRippedPosterItem,
  3004: MasterKeysItem,
  3005: SSLFormsItem,
  3006: OrangeEcherviaSucculentItem,
  3007: AloeVeraSucculentItem,
  3008: LavenderEcherviaSucculentItem,
  3009: MoonCactusSucculentItem,
  3010: StrawberrySempervivumSucculentItem,
  3011: RedEcherviaSucculentItem,
  3012: BurrosTailSucculentItem,
  3013: WhiteHaworthiaSucculentItem,
  3014: BallCactusSucculentItem,
  3015: SpeedcubeLubeItem,
  3016: TeachersPassItem,
  3017: GymKeysItem,
  3018: TableTennisPaddleItem,
  3019: ShreddedSSLFormsItem,
  3020: StolenFurryBookItem,

  4001: RedCrayonItem,
  4002: OrangeCrayonItem,
  4003: YellowCrayonItem,
  4004: GreenCrayonItem,
  4005: BlueCrayonItem,
  4006: PurpleCrayonItem,
  4007: BrownCrayonItem,
  
  5001: IronicCriminalPursuitQuest,
  5002: OverdueSSLFormsQuest,
  5003: SucculentQuest,
  5004: GrammarCheckerQuest,
  5005: TableTennisQuest,
  
  6001: WelcomeToClementeEmail,
  6002: IEDOverdoseEmail,
  6003: PoolesvilleAcceptanceEmail,
  6004: MESAEmail,
  6005: MESAFollowUpEmail,
  6006: RainbowHawksEmail,
  6007: CodeHSAnswersEmail,
  6008: AssignmentGradedEmail,
  6009: RCMSLoreEmail,
  6010: WantedCriminalEmail,
  6011: BaldastanEmail,
  6012: NameChangeEmail,
  6013: NursesOfficeEmail,
  6014: BrainSTEMOrderEmail,
  6015: BrainSTEMOrderFollowUpEmail,
  
  7001: ScrollOfSupportItem,
  7002: ScrollOfDiversityItem,
  7003: ScrollOfPresenceItem,
  7004: ScrollOfCompassionItem,
  7005: ScrollOfOwnershipItem,
  7006: ScrollOfWellbeingItem,
  7007: ScrollOfEqualityItem,

}

# TODO: Rename ContentError to ContentError


def getID(thing):
  # Hi Ms. Ramasamy, please don't dock points for this monstrosity of a function thank you so much ^_^
  for key, val in INTERNAL_IDS.items():
    try:
      if val.name == thing.name:
        return int(key)
    except:
      try:
        if val(0, False).name == thing.name:
          return int(key)
      except:
        try:
          if val(False, False).subject == thing.subject:
            return int(key)
        except:
          try:
            if val(0).name == thing.name:
              return int(key)
          except:
            try:
              assert val == None
              if thing == None:
                return 0
            except:
              # Omar balenciaga moment
              # also we have so much rnaodm comments in this game that ms. ramamsamy might find and be like -_-

              # raise ContentError()
              
              pass

  clear()
  printC("Couldn't find an ID for " + str(thing))
  print()
  raise ContentError()
