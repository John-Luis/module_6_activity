
# pet_class.py
class Pet:
    def __init__(self):
        # Initialize hidden attributes using double underscores as private members
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0