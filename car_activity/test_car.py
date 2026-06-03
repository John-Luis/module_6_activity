import os
import time
from car_class import Car


def clear_screen():
    """Clears the terminal screen for a clean UI feel."""
    # Works for both Windows (nt) and Mac/Linux
    os.system("cls" if os.name == "nt" else "clear")


def display_dashboard(car, status_msg):
    """Prints a simple text-based dashboard."""
    clear_screen()
    print("=" * 40)
    print(f" MACHINE : {car.get_name()}")
    print(f" STATUS  : {status_msg}")
    print("-" * 40)
    print(f" SPEED   : {car.get_speed()} km/h")
    print(f" GEAR    : {car.get_gear()}")
    print("=" * 40)


if __name__ == "__main__":
    # Initialize the car
    my_car = Car("2026", "Lamborghini Aventador")

    print("⚡ BOOTING UP ECU... ENGINE IS IDLING VROOOM! ⚡\n")
    time.sleep(1.2)

    status = "Engine idling. Ready to drive!"

    # Interactive Driving Loop
    while True:
        display_dashboard(my_car, status)

        print("\n[W] Accelerate  [S] Brake  [Q] Quit")
        choice = input("Action > ").strip().lower()

        if choice == "w":
            my_car.accelerate()
            status = "PUSHING GAS! 🏎️"
        elif choice == "s":
            my_car.brake()
            status = "STOMPING BRAKES! 🛑"
        elif choice == "q":
            status = "Shutting down engine..."
            display_dashboard(my_car, status)
            time.sleep(1.0)
            break
        else:
            status = "Invalid input! Use W, S, or Q."

    print("\n✓ Session logged. Diagnostics clean. 🏁")