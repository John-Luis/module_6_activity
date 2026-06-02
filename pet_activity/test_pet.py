# test_pet.py
import time
import random
from pet_class import pet

if __name__ == "__main__":
    my_pet = pet()

    print("┌────────────────────────────────────────┐")
    print("│     CORE SYSTEM: PET REGISTRATION      │")
    print("└────────────────────────────────────────┘")

    pet_name = input("Enter Pet Name : ")
    pet_type = input("Animal Type    : ")
    pet_age = int(input("Pet Age (yrs)   : "))

    # fixed the setters
    my_pet.set_name(pet_name)
    my_pet.set_animal_type(pet_type)
    my_pet.set_age(pet_age)

    print("\n[*] INITIALIZING DATA ENCAPSULATION...")
    time.sleep(0.4)

    # Fake loading progress bar
    print("[", end="", flush=True)
    for _ in range(20):
        time.sleep(random.uniform(0.02, 0.08))
        print("█", end="", flush=True)
    print("] 100% SECURE")

    # Generating a mock memory address pointer to make it look technical
    mock_address = f"0x{random.randint(0x1000A, 0x9999F):X}"
    print(f"[✓] BUNDLED RELATED ATTRIBUTES AT MEMORY: {mock_address}")
    time.sleep(0.4)
    print("[!] LOCKING PRIVATE FIELDS EXCLUSIVELY TO ACCESSORS...")
    time.sleep(0.5)
    print("[✓] TARGET DATA STREAM ENGAGED.\n")
    time.sleep(0.2)

    # Final Dashboard Block Output
    print("╔════════════════════════════════════════╗")
    print("║         PET NAME IDENTIFICATION        ║")
    print("╠════════════════════════════════════════╣")
    print(f"║  • TARGET ID   : {my_pet.get_name().upper():<21} ║")
    print(f"║  • CLASSIFY    : {my_pet.get_animal_type().upper():<21} ║")
    print(f"║  • LIFESPAN    : {str(my_pet.get_age()) + ' CYCLES':<21} ║")
    print("╚════════════════════════════════════════╝")