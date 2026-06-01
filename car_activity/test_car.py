# test_car.py
from car_class import Car

if __name__ == "__main__":
    # Create a Car object
    my_car = Car("2026", "Lamborghini")

    # Call the accelerate method 5 times
    print("Accelerating...")
    for i in range(5):
        my_car.accelerate()
        print(f"Current speed: {my_car.get_speed()} km/h")

    print("\nBraking...")
    # Call the brake method 5 times
    for i in range(5):
        my_car.brake()
        print(f"Current speed: {my_car.get_speed()} km/h")
