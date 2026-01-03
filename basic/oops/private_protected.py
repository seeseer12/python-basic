# there is no true private or protected access modifier in Python,
# but by convention, a single underscore (_) before a variable or method name indicates that it is intended for internal use (protected),
# and a double underscore (__) indicates that it is intended to be private.

class Person:
    def __init__(self, name, age):
        self.name = name          # public attribute
        self._age = age          # protected attribute
        self.__ssn = "123-45-6789"  # private attribute
        
    def __hehes(self):
        print("This is a private method")



    def display_info(self):
        print("name:",self.name)
        print("age:",self._age)
        print("ssn:",self.__ssn)    
        self.__hehes()

    
        

# Usage
p = Person("Alice", 30)
p.display_info()
print(p.name)        # Accessible
print(p._age)       # Accessible but should be treated as protected    
print(p._Person__ssn)  # Accessible but should be treated as private (name mangling)
# print(p.__ssn)     # Not accessible, will raise AttributeError   