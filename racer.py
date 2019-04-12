from string import ascii_uppercase
from random import random, randint, choice as randchoice
from random import uniform

TERRAINS = ["asphalt", "sand", "mud", "rocky"]
COMPLEXITIES = ["normal", "rapid", "subtle"]

list_car_pilots = []


print("              Welcome, let's plays racer!!\n\n")


class TrackPart:
    """This class is going to generate a part of the final racetrack"""

    
    def __init__(self):
        self.length = randint(1,10)
        self.terrain = randchoice(TERRAINS)
        self.complexity = randchoice(COMPLEXITIES)
        
   

class Track(TrackPart):
    """This class is adding parts to generate a complete track.
        there are 20 parts originally"""


    def __init__(self):
        self.parts = []            


    def add_parts(self):
        for i in range(20):
            self.parts.append(Track())
           
        for elt in self.parts:
            print(elt.show_part(), end = ' + ' )

    def show_part(self):
        return(TrackPart().complexity +" "+ TrackPart().terrain + " "  + "(" + str(TrackPart().length) + ")")
            
     
t = Track()
print("Using track:\n")
t.add_parts()

class Pilot:
    """This class creates a pilot"""

    def __init__(self):
        self.name = randchoice(ascii_uppercase)
        self.normal_speed = uniform(0.5, 1.5)
        self.rapid_speed = uniform(0.5, 1.5)
        self.subtle_speed = uniform(0.5, 1.5)

        

class Car(Pilot):
    """This class creates a car"""

    def __init__(self):
        Pilot.__init__(self)
        self.carname = randint(0,20)
        self.asphalt_speed = uniform(0.5, 1.5)
        self.sand_speed = uniform(0.5, 1.5)
        self.mud_speed = uniform(0.5, 1.5)
        self.rocky_speed = uniform(0.5, 1.5)

    def pilot_car(self):
        for i in range(5):
            list_car_pilots.append(Car())
            
        for pc in list_car_pilots:
            print("Car ",pc.carname, "with pilot", pc.name, end = " ; ")
       
            

print("\n\nThe contestants are:\n")
p = Car()
p.pilot_car()

        
        

    



