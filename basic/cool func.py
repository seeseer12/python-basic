def add(*args):
    return sum(args)

print(add(2,3))
print(add(2,3,4,5))













# def profile(**info):
#     print(info)

# profile(name="Shishir", hobby="Coding")
# profile(name="Alice", age=30, city="New York")











# lambda function
# they are small anonymous function
# sum=lambda a,b: a+b
avg=lambda *args: sum(args)/len(args)
print(avg(2,3,4,5,6))
# print(sum(2,3))







