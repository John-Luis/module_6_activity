# car_class.py
class Car:
    def __init__(self, year, make):
        self.__year = year
        self.__make = make
        self.__speed = 0
        self.__gear = 1  # Starts at Gear 1

    def accelerate(self):
        self.__speed += 5
        self.__update_gear()  # Auto-shift gear after accelerating

    def brake(self):
        self.__speed -= 5
        if self.__speed < 0:
            self.__speed = 0
        self.__update_gear()  # Auto-shift gear after braking

    def __update_gear(self):
        """Internal helper to calculate gear based on 5km/h steps (Max 25 km/h)"""
        if self.__speed == 0:
            self.__gear = 1
        elif self.__speed <= 5:
            self.__gear = 1
        elif self.__speed <= 10:
            self.__gear = 2
        elif self.__speed <= 15:
            self.__gear = 3
        elif self.__speed <= 20:
            self.__gear = 4
        else:
            self.__gear = 5  # Top gear at 25 km/h

    def get_speed(self):
        return self.__speed

    def get_gear(self):
        return self.__gear

    def get_name(self):
        return f"{self.__year} {self.__make}"