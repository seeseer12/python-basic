# # single inheritance
# class Animal:
#     def __init__(self):
#         print( "Animal speaks" )


# class Dog(Animal):
#     def bark(self):
#         return "Dog barks"      
# # Usage
# dog = Dog()      
# print(dog.bark())   # Dog's own method







# multilevel inheritance
# when obj is created of bmwX5 class it will call constructor of bmwX5 class if not found then it will call constructor of bmw class if not found then it will call constructor of car class
# here it only calls bmwx5 constructor as it is defined in that class

class car:
    def __init__(self,type,color="red"):
        self.type=type
        self.color=color
        print("car started")
    
class bmw(car):
    def __init__(self,accelerate=10):
        self.accelerate=accelerate
        print("bmw accelarating by",accelerate,"m/s")
class bmwX5(bmw):
    def __init__(self):
        print("bmw x5 constructor")
    
# Usage
my_bmw = bmwX5()  # This will call the constructor of bmwX5 class
# my_bmw = bmw(20)  # This will call the constructor of bmw class
my_car = car("sedan","pink")  # This will call the constructor of car class




