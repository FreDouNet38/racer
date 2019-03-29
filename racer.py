from string import ascii_uppercase
from random import random, randint, choice as randchoice
from random import uniform

TERRAINS = ["asphalt", "sand", "mud", "rocky"]
COMPLEXITIES = ["normal", "rapid", "subtle"]

class TrackPart:
    """This class is going to generate a part of the final racetrack"""

    
    def __init__(self,length,terrain,complexity):
        self.lenght = random.randint(0,10)
        self.terrain = random.randchoice(TERRAINS) #faut-il l'écrire autrement par exemple TERRAINS[]
        self.complexity = random.randchoice(COMPLEXITIES)

#j'aimerai retourner une trackpart = complexity terrain (length)
        

class Track:
    """This class is creating the racetrack by adding 20 parts from TrackPart"""

    def __init__(self):
        track = []
        for i in range(20):
        track.append     #je voudrai que la fonction fasse une liste de 20 parts depuis TrackPart
                        #il va y avoir le print ici

class Pilot:
    """This class create a pilot"""

    def __init__(self, name, normal_speed, rapid_speed, subtle_speed):
        self.name = random.choice(ascii_uppercase)
        self.normal_speed = uniform(0.5, 1.5)
        self.rapid_speed = uniform(0.5, 1.5)
        self.subtle_speed = uniform(0.5, 1.5)
        
    pilot = Pilot() #je voudrai que cela crée un pilote au hasard

        
class Car:
    """This class create a car"""

    def __init__(self, name, pilot, asphalt_speed, sand_speed, mud_speed, rocky_speed):
        self.name = random.randint(0,20)
        self.pilot = pilot
        self.asphalt_speed = uniform(0.5, 1.5)
        self.sand_speed = uniform(0.5, 1.5)
        self.mud_speed = uniform(0.5, 1.5)
        self.rocky_speed = uniform(0.5, 1.5)
    
    #pareil je ne sais pas comment retourner ma voiture
        
