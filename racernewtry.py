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
        self.track = []
        while len(self.track)< 20:
            self.track.append(TrackPart())

    def show_track(self):
        for elt in self.track:
            print(elt.terrain, elt.complexity,"(",elt.length,")",  end = " , ")
        
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
        print("Car", self.name, "with Pilot", self.pilot.name)
        
t = Track()
t.show_track()
a = Car()
b = Car()
c = Car()
d = Car()
e = Car()

for elt in carlist:
    elt.show_car()
