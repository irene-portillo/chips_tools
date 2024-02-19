import cc_dat_utils

#Part 3
#Load your custom JSON file
#Convert JSON data to CCLevelPack
#Save converted data to DAT file



### Load custom JSON File --------------------------- CODE FROM PAST FILE, pt 2
import own_levels
import json

#Creates and returns a LevelLibrary object(defined in own_levels) from loaded json_data
def make_level_library_from_json( json_data ):
    
    #Initialize a new LevelLibrary - aka create LevelLibrary obj
    level_library = own_levels.LevelLibrary()

    #Loop through the json_data
    for level in json_data["Levels"]: 
        #Create a new level object from the json_data by reading
        num = level["level_num"]
        timeLim = level["time_lim"]
        chips = level["chip_num"]
        upperLayer = level["upper_layer"]
        lowerLayer = level["lower_layer"]
        #Optional fields
        title = level["optional_fields"]["title"]
        password = level["optional_fields"]["password"]
        hint = level["optional_fields"]["hint"]
        movingObjs = level["optional_fields"]["moving_objs"]

        #Create the level obj
        new_level_obj = own_levels.Level(num, timeLim, chips, upperLayer, lowerLayer, title, password, hint, movingObjs)
        
        #Add that level object to the level_library
        level_library.add_level(new_level_obj)


    return level_library

#Assign file
input_json_file = "data/own_levels.json"

#Open the JSON file
with open(input_json_file, "r") as reader:
    #load the JSON data and store it in the variable family_json_data
    json_data = json.load(reader)
    var = make_level_library_from_json(json_data)
    print(var)

print('Done loading json files!')

#Convert JSON data to CCLevelPack -----------------------------------------CODE FROM PAST FILE, pt 1 
input_dat_file = "data/own_levels.dat"## how do i make this???????????

#Use cc_dat_utils.make_cc_level_pack_from_dat() to load the file specified by input_dat_file
# level = cc_dat_utils.make_cc_level_pack_from_dat(input_dat_file) 
# print(level)