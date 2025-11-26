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
##This sections is here for ensuring that an animal that in is enclosure, making sure that the animal is healthy and makes sure that it matches the enclosure's allowed animla type before it is added

    def add_animal(self, animal):
        if not animal.is_healthy():
            return f"{animal.name} cannot be moved; under treatment."

        if self.animal_type is None:
            self.animal_type = animal.category

        if animal.category != self.animal_type:
            return f"Cannot add {animal.name}. Only {self.animal_type} allowed."

        self.animals.append(animal)
        return f"{animal.name} added to {self.name}"

#These methods let the enclosure manage animals, stay clean, and provide a status report of its details and residents.
    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
            return f"{animal.name} removed from {self.name}"
        return f"{animal.name} not found in {self.name}"

    def list_animals(self):
        return [f"{a.name}({a.species})" for a in self.animals] if self.animals else []

    def clean(self):
        self.cleanliness = 100
        return f"{self.name} has been cleaned"

    def report_status(self):
        return {
            "name": self.name,
            "size": self.size,
            "environment": self.environment_type,
            "cleanliness": self.cleanliness,
            "animals": self.list_animals() if self.animals else "No animals"
        }