# We import the Fan class from our fan.py file
from fan_class import fan

if __name__ == "__main__":
    # Object 1: maximum speed (FAST), radius 10, color yellow, turned on
    fan_1 = fan(speed=fan.FAST, radius=10, color="yellow", on=True)

    # Object 2: medium speed, radius 5, color blue, turned off
    fan_2 = fan(speed=fan.MEDIUM, radius=5, color="blue", on=False)

    # Display fan_1 properties
    print("Fan 1 Properties:")
    print(f"Speed: {fan_1.get_speed()}")
    print(f"Radius: {fan_1.get_radius()}")
    print(f"Color: {fan_1.get_color()}")
    print(f"Is On: {fan_1.get_on()}")

    print("-" * 20)

    # Display fan_2 properties
    print("Fan 2 Properties:")
    print(f"Speed: {fan_2.get_speed()}")
    print(f"Radius: {fan_2.get_radius()}")
    print(f"Color: {fan_2.get_color()}")
    print(f"Is On: {fan_2.get_on()}")