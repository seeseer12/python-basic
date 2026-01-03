# static methods are methods that belong to a class rather than an instance of a class. They do not require an instance to be called and do not have access to the instance (self) or class (cls) variables. They are defined using the @staticmethod decorator.
#they can be used when some functionality is related to the class but does not need to access any class or instance-specific data.


class shishir:
    @staticmethod
    def greet():
        print("Hello, welcome to the static method example!")

# Usage
shishir.greet()  # Calling static method without creating an instance