

#Represents a reptile in the zoo, building on the base animal class with reptile-specific characteristics and behaviour.

from animal import Animal
class Reptile(Animal):
    def __init__(self, name, species, age, diet="Carnivore"):
        super().__init__(name, species, age, category="Reptile", diet=diet)

    def make_sound(self):
        return f"{self.name} the {self.species} hisses"

