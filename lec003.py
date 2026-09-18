class Dog:

    def __init__(self):
        raise NotImplementedError("Not implemented yet")

""" should have:

#_breed: str
#_age: int
#_name: str
#_Weight: float

#_last_fed_time: Datetime
#_last_walk_time: Datetime

#accessor
# is_fed(): bool
# is_walked(): bool
#_is_healthy_weight(): bool


#mutator 
# feed()
# walk()
# set_weight(new_weight, in_kg)


"""


def __init__(self, 
             breed: str, 
             age: int, 
             name: str, 
             weight: float):
    """
    Constructor for Dog class

    Parameters
    name: Name of the dog
    breed: Breed of the dog
    age: Age of the dog
    weight: Weight of the dog in kg
    ""
    #raise NotImplementedError("Not implemented yet")

    self._name = name
    self._breed = breed
    self._age = age
    self._weight = weight
    self._last_fed_time = None
    self._last_walk_time = None


    # Accessors:
    """

    def is_fed():
        #Stub
        raise NotImplementedError("Not implemented yet")

    def is_walked():
        #Stub
        raise NotImplementedError("Not implemented yet")

    def _is_healthy_weight():
        #Stub
        raise NotImplementedError("Not implemented yet")

    def bark(self):
        print("woof")

    def get_weight(self):
        return self._weight


    #Mutators
    
    def feed():
        #Stub
        raise NotImplementedError("Not implemented yet")

    def walk():
        #Stub
        raise NotImplementedError("Not implemented yet")

    def set_weight(new_weight, in_kg : float):
        #Stub
        raise NotImplementedError("Not implemented yet")
    


#Main Function
if __name__ == "__main__":
    waffle = Dog("waffle", "newfoundland (Landseer)", 8, 58.97)

    waffle.bark()
    waffle.set_weight(57.23, in_kg=57.23)

    jazz = Dog("jazz", "Goldendoodle", 6, 27.5)

