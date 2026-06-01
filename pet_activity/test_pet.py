# test_pet.py
from pet_class import pet

if __name__ == "__main__":
    # Create an object of the Pet class
    my_pet = pet()

    pet_name = input("Enter your pet's name: ")
    pet_type = input("Enter your pet's animal type (e.g., Dog, Cat, Bird): ")
    pet_age = int(input("Enter your pet's age: "))

