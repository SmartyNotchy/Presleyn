from imports import *

######################
## CUSTOM LOCATIONS ##
######################

# PROLOGUE LOCATIONS
setSimpleLocation("PROLOGUE_ENT", "PROLOGUE_AREA", 164)
createHorizHallway("PROLOGUE_SIDE", "PROLOGUE_AREA", [236, 244, 252])
createHorizHallway("PROLOGUE_SIDEWALK", "PROLOGUE_AREA", [308, 316, 324, 332, 340, 348])
connectVert("PROLOGUE_ENT", "PROLOGUE_SIDE_1", "PROLOGUE_SIDEWALK_3")
connectVert("PROLOGUE_SIDE_2", "PROLOGUE_SIDEWALK_4")
connectVert("PROLOGUE_SIDE_3", "PROLOGUE_SIDEWALK_5")

# MAIN ENTRANCE LOCATIONS
createVertHallway("ENTRANCE_HALLWAY", "MAIN_ENTRANCE", [156, 268, 444, 639, 837, 1035], start_idx = 3)
createHorizHallway("BAND_HALLWAY", "MAIN_ENTRANCE", [232, 238, 246, 251, 256, 262])
setSimpleLocation("CAFE_TOP_ENTRANCE", "MAIN_ENTRANCE", 422)
setSimpleLocation("IED_BAND_CONNECTOR_2", "MAIN_ENTRANCE", 126)

connectVert("BAND_HALLWAY_3", "CAFE_TOP_ENTRANCE")
connectHoriz("BAND_HALLWAY_6", "ENTRANCE_HALLWAY_4")
connectVert("IED_BAND_CONNECTOR_2", "BAND_HALLWAY_2")

# ELECTIVE HALLWAY LOCATIONS
createVertHallway("ART_HALLWAY", "HALLWAY_ELECTIVE", [229, 388, 525, 721])
createHorizHallway("CENTRAL_IED_CONNECTOR", "HALLWAY_ELECTIVE", [911, 917, 923, 929, 934])
setSimpleLocation("IED_BAND_CONNECTOR_1", "HALLWAY_ELECTIVE", 1041)
connectVert("ART_HALLWAY_4", "CENTRAL_IED_CONNECTOR_1", "IED_BAND_CONNECTOR_1", "IED_BAND_CONNECTOR_2")

# CENTRAL AREA LOCATIONS
setComplexLocation("ENTRANCE_HALLWAY_1", {"HALLWAY_ELECTIVE": 941, "HALLWAY_6": 1039})
setSimpleLocation("ENTRANCE_HALLWAY_2", "HALLWAY_ELECTIVE", 1071)
LOCATIONS["ENTRANCE_HALLWAY_2"].pos["HALLWAY_6"] = 1171
connectVert("ENTRANCE_HALLWAY_1", "ENTRANCE_HALLWAY_2", "ENTRANCE_HALLWAY_3")
connectHoriz("CENTRAL_IED_CONNECTOR_5", "ENTRANCE_HALLWAY_1")

# 6TH GRADE HALLWAY LOCATIONS
createVertHallway("HALLWAY_6_LEFT", "HALLWAY_6", [319, 591, 864])
createVertHallway("HALLWAY_6_RIGHT", "HALLWAY_6", [329, 601, 874])
createHorizHallway("CENTRAL_6_CONNECTOR", "HALLWAY_6", [1045, 1050, 1056, 1062, 1068, 1073, 1078])
setSimpleLocation("HALLWAY_6_TOP", "HALLWAY_6", 323)
setSimpleLocation("HALLWAY_6_LOWERSTAIRS", "HALLWAY_6", 1204)

connectHoriz("HALLWAY_6_LEFT_1", "HALLWAY_6_TOP", "HALLWAY_6_RIGHT_1")
connectHoriz("ENTRANCE_HALLWAY_1", "CENTRAL_6_CONNECTOR_1")
connectVert("HALLWAY_6_LEFT_3", "CENTRAL_6_CONNECTOR_5")
connectVert("CENTRAL_6_CONNECTOR_6", "HALLWAY_6_LOWERSTAIRS")
connectVert("HALLWAY_6_RIGHT_3", "CENTRAL_6_CONNECTOR_7")

# 7TH GRADE HALLWAY LOCATIONS
setSimpleLocation("HALLWAY_7_TOP", "HALLWAY_7", 310)
createVertHallway("HALLWAY_7_LEFT", "HALLWAY_7", [304, 470, 668, 847, 969, 1097])
createVertHallway("HALLWAY_7_RIGHT", "HALLWAY_7", [194, 314, 480, 678, 857, 979])
createHorizHallway("CENTRAL_7_CONNECTOR", "HALLWAY_7", [990, 999])

connectHoriz("HALLWAY_7_LEFT_1", "HALLWAY_7_TOP", "HALLWAY_7_RIGHT_2")
connectHoriz("HALLWAY_7_LEFT_5", "HALLWAY_7_RIGHT_6", "CENTRAL_7_CONNECTOR_1")
connectHoriz("HALLWAY_7_LEFT_6", "IED_BAND_CONNECTOR_1") # Elective-7 Stairs

# 8TH GRADE HALLWAY LOCATIONS
createVertHallway("HALLWAY_8_LEFT", "HALLWAY_8", [171, 299, 555, 812, 1004, 1128])
createVertHallway("HALLWAY_8_RIGHT", "HALLWAY_8", [309, 565, 822, 1014])
setSimpleLocation("HALLWAY_8_TOP", "HALLWAY_8", 303)
createHorizHallway("CENTRAL_8_CONNECTOR", "HALLWAY_8", [984, 993])

connectHoriz("HALLWAY_8_LEFT_2", "HALLWAY_8_TOP", "HALLWAY_8_RIGHT_1")
connectHoriz("CENTRAL_8_CONNECTOR_2", "HALLWAY_8_LEFT_5", "HALLWAY_8_RIGHT_4")

LOCATIONS["HALLWAY_8_LEFT_6"].locRight = "HALLWAY_6_LOWERSTAIRS"
LOCATIONS["HALLWAY_6_LOWERSTAIRS"].locRight = "HALLWAY_8_LEFT_6"
LOCATIONS["HALLWAY_8_TOP"].locUp = "HALLWAY_6_TOP"
LOCATIONS["HALLWAY_6_TOP"].locUp = "HALLWAY_8_TOP"

# GYM HALLWAY LOCATIONS
createVertHallway("HALLWAY_GYM_LEFT", "HALLWAY_GYM", [208, 365, 524])
createVertHallway("HALLWAY_GYM_RIGHT", "HALLWAY_GYM", [238, 395, 554])
setSimpleLocation("HALLWAY_GYM_OUTSIDE_EXIT", "HALLWAY_GYM", 243)
createHorizHallway("HALLWAY_GYM_BOTTOM", "HALLWAY_GYM", [532, 539, 546])

connectHoriz("HALLWAY_GYM_RIGHT_1", "HALLWAY_GYM_OUTSIDE_EXIT")
connectHoriz("HALLWAY_GYM_LEFT_3", "HALLWAY_GYM_BOTTOM_1")
connectHoriz("HALLWAY_GYM_BOTTOM_3", "HALLWAY_GYM_RIGHT_3")
connectVert("HALLWAY_8_LEFT_6", "HALLWAY_GYM_RIGHT_1")

LOCATIONS["HALLWAY_8_LEFT_6"].pos["HALLWAY_GYM"] = 134

# SCIENCE & CENTRAL HALLWAY
setComplexLocation("SCIENCE_HALLWAY_1", {"HALLWAY_7": 571, "HALLWAY_8": 527})
setComplexLocation("SCIENCE_HALLWAY_2", {"HALLWAY_7": 765, "HALLWAY_8": 720})
setComplexLocation("SCIENCE_HALLWAY_3", {"HALLWAY_7": 885, "HALLWAY_8": 848})
setComplexLocation("LOWER_CENTRAL_1", {"HALLWAY_7": 1007, "HALLWAY_8": 976})
setComplexLocation("LOWER_CENTRAL_2", {"HALLWAY_7": 1135, "HALLWAY_8": 1100, "HALLWAY_GYM": 106})
LOCATIONS["LOWER_CENTRAL_1"].section = "HALLWAY_8"
LOCATIONS["LOWER_CENTRAL_2"].section = "HALLWAY_8"

connectVert("SCIENCE_HALLWAY_1", "SCIENCE_HALLWAY_2", "SCIENCE_HALLWAY_3", "LOWER_CENTRAL_1", "LOWER_CENTRAL_2")
connectHoriz("CENTRAL_7_CONNECTOR_2", "LOWER_CENTRAL_1")
connectHoriz("LOWER_CENTRAL_1", "CENTRAL_8_CONNECTOR_1")
connectVert("LOWER_CENTRAL_2", "HALLWAY_GYM_LEFT_1")

LOCATIONS["ENTRANCE_HALLWAY_2"].locRight = "LOWER_CENTRAL_2"
LOCATIONS["LOWER_CENTRAL_2"].locRight = "ENTRANCE_HALLWAY_2"

# OUTSIDE SCHOOL ENTRANCE WAYPOINTS
setSimpleLocation("OUTSIDE_SCHOOL_ENT", "OUTSIDE_ENTRANCE", 164)
createHorizHallway("OUTSIDE_SCHOOL_SIDEBRANCH", "OUTSIDE_ENTRANCE", [236, 244, 252])
createHorizHallway("OUTSIDE_SCHOOL_SIDEWALK", "OUTSIDE_ENTRANCE", [308, 316, 324, 332, 340, 348])

connectVert("OUTSIDE_SCHOOL_ENT", "OUTSIDE_SCHOOL_SIDEBRANCH_1", "OUTSIDE_SCHOOL_SIDEWALK_3")
connectVert("OUTSIDE_SCHOOL_SIDEBRANCH_2", "OUTSIDE_SCHOOL_SIDEWALK_4")
connectVert("OUTSIDE_SCHOOL_SIDEBRANCH_3", "OUTSIDE_SCHOOL_SIDEWALK_5")

# CARPOOL WAYPOINTS
setSimpleLocation("OUTSIDE_SCHOOL_SIDEWALK_7", "CARPOOL_LANE", 396)

createVertHallway("CARPOOL_WALK", "CARPOOL_LANE", [67, 149, 238, 320, 402])

connectHoriz("OUTSIDE_SCHOOL_SIDEWALK_6", "OUTSIDE_SCHOOL_SIDEWALK_7", "CARPOOL_WALK_5")

# SIDE ENTRANCE WAYPOINTS
setSimpleLocation("OUTSIDE_SIDE_ENT", "SIDE_ENTRANCE", 101)
createVertHallway("OUTSIDE_LOCKER_PATHWAY", "SIDE_ENTRANCE", [106, 227, 312, 434])
createVertHallway("OUTSIDE_SIDE_PATHWAY", "SIDE_ENTRANCE", [74, 111, 167, 232, 317, 400, 478])

connectHoriz("OUTSIDE_SIDE_ENT", "OUTSIDE_LOCKER_PATHWAY_1", "OUTSIDE_SIDE_PATHWAY_2")
connectHoriz("OUTSIDE_LOCKER_PATHWAY_2", "OUTSIDE_SIDE_PATHWAY_4")
connectHoriz("OUTSIDE_LOCKER_PATHWAY_3", "OUTSIDE_SIDE_PATHWAY_5")

LOCATIONS["CARPOOL_WALK_1"].locUp = "OUTSIDE_SIDE_PATHWAY_7"

#connectVert("OUTSIDE_SIDE_PATHWAY_7", "CARPOOL_WALK_1")

# BLACKTOP WAYPOINTS

createVertHallway("BLACKTOP_PATHWAY", "BLACKTOP", [138, 217, 305, 387, 479, 564, 648])

connectVert("BLACKTOP_PATHWAY_7", "OUTSIDE_SIDE_PATHWAY_1")

# PROLOGUE AREA CLASSROOMS

classroomSetWaypoints(PrologueEntranceClassroom(), ["PROLOGUE_ENT"])

# MAIN ENTRANCE CLASSROOMS

classroomSetWaypoints(CafeteriaClassroom(), ["ENTRANCE_HALLWAY_7", "CAFE_TOP_ENTRANCE"])
classroomSetWaypoints(MainOfficeClassroom(), ["ENTRANCE_HALLWAY_8"])
classroomSetWaypoints(NursesOfficeClassroom(), ["ENTRANCE_HALLWAY_6"])
classroomSetWaypoints(Room241Classroom(), ["BAND_HALLWAY_6"])
classroomSetWaypoints(Room242Classroom(), ["BAND_HALLWAY_5"])
classroomSetWaypoints(Room246Classroom(), ["BAND_HALLWAY_3"])
classroomSetWaypoints(BuildingServicesClassroom(), ["BAND_HALLWAY_1"])
classroomSetWaypoints(SchoolExitClassroom(), ["ENTRANCE_HALLWAY_8", "OUTSIDE_SIDE_PATHWAY_7"])

# ELECTIVE HALL CLASSROOMS

classroomSetWaypoints(Room235Classroom(), ["CENTRAL_IED_CONNECTOR_1"])
classroomSetWaypoints(Room236AClassroom(), ["CENTRAL_IED_CONNECTOR_1"])
classroomSetWaypoints(Room236CClassroom(), ["ART_HALLWAY_3"])
classroomSetWaypoints(Room238Classroom(), ["ART_HALLWAY_3"])
classroomSetWaypoints(Room237BClassroom(), ["ART_HALLWAY_2"])
classroomSetWaypoints(Room239Classroom(), ["ART_HALLWAY_1"])
classroomSetWaypoints(Room240Classroom(), ["ART_HALLWAY_1"])

classroomSetWaypoints(Room234Classroom(), ["CENTRAL_IED_CONNECTOR_2"])
classroomSetWaypoints(Room232Classroom(), ["CENTRAL_IED_CONNECTOR_3"])
classroomSetWaypoints(Room230Classroom(), ["CENTRAL_IED_CONNECTOR_4"])

# UPPER FLOOR COMMON CLASSROOMS

classroomSetWaypoints(MediaCenterClassroom(), ["ENTRANCE_HALLWAY_1"])
classroomSetWaypoints(ElevatorClassroom(), ["ENTRANCE_HALLWAY_2", "LOWER_CENTRAL_2"])

# SIXTH GRADE HALLWAY CLASSROOMS

classroomSetWaypoints(Room225Classroom(), ["CENTRAL_6_CONNECTOR_3"])
classroomSetWaypoints(Room224Classroom(), ["HALLWAY_6_LEFT_3"])
classroomSetWaypoints(Room222Classroom(), ["HALLWAY_6_LEFT_2"])
classroomSetWaypoints(Room221Classroom(), ["HALLWAY_6_LEFT_1"])
classroomSetWaypoints(Room220Classroom(), ["HALLWAY_6_LEFT_1"])

classroomSetWaypoints(Room219Classroom(), ["HALLWAY_6_RIGHT_1"])
classroomSetWaypoints(Room218Classroom(), ["HALLWAY_6_RIGHT_1"])
classroomSetWaypoints(Room217Classroom(), ["HALLWAY_6_RIGHT_1"])
classroomSetWaypoints(Room216Classroom(), ["HALLWAY_6_RIGHT_2"])
classroomSetWaypoints(Room213Classroom(), ["HALLWAY_6_RIGHT_3"])
classroomSetWaypoints(Room211Classroom(), ["HALLWAY_6_RIGHT_3"])
classroomSetWaypoints(Room212Classroom(), ["CENTRAL_6_CONNECTOR_7"])

# LOWER FLOOR COMMON CLASSROOMS

classroomSetWaypoints(Room130Classroom(), ["SCIENCE_HALLWAY_1"])
classroomSetWaypoints(Room129Classroom(), ["SCIENCE_HALLWAY_1"])
classroomSetWaypoints(Room128Classroom(), ["SCIENCE_HALLWAY_2"])
classroomSetWaypoints(Room131Classroom(), ["SCIENCE_HALLWAY_2"])

# EIGHTH GRADE HALLWAY CLASSROOMS
classroomSetWaypoints(Room126Classroom(), ["CENTRAL_8_CONNECTOR_1"])
classroomSetWaypoints(Room125Classroom(), ["CENTRAL_8_CONNECTOR_2"])
classroomSetWaypoints(Room124Classroom(), ["HALLWAY_8_LEFT_4"])
classroomSetWaypoints(Room122Classroom(), ["HALLWAY_8_LEFT_3"])
classroomSetWaypoints(Room121Classroom(), ["HALLWAY_8_LEFT_2"])
classroomSetWaypoints(Room120Classroom(), ["HALLWAY_8_LEFT_1"])
classroomSetWaypoints(Room119Classroom(), ["HALLWAY_8_RIGHT_1"])
classroomSetWaypoints(Room118Classroom(), ["HALLWAY_8_RIGHT_1"])
classroomSetWaypoints(Room117Classroom(), ["HALLWAY_8_RIGHT_1"])
classroomSetWaypoints(Room116Classroom(), ["HALLWAY_8_RIGHT_2"])
classroomSetWaypoints(Room113Classroom(), ["HALLWAY_8_RIGHT_2"])
classroomSetWaypoints(Room112Classroom(), ["HALLWAY_8_RIGHT_3"])
classroomSetWaypoints(Room111Classroom(), ["HALLWAY_8_RIGHT_3"])

# SEVENTH GRADE HALLWAY CLASSROOMS

classroomSetWaypoints(Room136Classroom(), ["CENTRAL_7_CONNECTOR_2"])
classroomSetWaypoints(Room137Classroom(), ["CENTRAL_7_CONNECTOR_1"])
classroomSetWaypoints(Room140Classroom(), ["HALLWAY_7_RIGHT_6", "HALLWAY_7_RIGHT_5"])
classroomSetWaypoints(Room143Classroom(), ["HALLWAY_7_RIGHT_3"])
classroomSetWaypoints(Room145Classroom(), ["HALLWAY_7_RIGHT_2"])
classroomSetWaypoints(Room146Classroom(), ["HALLWAY_7_RIGHT_1"])

classroomSetWaypoints(Room147Classroom(), ["HALLWAY_7_LEFT_1"])
classroomSetWaypoints(Room148Classroom(), ["HALLWAY_7_LEFT_1"])
classroomSetWaypoints(Room149Classroom(), ["HALLWAY_7_LEFT_1"])
classroomSetWaypoints(Room150Classroom(), ["HALLWAY_7_LEFT_2"])
classroomSetWaypoints(Room154Classroom(), ["HALLWAY_7_LEFT_3"])
classroomSetWaypoints(Room155Classroom(), ["HALLWAY_7_LEFT_4", "HALLWAY_7_LEFT_5"])
classroomSetWaypoints(Room156Classroom(), ["HALLWAY_7_LEFT_6"])

# GYM HALLWAY CLASSROOMS

classroomSetWaypoints(MainGymClassroom(), ["HALLWAY_GYM_BOTTOM_1", "HALLWAY_GYM_BOTTOM_3", "HALLWAY_GYM_RIGHT_3", "HALLWAY_GYM_RIGHT_1", "HALLWAY_8_LEFT_6"])
classroomSetWaypoints(DanceStudioClassroom(), ["HALLWAY_GYM_LEFT_3", "HALLWAY_GYM_BOTTOM_1"])
classroomSetWaypoints(WeightRoomClassroom(), ["HALLWAY_GYM_BOTTOM_1", "HALLWAY_GYM_BOTTOM_2"])
classroomSetWaypoints(AuxiliaryGymClassroom(), ["HALLWAY_GYM_BOTTOM_2", "HALLWAY_GYM_BOTTOM_3"])
#classroomSetWaypoints(GirlsLockerInnerClassroom(), ["HALLWAY_GYM_RIGHT_3"])
#classroomSetWaypoints(BoysLockerInnerClassroom(), ["HALLWAY_GYM_RIGHT_2"])
classroomSetWaypoints(GreatOutdoorsEntranceClassroom(), ["HALLWAY_GYM_OUTSIDE_EXIT"])

# OUTSIDE HALLWAY CLASSROOMS

classroomSetWaypoints(OutsideMainEntranceClassroom(), ["OUTSIDE_SCHOOL_ENT"])
classroomSetWaypoints(GreatIndoorsEntranceClassroom(), ["OUTSIDE_SIDE_ENT"])
classroomSetWaypoints(DuckPondClassroom(), ["BLACKTOP_PATHWAY_7", "BLACKTOP_PATHWAY_6", "BLACKTOP_PATHWAY_5"])
classroomSetWaypoints(BlacktopClassroom(), ["BLACKTOP_PATHWAY_1", "BLACKTOP_PATHWAY_2", "BLACKTOP_PATHWAY_3", "BLACKTOP_PATHWAY_4"])
classroomSetWaypoints(GreenhouseClassroom(), ["OUTSIDE_SIDE_PATHWAY_3"])

# Greenhouse
# Pond
# Blacktop
# Great Outdoors Entrance
# Locker Rooms