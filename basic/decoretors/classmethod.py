# classmethod ia a built-in decorator in Python that is used to define a method that is bound to the class and not the instance of the class.
# This means that the method can be called on the class itself, rather than on an instance of the class.
# note: staticmethod does not take any default parameters but classmethod takes cls as default parameter which refers to the class itself.
# staticmethod cant access class or modify class state but classmethod can access or modify class state.


class person:
    name='unknown'
    @classmethod
    def change(cls, name):
        cls.name = name
       

p=person()
print(p.name)  # Output: unknown
print(person.name)  # Output: unknown
p.change("shishir")
print(p.name)  # Output: shishir
print(person.name)  # Output: shishir

p2=person()
print(p2.name)  # Output: shishir