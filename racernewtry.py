"""Project racer"""

from string import ascii_uppercase
from random import random, randint, choice as randchoice
from random import uniform

TERRAINS = ["asphalt", "sand", "mud", "rocky"]
COMPLEXITIES = ["normal", "rapid", "subtle"]
carlist = []
times = []

class TrackPart:
    """a class to generate a part of a racetrack"""

    def __init__(self):
        self.length = randint(1, 10)
        self.terrain = randchoice(TERRAINS)
        self.complexity = randchoice(COMPLEXITIES)

class Track:
    """a class to generate the entire racetrack"""

    def __init__(self):
        self.trackpart = []
        while len(self.trackpart) < 20:
            self.trackpart.append(TrackPart())

    def __repr__(self):
        for elt in self.trackpart:
            return"{} {} ({})".format(elt.terrain, elt.complexity, elt.length)

class Pilot:
    """a class to generate a pilot"""

    def __init__(self):
        self.name = randchoice(ascii_uppercase)
        self.normal_speed = uniform(0.5, 1.5)
        self.rapid_speed = uniform(0.5, 1.5)
        self.subtle_speed = uniform(0.5, 1.5)

class Car:
    """a class to create a car with a pilot"""

    def __init__(self):
        self.name = randint(1, 20)
        self.pilot = Pilot()
        self.asphalt_speed = uniform(0.5, 1.5)
        self.sand_speed = uniform(0.5, 1.5)
        self.mud_speed = uniform(0.5, 1.5)
        self.rocky_speed = uniform(0.5, 1.5)
        carlist.append(self)

    def show_car(self):
        return"Car {} with pilot {}" .format(self.name, self.pilot.name)


    def time_for_part(self, trackpart):
        timecar = 0
        if trackpart.terrain == "asphalt":
            timecar = self.asphalt_speed
        elif trackpart.terrain == "sand":
            timecar = self.sand_speed
        elif trackpart.terrain == "mud":
            timecar = self.mud_speed
        else:
            timecar = self.rocky_speed

        timepilot = 0
        if trackpart.complexity == "normal":
            timepilot = self.pilot.normal_speed
        elif trackpart.complexity == "rapid":
            timepilot = self.pilot.rapid_speed
        else:
            timepilot = self.pilot.subtle_speed

        timecarpilot = (timecar + timepilot)* trackpart.length

        return timecarpilot

    def time_for_track(self, track):
        time = 0
        for trackpart in track.trackpart:
            time += self.time_for_part(trackpart)
            return time

t = Track()
print(t)
a = Car()
b = Car()
c = Car()
d = Car()
e = Car()
for elt in carlist:
    print(elt.show_car())

times = [[elt.show_car(), elt.time_for_track(t)] for elt in carlist]
print("The times are :", times)
times.sort(key=lambda x: x[1])
print("The winner is", times[0])