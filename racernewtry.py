from string import ascii_uppercase
from random import random, randint, choice as randchoice
from random import uniform

TERRAINS = ["asphalt", "sand", "mud", "rocky"]
COMPLEXITIES = ["normal", "rapid", "subtle"]
carlist = []

class TrackPart:
    """a class to generate a part of a racetrack"""

    def __init__(self):
        self.length = randint(1,10)
        self.terrain = randchoice(TERRAINS)
        self.complexity = randchoice(COMPLEXITIES)
        

class Track:
    """a class to generate the entire racetrack"""

    def __init__(self):
        self.trackpart = []
        while len(self.trackpart)< 20:
            self.trackpart.append(TrackPart())
        
    def show_track(self):
        print("Using track:")
        for elt in self.trackpart:
            print(elt.terrain,elt.complexity, "(",elt.length,")", end = ",")

    
class Pilot:
    """a class to generate a pilot"""

    def __init__(self):
        self.name = randchoice(ascii_uppercase)
        self.normal_speed = uniform(0.5 , 1.5)
        self.rapid_speed = uniform(0.5 , 1.5)
        self.subtle_speed = uniform(0.5 , 1.5)

class Car:
    """a class to create a car with a pilot"""
    
    def __init__(self):
        self.name = randint(1,20)
        self.pilot = Pilot()
        self.asphalt_speed = uniform(0.5 , 1.5)
        self.sand_speed = uniform(0.5 , 1.5)
        self.mud_speed = uniform(0.5 , 1.5)
        self.rocky_speed = uniform(0.5 , 1.5)
        carlist.append(self)

    def show_car(self):
        print("Car", self.name, "with Pilot", self.pilot.name, end = " ; ")


    def time_for_part(self, i):
        timecar = 0
        if t.trackpart[i].terrain == "asphalt":
            timecar = self.asphalt_speed
        elif t.trackpart[i].terrain == "sand":
            timecar = self.sand_speed
        elif t.trackpart[i].terrain == "mud":
            timecar = self.mud_speed
        else:
            timecar = self.rocky_speed

        timepilot = 0
        if t.trackpart[i].complexity == "normal":
            timepilot = self.pilot.normal_speed
        elif t.trackpart[i].complexity == "rapid":
            timepilot = self.pilot.rapid_speed
        else:
            timepilot = self.pilot.subtle_speed

        timecarpilot = (timecar + timepilot)* t.trackpart[i].length
            
        return(timecarpilot)

    def time_for_track(self):
        time = 0
        i = 0
        while i < 20:
            self.time_for_part(i)
            time += self.time_for_part(i) 
            i += 1
        print(time)
            

t = Track()
t.show_track()
a = Car()
b = Car()
c = Car()
d = Car()
e = Car()
print("\nWith cars:")
for elt in carlist:
    elt.show_car()

print("\nThe times are:")
for elt in carlist:
    elt.show_car()
    elt.time_for_track()
