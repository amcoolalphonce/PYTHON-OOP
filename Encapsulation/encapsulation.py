class Car:
  def __init__(self, speed, color):
    self.__speed = speed
    self.__color = color
  #to prevent modification when acccess is granted to other people we defin functions for setting and getting attributes within the class
  #values assigned outside the class will not be reflected as genuine ones
  def set_speed(self, value):
    self.__speed = value
  def set_Speed(self):
    return self.__speed

  def set_color(self, value):
    self.__color = value

  def get_color(self):
    return self.__color

v8 = Car(240, "Black") # are overriden once we set the class attributes to private
# new values are set using the functions defined within the class

v8.set_speed(320)
v8.set_color("Dark grey")

print(v8.get_speed()) # returns 320
print(v8.get_color()) # Dark grey

print(v8.color) #no attribute named color in car
print(v8.speed) # no attribute named speed in the class Car
            
            
