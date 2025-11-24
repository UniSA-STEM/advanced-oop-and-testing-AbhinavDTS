

#Represents a mammal in the zoo and customises the base animal behaviours to suit mammal-specific traits.

from animal import Animal

class Mammal(Animal):
    def __init__(self, name, species, age, diet="Omnivore"):
        super().__init__(name, species, age, category="Mammal", diet=diet)

    def make_sound(self):
        return f"{self.name} the {self.species} makes a mammal sound"
