# SyntaxError
# print "Hi"
print("Hi")

# NameError
# print(name)
name = "hi"
print(name)

# IndexError
my_list = [1, 2, 3, 4, 5]
# print(my_list[5])
print(my_list[4])

# ModuleNotFoundError
# import maths
import math

# AttributeError
# print(math.PI)
print(math.pi)

# KeyError
my_dict = {"Name": "Mike", "Surname": "Ballester", "Age": 29}
# print(my_dict["Names"])
print(my_dict["Name"])

# ImportError
# from math import PI
from math import pi

# ValueError
# my_int = int("10S")
my_int = int("10")
print(type(my_int))

# ZeroDivisionError
# print(1 / 0)
print(1 / 1)
