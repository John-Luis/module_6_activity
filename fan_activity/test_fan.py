# We import the Fan class from our fan.py file
from fan import Fan

if __name__ == "__main__":
    # Object 1: maximum speed (FAST), radius 10, color yellow, turned on
    fan_1 = Fan(speed=Fan.FAST, radius=10, color="yellow", on=True)