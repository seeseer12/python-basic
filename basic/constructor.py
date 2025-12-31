# # class shishir:
# #     # id=3
# #     # name="shishir"
# #     id=44
    




# #     def __init__(self,name="shishir",age=24):
# #         # print("This is  parameterized constructor")
# #         self.name=name
# #         self.age=age
        
        
# # s=shishir("steve",25)
# # su=shishir("tim",30)
# # tu=shishir()  
# # print(s.name,s.age,s.id)
# # print(su.name,su.age,su.id)
# # print(tu.name,tu.age,tu.id)



# # two init method not allowed in python as 1st one is overwritten by 2nd one






# # Q.>>  create a class and constructor for student thattakes names and marks of 3 sub and return their avg
# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def avg(self):
#         sum=0
#         count=0
#         for i in self.marks:
#             sum+=i
#             count+=1
#         print("average marks of " ,self.name,sum/count)
    

# s=student("shishir",[90,80,70])
# s.avg()



# decorator in constructor -> staticmethod
class example:
    @staticmethod
    def info():
        print("This is static method in constructor")
    
    def __init__(self):
        self.info()

e=example()
e.info()