'''
File: main.py
Author: Abhinav Sharma
ID: 110376072
Username: shaay186
This is my own work as defined by the University's Academic Integrity Policy.
'''

# This main.py sets up the zoo system demo by importing the animal, enclosure, and staff classes, and starts with a simple demonstration function to showcase functionality.
from animal import Mammal, Bird, Reptile
from enclosure import Enclosure
from staff import Zookeeper, Veterinarian

def demo():
    print("=== Zoo System Demo ===\n")

    # Create Animals
    leo = Mammal("Leo", "Lion", 5, diet="Carnivore")
    molly = Bird("Molly", "Parrot", 2)
    slither = Reptile("Slither", "Corn Snake", 3)

    print("Created animals:")
    for a in [leo, molly, slither]:
        print(f"{a.__class__.__name__}(name='{a.name}', species='{a.species}', age={a.age}, category='{a.category}')")
    print()

    # Create Enclosures
    savannah = Enclosure("Savannah Exhibit", 200.0, "Savannah", cleanliness=85)
    aviary = Enclosure("Aviary", 50.0, "Forest", cleanliness=90)
    reptile_house = Enclosure("Reptile House", 80.0, "Tropical", cleanliness=95)

    enclosures = [savannah, aviary, reptile_house]

    print("Created enclosures:")
    for e in enclosures:
        print(
            f"Enclosure '{e.name}' [{e.environment_type}] - Cleanliness: {e.cleanliness}% - Animals: {e.list_animals() or 'No animals'}")
    print()

    # Create Staff
    alice = Zookeeper("Alice")
    dr_bob = Veterinarian("Dr Bob")

    print("Staff created:")
    print(f"{alice.name} - {alice.role}")
    print(f"{dr_bob.name} - {dr_bob.role}")
    print()

    # Add animals to enclosures
    print("Adding animals to enclosures...")
    print(savannah.add_animal(leo))
    print(aviary.add_animal(molly))
    print(reptile_house.add_animal(slither))
    print()

    # Staff Actions
    print(alice.feed_animal(leo))
    print(alice.feed_animal(molly))
    print(alice.clean_enclosure(savannah))
    print()

    # Health Checks
    print(dr_bob.perform_health_check(leo, description="Limping on front left paw", severity="Medium",
                                      treatment="Restricted activity; analgesic prescribed."))
    print()

    # Enclosure Reports
    print("Enclosure Reports:")
    for e in enclosures:
        print(e.report_status())
    print()



