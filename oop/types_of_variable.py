"""
There are two types of variables:
1. Instance variables ===> instance variables are in init function normally. Their values are limited to specific objects
2. Class variables ===> The value of Class variables are shared by whole class and if we change its value, the value will be changed in every object

"""
"""
Class and Static are same in variables but they are different in methods 
"""


class Cars:
    wheels = "4 wheels"

    def __init__(self):
        self.mile = "7 miles"
        self.comp = "Audi"


car1 = Cars()
car2 = Cars()

car2.mile = "12 miles"
car2.comp = "BMW"
car1.wheels = 23
# Cars.wheels = 23
print(car1.comp, car1.mile, car1.wheels)
print(car2.comp, car2.mile, car2.wheels)
# print(Cars.wheels)
