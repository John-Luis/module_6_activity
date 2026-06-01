# test_pet.py
from pet_class import pet

if __name__ == "__main__":
    # Create an object of the Pet class
    my_pet = pet()

    pet_name = input("Enter your pet's name: ")
    pet_type = input("Enter your pet's animal type (e.g., Dog, Cat, Bird): ")
    pet_age = int(input("Enter your pet's age: "))

    my_pet.set_name(pet_name)
    my_pet.set_animal_type(pet_type)
    my_pet.set_age(pet_age)

    print("\n--- Pet Registration Details ---")
    print(f"Pet Name:    {my_pet.get_name()}")
    print(f"Animal Type: {my_pet.get_animal_type()}")
    print(f"Pet Age:     {my_pet.get_age()} years old")
