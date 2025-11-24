
from animal import Animal

#Represents a bird in the zoo, extending the base animal class with bird-specific traits and behaviours.
class Bird(Animal):
    def __init__(self, name, species, age, diet="Omnivore"):
        super().__init__(name, species, age, category="Bird", diet=diet)

    def make_sound(self):
        return f"{self.name} the {self.species} chirps"
