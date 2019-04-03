from string import ascii_uppercase
from random import random, randint, choice as randchoice
from random import uniform

TERRAINS = ["asphalt", "sand", "mud", "rocky"]
COMPLEXITIES = ["normal", "rapid", "subtle"]



class TrackPart:
    """This class is going to generate a part of the final racetrack"""

    
    def __init__(self):
        self.length = randint(1,10)
        self.terrain = randchoice(TERRAINS)
        self.complexity = randchoice(COMPLEXITIES)

    def __str__(self):
        return "{} {} {}".format(self.terrain, self.complexity, self.length)

        
   

class Track(TrackPart):
    """This class is creating the racetrack by adding 20 parts from TrackPart"""

    def __init__(self):
        TrackPart.__init__(self)

parts = []

for p in range(0,20):
    parts.append(str(Track()))
   
print ("using track"," + ".join(parts))
    

       
