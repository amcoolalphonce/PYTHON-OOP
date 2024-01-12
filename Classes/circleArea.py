import math

class Circle:
  def __init__(self, radius):
    self.radius = radius

  def calculate_area(self):
    return round(math.pi * self.radius **2, 2)


class Rectangle:
  def __init__(self, length, width):
    self.width = width
    self.length = length

  def rectangle_area(self):
    
#usage
circle_1 = Circle(42)
print(circle_1.radius)# 42
print(circle_1.calculate_area()) #5541.77

