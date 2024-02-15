import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    
    #Initialize a new GameLibrary - aka create GameLibrary obj
    game_library = test_data.GameLibrary()

    print('code running...')

    #Loop through the json_data
    for game in json_data: # shouldn't this be looping through test_data since it holds the games?
        #Create a new Game object from the json_data by reading
        print(game)

        #Get platform info seperately (which requires reading name and launch_year)
        launch_yr = game["platform"]["launch year"]
        plat_name = game["platform"]["name"]
        curr_plat = test_data.Platform(plat_name, launch_yr) 
        #Create the game obj
        new_game_obj = test_data.Game( game["title"], curr_plat, game["year"])
        #Add that Game object to the game_library
        game_library.add_game(new_game_obj)
    
    ### End Add Code Here ### -- not sure what's supposed to go on here
    return game_library


#Part 2
input_json_file = "data/test_data.json"

### Begin Add Code Here ###
#Open the file specified by input_json_file
#Use the json module to load the data from the file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print()
### End Add Code Here ###

#Open the JSON file
with open(input_json_file, "r") as reader:
    #load the JSON data and store it in the variable family_json_data
    json_data = json.load(reader)
    test_var = make_game_library_from_json(json_data)
    print(test_var)
