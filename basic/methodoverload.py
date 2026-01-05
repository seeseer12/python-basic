def sum(a=None, b=None,c=None):
    if a!= None and b!= None and c != None:
        return a + b + c
    elif a != None and b != None:
        return a + b
    elif a != None:
        return a 
    else:
        return "No arguments provided"
print(sum(2,3))
print(sum(2,3,4))
print(sum(5))

   