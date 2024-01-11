class Car:
  def __init__(self, speed, color):
    self.__speed = speed
    self.__color = color
  #to prevent modificatio when acccess is granted to other people
  def set_Speed(self, value):
    self.__speed = value
  def set_Speed(self):
    return self.__speed



v8 = Car(240, "Black")
lexus = Car(190, "Grey")
v8.set_speed(320)

print(v8.__speed) # returns 320
print(v8.color) #no attribute named color in car
print(lexus.speed)
            
            
