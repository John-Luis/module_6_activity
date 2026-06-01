# car.py
class car:
    def __init__(self, year_model, make):
        # Private data attributes using double underscores
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0  # Default speed starts at 0