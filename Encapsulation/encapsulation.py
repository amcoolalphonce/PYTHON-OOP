class Car:
  def __init__(self, speed, color):
    self.__speed = speed
    self.__color = color
  #to prevent modificatio when acccess is granted to other people
  def set_speed(self, value):
    self.__speed = value
  def set_Speed(self):
    return self.__speed

  def set_color(self, value):
    self.__color = value

  def get_color(self):
    return self.__color

v8 = Car(240, "Black")
lexus = Car(190, "Grey")
v8.set_speed(320)
v8.set_color("Dark grey")

print(v8.__speed) # returns 320

print(v8.color) #no attribute named color in car
print(lexus.speed)
            
            
