# test_pet.py
import time
from pet_class import pet

if __name__ == "__main__":
    my_pet = pet()

    print("┌────────────────────────────────────────┐")
    print("│     CORE SYSTEM: PET REGISTRATION      │")
    print("└────────────────────────────────────────┘")

    pet_name = input(" SYS_INIT // Enter Pet Name : ")
    pet_type = input("SYS_INIT // Animal Type    : ")
    pet_age = int(input("SYS_INIT // Pet Age (yrs)   : "))

    my_pet.set_name(pet_name)
    my_pet.set_animal_type(pet_type)
    my_pet.set_age(pet_age)

    print("\n[!] BUNDLING RELATED ATTRIBUTES...")
    time.sleep(0.4)
    print("[!] ENCAPSULATING DATA INTO SECURE OBJECT MEMORY...")
    time.sleep(0.6)
    print("[✓] TRANSMISSION COMPLETE.\n")
    time.sleep(0.3)

    # Final Dashboard Block Output
    print("╔════════════════════════════════════════╗")
    print("║         PET NAME IDENTIFICATION        ║")
    print("╠════════════════════════════════════════╣")
    print(f"║  • TARGET ID   : {my_pet.get_name().upper():<21} ║")
    print(f"║  • CLASSIFY    : {my_pet.get_animal_type().upper():<21} ║")
    print(f"║  • LIFESPAN    : {str(my_pet.get_age()) + ' CYCLES':<21} ║")
    print("╚════════════════════════════════════════╝")