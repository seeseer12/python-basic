print("hey enter the value of a and b")
a = int(input("hey enter the value of a: "))
b = int(input("hey enter the value of b: "))
try:
    c = a/b
    print(c)
except ZeroDivisionError:
    print("you cannot divide by zero")