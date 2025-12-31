# hiding the internal details and showing only functionality to the user

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self._speed = 0  # private attribute

    def accelerate(self, increment):
        self._speed += increment
        print(f"The car has accelerated to {self._speed} km/h.")

    def brake(self, decrement):
        self._speed = max(0, self._speed - decrement)
        print(f"The car has slowed down to {self._speed} km/h.")

    def get_speed(self):
        return self._speed
# Usage
my_car = Car("Toyota", "Corolla", 2020) 
my_car.accelerate(50)
my_car.brake(20)
print(f"Current speed: {my_car.get_speed()} km/h")



# here implementation details of speed management are hidden from the user i.e abstraction
