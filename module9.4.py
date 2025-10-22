import random

race_cars = []

class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_travelled = 0

    def accelerate(self, change_speed):
        self.current_speed += change_speed
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def drive(self, hours):
        distance_driven = self.current_speed * hours
        self.distance_travelled += distance_driven



for i in range(1, 11):
    max_speed = random.randint(100, 200)
    reg_number = f"ABC-{i}"
    race_cars.append(Car(reg_number, max_speed))


drive_hour = 0
race_continue = True

while race_continue == True:
    drive_hour += 1

    for car in race_cars:
        change_speed = random.randint(-10, 15)
        car.accelerate(change_speed)
        car.drive(drive_hour)

        if car.distance_travelled >= 10000:
            race_continue = False
            winner = car
            break


print(f"The winner is {winner.reg_number}!")
print(f"{'Reg Number':<14}{'Max Speed':>10}{'Current Speed':>18}{'Distance':>11}")
for car in race_cars:
    print(f"{car.reg_number:<12}{car.max_speed:>10}"
          f"{car.current_speed:>15}{car.distance_travelled:>15.1f}")
