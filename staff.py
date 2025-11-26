'''
File: staff.py
Author: Abhinav Sharma
ID: 110376072
Username: shaay186
This is my own work as defined by the University's Academic Integrity Policy.
'''


# The Staff class represents a zoo staff member, storing their name and role, and allowing them to be assigned to specific animals and enclosures.
class Staff:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.assigned_animals = []
        self.assigned_enclosures = []

    def assign_animal(self, animal):
        self.assigned_animals.append(animal)

    def assign_enclosure(self, enclosure):
        self.assigned_enclosures.append(enclosure)
