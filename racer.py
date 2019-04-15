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

    def show_part(self):
        return(TrackPart().complexity +" "+ TrackPart().terrain + " "  + "(" + str(TrackPart().length) + ")" + " + ")
        
   

class Track(TrackPart):
    """This class is adding parts to generate a complete track.
        there are 20 parts originally"""


    def __init__(self):
        self.parts = []            


    def add_parts(self):
        for i in range(20):
            self.parts.append(TrackPart())
           
        for elt in self.parts:
            print(elt.show_part(), end = ' ')

class Pilot:
    """This class creates a pilot"""

    def __init__(self):
        self.name = randchoice(ascii_uppercase)
        self.normal_speed = uniform(0.5, 1.5)
        self.rapid_speed = uniform(0.5, 1.5)
        self.subtle_speed = uniform(0.5, 1.5)

    def show_pilot(self):
        print ("\nPilot", self.name)

    def pilot_speed(self):
        speed = 0
        if TrackPart().complexity == "normal":
            speed = self.normal_speed
        if TrackPart().complexity == "rapid":
            speed = self.rapid_speed
        if TrackPart().complexity == "subtle":
            speed = self.subtle_speed
        return speed

class Car(Pilot):
    """This class creates a car"""

    def __init__(self):
        self.carname = randint(0,20)
        self.asphalt_speed = uniform(0.5, 1.5)
        self.sand_speed = uniform(0.5, 1.5)
        self.mud_speed = uniform(0.5, 1.5)
        self.rocky_speed = uniform(0.5, 1.5)
        self.list_car_pilots = []

    def show_car_pilot(self):
        print("Car", self.carname, "with Pilot", Pilot().name)
     

    def add_contestants(self):
        print("\nThe contestants are:")
        for i in range(5):
            self.list_car_pilots.append(Car())
                        
        for pc in self.list_car_pilots:
            pc.show_car_pilot()

    def car_speed(self):
        cspeed = 0
        if TrackPart().terrain == "asphalt":
            cspeed = self.asphalt_speed
        if TrackPart().terrain == "sand":
            cspeed = self.sand_speed
        if TrackPart().terrain == "mud":
            cspeed = self.mud_speed
        if TrackPart().terrain == "rocky":
            cspeed = self.rocky_speed
        return cspeed

    
if __name__ == '__main__':
    Track().add_parts()
    Car().add_contestants()
    


        
        

    



