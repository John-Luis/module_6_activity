
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