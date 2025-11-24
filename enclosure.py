'''
File: enclosure.py
Author: Abhinav Sharma
ID: 110376072
Username: shaay186
This is my own work as defined by the University's Academic Integrity Policy.
'''

#Representing a habitat in the zoo for managing the environment, cleanliness, and making sure that only compatible animals are housed inside.

class Enclosure:
    def __init__(self, name, size, environment_type, animal_type=None, cleanliness=100):
        self.name = name
        self.size = size
        self.environment_type = environment_type
        self.cleanliness = cleanliness
        self.animals = []
        self.animal_type = animal_type