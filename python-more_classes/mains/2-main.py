#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(f"Area = {my_rectangle.area()} and Perimeter = {my_rectangle.perimeter()}")

print("--")

my_rectangle.width = 5
my_rectangle.height = 5
print(f"Area = {my_rectangle.area()} and Perimeter = {my_rectangle.perimeter()}")

print("--")

my_rectangle.width = 5
my_rectangle.height = 0
print(f"Area = {my_rectangle.area()} and Perimeter = {my_rectangle.perimeter()}")
