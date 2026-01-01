class animal:
    
    

    def __init__(self,type):
        print( "Animal object created " )
        self.type=type

    def speak(self):
        print("Animal speaks")
        


class dog(animal):
    def __init__(self,type="German Shepherd"):
        super().__init__(type)
        
# Usage
dog = dog() 
# print(dog.bark())   # Dog's own method
print(dog.type)  # Inherited attribute from Animal class
    # Inherited method from Animal class