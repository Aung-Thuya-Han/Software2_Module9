class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

car = Car("ABC-123", 142)

print("Car status check...")
print(f"Registration number: {car.reg_number:s}")
print(f"Maximum speed: {car.max_speed:d} km/h")
print(f"Current speed: {car.current_speed:d} km/h")
print(f"Travelled distance: {car.travelled_distance:d} km")
