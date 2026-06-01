# car.py
class car:
    def __init__(self, year_model, make):
        # Private data attributes using double underscores
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0  # Default speed starts at 0

        # Accelerate method adds 5 km/h to current speed
        def accelerate(self):
            self.__speed += 5

        # Brake method drops speed by 5 km/h safely
        def brake(self):
            if self.__speed >= 5:
                self.__speed -= 5
            else:
                self.__speed = 0