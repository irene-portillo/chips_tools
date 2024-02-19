# CLASSES
# For building level, python

class Level:
    # num
    # time
    # chips
    # upperLayer
    # lowerLayer

    # title
    # password 
    # hint
    # movingObjs
    def __init__(self, num, timeLim, chips, upperLayer, lowerLayer, title='Unamed', password=None, hint='No hint', movingObjs=[]):
        self.num = num
        self.timeLim = timeLim
        self.chips = chips
        self.upperLayer = upperLayer 
        self.lowerLayer = lowerLayer 

        #fields
        self.title = title
        self.password = password
        self.hint = hint
        self.movingObjs = movingObjs 

class LevelLibrary:
    def __init__(self):
        self.levels = []

    def add_level(self, level):
        self.levels.append(level)

    def __str__(self):
        return_str = "Analyzing level library data:\n"
        for level in self.levels:            
            return_str += f"\tLevel {level.num}\n"
            return_str += f"\t\ttime Limit  = {level.timeLim}\n"
            return_str += f"\t\tChips  = {level.chips}\n"
            # return_str += f"\t\tUpperLayer  = {level.upperLayer}\n"
            # return_str += f"\t\t\tLowerLayer  = {level.lowerLayer}\n"

            return_str += "\t\tOptional Fields:" + "\n"
            return_str += f"\t\t\tTitle  = {level.title}\n"
            return_str += f"\t\t\tPassword  = {level.password}\n"
            return_str += f"\t\t\tHint  = {level.hint}\n"
            return_str += f"\t\t\tMoving Objs  = {level.movingObjs}\n"
            
        return return_str
