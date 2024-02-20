import cc_dat_utils

#Part 3
#Load your custom JSON file
#Convert JSON data to CCLevelPack
#Save converted data to DAT file

### Load custom JSON File
import cc_classes
import json

# Create CC Coordinates 
def createCoordinates(movingObsList):
    listForField = []
    for monsterList in movingObsList:
        newCoord = cc_classes.CCCoordinate( monsterList[0], monsterList[1] )
        listForField.append(newCoord)
    return listForField

# Create optional fields
def make_optional_fields(level, newLevel):        
    #Title field
    title = level["optional_fields"]["title"] 
    titleField = cc_classes.CCMapTitleField(title)
    #Password field 
    password = level["optional_fields"]["password"]
    passField = cc_classes.CCEncodedPasswordField(password)
    # Hint field
    hint = level["optional_fields"]["hint"]
    hintField = cc_classes.CCMapHintField(hint)
    # Moving objs field
    movingObjs = level["optional_fields"]["moving_objs"] # starting pos
    movingObjsField = cc_classes.CCMonsterMovementField( createCoordinates(movingObjs))
    # SET optional fields
    newLevel.optional_fields = [titleField,passField, hintField, movingObjsField]

#Creates and returns a LevelLibrary object(defined in own_levels) from loaded json_data
def make_level_library_from_json( json_data ):
    #Initialize a new LevelLibrary 
    level_library = cc_classes.CCLevelPack()

    #Loop through the json_data
    for level in json_data["Levels"]: 
        #Initialize a new level obj
        newLevel = cc_classes.CCLevel()
        #Create a new level object from the json_data by reading
        newLevel.level_number = level["level_num"]
        newLevel.time = level["time_lim"]
        newLevel.num_chips = level["chip_num"]
        newLevel.upper_layer = level["upper_layer"]
        newLevel.lower_layer = level["lower_layer"]
        make_optional_fields(level, newLevel)
        #Add that level object to the level_library
        level_library.add_level(newLevel)
    
    # print(level_library)
    return level_library #Return -> Converted JSON data to CCLevelPack 


#Assign file
input_json_file = "data/own_levels.json"

#Open the JSON file
with open(input_json_file, "r") as reader:
    #load the JSON data and store it in the variable family_json_data
    json_data = json.load(reader)
    levelLibrary = make_level_library_from_json(json_data)
    print('Done loading json files! Created levelLibrary')

    # make ccLevelPack into a dat file
    datFile = cc_dat_utils.write_cc_level_pack_to_dat(levelLibrary, "own_levels.dat")
    print(datFile)
    print('created dat file')

    #Use cc_dat_utils.make_cc_level_pack_from_dat() to load the file specified by input_dat_file - Used from pt1
    input_dat_file = "data/own_levels.dat"
    attemptLevel = cc_dat_utils.make_cc_level_pack_from_dat(input_dat_file) 
    # print(attemptLevel)
    print("END--------------------------------------------------------------------------------------------------")