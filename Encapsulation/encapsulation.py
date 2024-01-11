class Car:
  def __init__(self, speed, color):
    self.__speed = speed
    self.__color = color
  #to prevent modificatio when acccess is granted to other people
  def set_Speed(self, value):
    self.speed = value
  def set_Speed(self):
    return self.speed



v8 = Car(240, "Black")
lexus = Car(190, "Grey")

v8.set_speed(300)
print(v8.get_speed())
            
# to chnage any value of the attributtes
v8.speed = 300 #new v8 speed is 300 from 240


print(v8.speed)
print(lexus.speed)
            
            
