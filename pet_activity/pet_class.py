
# pet_class.py
class pet:
    def __init__(self):
        # Initialize hidden attributes using double underscores as private members
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0

    # Mutator methods (Setters)
    def set_name(self, name):
        self.__name = name

    # Accessor methods (Getters)
    def get_name(self):
        return self.__name

    # Mutator methods (Setters)
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    # Accessor methods (Getters)
    def get_animal_type(self):
        return self.__animal_type

    # Mutator methods (Setters)
    def set_age(self, age):
        self.__age = age

    # Accessor methods (Getters)
    def get_age(self):
        return self.__age