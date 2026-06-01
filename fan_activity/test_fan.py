# We import the Fan class from our fan.py file
from fan_class import fan

if __name__ == "__main__":
    # Object 1: maximum speed (FAST), radius 10, color yellow, turned on
    fan_1 = fan(speed=fan.FAST, radius=10, color="yellow", on=True)