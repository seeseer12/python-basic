# property method example
# class marks:
#     def __init__(self, math, science):
#         self.math=math
#         self.science=science
        
#     @property
#     def percentage(self):
#         return str((self.math + self.science) / 2)

# marks1=marks(90,80)
# print("Percentage:", marks1.percentage)  # Output: Percentage: 85.0
# marks1.math=100
# marks1.science=90
# print(marks1.percentage)





# property method with setter
class marks:
    def __init__(self, math, science):
        self.math=math
        self.science=science
        
    @property
    def percentage(self):
        return str((self.math + self.science) / 2)
    
    @percentage.setter
    def percentage(self, value):
        total_marks = value * 2
        self.math = total_marks / 2
        self.science = total_marks / 2
marks1=marks(90,80)
print("Percentage:", marks1.percentage)  # Output: Percentage: 85.0
marks1.percentage = 95  # Setting new percentage
print("Updated Math Marks:", marks1.math)      # Output: Updated Math Marks: 95.0
print("Updated Science Marks:", marks1.science)  # Output: Updated Science Marks: 95.0  
