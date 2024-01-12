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
    return (length * width)
    
#usage
circle_1 = Circle(42)
rectangle1 = Rectangle(40, 20)
print(f'Width of rectangle1 is: {rectangle1.width} , length is {rectangle1.length}')
print(f'Area of rectangle is : {rectangle1.rectangle_area()}')
print('Circle area is :', circle_1.radius)# 42
print('Circle area is : ' , circle_1.calculate_area()) #5541.77

