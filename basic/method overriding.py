class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):          # overriding
        print("Dog barks")
        super().speak()
        

        


d = Dog()
d.speak()
# Output: Dog barks



# note:
# Method name must be same

# Parameters should be same

# Inheritance must exist

# Child method is called at runtime