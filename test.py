'''
File: test.py
Author: Abhinav Sharma
ID: 110376072
Username: shaay186
This is my own work as defined by the University's Academic Integrity Policy.
'''

import unittest
from animal import Mammal, Bird, Reptile
from enclosure import Enclosure
from staff import Zookeeper, Veterinarian

class TestAnimals(unittest.TestCase):
    def setUp(self):
        self.lion = Mammal("Leo", "Lion", 5, diet="Carnivore")
        self.parrot = Bird("Molly", "Parrot", 2)
        self.snake = Reptile("Slither", "Corn Snake", 3)

    def test_animal_attributes(self):
        self.assertEqual(self.lion.name, "Leo")
        self.assertEqual(self.lion.species, "Lion")
        self.assertEqual(self.lion.age, 5)
        self.assertEqual(self.lion.category, "Mammal")

    def test_make_sound(self):
        self.assertIsInstance(self.lion.make_sound(), str)
        self.assertIsInstance(self.parrot.make_sound(), str)
        self.assertIsInstance(self.snake.make_sound(), str)

    def test_health_methods(self):
        # Initially healthy
        self.assertTrue(self.lion.is_healthy())

        # Add health issue
        self.lion.add_health_issue("Cough", severity="Low", treatment="Rest")
        report = self.lion.get_health_report()
        # Check that the issue exists in the list of dicts
        self.assertTrue(any(issue['description'] == "Cough" for issue in report))
        self.assertFalse(self.lion.is_healthy())

class TestEnclosure(unittest.TestCase):
    def setUp(self):
        self.lion = Mammal("Leo", "Lion", 5, diet="Carnivore")
        self.parrot = Bird("Molly", "Parrot", 2)
        self.savannah = Enclosure("Savannah Exhibit", 200.0, "Savannah", cleanliness=85)
        self.aviary = Enclosure("Aviary", 50.0, "Forest", cleanliness=90)

    def test_add_animal(self):
        result = self.savannah.add_animal(self.lion)
        self.assertIn("added", result)
        self.assertEqual(self.savannah.animal_type, "Mammal")

        result2 = self.savannah.add_animal(self.parrot)
        self.assertIn("Cannot add", result2)

    def test_remove_animal(self):
        self.savannah.add_animal(self.lion)
        result = self.savannah.remove_animal(self.lion)
        self.assertIn("removed", result)
        result2 = self.savannah.remove_animal(self.lion)
        self.assertIn("not found", result2)

    def test_clean_enclosure(self):
        self.savannah.cleanliness = 50
        self.savannah.clean()
        self.assertEqual(self.savannah.cleanliness, 100)

    def test_list_animals(self):
        self.assertEqual(self.aviary.list_animals(), [])
        self.aviary.add_animal(self.parrot)
        self.assertIn("Molly(Parrot)", self.aviary.list_animals())

class TestStaff(unittest.TestCase):
    def setUp(self):
        self.lion = Mammal("Leo", "Lion", 5, diet="Carnivore")
        self.parrot = Bird("Molly", "Parrot", 2)
        self.savannah = Enclosure("Savannah Exhibit", 200.0, "Savannah")
        self.alice = Zookeeper("Alice")
        self.dr_bob = Veterinarian("Dr Bob")

    def test_zookeeper_feed(self):
        result = self.alice.feed_animal(self.lion)
        self.assertIn("feeds", result)
        self.assertIn(self.lion.name, result)

    def test_zookeeper_clean(self):
        self.savannah.cleanliness = 70
        self.alice.clean_enclosure(self.savannah)
        self.assertEqual(self.savannah.cleanliness, 100)

    def test_veterinarian_health_check(self):
        # Initially no health issues
        report_before = self.lion.get_health_report()
        self.assertEqual(report_before, [])

        # Perform health check
        self.dr_bob.perform_health_check(
            self.lion, description="Limping", severity="Medium", treatment="Rest"
        )
        report_after = self.lion.get_health_report()
        self.assertTrue(any(issue['description'] == "Limping" for issue in report_after))

if __name__ == "__main__":
    unittest.main()
