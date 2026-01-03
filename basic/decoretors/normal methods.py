# These are normal instances methods which takes self as 1st parameter
class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def start(self):
        print(f"{self.brand} {self.model} is starting.")

    def stop(self):
        print(f"{self.brand} {self.model} is stopping.")

# Usage
my_car=car("Toyota","Camry")    
my_car.start()
my_car.stop()
