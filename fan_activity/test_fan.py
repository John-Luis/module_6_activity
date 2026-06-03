# test_fan.py
import time
import sys
from fan_class import fan


def display_dashboard(fan_obj, fan_label):
    """Prints a simple text-based dashboard for the fan status."""
    print("=" * 40)
    print(f" DEVICE : {fan_label.upper()}")

    # Check if fan is on or off
    if not fan_obj.get_on():
        print(" STATUS : [○] STATIONARY (POWER OFF)")
        print("-" * 40)
        print(" SPEED  : N/A")
    else:
        # Determine speed text description
        speed_level = fan_obj.get_speed()
        if speed_level == fan.SLOW:
            speed_text = "LOW VELOCITY"
        elif speed_level == fan.MEDIUM:
            speed_text = "BALANCED VELOCITY"
        else:
            speed_text = "MAXIMUM ROTATIONAL VELOCITY"

        print(" STATUS : [▶] ENGINE ENGAGED // SPINNING")
        print("-" * 40)
        print(f" SPEED  : Level {speed_level} ({speed_text})")

    print("=" * 40)


if __name__ == "__main__":
    # Initialize your fan object (Assuming default constructor)
    my_fan = fan()
    fan_name = "Cooler Master X1"

    print("INITIALIZING FAN HARDWARE CORE... \n")
    time.sleep(1.0)

    # Interactive Fan Control Loop
    while True:
        display_dashboard(my_fan, fan_name)

        print("\n[1] Toggle Power (On/Off)  [2] Change Speed  [Q] Quit")
        choice = input("Action > ").strip().lower()

        if choice == "1":
            # Toggle power state
            current_power = my_fan.get_on()
            my_fan.set_on(not current_power)

        elif choice == "2":
            if not my_fan.get_on():
                input("\n[!] Cannot change speed while the fan is OFF. Press Enter to continue...")
            else:
                print("\nSelect Speed: [1] SLOW  [2] MEDIUM  [3] FAST")
                speed_choice = input("Speed Level > ").strip()

                if speed_choice == "1":
                    my_fan.set_speed(fan.SLOW)
                elif speed_choice == "2":
                    my_fan.set_speed(fan.MEDIUM)
                elif speed_choice == "3":
                    my_fan.set_speed(fan.FAST)
                else:
                    input("\n[!] Invalid speed choice. Press Enter to continue...")

        elif choice == "q":
            print("\nShutting down core cooling systems...")
            time.sleep(0.8)
            break
        else:
            input("\n[!] Invalid option. Press Enter to continue...")

    print("\n✓ Fan diagnostics closed cleanly.")