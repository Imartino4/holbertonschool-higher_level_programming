#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

#Trying properties
my_rectangle = Rectangle(2, 4)
print(my_rectangle.height)

#Trying message errors when negative numbers
try:
    my_rectangle = Rectangle(2, -3)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    my_rectangle = Rectangle(-2, 3)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

#Trying when only one parameter is given
my_rectangle = Rectangle(4)
print("{} - {}".format(my_rectangle.width, my_rectangle.height))
