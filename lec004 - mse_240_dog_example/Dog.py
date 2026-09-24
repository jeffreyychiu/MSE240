#
# Author: Oliver Schneider
# Email: oliver.schneider@uwaterloo.ca
# Student ID: 1234567890
#
# Source code for the Dog class.
#

from datetime import date


class Dog:
    """ Dog
    A class representing an individual dog.
    """

    def __init__(self, name: str, breed: str, gender: str, initial_weight: float,
                 colour: str, potential_health_issues: list[str], birth_year: int):
        """ Dog constructor
        name                     the dog's given name
        breed                    the dog's breed
        gender                   the dog's gender
        initial_weight           the dog's initial weight (lbs)
        colour                   a description of the dog's colour
        potential_health_issues  a list of known potential health issues (each a string)
        birth_year               the year the dog was born
        """
        self.name = name
        self.breed = breed
        self.gender = gender
        self.weight = initial_weight
        self.colour = colour
        # store a copy so changes to the caller's list don't affect the dog
        self.potential_health_issues = list(potential_health_issues)
        self.birth_year = birth_year

    #############
    # Accessors #
    #############

    def get_name(self) -> str:
        """ get_name
        returns the dog's name as a string
        """
        return self.name

    def get_breed(self) -> str:
        """ get_breed
        returns the dog's breed as a string
        """
        return self.breed

    def get_gender(self) -> str:
        """ get_gender
        returns the dog's gender as a string
        """
        return self.gender

    def get_weight(self) -> float:
        """ get_weight
        return the dog's weight in lbs
        """
        return self.weight

    def get_colour(self) -> str:
        """ get_colour
        return the dog's colour as a description
        """
        return self.colour

    def get_potential_health_issues(self) -> list[str]:
        """ get_potential_health_issues
        return the dog's known potential_health_issues as a list
        """
        return list(self.potential_health_issues)

    def get_age(self) -> int:
        """ get_age
        return the dog's age
        """
        return date.today().year - self.birth_year

    ############
    # Mutators #
    ############

    def set_name(self, new_name: str):
        """ set_name
        new_name  the dog's new name
        """
        self.name = new_name

    def set_weight(self, new_weight: float):
        """ set_weight
        new_weight  the new measured weight of the dog (in lbs)
        """
        self.weight = new_weight

    def add_potential_health_issue(self, health_issue: str):
        """ add_potential_health_issue
        add a health issue to the potential health issues
        """
        self.potential_health_issues.append(health_issue)



        def setUp(self):
            """ setUp
            set up the test fixture before exercising it
            """
            self.typical1 = Dog("Waffle", "Newfoundland", "male", 130, "Black", [], 2018)
            self.typical2 = Dog("Buddy", "Golden Retriever", "male", 70, "Golden", [], 2019)