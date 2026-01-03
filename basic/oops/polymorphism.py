# polymerphism is the ability to take more than one form
# it allows methods to do different things based on the object it is acting upon




# __add__ method is used to overload the + operator
# by default + operator adds numbers but we can overload it to add complex numbers

# __sub__ method is used to overload the - operator
# __mul__ method is used to overload the * operator
# __truediv__ method is used to overload the / operator
# __floordiv__ method is used to overload the // operator


class complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag


    def __add__(self,other):
        return complex(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self,other):
        return complex(self.real - other.real, self.imag - other.imag)

    def show(self):
        print(f"{self.real} +{self.imag}i")

complex1=complex(2,3)
complex2=complex(5,7)
complex3=complex1 + complex2
complex4=complex2 - complex1
complex4.show()
complex3.show()

    