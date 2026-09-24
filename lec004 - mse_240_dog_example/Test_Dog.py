import unittest
from Dog import Dog


class TestDog(unittest.TestCase):
    """ TestDog
    Unit test for the Dog class
    """

    def test_constructor_typical1(self):
        dog = Dog("Waffle", "Newfoundland", "male", 130, "Black", [], 2018)
        self.assertEqual("Waffle", dog.get_name())
        self.assertEqual("Newfoundland", dog.get_breed())
        self.assertEqual("male", dog.get_gender())
        self.assertEqual(130, dog.get_weight())
        self.assertEqual("Black", dog.get_colour())
        self.assertEqual([], dog.get_potential_health_issues())
        self.assertEqual(8, dog.get_age())

    def test_get_name_typical1(self):
        dog = Dog("Waffle", "Newfoundland", "male", 130, "Black", [], 2018)
        self.assertEqual("Waffle", dog.get_name())

    def test_get_breed_typical1(self):
        dog = Dog("Waffle", "Newfoundland", "male", 130, "Black", [], 2018)
        self.assertEqual("Newfoundland", dog.get_breed())

    def test_get_gender_typical1(self):
        dog = Dog("Waffle", "Newfoundland", "male", 130, "Black", [], 2018)
        self.assertEqual("male", dog.get_gender())

    def test_get_weight_typical1(self):
        dog = Dog("Waffle", "Newfoundland", "male", 130, "Black", [], 2018)
        self.assertEqual(130, dog.get_weight())

    def test_set_name_unusual1(self):
        dog = Dog("Waffle", "Newfoundland", "male", 130, "Black", [], 2018)
        dog.set_name("Mary-Anne")
        self.assertEqual(dog.get_name(), "Mary-Anne")


if __name__ == "__main__":
    unittest.main()