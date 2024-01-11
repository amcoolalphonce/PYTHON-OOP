class Car:
  def __init__(self, speed, color):
    self.speed = speed
    self.color = color
  #to prevenr modificatio when acccess is granted to other people
  def set_Speed(self, value):
    self.speed = value
  def set_Speed(self):
    return self.speed



v8 = Car(240, "Black")
lexus = Car(190, "Grey")
            
# to chnage any value of the attributtes
v8.speed = 300 #new v8 speed is 300 from 240


print(v8.speed)
print(lexus.speed)
            
            
