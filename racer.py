from string import ascii_uppercase
from random import random, randint, choice as randchoice
from random import uniform

TERRAINS = ["asphalt", "sand", "mud", "rocky"]
COMPLEXITIES = ["normal", "rapid", "subtle"]

list_parts = []

class TrackPart:
    """This class is going to generate a part of the final racetrack"""

    
    def __init__(self):
        self.length = randint(1,10)
        self.terrain = randchoice(TERRAINS)
        self.complexity = randchoice(COMPLEXITIES)
        
   

class Track:
    """This class is adding parts to generate a complete track.
        there are 20 parts originally"""


    def __init__(self, parts = 20):
        TrackPart.__init__(self)
        self.parts = parts    

    def show_part(self):
        return(self.complexity +" "+ self.terrain + " "  + "(" + str(self.length) + ")")

    def add_parts(self):
        for i in range(0, self.parts):
            list_parts.append(Track())
           
        for elt in list_parts:
            print(elt.show_part(), end = ' + ')
     
t = Track()
print(t.add_parts())



