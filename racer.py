from string import ascii_uppercase
from random import random, randint, choice as randchoice
from random import uniform

TERRAINS = ["asphalt", "sand", "mud", "rocky"]
COMPLEXITIES = ["normal", "rapid", "subtle"]



print("              Welcome, let's plays racer!!\n\n")


class TrackPart:
    """This class is going to generate a part of the final racetrack"""

    
    def __init__(self):
        self.length = randint(1,10)
        self.terrain = randchoice(TERRAINS)
        self.complexity = randchoice(COMPLEXITIES)
        

class Track:
    """This class is adding parts to generate a complete track."""




class Pilot:
    """This class creates a pilot"""

    def __init__(self):
        self.name = randchoice(ascii_uppercase)
        self.normal_speed = uniform(0.5, 1.5)
        self.rapid_speed = uniform(0.5, 1.5)
        self.subtle_speed = uniform(0.5, 1.5)

   

    

class Car:
    """This class creates a car"""

    def __init__(self):
        self.carname = randint(0,20)
        self.asphalt_speed = uniform(0.5, 1.5)
        self.sand_speed = uniform(0.5, 1.5)
        self.mud_speed = uniform(0.5, 1.5)
        self.rocky_speed = uniform(0.5, 1.5)
        self.cars = []

      

if __name__ == '__main__':

    
   
